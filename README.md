<!-- Este arquivo é gerado automaticamente por scripts/build_readme.py. Edite data/apis.yaml ou scripts/README.template.md. -->

<div align="center">

# 🇧🇷 APIs Públicas Brasileiras

**Uma lista de APIs públicas e gratuitas do Brasil que se verifica sozinha todos os dias.**

![APIs: 95](https://img.shields.io/badge/APIs-95-009c3b) ![verificação: aguardando](https://img.shields.io/badge/verifica%C3%A7%C3%A3o-aguardando-lightgrey)

</div>

São **95 APIs** em **22 categorias**: CEP, CNPJ, bancos, Pix, câmbio, IBGE, Câmara, Senado, FIPE, feriados, clima e mais. Todo dia um robô testa cada uma e atualiza esta página com o status, o tempo de resposta e se ela aceita chamadas direto do navegador (CORS).

A primeira verificação automática ainda não rodou.

> Achou útil? Deixe uma ⭐ para ajudar mais gente a encontrar a lista.

## Por que mais uma lista?

- **Status de verdade:** listas de APIs costumam acumular links quebrados. Aqui, cada API é testada diariamente e quem está fora do ar aparece marcado.
- **Exemplo pronto:** cada API tem um link de exemplo que você abre no navegador e já vê a resposta.
- **Feita para quem desenvolve no Brasil:** só APIs úteis no dia a dia de projetos brasileiros, descritas em português.

## Índice

- [CEP e Endereços](#cep-e-endereços) (7)
- [CNPJ e Empresas](#cnpj-e-empresas) (7)
- [Bancos e Pagamentos](#bancos-e-pagamentos) (4)
- [Economia e Mercado Financeiro](#economia-e-mercado-financeiro) (10)
- [Governo, Legislativo e Justiça](#governo-legislativo-e-justiça) (11)
- [IBGE e Geografia](#ibge-e-geografia) (9)
- [Calendário e Feriados](#calendário-e-feriados) (2)
- [Clima e Tempo](#clima-e-tempo) (5)
- [Veículos](#veículos) (2)
- [Transporte](#transporte) (1)
- [Saúde](#saúde) (1)
- [Comércio e Tributos](#comércio-e-tributos) (3)
- [Internet, Telefonia e Domínios](#internet-telefonia-e-domínios) (4)
- [Livros, Cultura e Língua](#livros-cultura-e-língua) (4)
- [Ciência e Educação](#ciência-e-educação) (1)
- [Meio Ambiente](#meio-ambiente) (1)
- [Agropecuária](#agropecuária) (1)
- [Segurança Pública](#segurança-pública) (1)
- [Esportes e Loterias](#esportes-e-loterias) (4)
- [Utilidades](#utilidades) (1)
- [Portais de Dados Abertos (CKAN)](#portais-de-dados-abertos-ckan) (10)
- [Internacionais com Dados do Brasil](#internacionais-com-dados-do-brasil) (6)

## APIs

### CEP e Endereços

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [ApiCEP](https://apicep.com) | Endereço por CEP servido como arquivo JSON estático em CDN<br><sub>[exemplo](https://cdn.apicep.com/file/apicep/01001-000.json)</sub> | Não | ? | ⚪ aguardando |
| [AwesomeAPI CEP](https://docs.awesomeapi.com.br) | Endereço por CEP com latitude, longitude e código IBGE<br><sub>[exemplo](https://cep.awesomeapi.com.br/json/01001000)</sub> | Opcional | ? | ⚪ aguardando |
| [Brasil Aberto](https://docs.brasilaberto.com) | CEP, cidades, bairros, ruas, CNPJ e rastreio de encomendas | Chave grátis | ? | 🔑 requer chave |
| [BrasilAPI CEP v2](https://brasilapi.com.br/docs) | CEP com coordenadas geográficas, consultando vários provedores com fallback<br><sub>[exemplo](https://brasilapi.com.br/api/cep/v2/01001000)</sub> | Não | ? | ⚪ aguardando |
| [CEP Aberto](https://www.cepaberto.com/api_key) | CEP, busca por coordenadas e listagem de cidades por estado | Chave grátis | ? | 🔑 requer chave |
| [OpenCEP](https://opencep.com) | Consulta de endereço por CEP, gratuita e sem cadastro<br><sub>[exemplo](https://opencep.com/v1/01001000)</sub> | Não | ? | ⚪ aguardando |
| [ViaCEP](https://viacep.com.br) | Consulta de endereço por CEP e busca de CEP por endereço<br><sub>[exemplo](https://viacep.com.br/ws/01001000/json/)</sub> | Não | ? | ⚪ aguardando |

**[⬆ voltar ao índice](#índice)**

### CNPJ e Empresas

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [BrasilAPI CNPJ](https://brasilapi.com.br/docs) | Dados cadastrais de empresas pela base pública da Receita Federal<br><sub>[exemplo](https://brasilapi.com.br/api/cnpj/v1/19131243000197)</sub> | Não | ? | ⚪ aguardando |
| [BrasilAPI Corretoras](https://brasilapi.com.br/docs) | Corretoras de valores registradas na CVM<br><sub>[exemplo](https://brasilapi.com.br/api/cvm/corretoras/v1)</sub> | Não | ? | ⚪ aguardando |
| [CNPJ.ws Pública](https://docs.cnpj.ws/referencia-de-api/api-publica) | Consulta de CNPJ com dados de sócios, atividades e inscrições estaduais<br><sub>[exemplo](https://publica.cnpj.ws/cnpj/19131243000197) · limite: 3 req/min por IP</sub> | Não | ? | ⚪ aguardando |
| [CNPJá Open](https://cnpja.com/api/open) | Dados cadastrais de estabelecimentos, sócios e atividades por CNPJ<br><sub>[exemplo](https://open.cnpja.com/office/19131243000197) · limite: 5 req/min por IP</sub> | Não | ? | ⚪ aguardando |
| [Minha Receita](https://docs.minhareceita.org) | Dados públicos de CNPJ da Receita Federal, projeto de código aberto<br><sub>[exemplo](https://minhareceita.org/19131243000197)</sub> | Não | ? | ⚪ aguardando |
| [OpenCNPJ](https://opencnpj.org) | Consulta de CNPJ com base nos dados públicos da Receita Federal<br><sub>[exemplo](https://api.opencnpj.org/19131243000197)</sub> | Não | ? | ⚪ aguardando |
| [ReceitaWS](https://developers.receitaws.com.br) | Consulta de CNPJ com situação cadastral e quadro de sócios<br><sub>[exemplo](https://receitaws.com.br/v1/cnpj/19131243000197) · limite: 3 req/min no plano gratuito</sub> | Não | ? | ⚪ aguardando |

**[⬆ voltar ao índice](#índice)**

### Bancos e Pagamentos

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [Banco Central Estatísticas do Pix](https://dadosabertos.bcb.gov.br/dataset/pix) | Chaves cadastradas, transações por município e estatísticas de fraudes do Pix<br><sub>[exemplo](https://olinda.bcb.gov.br/olinda/servico/Pix_DadosAbertos/versao/v1/odata/)</sub> | Não | ? | ⚪ aguardando |
| [Banco Central Postos de Atendimento](https://olinda.bcb.gov.br/olinda/servico/Informes_PostosDeAtendimentoEletronico/versao/v1/swagger-ui3) | Postos de atendimento eletrônico de instituições financeiras<br><sub>[exemplo](https://olinda.bcb.gov.br/olinda/servico/Informes_PostosDeAtendimentoEletronico/versao/v1/odata/)</sub> | Não | ? | ⚪ aguardando |
| [BrasilAPI Bancos](https://brasilapi.com.br/docs) | Lista de bancos com código de compensação e ISPB<br><sub>[exemplo](https://brasilapi.com.br/api/banks/v1)</sub> | Não | ? | ⚪ aguardando |
| [BrasilAPI Participantes do Pix](https://brasilapi.com.br/docs) | Instituições participantes do Pix, com modalidade e início da operação<br><sub>[exemplo](https://brasilapi.com.br/api/pix/v1/participants)</sub> | Não | ? | ⚪ aguardando |

**[⬆ voltar ao índice](#índice)**

### Economia e Mercado Financeiro

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [AwesomeAPI Moedas](https://docs.awesomeapi.com.br) | Cotação de moedas e criptomoedas em tempo real e histórico<br><sub>[exemplo](https://economia.awesomeapi.com.br/json/last/USD-BRL) · limite: 100 mil req/mês grátis com chave</sub> | Opcional | ? | ⚪ aguardando |
| [Banco Central Focus (Expectativas)](https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/documentacao) | Expectativas do mercado para inflação, Selic, PIB e câmbio (Boletim Focus)<br><sub>[exemplo](https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoAnuais?$top=5&$format=json)</sub> | Não | ? | ⚪ aguardando |
| [Banco Central PTAX](https://dadosabertos.bcb.gov.br) | Cotações oficiais PTAX de moedas estrangeiras<br><sub>[exemplo](https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/Moedas?$format=json)</sub> | Não | ? | ⚪ aguardando |
| [Banco Central SGS](https://dadosabertos.bcb.gov.br) | Séries temporais do Banco Central, como Selic, IPCA e CDI<br><sub>[exemplo](https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados/ultimos/1?formato=json)</sub> | Não | ? | ⚪ aguardando |
| [brapi](https://brapi.dev/docs) | Cotações, histórico e dividendos de ações, FIIs e BDRs da B3<br><sub>[exemplo](https://brapi.dev/api/quote/PETR4) · limite: PETR4, MGLU3, VALE3 e ITUB4 funcionam sem chave</sub> | Chave grátis | ? | ⚪ aguardando |
| [BrasilAPI Câmbio](https://brasilapi.com.br/docs) | Moedas disponíveis e cotações de câmbio por data<br><sub>[exemplo](https://brasilapi.com.br/api/cambio/v1/moedas)</sub> | Não | ? | ⚪ aguardando |
| [BrasilAPI Taxas](https://brasilapi.com.br/docs) | Valores atuais de Selic, CDI e IPCA<br><sub>[exemplo](https://brasilapi.com.br/api/taxas/v1)</sub> | Não | ? | ⚪ aguardando |
| [Ipeadata](http://www.ipeadata.gov.br/api/) | Milhares de séries econômicas, sociais e regionais do Ipea<br><sub>[exemplo](http://www.ipeadata.gov.br/api/odata4/Temas/)</sub> | Não | ? | ⚪ aguardando |
| [Mercado Bitcoin](https://api.mercadobitcoin.net/api/v4/docs) | Pares negociados, cotações, livro de ofertas e candles de criptomoedas em reais<br><sub>[exemplo](https://api.mercadobitcoin.net/api/v4/symbols)</sub> | Não | ? | ⚪ aguardando |
| [SICONFI (Tesouro Nacional)](https://apidatalake.tesouro.gov.br/docs/siconfi/) | Relatórios fiscais e contábeis de estados e municípios (RREO, RGF, DCA)<br><sub>[exemplo](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/entes)</sub> | Não | ? | ⚪ aguardando |

**[⬆ voltar ao índice](#índice)**

### Governo, Legislativo e Justiça

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [Brasil.IO](https://blog.brasil.io/2020/10/10/como-acessar-os-dados-do-brasil-io/) | Dados públicos tratados, como sócios de empresas, eleições e gastos | Chave grátis | ? | 🔑 requer chave |
| [Câmara dos Deputados](https://dadosabertos.camara.leg.br/swagger/api.html) | Deputados, proposições, votações, despesas e eventos da Câmara<br><sub>[exemplo](https://dadosabertos.camara.leg.br/api/v2/deputados?itens=5)</sub> | Não | ? | ⚪ aguardando |
| [Compras.gov.br Dados Abertos](https://dadosabertos.compras.gov.br/swagger-ui/index.html) | Licitações, contratos, materiais, serviços e fornecedores do governo federal<br><sub>[exemplo](https://dadosabertos.compras.gov.br/swagger-ui/index.html)</sub> | Não | ? | ⚪ aguardando |
| [DataJud](https://datajud-wiki.cnj.jus.br/api-publica/) | Metadados de processos judiciais de todos os tribunais do país (CNJ) | Chave pública | ? | 🔑 requer chave |
| [LexML](https://www12.senado.leg.br/dados-abertos/legislativo/legislacao/acervo-do-portal-lexml) | Busca em leis, decretos, jurisprudência e proposições de todo o país (SRU, XML)<br><sub>[exemplo](https://www.lexml.gov.br/busca/SRU?operation=searchRetrieve&query=urn+any+lei&maximumRecords=1)</sub> | Não | ? | ⚪ aguardando |
| [PNCP (Portal Nacional de Contratações Públicas)](https://pncp.gov.br/api/consulta/swagger-ui/index.html) | Contratações, atas e contratos de todos os entes públicos do país<br><sub>[exemplo](https://pncp.gov.br/api/consulta/v1/contratacoes/publicacao?dataInicial=20260101&dataFinal=20260102&codigoModalidadeContratacao=8&pagina=1)</sub> | Não | ? | ⚪ aguardando |
| [Portal Brasileiro de Dados Abertos](https://www.gov.br/conecta/catalogo/apis/api-portal-de-dados-abertos) | Catálogo nacional de conjuntos de dados abertos do governo (dados.gov.br) | Chave grátis | ? | 🔑 requer chave |
| [Portal da Transparência](https://portaldatransparencia.gov.br/api-de-dados) | Gastos, contratos, servidores e benefícios do governo federal | Chave grátis | ? | 🔑 requer chave |
| [Querido Diário](https://docs.queridodiario.ok.org.br/en/latest/using/public-api.html) | Busca textual em diários oficiais de municípios brasileiros<br><sub>[exemplo](https://api.queridodiario.ok.org.br/gazettes?querystring=educacao&size=1) · limite: Recomenda até 60 req/min</sub> | Não | ? | ⚪ aguardando |
| [Senado Federal](https://legis.senado.leg.br/dadosabertos/docs/) | Senadores, matérias, votações e comissões do Senado<br><sub>[exemplo](https://legis.senado.leg.br/dadosabertos/senador/lista/atual.json)</sub> | Não | ? | ⚪ aguardando |
| [Transferegov](https://api-publica.transferegov.gestao.gov.br/ted/docs) | Transferências da União, emendas especiais, fundo a fundo e parcerias<br><sub>[exemplo](https://api-publica.transferegov.gestao.gov.br/ted/docs)</sub> | Não | ? | ⚪ aguardando |

**[⬆ voltar ao índice](#índice)**

### IBGE e Geografia

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [IBGE Agregados (SIDRA)](https://servicodados.ibge.gov.br/api/docs/agregados?versao=3) | Tabelas de pesquisas do IBGE, como PNAD, Censo e PIB<br><sub>[exemplo](https://servicodados.ibge.gov.br/api/v3/agregados)</sub> | Não | ? | ⚪ aguardando |
| [IBGE Calendário](https://servicodados.ibge.gov.br/api/docs/calendario?versao=3) | Calendário de divulgações de pesquisas e eventos do IBGE<br><sub>[exemplo](https://servicodados.ibge.gov.br/api/v3/calendario/?qtd=1)</sub> | Não | ? | ⚪ aguardando |
| [IBGE CNAE](https://servicodados.ibge.gov.br/api/docs/cnae?versao=2) | Classificação Nacional de Atividades Econômicas (seções, classes e subclasses)<br><sub>[exemplo](https://servicodados.ibge.gov.br/api/v2/cnae/secoes)</sub> | Não | ? | ⚪ aguardando |
| [IBGE Localidades](https://servicodados.ibge.gov.br/api/docs/localidades) | Regiões, estados, municípios e distritos com códigos oficiais<br><sub>[exemplo](https://servicodados.ibge.gov.br/api/v1/localidades/estados)</sub> | Não | ? | ⚪ aguardando |
| [IBGE Malhas](https://servicodados.ibge.gov.br/api/docs/malhas?versao=3) | Contornos geográficos de estados e municípios em GeoJSON ou SVG<br><sub>[exemplo](https://servicodados.ibge.gov.br/api/v3/malhas/estados/SP?formato=application/vnd.geo+json)</sub> | Não | ? | ⚪ aguardando |
| [IBGE Nomes](https://servicodados.ibge.gov.br/api/docs/nomes?versao=2) | Frequência e ranking de nomes por década, segundo o Censo<br><sub>[exemplo](https://servicodados.ibge.gov.br/api/v2/censos/nomes/maria)</sub> | Não | ? | ⚪ aguardando |
| [IBGE Notícias](https://servicodados.ibge.gov.br/api/docs/noticias?versao=3) | Notícias e releases publicados pela Agência IBGE<br><sub>[exemplo](https://servicodados.ibge.gov.br/api/v3/noticias/?qtd=1)</sub> | Não | ? | ⚪ aguardando |
| [IBGE Países](https://servicodados.ibge.gov.br/api/docs/paises) | Indicadores, histórico e dados gerais de países<br><sub>[exemplo](https://servicodados.ibge.gov.br/api/v1/paises/BR)</sub> | Não | ? | ⚪ aguardando |
| [IBGE SIDRA](https://apisidra.ibge.gov.br/home/ajuda) | Valores das tabelas do SIDRA, como IPCA, PNAD, PIB e Censo<br><sub>[exemplo](https://apisidra.ibge.gov.br/values/t/7060/n1/all/v/63/p/last/c315/7169)</sub> | Não | ? | ⚪ aguardando |

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
| [CPTEC/INPE (XML)](http://servicos.cptec.inpe.br/XML/) | Previsão de 7 dias por cidade direto do serviço oficial do CPTEC, em XML<br><sub>[exemplo](http://servicos.cptec.inpe.br/XML/cidade/7dias/241/previsao.xml)</sub> | Não | ? | ⚪ aguardando |
| [HG Brasil Weather](https://hgbrasil.com/docs) | Previsão do tempo para cidades brasileiras | Chave grátis | ? | 🔑 requer chave |
| [INMET Alertas](https://portal.inmet.gov.br/noticias/saiba-como-acessar-os-dados-meteorol%C3%B3gicos-dispon%C3%ADveis-no-site-do-inmet) | Avisos meteorológicos oficiais em feed RSS<br><sub>[exemplo](https://apiprevmet3.inmet.gov.br/avisos/rss)</sub> | Não | ? | ⚪ aguardando |
| [INMET Estações](https://portal.inmet.gov.br/manual/manual-de-uso-da-api-esta%C3%A7%C3%B5es) | Dados horários e diários das estações meteorológicas automáticas e convencionais<br><sub>limite: Até cerca de 6 meses por consulta</sub> | Token grátis | ? | 🔑 requer chave |

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
| [Cosmos Bluesoft](https://cosmos.bluesoft.com.br) | Catálogo de produtos por GTIN/EAN e produtos por NCM | Chave grátis | ? | 🔑 requer chave |
| [SI5 Global](https://global.si5.com.br/documentacao) | Dados de produto, NCM e CEST a partir do código de barras (GTIN/EAN)<br><sub>limite: 100 consultas/dia no plano gratuito</sub> | Chave grátis | ? | 🔑 requer chave |

**[⬆ voltar ao índice](#índice)**

### Internet, Telefonia e Domínios

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [BrasilAPI DDD](https://brasilapi.com.br/docs) | Estado e cidades atendidos por um DDD<br><sub>[exemplo](https://brasilapi.com.br/api/ddd/v1/11)</sub> | Não | ? | ⚪ aguardando |
| [BrasilAPI Registro.br](https://brasilapi.com.br/docs) | Situação e disponibilidade de domínios .br<br><sub>[exemplo](https://brasilapi.com.br/api/registrobr/v1/brasilapi.com.br)</sub> | Não | ? | ⚪ aguardando |
| [Registro.br RDAP](https://rdap.registro.br) | Dados públicos de registro de domínios .br no padrão RDAP<br><sub>[exemplo](https://rdap.registro.br/domain/registro.br)</sub> | Não | ? | ⚪ aguardando |
| [TabNews](https://www.tabnews.com.br/GabrielSozinho/documentacao-da-api-do-tabnews) | Publicações e comentários da comunidade TabNews (leitura sem login)<br><sub>[exemplo](https://www.tabnews.com.br/api/v1/contents?per_page=1)</sub> | Não | ? | ⚪ aguardando |

**[⬆ voltar ao índice](#índice)**

### Livros, Cultura e Língua

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [A Bíblia Digital](https://github.com/omarciovsena/abibliadigital/blob/master/DOCUMENTATION.md) | Livros, capítulos e versículos da Bíblia em várias versões em português<br><sub>[exemplo](https://www.abibliadigital.com.br/api/books) · limite: 20 req/hora por endpoint sem token</sub> | Opcional | ? | ⚪ aguardando |
| [BrasilAPI ISBN](https://brasilapi.com.br/docs) | Dados de livros por ISBN, consultando várias fontes<br><sub>[exemplo](https://brasilapi.com.br/api/isbn/v1/9788545702870)</sub> | Não | ? | ⚪ aguardando |
| [Dicionário Aberto](https://api.dicionario-aberto.net/index.html) | Dicionário da língua portuguesa com definições e busca por prefixo e sufixo<br><sub>[exemplo](https://api.dicionario-aberto.net/word/casa)</sub> | Não | ? | ⚪ aguardando |
| [Vagalume](https://api.vagalume.com.br/docs/) | Letras, traduções, artistas e discografias de músicas | Chave grátis | ? | 🔑 requer chave |

**[⬆ voltar ao índice](#índice)**

### Ciência e Educação

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [SciELO ArticleMeta](http://articlemeta.scielo.org) | Metadados de periódicos e artigos científicos da rede SciELO<br><sub>[exemplo](http://articlemeta.scielo.org/api/v1/journal/identifiers/?collection=scl&limit=1)</sub> | Não | ? | ⚪ aguardando |

**[⬆ voltar ao índice](#índice)**

### Meio Ambiente

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [TerraBrasilis (INPE)](https://terrabrasilis.dpi.inpe.br/about/) | Desmatamento PRODES e alertas DETER via GeoServer (WFS/WMS)<br><sub>[exemplo](https://terrabrasilis.dpi.inpe.br/geoserver/ows?service=WFS&version=2.0.0&request=GetCapabilities)</sub> | Não | ? | ⚪ aguardando |

**[⬆ voltar ao índice](#índice)**

### Agropecuária

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [Embrapa AgroAPI](https://www.agroapi.cnptia.embrapa.br/portal/) | APIs da Embrapa de clima agrícola, solos, cultivares, agrotóxicos e satélite | Chave grátis | ? | 🔑 requer chave |

**[⬆ voltar ao índice](#índice)**

### Segurança Pública

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [Fogo Cruzado](https://api.fogocruzado.org.br) | Tiroteios registrados nas regiões metropolitanas de Rio, Recife, Salvador e Belém | Chave grátis | ? | 🔑 requer chave |

**[⬆ voltar ao índice](#índice)**

### Esportes e Loterias

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [API-Futebol](https://www.api-futebol.com.br) | Campeonatos, tabelas, rodadas e partidas do futebol brasileiro | Chave grátis | ? | 🔑 requer chave |
| [Cartola FC](https://github.com/giovanigenerali/cartrolandofc/blob/master/nova-api.md) | Status do mercado, atletas, clubes e partidas do fantasy game da Globo (API não oficial)<br><sub>[exemplo](https://api.cartola.globo.com/mercado/status)</sub> | Não | ? | ⚪ aguardando |
| [Loterias Caixa API](https://github.com/guto-alves/loterias-api) | Resultados da Mega-Sena, Lotofácil, Quina e demais loterias da Caixa<br><sub>[exemplo](https://loteriascaixa-api.herokuapp.com/api/megasena/latest)</sub> | Não | ? | ⚪ aguardando |
| [Resultado Mega](https://resultadomega.com.br/api/) | Todos os concursos da Mega-Sena desde 1996, próximo concurso e estatísticas<br><sub>[exemplo](https://resultadomega.com.br/api/ultimo.json)</sub> | Não | ? | ⚪ aguardando |

**[⬆ voltar ao índice](#índice)**

### Utilidades

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [Invertexto](https://api.invertexto.com) | Utilidades para devs brasileiros, como CEP, CNPJ, feriados e validação de documentos | Chave grátis | ? | 🔑 requer chave |

**[⬆ voltar ao índice](#índice)**

### Portais de Dados Abertos (CKAN)

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [ANTT Dados Abertos](https://dados.antt.gov.br) | Rodovias concedidas, pedágios, ferrovias e transporte de passageiros<br><sub>[exemplo](https://dados.antt.gov.br/api/3/action/status_show)</sub> | Não | ? | ⚪ aguardando |
| [CAPES Dados Abertos](https://dadosabertos.capes.gov.br) | Pós-graduação, bolsas, teses, dissertações e avaliação de programas<br><sub>[exemplo](https://dadosabertos.capes.gov.br/api/3/action/status_show)</sub> | Não | ? | ⚪ aguardando |
| [CCEE Dados Abertos](https://dadosabertos.ccee.org.br) | Preços, geração, consumo e contratos do mercado de energia elétrica<br><sub>[exemplo](https://dadosabertos.ccee.org.br/api/3/action/status_show)</sub> | Não | ? | ⚪ aguardando |
| [CVM Dados Abertos](https://dados.cvm.gov.br) | Fundos de investimento, companhias abertas e intermediários do mercado de capitais<br><sub>[exemplo](https://dados.cvm.gov.br/api/3/action/status_show)</sub> | Não | ? | ⚪ aguardando |
| [Distrito Federal Dados Abertos](https://dados.df.gov.br) | Dados abertos do Governo do Distrito Federal<br><sub>[exemplo](https://dados.df.gov.br/api/3/action/status_show)</sub> | Não | ? | ⚪ aguardando |
| [Prefeitura de Fortaleza Dados Abertos](https://dados.fortaleza.ce.gov.br) | Dados abertos da cidade de Fortaleza<br><sub>[exemplo](https://dados.fortaleza.ce.gov.br/api/3/action/status_show)</sub> | Não | ? | ⚪ aguardando |
| [Prefeitura de Porto Alegre Dados Abertos](https://dadosabertos.poa.br) | Dados abertos da cidade de Porto Alegre<br><sub>[exemplo](https://dadosabertos.poa.br/api/3/action/status_show)</sub> | Não | ? | ⚪ aguardando |
| [Prefeitura de São Paulo Dados Abertos](https://dados.prefeitura.sp.gov.br) | Dados abertos da cidade de São Paulo<br><sub>[exemplo](https://dados.prefeitura.sp.gov.br/api/3/action/status_show)</sub> | Não | ? | ⚪ aguardando |
| [Prefeitura do Recife Dados Abertos](https://dados.recife.pe.gov.br) | Dados abertos da cidade do Recife<br><sub>[exemplo](https://dados.recife.pe.gov.br/api/3/action/status_show)</sub> | Não | ? | ⚪ aguardando |
| [TSE Dados Abertos](https://dadosabertos.tse.jus.br) | Resultados eleitorais, candidatos, eleitorado e prestação de contas<br><sub>[exemplo](https://dadosabertos.tse.jus.br/api/3/action/status_show)</sub> | Não | ? | ⚪ aguardando |

**[⬆ voltar ao índice](#índice)**

### Internacionais com Dados do Brasil

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [Banco Mundial](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392) | Indicadores econômicos e sociais do Brasil, como PIB, pobreza e educação<br><sub>[exemplo](https://api.worldbank.org/v2/country/BR/indicator/NY.GDP.MKTP.CD?format=json&per_page=1)</sub> | Não | ? | ⚪ aguardando |
| [CoinGecko](https://www.coingecko.com/pt/api/documentation) | Cotação de criptomoedas em reais e outras moedas<br><sub>[exemplo](https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=brl)</sub> | Opcional | ? | ⚪ aguardando |
| [Frankfurter](https://frankfurter.dev) | Câmbio do real e de outras moedas com base nas taxas do Banco Central Europeu<br><sub>[exemplo](https://api.frankfurter.app/latest?from=BRL)</sub> | Não | ? | ⚪ aguardando |
| [Open-Meteo](https://open-meteo.com/en/docs) | Previsão do tempo e histórico climático para qualquer coordenada do Brasil<br><sub>[exemplo](https://api.open-meteo.com/v1/forecast?latitude=-23.55&longitude=-46.63&current_weather=true)</sub> | Não | ? | ⚪ aguardando |
| [REST Countries](https://restcountries.com) | Dados gerais de países, como população, moeda, idiomas e fronteiras<br><sub>[exemplo](https://restcountries.com/v3.1/alpha/br)</sub> | Não | ? | ⚪ aguardando |
| [Wikipédia em Português](https://pt.wikipedia.org/api/rest_v1/) | Resumos, conteúdo e mídias de artigos da Wikipédia lusófona<br><sub>[exemplo](https://pt.wikipedia.org/api/rest_v1/page/summary/Brasil)</sub> | Não | ? | ⚪ aguardando |

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
