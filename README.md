<!-- Este arquivo é gerado automaticamente por scripts/build_readme.py. Edite data/apis.yaml ou scripts/README.template.md. -->

<div align="center">

# 🇧🇷 APIs Públicas Brasileiras

**Uma lista de APIs públicas e gratuitas do Brasil que se verifica sozinha todos os dias.**

![APIs: 41](https://img.shields.io/badge/APIs-41-009c3b) ![verificação: aguardando](https://img.shields.io/badge/verifica%C3%A7%C3%A3o-aguardando-lightgrey)

</div>

São **41 APIs** em **15 categorias**: CEP, CNPJ, bancos, Pix, câmbio, IBGE, Câmara, Senado, FIPE, feriados, clima e mais. Todo dia um robô testa cada uma e atualiza esta página com o status, o tempo de resposta e se ela aceita chamadas direto do navegador (CORS).

A primeira verificação automática ainda não rodou.

> Achou útil? Deixe uma ⭐ para ajudar mais gente a encontrar a lista.

## Por que mais uma lista?

- **Status de verdade:** listas de APIs costumam acumular links quebrados. Aqui, cada API é testada diariamente e quem está fora do ar aparece marcado.
- **Exemplo pronto:** cada API tem um link de exemplo que você abre no navegador e já vê a resposta.
- **Feita para quem desenvolve no Brasil:** só APIs úteis no dia a dia de projetos brasileiros, descritas em português.

## Índice

- [CEP e Endereços](#cep-e-endereços) (3)
- [CNPJ e Empresas](#cnpj-e-empresas) (5)
- [Bancos e Pagamentos](#bancos-e-pagamentos) (2)
- [Economia e Mercado Financeiro](#economia-e-mercado-financeiro) (6)
- [Governo, Legislativo e Justiça](#governo-legislativo-e-justiça) (5)
- [IBGE e Geografia](#ibge-e-geografia) (6)
- [Calendário e Feriados](#calendário-e-feriados) (2)
- [Clima e Tempo](#clima-e-tempo) (2)
- [Veículos](#veículos) (2)
- [Transporte](#transporte) (1)
- [Saúde](#saúde) (1)
- [Comércio e Tributos](#comércio-e-tributos) (1)
- [Internet, Telefonia e Domínios](#internet-telefonia-e-domínios) (3)
- [Livros](#livros) (1)
- [Esportes](#esportes) (1)

## APIs

### CEP e Endereços

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [AwesomeAPI CEP](https://docs.awesomeapi.com.br) | Endereço por CEP com latitude, longitude e código IBGE<br><sub>[exemplo](https://cep.awesomeapi.com.br/json/01001000)</sub> | Opcional | ? | ⚪ aguardando |
| [BrasilAPI CEP v2](https://brasilapi.com.br/docs) | CEP com coordenadas geográficas, consultando vários provedores com fallback<br><sub>[exemplo](https://brasilapi.com.br/api/cep/v2/01001000)</sub> | Não | ? | ⚪ aguardando |
| [ViaCEP](https://viacep.com.br) | Consulta de endereço por CEP e busca de CEP por endereço<br><sub>[exemplo](https://viacep.com.br/ws/01001000/json/)</sub> | Não | ? | ⚪ aguardando |

**[⬆ voltar ao índice](#índice)**

### CNPJ e Empresas

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [BrasilAPI CNPJ](https://brasilapi.com.br/docs) | Dados cadastrais de empresas pela base pública da Receita Federal<br><sub>[exemplo](https://brasilapi.com.br/api/cnpj/v1/19131243000197)</sub> | Não | ? | ⚪ aguardando |
| [BrasilAPI Corretoras](https://brasilapi.com.br/docs) | Corretoras de valores registradas na CVM<br><sub>[exemplo](https://brasilapi.com.br/api/cvm/corretoras/v1)</sub> | Não | ? | ⚪ aguardando |
| [CNPJ.ws Pública](https://docs.cnpj.ws/referencia-de-api/api-publica) | Consulta de CNPJ com dados de sócios, atividades e inscrições estaduais<br><sub>[exemplo](https://publica.cnpj.ws/cnpj/19131243000197) · limite: 3 req/min por IP</sub> | Não | ? | ⚪ aguardando |
| [CNPJá Open](https://cnpja.com/api/open) | Dados cadastrais de estabelecimentos, sócios e atividades por CNPJ<br><sub>[exemplo](https://open.cnpja.com/office/19131243000197) · limite: 5 req/min por IP</sub> | Não | ? | ⚪ aguardando |
| [ReceitaWS](https://developers.receitaws.com.br) | Consulta de CNPJ com situação cadastral e quadro de sócios<br><sub>[exemplo](https://receitaws.com.br/v1/cnpj/19131243000197) · limite: 3 req/min no plano gratuito</sub> | Não | ? | ⚪ aguardando |

**[⬆ voltar ao índice](#índice)**

### Bancos e Pagamentos

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [BrasilAPI Bancos](https://brasilapi.com.br/docs) | Lista de bancos com código de compensação e ISPB<br><sub>[exemplo](https://brasilapi.com.br/api/banks/v1)</sub> | Não | ? | ⚪ aguardando |
| [BrasilAPI Participantes do Pix](https://brasilapi.com.br/docs) | Instituições participantes do Pix, com modalidade e início da operação<br><sub>[exemplo](https://brasilapi.com.br/api/pix/v1/participants)</sub> | Não | ? | ⚪ aguardando |

**[⬆ voltar ao índice](#índice)**

### Economia e Mercado Financeiro

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [AwesomeAPI Moedas](https://docs.awesomeapi.com.br) | Cotação de moedas e criptomoedas em tempo real e histórico<br><sub>[exemplo](https://economia.awesomeapi.com.br/json/last/USD-BRL) · limite: 100 mil req/mês grátis com chave</sub> | Opcional | ? | ⚪ aguardando |
| [Banco Central PTAX](https://dadosabertos.bcb.gov.br) | Cotações oficiais PTAX de moedas estrangeiras<br><sub>[exemplo](https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/Moedas?$format=json)</sub> | Não | ? | ⚪ aguardando |
| [Banco Central SGS](https://dadosabertos.bcb.gov.br) | Séries temporais do Banco Central, como Selic, IPCA e CDI<br><sub>[exemplo](https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados/ultimos/1?formato=json)</sub> | Não | ? | ⚪ aguardando |
| [brapi](https://brapi.dev/docs) | Cotações, histórico e dividendos de ações, FIIs e BDRs da B3<br><sub>[exemplo](https://brapi.dev/api/quote/PETR4) · limite: PETR4, MGLU3, VALE3 e ITUB4 funcionam sem chave</sub> | Chave grátis | ? | ⚪ aguardando |
| [BrasilAPI Câmbio](https://brasilapi.com.br/docs) | Moedas disponíveis e cotações de câmbio por data<br><sub>[exemplo](https://brasilapi.com.br/api/cambio/v1/moedas)</sub> | Não | ? | ⚪ aguardando |
| [BrasilAPI Taxas](https://brasilapi.com.br/docs) | Valores atuais de Selic, CDI e IPCA<br><sub>[exemplo](https://brasilapi.com.br/api/taxas/v1)</sub> | Não | ? | ⚪ aguardando |

**[⬆ voltar ao índice](#índice)**

### Governo, Legislativo e Justiça

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [Câmara dos Deputados](https://dadosabertos.camara.leg.br/swagger/api.html) | Deputados, proposições, votações, despesas e eventos da Câmara<br><sub>[exemplo](https://dadosabertos.camara.leg.br/api/v2/deputados?itens=5)</sub> | Não | ? | ⚪ aguardando |
| [DataJud](https://datajud-wiki.cnj.jus.br/api-publica/) | Metadados de processos judiciais de todos os tribunais do país (CNJ) | Chave pública | ? | 🔑 requer chave |
| [Portal da Transparência](https://portaldatransparencia.gov.br/api-de-dados) | Gastos, contratos, servidores e benefícios do governo federal | Chave grátis | ? | 🔑 requer chave |
| [Querido Diário](https://docs.queridodiario.ok.org.br/en/latest/using/public-api.html) | Busca textual em diários oficiais de municípios brasileiros<br><sub>[exemplo](https://api.queridodiario.ok.org.br/gazettes?querystring=educacao&size=1) · limite: Recomenda até 60 req/min</sub> | Não | ? | ⚪ aguardando |
| [Senado Federal](https://legis.senado.leg.br/dadosabertos/docs/) | Senadores, matérias, votações e comissões do Senado<br><sub>[exemplo](https://legis.senado.leg.br/dadosabertos/senador/lista/atual.json)</sub> | Não | ? | ⚪ aguardando |

**[⬆ voltar ao índice](#índice)**

### IBGE e Geografia

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [IBGE Agregados (SIDRA)](https://servicodados.ibge.gov.br/api/docs/agregados?versao=3) | Tabelas de pesquisas do IBGE, como PNAD, Censo e PIB<br><sub>[exemplo](https://servicodados.ibge.gov.br/api/v3/agregados)</sub> | Não | ? | ⚪ aguardando |
| [IBGE Localidades](https://servicodados.ibge.gov.br/api/docs/localidades) | Regiões, estados, municípios e distritos com códigos oficiais<br><sub>[exemplo](https://servicodados.ibge.gov.br/api/v1/localidades/estados)</sub> | Não | ? | ⚪ aguardando |
| [IBGE Malhas](https://servicodados.ibge.gov.br/api/docs/malhas?versao=3) | Contornos geográficos de estados e municípios em GeoJSON ou SVG<br><sub>[exemplo](https://servicodados.ibge.gov.br/api/v3/malhas/estados/SP?formato=application/vnd.geo+json)</sub> | Não | ? | ⚪ aguardando |
| [IBGE Nomes](https://servicodados.ibge.gov.br/api/docs/nomes?versao=2) | Frequência e ranking de nomes por década, segundo o Censo<br><sub>[exemplo](https://servicodados.ibge.gov.br/api/v2/censos/nomes/maria)</sub> | Não | ? | ⚪ aguardando |
| [IBGE Notícias](https://servicodados.ibge.gov.br/api/docs/noticias?versao=3) | Notícias e releases publicados pela Agência IBGE<br><sub>[exemplo](https://servicodados.ibge.gov.br/api/v3/noticias/?qtd=1)</sub> | Não | ? | ⚪ aguardando |
| [IBGE Países](https://servicodados.ibge.gov.br/api/docs/paises) | Indicadores, histórico e dados gerais de países<br><sub>[exemplo](https://servicodados.ibge.gov.br/api/v1/paises/BR)</sub> | Não | ? | ⚪ aguardando |

**[⬆ voltar ao índice](#índice)**

### Calendário e Feriados

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [BrasilAPI Feriados](https://brasilapi.com.br/docs) | Feriados nacionais de um ano, incluindo os móveis<br><sub>[exemplo](https://brasilapi.com.br/api/feriados/v1/2026)</sub> | Não | ? | ⚪ aguardando |
| [Nager.Date](https://date.nager.at) | Feriados públicos do Brasil e de outros 100+ países<br><sub>[exemplo](https://date.nager.at/api/v3/PublicHolidays/2026/BR)</sub> | Não | ? | ⚪ aguardando |

**[⬆ voltar ao índice](#índice)**

### Clima e Tempo

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [BrasilAPI CPTEC](https://brasilapi.com.br/docs) | Previsão do tempo, condições nas capitais e ondas, com dados do CPTEC/INPE<br><sub>[exemplo](https://brasilapi.com.br/api/cptec/v1/clima/capital)</sub> | Não | ? | ⚪ aguardando |
| [HG Brasil Weather](https://hgbrasil.com/docs) | Previsão do tempo para cidades brasileiras | Chave grátis | ? | 🔑 requer chave |

**[⬆ voltar ao índice](#índice)**

### Veículos

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [BrasilAPI FIPE](https://brasilapi.com.br/docs) | Marcas, veículos, preços e tabelas de referência da FIPE<br><sub>[exemplo](https://brasilapi.com.br/api/fipe/marcas/v1/carros)</sub> | Não | ? | ⚪ aguardando |
| [FIPE (Parallelum)](https://github.com/deividfortuna/fipe) | Marcas, modelos, anos e preços da Tabela FIPE<br><sub>[exemplo](https://parallelum.com.br/fipe/api/v2/cars/brands)</sub> | Opcional | ? | ⚪ aguardando |

**[⬆ voltar ao índice](#índice)**

### Transporte

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [SPTrans Olho Vivo](https://www.sptrans.com.br/desenvolvedores/api-do-olho-vivo-guia-de-referencia/documentacao-api/) | Posição dos ônibus, linhas, paradas e previsão de chegada em São Paulo | Token grátis | ? | 🔑 requer chave |

**[⬆ voltar ao índice](#índice)**

### Saúde

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [OpenDataSUS](https://opendatasus.saude.gov.br) | Catálogo de dados abertos do Ministério da Saúde (API CKAN)<br><sub>[exemplo](https://opendatasus.saude.gov.br/api/3/action/package_list)</sub> | Não | ? | ⚪ aguardando |

**[⬆ voltar ao índice](#índice)**

### Comércio e Tributos

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [BrasilAPI NCM](https://brasilapi.com.br/docs) | Busca na Nomenclatura Comum do Mercosul usada em notas fiscais<br><sub>[exemplo](https://brasilapi.com.br/api/ncm/v1?search=3305)</sub> | Não | ? | ⚪ aguardando |

**[⬆ voltar ao índice](#índice)**

### Internet, Telefonia e Domínios

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [BrasilAPI DDD](https://brasilapi.com.br/docs) | Estado e cidades atendidos por um DDD<br><sub>[exemplo](https://brasilapi.com.br/api/ddd/v1/11)</sub> | Não | ? | ⚪ aguardando |
| [BrasilAPI Registro.br](https://brasilapi.com.br/docs) | Situação e disponibilidade de domínios .br<br><sub>[exemplo](https://brasilapi.com.br/api/registrobr/v1/brasilapi.com.br)</sub> | Não | ? | ⚪ aguardando |
| [Registro.br RDAP](https://rdap.registro.br) | Dados públicos de registro de domínios .br no padrão RDAP<br><sub>[exemplo](https://rdap.registro.br/domain/registro.br)</sub> | Não | ? | ⚪ aguardando |

**[⬆ voltar ao índice](#índice)**

### Livros

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [BrasilAPI ISBN](https://brasilapi.com.br/docs) | Dados de livros por ISBN, consultando várias fontes<br><sub>[exemplo](https://brasilapi.com.br/api/isbn/v1/9788545702870)</sub> | Não | ? | ⚪ aguardando |

**[⬆ voltar ao índice](#índice)**

### Esportes

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [API-Futebol](https://www.api-futebol.com.br) | Campeonatos, tabelas, rodadas e partidas do futebol brasileiro | Chave grátis | ? | 🔑 requer chave |

**[⬆ voltar ao índice](#índice)**

## Legenda

| Coluna | Significado |
|---|---|
| **Autenticação** | **Não**: é só chamar · **Opcional**: funciona sem chave, mas uma chave grátis aumenta os limites · **Chave grátis / Token grátis**: exige cadastro gratuito · **Chave pública**: a chave é divulgada publicamente pelo órgão |
| **CORS** | **Sim**: pode ser chamada direto do navegador (front-end) · **Não**: chame pelo seu servidor · **?**: ainda não verificado |
| **Status** | 🟢 online · 🟡 lenta (acima de 3 s) ou instável (disponibilidade abaixo de 95% nos últimos 30 dias) · 🔴 fora do ar na última verificação · 🔑 requer chave, por isso não é testada automaticamente · ⚪ aguardando a primeira verificação |

A porcentagem mostra a disponibilidade nos últimos 30 dias de verificação.

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

Um [GitHub Action](.github/workflows/verificar.yml) roda esse fluxo todo dia e sempre que o `apis.yaml` muda na branch principal. Para rodar localmente:

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
