"""Gera o README.md a partir de data/apis.yaml, data/status.json e do modelo.

Uso: python scripts/build_readme.py
"""

from __future__ import annotations

import re
import unicodedata
from datetime import datetime
from pathlib import Path
from urllib.parse import quote

from common import AUTENTICACOES, RAIZ, carregar_dados, carregar_status, deve_testar

MODELO = Path(__file__).resolve().parent / "README.template.md"
SAIDA = RAIZ / "README.md"
LIMITE_LENTA_MS = 3000
LIMITE_INSTAVEL = 95  # % de disponibilidade abaixo do qual a API é marcada como instável


def ancora(texto: str) -> str:
    """Gera a âncora no mesmo formato que o GitHub usa nos títulos."""
    texto = texto.strip().lower()
    texto = re.sub(r"[^\w\- ]", "", texto, flags=re.UNICODE)
    return texto.replace(" ", "-")


def escapar(texto: str) -> str:
    return str(texto).replace("|", "\\|")


def celula_status(api: dict, status: dict) -> str:
    if not deve_testar(api):
        return "🔑 requer chave"
    info = status.get(api["nome"])
    if not info:
        return "⚪ aguardando"
    if not info["ok"]:
        return "🔴 fora do ar"

    historico = info.get("historico") or [1]
    disponibilidade = round(100 * sum(historico) / len(historico))
    ms = info.get("ms")

    if ms and ms > LIMITE_LENTA_MS:
        rotulo = "🟡 lenta"
    elif disponibilidade < LIMITE_INSTAVEL:
        rotulo = "🟡 instável"
    else:
        rotulo = "🟢 online"

    detalhes = f"{disponibilidade}%"
    if ms:
        detalhes += f" · {ms} ms"
    return f"{rotulo}<br><sub>{detalhes}</sub>"


def celula_cors(api: dict, status: dict) -> str:
    cors = (status.get(api["nome"]) or {}).get("cors")
    if cors is True:
        return "Sim"
    if cors is False:
        return "Não"
    return "?"


def celula_api(api: dict) -> str:
    return f"[{escapar(api['nome'])}]({api['docs']})"


def celula_descricao(api: dict) -> str:
    texto = escapar(api["descricao"])
    extras = []
    if deve_testar(api):
        extras.append(f"[exemplo]({api['exemplo']})")
    if api.get("limite"):
        extras.append(f"limite: {escapar(api['limite'])}")
    if extras:
        texto += "<br><sub>" + " · ".join(extras) + "</sub>"
    return texto


def gerar_tabelas(dados: dict, status: dict) -> tuple[str, str]:
    indice, secoes = [], []
    for categoria in dados["categorias"]:
        apis = [a for a in dados["apis"] if a["categoria"] == categoria["id"]]
        apis.sort(key=lambda a: unicodedata.normalize("NFKD", a["nome"].lower()))
        titulo = categoria["nome"]
        indice.append(f"- [{titulo}](#{ancora(titulo)}) ({len(apis)})")

        linhas = [
            f"### {titulo}",
            "",
            "| API | Descrição | Autenticação | CORS | Status |",
            "|---|---|:---:|:---:|:---:|",
        ]
        for api in apis:
            linhas.append(
                "| "
                + " | ".join(
                    [
                        celula_api(api),
                        celula_descricao(api),
                        AUTENTICACOES[api["autenticacao"]],
                        celula_cors(api, status),
                        celula_status(api, status),
                    ]
                )
                + " |"
            )
        linhas.append("")
        linhas.append("**[⬆ voltar ao índice](#índice)**")
        secoes.append("\n".join(linhas))

    return "\n".join(indice), "\n\n".join(secoes)


def badge(rotulo: str, valor: str, cor: str) -> str:
    def q(s: str) -> str:
        return quote(s.replace("-", "--").replace("_", "__"), safe="")

    return f"![{rotulo}: {valor}](https://img.shields.io/badge/{q(rotulo)}-{q(valor)}-{cor})"


def main() -> None:
    dados = carregar_dados()
    status_completo = carregar_status()
    status = status_completo.get("apis", {})

    total = len(dados["apis"])
    verificadas = [a for a in dados["apis"] if deve_testar(a) and a["nome"] in status]
    online = sum(1 for a in verificadas if status[a["nome"]]["ok"])

    verificado_em = status_completo.get("verificado_em")
    if verificado_em:
        data = datetime.strptime(verificado_em, "%Y-%m-%dT%H:%M:%SZ").strftime("%d/%m/%Y")
        texto_verificacao = f"Última verificação automática: **{data}** · {online} de {len(verificadas)} APIs testadas estão no ar."
        badges_status = [
            badge("online", f"{online}/{len(verificadas)}", "2ea44f" if online == len(verificadas) else "dfb317"),
            badge("verificado em", data, "blue"),
        ]
    else:
        texto_verificacao = "A primeira verificação automática ainda não rodou."
        badges_status = [badge("verificação", "aguardando", "lightgrey")]

    indice, tabelas = gerar_tabelas(dados, status)
    badges = " ".join([badge("APIs", str(total), "009c3b"), *badges_status])

    conteudo = MODELO.read_text(encoding="utf-8")
    substituicoes = {
        "{{BADGES}}": badges,
        "{{TOTAL}}": str(total),
        "{{TOTAL_CATEGORIAS}}": str(len(dados["categorias"])),
        "{{VERIFICACAO}}": texto_verificacao,
        "{{INDICE}}": indice,
        "{{TABELAS}}": tabelas,
    }
    for marcador, valor in substituicoes.items():
        conteudo = conteudo.replace(marcador, valor)

    SAIDA.write_text(conteudo, encoding="utf-8")
    print(f"README.md gerado com {total} APIs.")


if __name__ == "__main__":
    main()
