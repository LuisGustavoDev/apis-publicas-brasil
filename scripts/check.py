"""Verifica se cada API está no ar e se aceita CORS.

Uso: python scripts/check.py
Faz uma requisição GET ao 'exemplo' de cada API (exceto as com teste: false)
e grava o resultado em data/status.json, mantendo um histórico curto.

As APIs marcadas com 'acesso: brasil' bloqueiam acessos de fora do país. Elas são
testadas por uma função na nuvem, em São Paulo, quando ela está configurada:
na Vercel (veja vercel/LEIA-ME.md), no Google Cloud (veja google/LEIA-ME.md)
ou na AWS (veja aws/LEIA-ME.md). Sem nenhuma, essas APIs ficam sem teste.
"""

from __future__ import annotations

import json
import os
import subprocess
import tempfile
import urllib.request
from datetime import datetime, timezone

from common import (
    carregar_dados,
    carregar_status,
    deve_testar,
    salvar_status,
    so_do_brasil,
    testa_sem_chave,
    url_teste,
)
from verificacao import verificar_lista

TAMANHO_HISTORICO = 30  # dias guardados para calcular a disponibilidade
FUNCAO_LAMBDA = os.environ.get("AWS_LAMBDA_FUNCAO", "verificador-apis-brasil")
REGIAO_LAMBDA = os.environ.get("AWS_LAMBDA_REGIAO", "sa-east-1")
# Função HTTP em São Paulo (Vercel ou Google Cloud). Os nomes GCP_* são aceitos por compatibilidade.
FUNCAO_URL = (os.environ.get("VERIFICADOR_BR_URL") or os.environ.get("GCP_VERIFICADOR_URL") or "").strip()
FUNCAO_TOKEN = (os.environ.get("VERIFICADOR_BR_TOKEN") or os.environ.get("GCP_VERIFICADOR_TOKEN") or "").strip()


def funcao_http_configurada() -> bool:
    return bool(FUNCAO_URL and FUNCAO_TOKEN)


def verificar_pela_funcao_http(apis: dict[str, str]) -> dict[str, dict] | None:
    """Pede para a função em São Paulo (Vercel ou Google Cloud) testar as APIs. Devolve None se falhar."""
    pedido = urllib.request.Request(
        FUNCAO_URL,
        data=json.dumps({"apis": apis}).encode("utf-8"),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {FUNCAO_TOKEN}"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(pedido, timeout=400) as resposta:
            return json.loads(resposta.read().decode("utf-8")).get("resultados")
    except Exception as erro:
        print(f"Aviso: a chamada à função em São Paulo falhou ({erro}).")
        return None


def aws_configurada() -> bool:
    return bool(os.environ.get("AWS_ACCESS_KEY_ID") and os.environ.get("AWS_SECRET_ACCESS_KEY"))


def verificar_pelo_brasil(apis: dict[str, str]) -> dict[str, dict] | None:
    """Pede para a função na AWS (São Paulo) testar as APIs. Devolve None se falhar."""
    with tempfile.TemporaryDirectory() as pasta:
        saida = os.path.join(pasta, "saida.json")
        comando = [
            "aws", "lambda", "invoke",
            "--function-name", FUNCAO_LAMBDA,
            "--region", REGIAO_LAMBDA,
            "--cli-binary-format", "raw-in-base64-out",
            "--cli-read-timeout", "360",
            "--payload", json.dumps({"apis": apis}),
            saida,
        ]
        try:
            execucao = subprocess.run(comando, capture_output=True, text=True, timeout=400)
        except Exception as erro:
            print(f"Aviso: não foi possível chamar a função na AWS ({erro}).")
            return None
        if execucao.returncode != 0:
            print(f"Aviso: a chamada à função na AWS falhou: {execucao.stderr.strip()[:500]}")
            return None
        if "FunctionError" in execucao.stdout:
            with open(saida, encoding="utf-8") as f:
                print(f"Aviso: a função na AWS deu erro: {f.read()[:500]}")
            return None
        with open(saida, encoding="utf-8") as f:
            return json.load(f).get("resultados")


def imprimir(nome: str, resultado: dict, origem: str = "") -> None:
    simbolo = "OK  " if resultado["ok"] else "ERRO"
    detalhe = resultado["http"] if resultado["ok"] else resultado["erro"]
    aviso = f" [aviso: {resultado['aviso']}]" if resultado.get("aviso") else ""
    if resultado.get("formato") == "html":
        aviso += " [atenção: devolveu uma página HTML, não dados]"
    if resultado.get("sem_chave"):
        aviso += " [testada sem chave]"
    tempo = f"{resultado['ms']} ms" if resultado["ms"] is not None else "sem resposta"
    print(f"[{simbolo}] {nome}: {detalhe} ({tempo}){aviso}{origem}")


def main() -> None:
    dados = carregar_dados()
    status_anterior = carregar_status().get("apis", {})
    testaveis = [api for api in dados["apis"] if deve_testar(api)]
    daqui = {
        api["nome"]: {"url": url_teste(api), "sem_chave": testa_sem_chave(api)}
        for api in testaveis
        if not so_do_brasil(api)
    }
    do_brasil = {api["nome"]: url_teste(api) for api in testaveis if so_do_brasil(api)}

    resultados = verificar_lista(daqui)

    mantidas: set[str] = set()
    resultados_brasil = None
    if do_brasil and funcao_http_configurada():
        print(f"Testando {len(do_brasil)} APIs pela função em São Paulo...")
        resultados_brasil = verificar_pela_funcao_http(do_brasil)
    elif do_brasil and aws_configurada():
        print(f"Testando {len(do_brasil)} APIs pela função na AWS em São Paulo...")
        resultados_brasil = verificar_pelo_brasil(do_brasil)
    elif do_brasil:
        print(f"{len(do_brasil)} APIs só acessíveis do Brasil ficaram sem teste (nenhuma função em São Paulo configurada).")

    if do_brasil and (funcao_http_configurada() or aws_configurada()):
        if resultados_brasil is None:
            # A falha foi na função em São Paulo, não nas APIs: mantém o último status conhecido.
            mantidas = {nome for nome in do_brasil if nome in status_anterior}
        else:
            resultados.update(resultados_brasil)

    novo_status = {}
    for nome in mantidas:
        novo_status[nome] = status_anterior[nome]

    for nome, resultado in resultados.items():
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
            "formato": resultado.get("formato"),
            "sem_chave": bool(resultado.get("sem_chave")),
            "historico": historico,
        }
        imprimir(nome, resultado, " [testada do Brasil]" if nome in do_brasil else "")

    salvar_status(
        {
            "verificado_em": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "apis": novo_status,
        }
    )
    online = sum(1 for nome in resultados if resultados[nome]["ok"])
    print(f"\n{online} de {len(resultados)} APIs verificadas estão no ar.")


if __name__ == "__main__":
    main()
