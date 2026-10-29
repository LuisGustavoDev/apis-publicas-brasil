"""Função da Vercel que testa, a partir de São Paulo, as APIs que bloqueiam acessos de fora do Brasil.

A região (gru1, São Paulo) e o tempo máximo ficam no vercel.json. A lógica dos testes
é a mesma do robô do GitHub e vem de scripts/verificacao.py. Guia: vercel/LEIA-ME.md.
"""

import json
import os
import sys
from http.server import BaseHTTPRequestHandler

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"))

from verificacao import processar_pedido  # noqa: E402

TAMANHO_MAXIMO = 100_000  # bytes aceitos no corpo do pedido


class handler(BaseHTTPRequestHandler):
    def _responder(self, dados: dict, codigo: int) -> None:
        corpo = json.dumps(dados, ensure_ascii=False).encode("utf-8")
        self.send_response(codigo)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(corpo)))
        self.end_headers()
        self.wfile.write(corpo)

    def do_GET(self) -> None:
        self._responder({"status": "no ar", "uso": "POST com {\"apis\": {nome: url}} e senha"}, 200)

    def do_POST(self) -> None:
        tamanho = int(self.headers.get("Content-Length") or 0)
        if tamanho > TAMANHO_MAXIMO:
            self._responder({"erro": "pedido grande demais"}, 413)
            return
        try:
            dados = json.loads(self.rfile.read(tamanho) or b"{}")
        except ValueError:
            dados = None
        # Tempos menores que no GitHub, para caber no limite de 60 s da função.
        resposta, codigo = processar_pedido(
            self.headers.get("Authorization", ""), dados, tempo_limite=15, espera=2
        )
        self._responder(resposta, codigo)
