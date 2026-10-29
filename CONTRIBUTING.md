# Como contribuir

Obrigado por querer ajudar! Toda a lista vive em um único arquivo: [`data/apis.yaml`](data/apis.yaml). O `README.md` é gerado automaticamente a partir dele, então **não edite as tabelas do README à mão**.

## Adicionar uma API

1. Confira se ela já não está na lista.
2. Abra o [`data/apis.yaml`](data/apis.yaml) e adicione um bloco no grupo da categoria certa:

```yaml
- nome: Nome da API
  categoria: cep
  descricao: O que ela faz, em uma frase curta e sem ponto final
  docs: https://link-da-documentacao
  autenticacao: nenhuma
  limite: 60 req/min          # opcional
  exemplo: https://url-de-exemplo-que-funciona
```

3. Abra um pull request. O GitHub valida o arquivo automaticamente.

Sem tempo para isso? [Sugira a API em uma issue](../../issues/new?template=sugerir-api.yml) e alguém adiciona.

## Campos

| Campo | Obrigatório | Como preencher |
|---|:---:|---|
| `nome` | sim | Nome pelo qual a API é conhecida. Precisa ser único na lista. |
| `categoria` | sim | Um dos `id` listados no topo do arquivo, em `categorias`. Para criar uma categoria nova, adicione-a lá também. |
| `descricao` | sim | Uma frase curta (até 120 caracteres), em português, sem ponto final. |
| `docs` | sim | Link da documentação oficial (ou da melhor documentação disponível). Prefira `https://`. |
| `autenticacao` | sim | `nenhuma`, `opcional`, `chave`, `chave-publica` ou `token`. |
| `limite` | não | Limite de uso conhecido, ex.: `3 req/min por IP`. |
| `exemplo` | sim | Uma URL GET que funciona de verdade e retorna dados. É ela que o robô testa todo dia. |
| `teste` | não | Use `teste: false` quando a API exige chave ou não aceita um GET simples. Nesse caso, coloque em `exemplo` o link da documentação. |

## O que entra na lista

- APIs **públicas** e **gratuitas**, ou com plano gratuito de verdade (não apenas um teste de poucos dias).
- Úteis para projetos brasileiros: dados do Brasil, serviços brasileiros ou APIs internacionais com boa cobertura do Brasil.
- Com documentação acessível.

## O que não entra

- APIs que exigem contrato ou pagamento para qualquer uso.
- Raspagem de sites que proíbem isso nos termos de uso.
- Serviços que expõem dados pessoais de forma indevida.

## Testando localmente (opcional)

```bash
pip install -r requirements.txt
python scripts/validate.py
python scripts/build_readme.py
```
