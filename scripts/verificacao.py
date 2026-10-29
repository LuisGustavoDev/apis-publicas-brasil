"""Testa se uma lista de APIs está no ar e se o que responde é, de fato, uma API.

Este arquivo é usado em dois lugares:
  1. Pelo robô do GitHub (scripts/check.py), que testa a partir dos EUA.
  2. Pela função da Vercel em São Paulo, que testa a partir do Brasil
     (api/verificar.py usa este arquivo direto; veja vercel/LEIA-ME.md).
Ele usa só a biblioteca padrão do Python.

Como a resposta é classificada (campo "formato"):
  json, xml, csv, outro  -> dados: a API respondeu com conteúdo de máquina
  documentacao           -> página de documentação de API (Swagger, Redoc, OpenAPI, WSDL...):
                            a API existe, mas o endereço testado não devolve dados
  bloqueio               -> página de firewall/captcha: o servidor está no ar, mas barrou o robô
  html                   -> página de site comum, sem sinais de ser uma API
"""

from __future__ import annotations

import hmac
import json
import os
import re
import ssl
import time
import urllib.error
import urllib.parse
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
LIMITE_LEITURA = 512 * 1024  # bytes lidos da resposta para conferir o conteúdo

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

# Sinais, no HTML, de que a página é a documentação de uma API.
SINAIS_DOCUMENTACAO = (
    "swagger-ui", "swaggerui", "swagger ui", "swagger.json", "swagger.yaml",
    "openapi.json", "openapi.yaml", "/api-docs", "v3/api-docs", "v2/api-docs",
    "redoc", "rapi-doc", "rapidoc", "stoplight", "@scalar/api-reference",
    "graphiql", "graphql-playground", "graphql playground",
    "wsdl", ".asmx", "service description", "web service",
    "api reference", "api documentation", "documentação da api", "documentacao da api",
)
# Sinais de página de firewall, captcha ou bloqueio de robôs.
SINAIS_BLOQUEIO = (
    "just a moment", "cf-browser-verification", "challenge-platform", "cf-chl",
    "attention required", "captcha", "request rejected", "the requested url was rejected",
    "access denied", "acesso negado", "incapsula", "ddos-guard", "sucuri", "bot protection",
)
# Onde procurar o arquivo OpenAPI a partir de uma página Swagger.
PADRAO_SPEC = re.compile(
    r"""["']([^"'\s<>]*?(?:swagger|openapi|api-docs)[^"'\s<>]*?)["']""", re.IGNORECASE
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


def analisar_html(corpo: bytes) -> str:
    """Diz se uma página HTML é documentação de API, bloqueio de robô ou um site comum."""
    texto = corpo[:LIMITE_LEITURA].decode("utf-8", "ignore").lower()
    if any(sinal in texto for sinal in SINAIS_BLOQUEIO):
        return "bloqueio"
    if any(sinal in texto for sinal in SINAIS_DOCUMENTACAO):
        return "documentacao"
    return "html"


def detectar_formato(content_type: str, corpo: bytes, completo: bool) -> str:
    """Classifica a resposta: json, xml, csv, outro, documentacao, bloqueio ou html."""
    tipo = (content_type or "").lower()
    inicio = corpo.lstrip()[:200].lower()
    if "html" in tipo or inicio.startswith((b"<!doctype html", b"<html")):
        return analisar_html(corpo)
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


def _get(url: str, modo: str, tempo_limite: float):
    pedido = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/json, */*;q=0.8",
            "Origin": ORIGEM_TESTE,
        },
    )
    return urllib.request.urlopen(pedido, timeout=tempo_limite, context=_contexto(modo))


def requisitar(
    url: str, modo: str = "normal", tempo_limite: float = TEMPO_LIMITE, aceitar_auth: bool = False
) -> dict:
    """Faz um GET e devolve o resultado. modo: normal, sem_certificado ou tls_antigo.

    Com aceitar_auth=True (APIs que exigem chave, testadas sem ela), respostas 400, 401 e 403
    contam como "no ar": o servidor respondeu e só recusou por falta da chave.
    """
    inicio = time.monotonic()
    try:
        with _get(url, modo, tempo_limite) as resposta:
            corpo = resposta.read(LIMITE_LEITURA + 1)
            codigo = resposta.status
            cabecalhos = resposta.headers
    except urllib.error.HTTPError as erro:
        codigo = erro.code
        cabecalhos = erro.headers
        try:
            corpo = erro.read(65536)
        except Exception:
            corpo = b""
    except Exception as erro:  # timeout, DNS, TLS, conexão recusada...
        texto = descrever_erro(erro)
        return {
            "ok": False,
            "http": None,
            "ms": None,
            "cors": None,
            "formato": None,
            "bloqueado": False,
            "erro": texto,
            "certificado_invalido": "CERTIFICATE_VERIFY_FAILED" in texto,
            "tls_antigo": any(sinal in texto for sinal in SINAIS_TLS_ANTIGO),
        }

    ms = round((time.monotonic() - inicio) * 1000)
    acao = (cabecalhos.get("Access-Control-Allow-Origin") or "").strip()
    cors = acao in ("*", ORIGEM_TESTE)
    sucesso = 200 <= codigo < 300
    formato = None
    if sucesso:
        completo = len(corpo) <= LIMITE_LEITURA
        formato = detectar_formato(cabecalhos.get("Content-Type", ""), corpo[:LIMITE_LEITURA], completo)

    # Sem a chave, algumas APIs respondem 400 (pedido incompleto) em vez de 401/403.
    resposta_de_chave = aceitar_auth and codigo in (400, 401, 403)
    # 401, 403 e 451, ou uma página de firewall, mostram que o servidor está no ar
    # mas recusou o robô: não é o mesmo que "fora do ar".
    pagina_de_bloqueio = formato == "bloqueio" or (
        not sucesso and corpo and analisar_html(corpo) == "bloqueio"
    )
    bloqueado = not resposta_de_chave and (codigo in (401, 403, 451) or pagina_de_bloqueio)

    # 429 significa que a API está no ar, apenas limitou a requisição.
    ok = (sucesso and formato != "bloqueio") or codigo == 429 or resposta_de_chave
    resultado = {
        "ok": ok,
        "http": codigo,
        "ms": ms,
        "cors": cors if sucesso else None,
        "formato": formato,
        "bloqueado": bloqueado,
        "erro": None if ok else ("recusou o robô (HTTP %d)" % codigo if bloqueado else f"HTTP {codigo}"),
    }
    if formato == "documentacao":
        resultado["_corpo"] = corpo[:LIMITE_LEITURA]  # usado para procurar o arquivo OpenAPI
    return resultado


def confirmar_openapi(url_pagina: str, corpo_html: bytes, tempo_limite: float) -> bool:
    """Procura, numa página de documentação, o arquivo OpenAPI/Swagger e confere se ele existe."""
    texto = corpo_html.decode("utf-8", "ignore")
    candidatos = []
    for trecho in PADRAO_SPEC.findall(texto):
        if trecho.lower().endswith((".js", ".css", ".png", ".svg", ".ico", ".html")):
            continue
        candidatos.append(urllib.parse.urljoin(url_pagina, trecho))
    base = url_pagina.split("#")[0]
    for caminho in ("openapi.json", "swagger.json", "v3/api-docs", "../v3/api-docs", "api-docs"):
        candidatos.append(urllib.parse.urljoin(base if base.endswith("/") else base + "/", caminho))
    vistos = set()
    for url in candidatos[:5]:
        if url in vistos or not url.startswith(("http://", "https://")):
            continue
        vistos.add(url)
        try:
            with _get(url, "sem_certificado", tempo_limite) as resposta:
                dados = json.loads(resposta.read(LIMITE_LEITURA).decode("utf-8-sig"))
            if isinstance(dados, dict) and ("openapi" in dados or "swagger" in dados):
                return True
        except Exception:
            continue
    return False


def verificar_url(
    url: str,
    tempo_limite: float = TEMPO_LIMITE,
    espera: float = ESPERA_ANTES_DE_REPETIR,
    aceitar_auth: bool = False,
) -> dict:
    """Testa uma URL, repetindo uma vez em caso de falha e contornando problemas de TLS."""
    resultado = requisitar(url, tempo_limite=tempo_limite, aceitar_auth=aceitar_auth)
    if not resultado["ok"] and not resultado["bloqueado"]:
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

    # Página de documentação: tenta achar o arquivo OpenAPI para confirmar que a API existe.
    corpo = resultado.pop("_corpo", None)
    if resultado.get("formato") == "documentacao" and corpo:
        resultado["openapi"] = confirmar_openapi(url, corpo, 5)

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


def _url_do_alvo(alvo) -> str | None:
    if isinstance(alvo, dict):
        alvo = alvo.get("url")
    return alvo if isinstance(alvo, str) and alvo.startswith(("https://", "http://")) else None


def processar_pedido(
    autorizacao: str,
    dados,
    tempo_limite: float = TEMPO_LIMITE,
    espera: float = ESPERA_ANTES_DE_REPETIR,
) -> tuple[dict, int]:
    """Valida a senha e o pedido de uma função HTTP e devolve (resposta, código HTTP).

    O pedido deve ser {"apis": {nome: url ou {"url": ..., "sem_chave": bool}}} com o
    cabeçalho "Authorization: Bearer <token>". O token precisa ser igual à variável de
    ambiente TOKEN_VERIFICADOR da função.
    """
    esperado = os.environ.get("TOKEN_VERIFICADOR", "")
    if not esperado or not hmac.compare_digest(autorizacao or "", f"Bearer {esperado}"):
        return {"erro": "não autorizado"}, 401
    apis = (dados or {}).get("apis") if isinstance(dados, dict) else None
    validas = isinstance(apis, dict) and 0 < len(apis) <= 50 and all(
        _url_do_alvo(alvo) for alvo in apis.values()
    )
    if not validas:
        return {"erro": "envie {\"apis\": {nome: url}} com 1 a 50 URLs http(s)"}, 400
    return {"resultados": verificar_lista(apis, 32, tempo_limite, espera)}, 200
