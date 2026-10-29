"""Gera o README.md a partir de data/apis.yaml, data/status.json e do modelo.

Uso: python scripts/build_readme.py
"""

from __future__ import annotations

import re
import unicodedata
from datetime import datetime
from pathlib import Path
from urllib.parse import quote

from common import (
    AUTENTICACOES,
    RAIZ,
    carregar_dados,
    carregar_status,
    deve_testar,
    exemplo_testavel,
    so_do_brasil,
)

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


# Situações possíveis de uma API, na ordem em que aparecem nos resumos:
# chave: (emoji, nome no singular, nome no plural, o que significa)
SITUACOES = {
    "online": ("🟢", "online", "online", "respondeu com dados (JSON, XML ou CSV) na última verificação"),
    "lenta": ("🟡", "lenta", "lentas", "respondeu, mas levou mais de 3 segundos"),
    "instavel": ("🟠", "instável", "instáveis", "está no ar, mas falhou em mais de 5% das verificações dos últimos 30 dias"),
    "fora": ("🔴", "fora do ar", "fora do ar", "não respondeu ou deu erro na última verificação"),
    "pagina": ("🟣", "não é API", "não são API", "o endereço de exemplo devolveu uma página de site (HTML), não dados"),
    "chave": ("🔑", "requer chave", "requerem chave", "precisa de chave ou cadastro, por isso não é testada automaticamente"),
    "brasil": ("🇧🇷", "só do Brasil", "só do Brasil", "bloqueia acessos de fora do país e ainda não foi testada a partir de São Paulo"),
    "aguardando": ("⚪", "aguardando", "aguardando", "entrou na lista e ainda não passou pela primeira verificação"),
}


def disponibilidade(info: dict) -> int:
    historico = info.get("historico") or [1]
    return round(100 * sum(historico) / len(historico))


def classificar(api: dict, status: dict) -> str:
    """Devolve a situação da API: uma das chaves de SITUACOES."""
    if not deve_testar(api):
        return "chave"
    info = status.get(api["nome"])
    if not info:
        return "brasil" if so_do_brasil(api) else "aguardando"
    if not info["ok"]:
        return "fora"
    if info.get("formato") == "html":
        return "pagina"
    ms = info.get("ms")
    if ms and ms > LIMITE_LENTA_MS:
        return "lenta"
    if disponibilidade(info) < LIMITE_INSTAVEL:
        return "instavel"
    return "online"


def rotulo(situacao: str) -> str:
    emoji, singular, _, _ = SITUACOES[situacao]
    return f"{emoji} {singular}"


def contar(apis: list[dict], status: dict) -> dict[str, int]:
    contagem = {chave: 0 for chave in SITUACOES}
    for api in apis:
        contagem[classificar(api, status)] += 1
    return contagem


def resumo_curto(contagem: dict[str, int]) -> str:
    """Ex.: '🟢 6 · 🟡 1 · 🔴 1 · 🔑 2' (só as situações que aparecem)."""
    return " · ".join(f"{SITUACOES[c][0]} {n}" for c, n in contagem.items() if n)


def linha_resumo(contagem: dict[str, int]) -> str:
    """Ex.: '🟢 136 online · 🔴 30 fora do ar · 🔑 34 requerem chave'."""
    partes = []
    for chave, (emoji, singular, plural, _) in SITUACOES.items():
        n = contagem[chave]
        if n:
            partes.append(f"{emoji} **{n}** {singular if n == 1 else plural}")
    return " · ".join(partes)


def tabela_resumo(contagem: dict[str, int], total: int) -> str:
    linhas = ["| | Situação | APIs | O que significa |", "|:---:|---|:---:|---|"]
    sempre = ("online", "lenta", "instavel", "fora", "chave")
    for chave, (emoji, _, plural, significado) in SITUACOES.items():
        if contagem[chave] or chave in sempre:
            nome = plural[0].upper() + plural[1:]
            linhas.append(f"| {emoji} | {nome} | **{contagem[chave]}** | {significado} |")
    linhas.append(f"| | **Total** | **{total}** | |")
    return "\n".join(linhas)


def celula_status(api: dict, status: dict) -> str:
    situacao = classificar(api, status)
    brasil = so_do_brasil(api)
    if situacao in ("chave", "brasil", "aguardando"):
        return rotulo(situacao)
    info = status[api["nome"]]
    if situacao == "fora":
        detalhe = "🇧🇷 só do Brasil" if brasil else ""
        return rotulo(situacao) + (f"<br><sub>{detalhe}</sub>" if detalhe else "")

    ms = info.get("ms")
    detalhes = f"{disponibilidade(info)}%"
    if ms:
        detalhes += f" · {ms} ms"
    if info.get("aviso") == "certificado SSL inválido ou incompleto":
        detalhes += " · ⚠️ certificado SSL"
    elif info.get("aviso"):
        detalhes += " · ⚠️ TLS antigo"
    if info.get("sem_chave"):
        detalhes += " · 🔑 testada sem chave"
    if brasil:
        detalhes += " · 🇧🇷 só do Brasil"
    return f"{rotulo(situacao)}<br><sub>{detalhes}</sub>"


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
    if exemplo_testavel(api):
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
        resumo = resumo_curto(contar(apis, status))
        indice.append(f"- [{titulo}](#{ancora(titulo)}) ({len(apis)}) — {resumo}")

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
    contagem_geral = contar(dados["apis"], status)
    resumo = linha_resumo(contagem_geral) + "\n\n" + tabela_resumo(contagem_geral, total)
    badges = " ".join([badge("APIs", str(total), "009c3b"), *badges_status])

    conteudo = MODELO.read_text(encoding="utf-8")
    substituicoes = {
        "{{BADGES}}": badges,
        "{{TOTAL}}": str(total),
        "{{TOTAL_CATEGORIAS}}": str(len(dados["categorias"])),
        "{{VERIFICACAO}}": texto_verificacao,
        "{{RESUMO}}": resumo,
        "{{INDICE}}": indice,
        "{{TABELAS}}": tabelas,
    }
    for marcador, valor in substituicoes.items():
        conteudo = conteudo.replace(marcador, valor)

    SAIDA.write_text(conteudo, encoding="utf-8")
    print(f"README.md gerado com {total} APIs.")


if __name__ == "__main__":
    main()
