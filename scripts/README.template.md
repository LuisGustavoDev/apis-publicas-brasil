<!-- Este arquivo é gerado automaticamente por scripts/build_readme.py. Edite data/apis.yaml ou scripts/README.template.md. -->

<div align="center">

# 🇧🇷 APIs Públicas Brasileiras

**Uma lista de APIs públicas e gratuitas do Brasil que se verifica sozinha todos os dias.**

{{BADGES}}

</div>

São **{{TOTAL}} APIs** em **{{TOTAL_CATEGORIAS}} categorias**: CEP, CNPJ, bancos, Pix, câmbio, IBGE, Câmara, Senado, FIPE, feriados, clima e mais. Todo dia um robô testa cada uma e atualiza esta página com o status, o tempo de resposta e se ela aceita chamadas direto do navegador (CORS).

{{VERIFICACAO}}

> Achou útil? Deixe uma ⭐ para ajudar mais gente a encontrar a lista.

## ⚠️ Antes de usar em produção

As APIs desta lista são de terceiros, gratuitas e, na maioria, sem garantia de funcionamento. O status mostrado é o da última verificação diária: uma API marcada como online pode cair, mudar o formato da resposta ou passar a exigir cadastro a qualquer momento, sem aviso.

Alguns cuidados ajudam a evitar surpresas:

- **Tenha um plano B.** Em funções importantes, como consulta de CEP ou CNPJ, use mais de uma API e troque automaticamente quando a principal falhar.
- **Respeite os limites e os termos de uso.** Muitas limitam o número de chamadas por minuto e bloqueiam o IP de quem passa do limite. Guarde em cache o que não muda com frequência.
- **Não confie cegamente nos dados.** Nem toda fonte é oficial ou está atualizada. Valide a resposta antes de usar e prefira a fonte oficial quando o dado for crítico.
- **Cuidado com dados pessoais.** Consultas de CNPJ podem trazer nomes de sócios, e dados de endereço podem identificar pessoas. Guardar ou repassar essas informações traz obrigações da LGPD.
- **Proteja suas chaves.** APIs que exigem chave não devem ser chamadas direto do navegador: a chave fica visível para qualquer pessoa. Faça a chamada pelo seu servidor.
- **Atenção à localização.** As APIs marcadas com 🇧🇷 recusam chamadas de servidores fora do Brasil, então podem falhar se o seu projeto rodar na Vercel, na AWS ou em outro serviço no exterior.

Esta lista é um ponto de partida. A responsabilidade pelo uso de cada API, e pelo cumprimento dos termos de cada provedor, é de quem a integra.


## Por que mais uma lista?

- **Status de verdade:** listas de APIs costumam acumular links quebrados. Aqui, cada API é testada diariamente e quem está fora do ar aparece marcado.
- **Exemplo pronto:** cada API tem um link de exemplo que você abre no navegador e já vê a resposta.
- **Feita para quem desenvolve no Brasil:** só APIs úteis no dia a dia de projetos brasileiros, descritas em português.

## Índice

**Situação das APIs na última verificação** (atualizada automaticamente a cada teste):

{{RESUMO}}

Ao lado de cada categoria aparecem as mesmas contagens, com os símbolos da tabela acima.

{{INDICE}}

## APIs

{{TABELAS}}

## Legenda

| Coluna | Significado |
|---|---|
| **Autenticação** | **Não**: é só chamar · **Opcional**: funciona sem chave, mas uma chave grátis aumenta os limites · **Chave grátis / Token grátis**: exige cadastro gratuito · **Chave pública**: a chave é divulgada publicamente pelo órgão |
| **CORS** | **Sim**: pode ser chamada direto do navegador (front-end) · **Não**: chame pelo seu servidor · **?**: ainda não verificado |
| **Status** | Mesmos símbolos da tabela de situação no [Índice](#índice). Nos detalhes: **🔑 testada sem chave** indica uma API que exige chave e foi testada sem ela (respondeu “não autorizado”, o que mostra que está no ar); **🇧🇷 só do Brasil** indica uma API que funciona quando acessada do Brasil, mas bloqueia servidores no exterior; **OpenAPI confirmado** indica que o robô encontrou o arquivo de especificação da API na página de documentação |

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

Encontrou um link quebrado ou uma informação errada? [Reporte um problema](../../issues/new?template=reportar-problema.yml).

## Como funciona

```
data/apis.yaml ──► scripts/check.py ──► data/status.json ──► scripts/build_readme.py ──► README.md
   (você edita)      (testa as APIs)       (resultados)          (monta as tabelas)
```

Um [GitHub Action](.github/workflows/verificar.yml) roda esse fluxo todo dia e sempre que o `apis.yaml` muda na branch principal. Cada API é testada de dois lugares: **do Brasil**, por uma [função na Vercel em São Paulo](vercel/LEIA-ME.md), que dá o resultado oficial, e **dos EUA**, pelo próprio GitHub, como segunda opinião. Quando uma API funciona do Brasil e falha dos EUA, ela ganha a marca 🇧🇷 automaticamente.

Além de ver se a API responde, o robô confere **o que** ela devolveu: dados (JSON, XML, CSV), a página de documentação da API (Swagger, Redoc, WSDL, conferindo o arquivo OpenAPI quando existe), uma página de bloqueio de robôs ou um site comum. Para rodar localmente:

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
