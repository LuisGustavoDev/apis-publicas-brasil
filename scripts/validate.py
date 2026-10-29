"""Valida o data/apis.yaml antes de gerar o README.

Uso: python scripts/validate.py
Sai com código 1 se encontrar algum erro.
"""

from __future__ import annotations

import sys

from common import ACESSOS, AUTENTICACOES, carregar_dados

CAMPOS_OBRIGATORIOS = ("nome", "categoria", "descricao", "docs", "autenticacao", "exemplo")
CAMPOS_PERMITIDOS = set(CAMPOS_OBRIGATORIOS) | {"limite", "teste", "acesso"}
TAMANHO_MAXIMO_DESCRICAO = 120


def validar(dados: dict) -> list[str]:
    erros: list[str] = []

    categorias = dados.get("categorias") or []
    ids_categorias = [c.get("id") for c in categorias]
    if len(ids_categorias) != len(set(ids_categorias)):
        erros.append("Há categorias com id repetido.")

    apis = dados.get("apis") or []
    if not apis:
        erros.append("Nenhuma API cadastrada.")

    nomes_vistos: set[str] = set()
    categorias_usadas: set[str] = set()

    for i, api in enumerate(apis, start=1):
        rotulo = f"API #{i} ({api.get('nome', 'sem nome')})"

        for campo in CAMPOS_OBRIGATORIOS:
            if not api.get(campo):
                erros.append(f"{rotulo}: campo obrigatório '{campo}' ausente.")

        for campo in api:
            if campo not in CAMPOS_PERMITIDOS:
                erros.append(f"{rotulo}: campo desconhecido '{campo}'.")

        nome = api.get("nome", "")
        chave_nome = nome.strip().lower()
        if chave_nome in nomes_vistos:
            erros.append(f"{rotulo}: nome repetido.")
        nomes_vistos.add(chave_nome)

        categoria = api.get("categoria")
        if categoria and categoria not in ids_categorias:
            erros.append(f"{rotulo}: categoria '{categoria}' não existe na lista de categorias.")
        categorias_usadas.add(categoria)

        autenticacao = api.get("autenticacao")
        if autenticacao and autenticacao not in AUTENTICACOES:
            opcoes = ", ".join(AUTENTICACOES)
            erros.append(f"{rotulo}: autenticacao '{autenticacao}' inválida. Use: {opcoes}.")

        for campo in ("docs", "exemplo"):
            valor = str(api.get(campo, ""))
            # Prefira https://. http:// é aceito para serviços oficiais que só respondem em HTTP.
            if valor and not valor.startswith(("https://", "http://")):
                erros.append(f"{rotulo}: '{campo}' precisa ser uma URL começando com https://.")

        descricao = str(api.get("descricao", ""))
        if descricao.endswith("."):
            erros.append(f"{rotulo}: tire o ponto final da descrição.")
        if len(descricao) > TAMANHO_MAXIMO_DESCRICAO:
            erros.append(
                f"{rotulo}: descrição com {len(descricao)} caracteres "
                f"(máximo {TAMANHO_MAXIMO_DESCRICAO})."
            )

        acesso = api.get("acesso")
        if acesso is not None and acesso not in ACESSOS:
            erros.append(f"{rotulo}: acesso '{acesso}' inválido. Use: {', '.join(ACESSOS)}.")

        teste = api.get("teste", True)
        if not isinstance(teste, bool):
            erros.append(f"{rotulo}: 'teste' deve ser true ou false.")

    for categoria in categorias:
        if categoria.get("id") not in categorias_usadas:
            erros.append(f"Categoria '{categoria.get('id')}' não tem nenhuma API.")

    return erros


def main() -> int:
    erros = validar(carregar_dados())
    if erros:
        print("Foram encontrados problemas no data/apis.yaml:\n")
        for erro in erros:
            print(f"  - {erro}")
        return 1
    print("data/apis.yaml está válido.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
