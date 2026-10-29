"""Verifica se cada API está no ar e se aceita CORS.

Uso: python scripts/check.py
Faz uma requisição GET ao 'exemplo' de cada API (exceto as com teste: false)
e grava o resultado em data/status.json, mantendo um histórico curto.
"""

from __future__ import annotations

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


def requisitar(url: str) -> dict:
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
        with urllib.request.urlopen(pedido, timeout=TEMPO_LIMITE) as resposta:
            resposta.read(65536)  # basta confirmar que o corpo começa a chegar
            codigo = resposta.status
            cabecalhos = resposta.headers
    except urllib.error.HTTPError as erro:
        codigo = erro.code
        cabecalhos = erro.headers
    except Exception as erro:  # timeout, DNS, TLS, conexão recusada...
        return {"ok": False, "http": None, "ms": None, "cors": None, "erro": type(erro).__name__}

    ms = round((time.monotonic() - inicio) * 1000)
    acao = (cabecalhos.get("Access-Control-Allow-Origin") or "").strip()
    cors = acao in ("*", ORIGEM_TESTE)
    # 429 significa que a API está no ar, apenas limitou a requisição.
    sucesso = 200 <= codigo < 300
    ok = sucesso or codigo == 429
    # Só confia no cabeçalho de CORS quando a resposta foi um sucesso normal.
    return {"ok": ok, "http": codigo, "ms": ms, "cors": cors if sucesso else None, "erro": None}


def verificar(api: dict) -> tuple[str, dict]:
    resultado = requisitar(api["exemplo"])
    if not resultado["ok"]:
        time.sleep(ESPERA_ANTES_DE_REPETIR)
        resultado = requisitar(api["exemplo"])
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
            "historico": historico,
        }
        simbolo = "OK " if resultado["ok"] else "ERRO"
        detalhe = resultado["http"] or resultado["erro"]
        print(f"[{simbolo}] {nome}: {detalhe} ({resultado['ms']} ms)")

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
