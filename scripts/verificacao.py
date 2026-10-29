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
import os
import ssl
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

TEMPO_LIMITE = 30  # segundos por requisição
ESPERA_ANTES_DE_REPETIR = 5  # segundos
ORIGEM_TESTE = "https://example.com"
USER_AGENT = "apis-publicas-brasil/1.0 (verificacao diaria de disponibilidade)"

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


def requisitar(url: str, modo: str = "normal", tempo_limite: float = TEMPO_LIMITE) -> dict:
    """Faz um GET e devolve o resultado. modo: normal, sem_certificado ou tls_antigo."""
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
            resposta.read(65536)  # basta confirmar que o corpo começa a chegar
            codigo = resposta.status
            cabecalhos = resposta.headers
    except urllib.error.HTTPError as erro:
        codigo = erro.code
        cabecalhos = erro.headers
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
    ok = sucesso or codigo == 429
    # Só confia no cabeçalho de CORS quando a resposta foi um sucesso normal.
    return {
        "ok": ok,
        "http": codigo,
        "ms": ms,
        "cors": cors if sucesso else None,
        "erro": None if ok else f"HTTP {codigo}",
    }


def verificar_url(
    url: str, tempo_limite: float = TEMPO_LIMITE, espera: float = ESPERA_ANTES_DE_REPETIR
) -> dict:
    """Testa uma URL, repetindo uma vez em caso de falha e contornando problemas de TLS."""
    resultado = requisitar(url, tempo_limite=tempo_limite)
    if not resultado["ok"]:
        time.sleep(espera)
        resultado = requisitar(url, tempo_limite=tempo_limite)

    # Alguns servidores públicos enviam a cadeia de certificados incompleta: o navegador
    # aceita, mas clientes como Python e Node recusam. Testa de novo sem verificar o
    # certificado, só para saber se a API está no ar, e registra o aviso.
    if not resultado["ok"] and resultado.get("certificado_invalido"):
        resultado = requisitar(url, modo="sem_certificado", tempo_limite=tempo_limite)
        resultado["aviso"] = AVISO_CERTIFICADO

    # Outros usam configurações de TLS antigas que o Python recusa por padrão.
    if not resultado["ok"] and resultado.get("tls_antigo"):
        resultado = requisitar(url, modo="tls_antigo", tempo_limite=tempo_limite)
        resultado["aviso"] = AVISO_TLS_ANTIGO

    resultado.pop("certificado_invalido", None)
    resultado.pop("tls_antigo", None)
    return resultado


def verificar_lista(
    apis: dict[str, str],
    paralelo: int = 8,
    tempo_limite: float = TEMPO_LIMITE,
    espera: float = ESPERA_ANTES_DE_REPETIR,
) -> dict[str, dict]:
    """Recebe {nome: url} e devolve {nome: resultado}."""
    nomes = list(apis)
    with ThreadPoolExecutor(max_workers=paralelo) as executor:
        resultados = list(
            executor.map(lambda nome: verificar_url(apis[nome], tempo_limite, espera), nomes)
        )
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
    return {"resultados": verificar_lista(apis, 16, tempo_limite, espera)}, 200


def verificar_http(request):
    """Ponto de entrada da função no Google Cloud (Cloud Run functions)."""
    return processar_pedido(request.headers.get("Authorization", ""), request.get_json(silent=True))


def lambda_handler(event, context):
    """Ponto de entrada da função na AWS. Recebe {"apis": {nome: url}}."""
    apis = event.get("apis") or {}
    return {"resultados": verificar_lista(apis, paralelo=16)}
