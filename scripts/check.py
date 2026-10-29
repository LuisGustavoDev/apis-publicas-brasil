"""Verifica se cada API está no ar e se aceita CORS.

Uso: python scripts/check.py
Faz uma requisição GET ao 'exemplo' de cada API (exceto as com teste: false)
e grava o resultado em data/status.json, mantendo um histórico curto.
"""

from __future__ import annotations

import ssl
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

from common import carregar_dados, carregar_status, deve_testar, salvar_status

TEMPO_LIMITE = 20  # segundos
ESPERA_ANTES_DE_REPETIR = 5  # segundos
TAMANHO_HISTORICO = 30  # dias guardados para calcular a disponibilidade
ORIGEM_TESTE = "https://example.com"
USER_AGENT = "apis-publicas-brasil/1.0 (verificacao diaria de disponibilidade)"


def descrever_erro(erro: Exception) -> str:
    """Transforma a exceção numa mensagem curta e legível para o log."""
    motivo = getattr(erro, "reason", erro)
    texto = str(motivo) or type(motivo).__name__
    return f"{type(motivo).__name__}: {texto}"[:200]


def erro_de_certificado(erro: Exception) -> bool:
    motivo = getattr(erro, "reason", erro)
    return isinstance(motivo, ssl.SSLCertVerificationError) or "CERTIFICATE_VERIFY_FAILED" in str(motivo)


def requisitar(url: str, verificar_certificado: bool = True) -> dict:
    pedido = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/json, */*;q=0.8",
            "Origin": ORIGEM_TESTE,
        },
    )
    contexto = None if verificar_certificado else ssl._create_unverified_context()
    inicio = time.monotonic()
    try:
        with urllib.request.urlopen(pedido, timeout=TEMPO_LIMITE, context=contexto) as resposta:
            resposta.read(65536)  # basta confirmar que o corpo começa a chegar
            codigo = resposta.status
            cabecalhos = resposta.headers
    except urllib.error.HTTPError as erro:
        codigo = erro.code
        cabecalhos = erro.headers
    except Exception as erro:  # timeout, DNS, TLS, conexão recusada...
        return {
            "ok": False,
            "http": None,
            "ms": None,
            "cors": None,
            "erro": descrever_erro(erro),
            "certificado_invalido": erro_de_certificado(erro),
        }

    ms = round((time.monotonic() - inicio) * 1000)
    acao = (cabecalhos.get("Access-Control-Allow-Origin") or "").strip()
    cors = acao in ("*", ORIGEM_TESTE)
    # 429 significa que a API está no ar, apenas limitou a requisição.
    sucesso = 200 <= codigo < 300
    ok = sucesso or codigo == 429
    # Só confia no cabeçalho de CORS quando a resposta foi um sucesso normal.
    erro = None if ok else f"HTTP {codigo}"
    return {"ok": ok, "http": codigo, "ms": ms, "cors": cors if sucesso else None, "erro": erro}


def verificar(api: dict) -> tuple[str, dict]:
    resultado = requisitar(api["exemplo"])
    if not resultado["ok"]:
        time.sleep(ESPERA_ANTES_DE_REPETIR)
        resultado = requisitar(api["exemplo"])

    # Alguns servidores públicos enviam a cadeia de certificados incompleta: o navegador
    # aceita, mas clientes como Python e Node recusam. Para saber se a API está no ar,
    # tenta de novo sem verificar o certificado e registra o aviso.
    if not resultado["ok"] and resultado.get("certificado_invalido"):
        resultado = requisitar(api["exemplo"], verificar_certificado=False)
        resultado["aviso"] = "certificado SSL inválido ou incompleto"

    return api["nome"], resultado


def main() -> None:
    dados = carregar_dados()
    status_anterior = carregar_status().get("apis", {})
    apis = [api for api in dados["apis"] if deve_testar(api)]

    with ThreadPoolExecutor(max_workers=8) as executor:
        resultados = dict(executor.map(verificar, apis))

    novo_status = {}
    for api in apis:
        nome = api["nome"]
        resultado = resultados[nome]
        anterior = status_anterior.get(nome, {})
        historico = (anterior.get("historico", []) + [1 if resultado["ok"] else 0])[-TAMANHO_HISTORICO:]

        # Se a verificação de hoje falhou, mantém o último CORS conhecido.
        cors = resultado["cors"] if resultado["cors"] is not None else anterior.get("cors")

        novo_status[nome] = {
            "ok": resultado["ok"],
            "http": resultado["http"],
            "ms": resultado["ms"],
            "cors": cors,
            "erro": resultado["erro"],
            "aviso": resultado.get("aviso"),
            "historico": historico,
        }
        simbolo = "OK  " if resultado["ok"] else "ERRO"
        detalhe = resultado["http"] if resultado["ok"] else resultado["erro"]
        aviso = f" [aviso: {resultado['aviso']}]" if resultado.get("aviso") else ""
        tempo = f"{resultado['ms']} ms" if resultado["ms"] is not None else "sem resposta"
        print(f"[{simbolo}] {nome}: {detalhe} ({tempo}){aviso}")

    salvar_status(
        {
            "verificado_em": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "apis": novo_status,
        }
    )
    online = sum(1 for s in novo_status.values() if s["ok"])
    print(f"\n{online} de {len(novo_status)} APIs verificadas estão no ar.")


if __name__ == "__main__":
    main()
