"""Testa se uma lista de APIs está no ar.

Este arquivo é usado em dois lugares:
  1. Pelo robô do GitHub (scripts/check.py), para as APIs comuns.
  2. Por uma função na nuvem, em São Paulo, para as APIs que bloqueiam acessos
     de fora do Brasil: na Vercel (api/verificar.py usa este arquivo direto; veja
     vercel/LEIA-ME.md), no Google Cloud (veja google/LEIA-ME.md) ou na AWS
     Lambda (veja aws/LEIA-ME.md). Ele usa só a biblioteca padrão do Python.
"""

from __future__ import annotations

import hmac
import json
import os
import ssl
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

TEMPO_LIMITE = 30  # segundos por requisição
ESPERA_ANTES_DE_REPETIR = 5  # segundos
ORIGEM_TESTE = "https://example.com"
# Formato usado por robôs legítimos: se identifica e informa onde saber mais.
USER_AGENT = (
    "Mozilla/5.0 (compatible; apis-publicas-brasil/1.0; "
    "+https://github.com/LuisGustavoDev/apis-publicas-brasil)"
)

LIMITE_LEITURA = 512 * 1024  # bytes lidos da resposta para conferir o formato

AVISO_CERTIFICADO = "certificado SSL inválido ou incompleto"
AVISO_TLS_ANTIGO = "configuração de segurança (TLS) antiga"

# Trechos de mensagens de erro que indicam servidor com TLS antigo ou incompatível.
SINAIS_TLS_ANTIGO = (
    "HANDSHAKE_FAILURE",
    "UNSAFE_LEGACY_RENEGOTIATION",
    "UNSUPPORTED_PROTOCOL",
    "DH_KEY_TOO_SMALL",
    "WRONG_VERSION_NUMBER",
)


def descrever_erro(erro: Exception) -> str:
    """Transforma a exceção numa mensagem curta e legível para o log."""
    motivo = getattr(erro, "reason", erro)
    texto = str(motivo) or type(motivo).__name__
    return f"{type(motivo).__name__}: {texto}"[:200]


def _contexto(modo: str) -> ssl.SSLContext | None:
    if modo == "sem_certificado":
        return ssl._create_unverified_context()
    if modo == "tls_antigo":
        contexto = ssl._create_unverified_context()
        contexto.set_ciphers("DEFAULT:@SECLEVEL=0")
        contexto.minimum_version = ssl.TLSVersion.TLSv1
        contexto.options |= getattr(ssl, "OP_LEGACY_SERVER_CONNECT", 0x4)
        return contexto
    return None


def detectar_formato(content_type: str, corpo: bytes, completo: bool) -> str:
    """Descobre o que a resposta contém: json, xml, csv, html (página de site) ou outro."""
    tipo = (content_type or "").lower()
    inicio = corpo.lstrip()[:200].lower()
    if "html" in tipo or inicio.startswith((b"<!doctype html", b"<html")):
        return "html"
    if "json" in tipo or inicio[:1] in (b"{", b"["):
        if completo:
            try:
                json.loads(corpo.decode("utf-8-sig"))
            except ValueError:
                return "outro"
        return "json"
    if "xml" in tipo or inicio.startswith(b"<"):
        return "xml"
    if "csv" in tipo:
        return "csv"
    return "outro"


def requisitar(
    url: str, modo: str = "normal", tempo_limite: float = TEMPO_LIMITE, aceitar_auth: bool = False
) -> dict:
    """Faz um GET e devolve o resultado. modo: normal, sem_certificado ou tls_antigo.

    Com aceitar_auth=True (APIs que exigem chave, testadas sem ela), respostas 400, 401 e 403
    contam como "no ar": o servidor respondeu e só recusou por falta da chave.
    """
    pedido = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/json, */*;q=0.8",
            "Origin": ORIGEM_TESTE,
        },
    )
    inicio = time.monotonic()
    try:
        with urllib.request.urlopen(pedido, timeout=tempo_limite, context=_contexto(modo)) as resposta:
            corpo = resposta.read(LIMITE_LEITURA + 1)
            codigo = resposta.status
            cabecalhos = resposta.headers
    except urllib.error.HTTPError as erro:
        codigo = erro.code
        cabecalhos = erro.headers
        corpo = b""
    except Exception as erro:  # timeout, DNS, TLS, conexão recusada...
        texto = descrever_erro(erro)
        return {
            "ok": False,
            "http": None,
            "ms": None,
            "cors": None,
            "erro": texto,
            "certificado_invalido": "CERTIFICATE_VERIFY_FAILED" in texto,
            "tls_antigo": any(sinal in texto for sinal in SINAIS_TLS_ANTIGO),
        }

    ms = round((time.monotonic() - inicio) * 1000)
    acao = (cabecalhos.get("Access-Control-Allow-Origin") or "").strip()
    cors = acao in ("*", ORIGEM_TESTE)
    # 429 significa que a API está no ar, apenas limitou a requisição.
    sucesso = 200 <= codigo < 300
    # Sem a chave, algumas APIs respondem 400 (pedido incompleto) em vez de 401/403.
    ok = sucesso or codigo == 429 or (aceitar_auth and codigo in (400, 401, 403))
    formato = None
    if sucesso:
        completo = len(corpo) <= LIMITE_LEITURA
        formato = detectar_formato(cabecalhos.get("Content-Type", ""), corpo[:LIMITE_LEITURA], completo)
    # Só confia no cabeçalho de CORS quando a resposta foi um sucesso normal.
    return {
        "ok": ok,
        "http": codigo,
        "ms": ms,
        "cors": cors if sucesso else None,
        "formato": formato,
        "erro": None if ok else f"HTTP {codigo}",
    }


def verificar_url(
    url: str,
    tempo_limite: float = TEMPO_LIMITE,
    espera: float = ESPERA_ANTES_DE_REPETIR,
    aceitar_auth: bool = False,
) -> dict:
    """Testa uma URL, repetindo uma vez em caso de falha e contornando problemas de TLS."""
    resultado = requisitar(url, tempo_limite=tempo_limite, aceitar_auth=aceitar_auth)
    if not resultado["ok"]:
        time.sleep(espera)
        resultado = requisitar(url, tempo_limite=tempo_limite, aceitar_auth=aceitar_auth)

    # Alguns servidores públicos enviam a cadeia de certificados incompleta: o navegador
    # aceita, mas clientes como Python e Node recusam. Testa de novo sem verificar o
    # certificado, só para saber se a API está no ar, e registra o aviso.
    if not resultado["ok"] and resultado.get("certificado_invalido"):
        resultado = requisitar(url, "sem_certificado", tempo_limite, aceitar_auth)
        resultado["aviso"] = AVISO_CERTIFICADO

    # Outros usam configurações de TLS antigas que o Python recusa por padrão.
    if not resultado["ok"] and resultado.get("tls_antigo"):
        resultado = requisitar(url, "tls_antigo", tempo_limite, aceitar_auth)
        resultado["aviso"] = AVISO_TLS_ANTIGO

    resultado.pop("certificado_invalido", None)
    resultado.pop("tls_antigo", None)
    if aceitar_auth:
        resultado["sem_chave"] = True
    return resultado


def verificar_lista(
    apis: dict,
    paralelo: int = 8,
    tempo_limite: float = TEMPO_LIMITE,
    espera: float = ESPERA_ANTES_DE_REPETIR,
) -> dict[str, dict]:
    """Recebe {nome: url} ou {nome: {"url": ..., "sem_chave": bool}} e devolve {nome: resultado}."""
    def testar(nome: str) -> dict:
        alvo = apis[nome]
        if isinstance(alvo, dict):
            return verificar_url(alvo["url"], tempo_limite, espera, bool(alvo.get("sem_chave")))
        return verificar_url(alvo, tempo_limite, espera)

    nomes = list(apis)
    with ThreadPoolExecutor(max_workers=paralelo) as executor:
        resultados = list(executor.map(testar, nomes))
    return dict(zip(nomes, resultados))


def processar_pedido(
    autorizacao: str,
    dados,
    tempo_limite: float = TEMPO_LIMITE,
    espera: float = ESPERA_ANTES_DE_REPETIR,
) -> tuple[dict, int]:
    """Valida a senha e o pedido de uma função HTTP e devolve (resposta, código HTTP).

    O pedido deve ser {"apis": {nome: url}} com o cabeçalho "Authorization: Bearer <token>".
    O token precisa ser igual à variável de ambiente TOKEN_VERIFICADOR da função.
    """
    esperado = os.environ.get("TOKEN_VERIFICADOR", "")
    if not esperado or not hmac.compare_digest(autorizacao or "", f"Bearer {esperado}"):
        return {"erro": "não autorizado"}, 401
    apis = (dados or {}).get("apis") if isinstance(dados, dict) else None
    validas = isinstance(apis, dict) and 0 < len(apis) <= 50 and all(
        isinstance(url, str) and url.startswith(("https://", "http://")) for url in apis.values()
    )
    if not validas:
        return {"erro": "envie {\"apis\": {nome: url}} com 1 a 50 URLs http(s)"}, 400
    return {"resultados": verificar_lista(apis, 32, tempo_limite, espera)}, 200


def verificar_http(request):
    """Ponto de entrada da função no Google Cloud (Cloud Run functions)."""
    return processar_pedido(request.headers.get("Authorization", ""), request.get_json(silent=True))


def lambda_handler(event, context):
    """Ponto de entrada da função na AWS. Recebe {"apis": {nome: url}}."""
    apis = event.get("apis") or {}
    return {"resultados": verificar_lista(apis, paralelo=16)}
