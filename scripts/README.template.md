<!-- Este arquivo é gerado automaticamente por scripts/build_readme.py. Edite data/apis.yaml ou scripts/README.template.md. -->

<div align="center">

# 🇧🇷 APIs Públicas Brasileiras

**Uma lista de APIs públicas e gratuitas do Brasil que se verifica sozinha todos os dias.**

{{BADGES}}

</div>

São **{{TOTAL}} APIs** em **{{TOTAL_CATEGORIAS}} categorias**: CEP, CNPJ, bancos, Pix, câmbio, IBGE, Câmara, Senado, FIPE, feriados, clima e mais. Todo dia um robô testa cada uma e atualiza esta página com o status, o tempo de resposta e se ela aceita chamadas direto do navegador (CORS).

{{VERIFICACAO}}

> Achou útil? Deixe uma ⭐ para ajudar mais gente a encontrar a lista.

## Por que mais uma lista?

- **Status de verdade:** listas de APIs costumam acumular links quebrados. Aqui, cada API é testada diariamente e quem está fora do ar aparece marcado.
- **Exemplo pronto:** cada API tem um link de exemplo que você abre no navegador e já vê a resposta.
- **Feita para quem desenvolve no Brasil:** só APIs úteis no dia a dia de projetos brasileiros, descritas em português.

## Índice

{{INDICE}}

## APIs

{{TABELAS}}

## Legenda

| Coluna | Significado |
|---|---|
| **Autenticação** | **Não**: é só chamar · **Opcional**: funciona sem chave, mas uma chave grátis aumenta os limites · **Chave grátis / Token grátis**: exige cadastro gratuito · **Chave pública**: a chave é divulgada publicamente pelo órgão |
| **CORS** | **Sim**: pode ser chamada direto do navegador (front-end) · **Não**: chame pelo seu servidor · **?**: ainda não verificado |
| **Status** | 🟢 online · 🟡 lenta (acima de 3 s) ou instável (disponibilidade abaixo de 95% nos últimos 30 dias) · 🔴 fora do ar na última verificação · 🔑 requer chave, por isso não é testada automaticamente · 🇧🇷 só do Brasil: a API bloqueia acessos de fora do país e é testada a partir de São Paulo · ⚪ aguardando a primeira verificação |

A porcentagem mostra a disponibilidade nos últimos 30 dias de verificação. O aviso **⚠️ certificado SSL** indica que o servidor envia um certificado incompleto: abre normalmente no navegador, mas pode dar erro de certificado em Python, Node e outros clientes de back-end. O aviso **⚠️ TLS antigo** indica um servidor com configuração de segurança antiga, que alguns clientes recusam por padrão. APIs marcadas com **🇧🇷 só do Brasil** não funcionam em servidores hospedados fora do país (por exemplo, nos EUA).

## Como contribuir

Conhece uma API pública brasileira que não está aqui? Adicionar é simples: você edita **um único arquivo**, o [`data/apis.yaml`](data/apis.yaml), e o README é gerado automaticamente.

```yaml
- nome: Nome da API
  categoria: cep
  descricao: O que ela faz, em uma frase curta e sem ponto final
  docs: https://link-da-documentacao
  autenticacao: nenhuma
  exemplo: https://url-de-exemplo-que-funciona
```

Veja todos os detalhes em [CONTRIBUTING.md](CONTRIBUTING.md). Também dá para só [sugerir uma API](../../issues/new?template=sugerir-api.yml) sem mexer em código.

## Como funciona

```
data/apis.yaml ──► scripts/check.py ──► data/status.json ──► scripts/build_readme.py ──► README.md
   (você edita)      (testa as APIs)       (resultados)          (monta as tabelas)
```

Um [GitHub Action](.github/workflows/verificar.yml) roda esse fluxo todo dia e sempre que o `apis.yaml` muda na branch principal. As APIs que bloqueiam acessos de fora do Brasil são testadas por uma [função na Vercel em São Paulo](vercel/LEIA-ME.md) (também há guias para [Google Cloud](google/LEIA-ME.md) e [AWS](aws/LEIA-ME.md)). Para rodar localmente:

```bash
pip install -r requirements.txt
python scripts/validate.py      # confere se o apis.yaml está correto
python scripts/check.py         # testa as APIs
python scripts/build_readme.py  # gera o README
```

## Aviso

Esta lista só reúne links e informações públicas. Cada API pertence ao seu mantenedor e tem os próprios termos de uso e limites: respeite-os. Um status 🟢 significa apenas que a URL de exemplo respondeu na última verificação.

## Licença

[MIT](LICENSE)
