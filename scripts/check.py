"""Verifica se cada API está no ar, se responde com dados e de onde ela funciona.

Uso: python scripts/check.py

Cada API é testada de dois lugares:
  1. Do Brasil, pela função da Vercel em São Paulo (veja vercel/LEIA-ME.md).
     Esse é o resultado oficial que aparece no README.
  2. Dos EUA, pelo próprio robô do GitHub. Serve de segunda opinião: quando uma API funciona
     do Brasil e falha dos EUA, ela é marcada automaticamente como "só do Brasil".
Sem a função em São Paulo configurada, vale o resultado dos EUA.

O resultado vai para data/status.json, com um histórico curto para calcular a disponibilidade.
"""

from __future__ import annotations

import json
import os
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

from common import (
    carregar_dados,
    carregar_status,
    deve_testar,
    salvar_status,
    testa_sem_chave,
    url_teste,
)
from verificacao import verificar_lista

TAMANHO_HISTORICO = 30  # dias guardados para calcular a disponibilidade
TAMANHO_LOTE = 30  # APIs por chamada à função em São Paulo (cabe no limite de 60 s da Vercel)
LOTES_SIMULTANEOS = 3
# Função HTTP da Vercel em São Paulo.
FUNCAO_URL = os.environ.get("VERIFICADOR_BR_URL", "").strip()
FUNCAO_TOKEN = os.environ.get("VERIFICADOR_BR_TOKEN", "").strip()


def funcao_http_configurada() -> bool:
    return bool(FUNCAO_URL and FUNCAO_TOKEN)


def verificar_pela_funcao_http(apis: dict) -> dict[str, dict] | None:
    """Pede para a função da Vercel em São Paulo testar as APIs. Devolve None se falhar."""
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


def verificar_em_lotes(apis: dict) -> dict[str, dict] | None:
    """Divide as APIs em lotes e envia cada um para a função HTTP em São Paulo."""
    nomes = list(apis)
    lotes = [
        {nome: apis[nome] for nome in nomes[i : i + TAMANHO_LOTE]}
        for i in range(0, len(nomes), TAMANHO_LOTE)
    ]
    with ThreadPoolExecutor(max_workers=LOTES_SIMULTANEOS) as executor:
        respostas = list(executor.map(verificar_pela_funcao_http, lotes))
    juntos: dict[str, dict] = {}
    for resposta in respostas:
        if resposta:
            juntos.update(resposta)
    falhas = sum(1 for r in respostas if r is None)
    if falhas:
        print(f"Aviso: {falhas} de {len(lotes)} lotes não puderam ser testados em São Paulo.")
    return juntos or None


def descrever(resultado: dict) -> str:
    if resultado["ok"]:
        texto = str(resultado["http"])
        formato = resultado.get("formato")
        if formato == "documentacao":
            texto += " documentação de API" + (" (OpenAPI confirmado)" if resultado.get("openapi") else "")
        elif formato == "html":
            texto += " página de site, sem dados"
        elif formato:
            texto += f" {formato}"
        if resultado.get("sem_chave"):
            texto += " [testada sem chave]"
        if resultado.get("aviso"):
            texto += f" [aviso: {resultado['aviso']}]"
        return texto
    return resultado["erro"] or "falhou"


def main() -> None:
    dados = carregar_dados()
    status_anterior = carregar_status().get("apis", {})
    alvos = {
        api["nome"]: {"url": url_teste(api), "sem_chave": testa_sem_chave(api)}
        for api in dados["apis"]
        if deve_testar(api)
    }

    print(f"Testando {len(alvos)} APIs a partir dos EUA (robô do GitHub)...")
    dos_eua = verificar_lista(alvos)

    do_brasil = None
    if funcao_http_configurada():
        print(f"Testando {len(alvos)} APIs a partir de São Paulo (função HTTP)...")
        do_brasil = verificar_em_lotes(alvos)
    else:
        print("Função em São Paulo não configurada: vale o resultado dos EUA.")
    do_brasil = do_brasil or {}

    novo_status = {}
    for nome in alvos:
        eua = dos_eua[nome]
        brasil = do_brasil.get(nome)
        anterior = status_anterior.get(nome, {})

        if brasil is None and anterior.get("so_do_brasil") and not eua["ok"]:
            # Hoje não deu para testar do Brasil uma API que só funciona de lá:
            # mantém o último resultado em vez de marcá-la como fora do ar.
            novo_status[nome] = anterior
            print(f"[MANTIDA] {nome}: sem teste de São Paulo hoje; mantido o último resultado")
            continue

        oficial = brasil if brasil is not None else eua
        so_do_brasil = bool(brasil and brasil["ok"] and not eua["ok"])
        historico = (anterior.get("historico", []) + [1 if oficial["ok"] else 0])[-TAMANHO_HISTORICO:]
        # Se a verificação de hoje falhou, mantém o último CORS conhecido.
        cors = oficial.get("cors") if oficial.get("cors") is not None else anterior.get("cors")
        novo_status[nome] = {
            "ok": oficial["ok"],
            "http": oficial["http"],
            "ms": oficial["ms"],
            "cors": cors,
            "erro": oficial["erro"],
            "aviso": oficial.get("aviso"),
            "formato": oficial.get("formato"),
            "openapi": oficial.get("openapi"),
            "bloqueado": bool(oficial.get("bloqueado")),
            "sem_chave": bool(oficial.get("sem_chave")),
            "testada_de": "brasil" if brasil is not None else "eua",
            "funciona_do_exterior": eua["ok"],
            "so_do_brasil": so_do_brasil,
            "historico": historico,
        }
        simbolo = "OK  " if oficial["ok"] else "ERRO"
        tempo = f"{oficial['ms']} ms" if oficial["ms"] is not None else "sem resposta"
        origem = "BR" if brasil is not None else "EUA"
        extra = ""
        if brasil is not None:
            extra = f" | EUA: {'ok' if eua['ok'] else descrever(eua)}"
        if so_do_brasil:
            extra += " -> só do Brasil"
        print(f"[{simbolo}] {nome} ({origem}): {descrever(oficial)} ({tempo}){extra}")

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
