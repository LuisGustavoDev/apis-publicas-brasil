"""Funções compartilhadas pelos scripts do repositório."""

from __future__ import annotations

import json
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parent.parent
ARQUIVO_APIS = RAIZ / "data" / "apis.yaml"
ARQUIVO_STATUS = RAIZ / "data" / "status.json"

AUTENTICACOES = {
    "nenhuma": "Não",
    "opcional": "Opcional",
    "chave": "Chave grátis",
    "chave-publica": "Chave pública",
    "token": "Token grátis",
}


def carregar_dados() -> dict:
    with ARQUIVO_APIS.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


ACESSOS = {"brasil": "só acessível do Brasil"}


def exemplo_testavel(api: dict) -> bool:
    """O 'exemplo' é uma URL de dados que funciona sem chave (teste diferente de false)."""
    return api.get("teste", True) is not False


def testa_sem_chave(api: dict) -> bool:
    """API que exige chave, mas é testada sem ela: 401/403 contam como 'no ar'."""
    return not exemplo_testavel(api) and bool(api.get("teste_sem_chave"))


def deve_testar(api: dict) -> bool:
    return exemplo_testavel(api) or testa_sem_chave(api)


def url_teste(api: dict) -> str:
    return api["teste_sem_chave"] if testa_sem_chave(api) else api["exemplo"]


def so_do_brasil(api: dict) -> bool:
    return api.get("acesso") == "brasil"


def carregar_status() -> dict:
    if not ARQUIVO_STATUS.exists():
        return {"verificado_em": None, "apis": {}}
    with ARQUIVO_STATUS.open(encoding="utf-8") as f:
        return json.load(f)


def salvar_status(status: dict) -> None:
    with ARQUIVO_STATUS.open("w", encoding="utf-8") as f:
        json.dump(status, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")
