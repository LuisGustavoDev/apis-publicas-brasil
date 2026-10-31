<!-- Este arquivo é gerado automaticamente por scripts/build_readme.py. Edite data/apis.yaml ou scripts/README.template.md. -->

<div align="center">

# 🇧🇷 APIs Públicas Brasileiras

**Uma lista de APIs públicas e gratuitas do Brasil que se verifica sozinha todos os dias.**

![APIs: 215](https://img.shields.io/badge/APIs-215-009c3b) ![online: 177/207](https://img.shields.io/badge/online-177%2F207-dfb317) ![verificado em: 31/10/2026](https://img.shields.io/badge/verificado%20em-31%2F10%2F2026-blue)

</div>

São **215 APIs** em **22 categorias**: CEP, CNPJ, bancos, Pix, câmbio, IBGE, Câmara, Senado, FIPE, feriados, clima e mais. Todo dia um robô testa cada uma e atualiza esta página com o status, o tempo de resposta e se ela aceita chamadas direto do navegador (CORS).

Última verificação automática: **31/10/2026** · 177 de 207 APIs testadas estão no ar.

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

🟢 **152** online · 🟡 **4** lentas · 🟠 **9** instáveis · 🔴 **20** fora do ar · 🔵 **5** documentação · 🛡️ **10** bloquearam o robô · 🟣 **7** não são API · 🔑 **8** requerem chave

| | Situação | APIs | O que significa |
|:---:|---|:---:|---|
| 🟢 | Online | **152** | respondeu com dados (JSON, XML ou CSV) na última verificação |
| 🟡 | Lentas | **4** | respondeu, mas levou mais de 3 segundos |
| 🟠 | Instáveis | **9** | está no ar, mas falhou em mais de 5% das verificações dos últimos 30 dias |
| 🔴 | Fora do ar | **20** | não respondeu ou deu erro na última verificação |
| 🔵 | Documentação | **5** | a API existe, mas o endereço de exemplo abre a documentação (Swagger, Redoc, WSDL...), não dados |
| 🛡️ | Bloquearam o robô | **10** | o servidor está no ar, mas recusou o teste automático (firewall, captcha ou acesso negado) |
| 🟣 | Não são API | **7** | o endereço de exemplo abre um site comum, sem dados nem documentação de API |
| 🔑 | Requerem chave | **8** | precisa de chave ou cadastro, por isso não é testada automaticamente |
| | **Total** | **215** | |

🇧🇷 Além disso, **11** APIs só funcionam quando acessadas do Brasil: elas bloqueiam servidores no exterior (como Vercel, AWS ou Heroku fora do país) e estão marcadas com 🇧🇷 nas tabelas.

Ao lado de cada categoria aparecem as mesmas contagens, com os símbolos da tabela acima.

- [CEP e Endereços](#cep-e-endereços) (8) — 🟢 7 · 🟣 1
- [CNPJ e Empresas](#cnpj-e-empresas) (7) — 🟢 7
- [Bancos e Pagamentos](#bancos-e-pagamentos) (6) — 🟢 6
- [Economia e Mercado Financeiro](#economia-e-mercado-financeiro) (15) — 🟢 11 · 🟡 1 · 🔵 2 · 🛡️ 1
- [Governo, Legislativo e Justiça](#governo-legislativo-e-justiça) (20) — 🟢 6 · 🔴 4 · 🔵 1 · 🛡️ 2 · 🟣 5 · 🔑 2 (🇧🇷 1 só do Brasil)
- [IBGE e Geografia](#ibge-e-geografia) (13) — 🟢 10 · 🟠 1 · 🔴 2 (🇧🇷 8 só do Brasil)
- [Calendário e Feriados](#calendário-e-feriados) (3) — 🟢 3
- [Clima e Tempo](#clima-e-tempo) (7) — 🟢 3 · 🟠 1 · 🔴 1 · 🛡️ 1 · 🔑 1
- [Veículos](#veículos) (3) — 🟢 2 · 🔑 1
- [Transporte](#transporte) (4) — 🟢 2 · 🔴 1 · 🔑 1
- [Saúde](#saúde) (2) — 🔴 1 · 🟣 1
- [Comércio e Tributos](#comércio-e-tributos) (5) — 🟢 4 · 🟠 1
- [Internet, Telefonia e Domínios](#internet-telefonia-e-domínios) (6) — 🟢 5 · 🟠 1
- [Livros, Cultura e Língua](#livros-cultura-e-língua) (21) — 🟢 15 · 🟠 2 · 🔴 3 · 🔵 1
- [Ciência e Educação](#ciência-e-educação) (11) — 🟢 8 · 🔴 2 · 🛡️ 1 (🇧🇷 1 só do Brasil)
- [Meio Ambiente](#meio-ambiente) (4) — 🟠 1 · 🔴 1 · 🔵 1 · 🔑 1
- [Agropecuária](#agropecuária) (2) — 🟢 2
- [Segurança Pública](#segurança-pública) (3) — 🟢 1 · 🛡️ 1 · 🔑 1
- [Esportes e Loterias](#esportes-e-loterias) (7) — 🟢 6 · 🟠 1
- [Utilidades](#utilidades) (5) — 🟢 5
- [Portais de Dados Abertos (CKAN)](#portais-de-dados-abertos-ckan) (29) — 🟢 18 · 🟡 1 · 🟠 1 · 🔴 5 · 🛡️ 4 (🇧🇷 1 só do Brasil)
- [Internacionais com Dados do Brasil](#internacionais-com-dados-do-brasil) (34) — 🟢 31 · 🟡 2 · 🔑 1

## APIs

### CEP e Endereços

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [ApiCEP](https://apicep.com) | Endereço por CEP servido como arquivo JSON estático em CDN<br><sub>[exemplo](https://cdn.apicep.com/file/apicep/01001-000.json)</sub> | Não | Sim | 🟢 online<br><sub>100% · 384 ms</sub> |
| [AwesomeAPI CEP](https://docs.awesomeapi.com.br) | Endereço por CEP com latitude, longitude e código IBGE<br><sub>[exemplo](https://cep.awesomeapi.com.br/json/01001000)</sub> | Opcional | ? | 🟢 online<br><sub>100% · 128 ms</sub> |
| [Brasil Aberto](https://docs.brasilaberto.com) | CEP, cidades, bairros, ruas, CNPJ e rastreio de encomendas | Chave grátis | Não | 🟣 não é API<br><sub>100% · 316 ms · 🔑 testada sem chave</sub> |
| [BrasilAPI CEP v2](https://brasilapi.com.br/docs) | CEP com coordenadas geográficas, consultando vários provedores com fallback<br><sub>[exemplo](https://brasilapi.com.br/api/cep/v2/01001000)</sub> | Não | Sim | 🟢 online<br><sub>100% · 143 ms</sub> |
| [CEP Aberto](https://www.cepaberto.com/api_key) | CEP, busca por coordenadas e listagem de cidades por estado | Chave grátis | ? | 🟢 online<br><sub>100% · 1351 ms · 🔑 testada sem chave</sub> |
| [OpenCEP](https://opencep.com) | Consulta de endereço por CEP, gratuita e sem cadastro<br><sub>[exemplo](https://opencep.com/v1/01001000)</sub> | Não | Sim | 🟢 online<br><sub>100% · 75 ms</sub> |
| [ViaCEP](https://viacep.com.br) | Consulta de endereço por CEP e busca de CEP por endereço<br><sub>[exemplo](https://viacep.com.br/ws/01001000/json/)</sub> | Não | Sim | 🟢 online<br><sub>100% · 436 ms</sub> |
| [Zippopotam.us](https://www.zippopotam.us) | Cidade e estado a partir do prefixo do CEP<br><sub>[exemplo](https://api.zippopotam.us/br/01000-000)</sub> | Não | Sim | 🟢 online<br><sub>100% · 199 ms</sub> |

**[⬆ voltar ao índice](#índice)**

### CNPJ e Empresas

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [BrasilAPI CNPJ](https://brasilapi.com.br/docs) | Dados cadastrais de empresas pela base pública da Receita Federal<br><sub>[exemplo](https://brasilapi.com.br/api/cnpj/v1/19131243000197)</sub> | Não | Sim | 🟢 online<br><sub>100% · 129 ms</sub> |
| [BrasilAPI Corretoras](https://brasilapi.com.br/docs) | Corretoras de valores registradas na CVM<br><sub>[exemplo](https://brasilapi.com.br/api/cvm/corretoras/v1)</sub> | Não | Sim | 🟢 online<br><sub>100% · 341 ms</sub> |
| [CNPJ.ws Pública](https://docs.cnpj.ws/referencia-de-api/api-publica) | Consulta de CNPJ com dados de sócios, atividades e inscrições estaduais<br><sub>[exemplo](https://publica.cnpj.ws/cnpj/19131243000197) · limite: 3 req/min por IP</sub> | Não | Sim | 🟢 online<br><sub>100% · 424 ms</sub> |
| [CNPJá Open](https://cnpja.com/api/open) | Dados cadastrais de estabelecimentos, sócios e atividades por CNPJ<br><sub>[exemplo](https://open.cnpja.com/office/19131243000197) · limite: 5 req/min por IP</sub> | Não | Sim | 🟢 online<br><sub>100% · 308 ms</sub> |
| [Minha Receita](https://docs.minhareceita.org) | Dados públicos de CNPJ da Receita Federal, projeto de código aberto<br><sub>[exemplo](https://minhareceita.org/19131243000197)</sub> | Não | Sim | 🟢 online<br><sub>100% · 296 ms</sub> |
| [OpenCNPJ](https://opencnpj.org) | Consulta de CNPJ com base nos dados públicos da Receita Federal<br><sub>[exemplo](https://api.opencnpj.org/19131243000197)</sub> | Não | Sim | 🟢 online<br><sub>100% · 373 ms</sub> |
| [ReceitaWS](https://developers.receitaws.com.br) | Consulta de CNPJ com situação cadastral e quadro de sócios<br><sub>[exemplo](https://receitaws.com.br/v1/cnpj/19131243000197) · limite: 3 req/min no plano gratuito</sub> | Não | Não | 🟢 online<br><sub>100% · 188 ms</sub> |

**[⬆ voltar ao índice](#índice)**

### Bancos e Pagamentos

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [Banco Central Agências](https://olinda.bcb.gov.br/olinda/servico/Informes_Agencias/versao/v1/swagger-ui3) | Agências bancárias por instituição, município e endereço<br><sub>[exemplo](https://olinda.bcb.gov.br/olinda/servico/Informes_Agencias/versao/v1/odata/)</sub> | Não | Sim | 🟢 online<br><sub>100% · 643 ms</sub> |
| [Banco Central Estatísticas do Pix](https://dadosabertos.bcb.gov.br/dataset/pix) | Chaves cadastradas, transações por município e estatísticas de fraudes do Pix<br><sub>[exemplo](https://olinda.bcb.gov.br/olinda/servico/Pix_DadosAbertos/versao/v1/odata/)</sub> | Não | Sim | 🟢 online<br><sub>100% · 79 ms</sub> |
| [Banco Central Postos de Atendimento](https://olinda.bcb.gov.br/olinda/servico/Informes_PostosDeAtendimentoEletronico/versao/v1/swagger-ui3) | Postos de atendimento eletrônico de instituições financeiras<br><sub>[exemplo](https://olinda.bcb.gov.br/olinda/servico/Informes_PostosDeAtendimentoEletronico/versao/v1/odata/)</sub> | Não | Sim | 🟢 online<br><sub>100% · 2624 ms</sub> |
| [Banco Central Taxas de Juros](https://dadosabertos.bcb.gov.br/dataset/taxas-de-juros-de-operacoes-de-credito) | Taxas de juros praticadas pelos bancos em cada modalidade de crédito<br><sub>[exemplo](https://olinda.bcb.gov.br/olinda/servico/taxaJuros/versao/v2/odata/)</sub> | Não | Sim | 🟢 online<br><sub>100% · 639 ms</sub> |
| [BrasilAPI Bancos](https://brasilapi.com.br/docs) | Lista de bancos com código de compensação e ISPB<br><sub>[exemplo](https://brasilapi.com.br/api/banks/v1)</sub> | Não | Sim | 🟢 online<br><sub>100% · 66 ms</sub> |
| [BrasilAPI Participantes do Pix](https://brasilapi.com.br/docs) | Instituições participantes do Pix, com modalidade e início da operação<br><sub>[exemplo](https://brasilapi.com.br/api/pix/v1/participants)</sub> | Não | Sim | 🟢 online<br><sub>100% · 50 ms</sub> |

**[⬆ voltar ao índice](#índice)**

### Economia e Mercado Financeiro

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [AwesomeAPI Moedas](https://docs.awesomeapi.com.br) | Cotação de moedas e criptomoedas em tempo real e histórico<br><sub>[exemplo](https://economia.awesomeapi.com.br/json/last/USD-BRL) · limite: 100 mil req/mês grátis com chave</sub> | Opcional | ? | 🟢 online<br><sub>100% · 35 ms</sub> |
| [Banco Central Focus (Expectativas)](https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/documentacao) | Expectativas do mercado para inflação, Selic, PIB e câmbio (Boletim Focus)<br><sub>[exemplo](https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoAnuais?$top=5&$format=json)</sub> | Não | Sim | 🟢 online<br><sub>100% · 100 ms</sub> |
| [Banco Central PTAX](https://dadosabertos.bcb.gov.br) | Cotações oficiais PTAX de moedas estrangeiras<br><sub>[exemplo](https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/Moedas?$format=json)</sub> | Não | Sim | 🟢 online<br><sub>100% · 67 ms</sub> |
| [Banco Central SGS](https://dadosabertos.bcb.gov.br) | Séries temporais do Banco Central, como Selic, IPCA e CDI<br><sub>[exemplo](https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados/ultimos/1?formato=json)</sub> | Não | Sim | 🟢 online<br><sub>100% · 71 ms</sub> |
| [brapi](https://brapi.dev/docs) | Cotações, histórico e dividendos de ações, FIIs e BDRs da B3<br><sub>[exemplo](https://brapi.dev/api/quote/PETR4) · limite: PETR4, MGLU3, VALE3 e ITUB4 funcionam sem chave</sub> | Chave grátis | Sim | 🟢 online<br><sub>100% · 279 ms</sub> |
| [BrasilAPI Câmbio](https://brasilapi.com.br/docs) | Moedas disponíveis e cotações de câmbio por data<br><sub>[exemplo](https://brasilapi.com.br/api/cambio/v1/moedas)</sub> | Não | Sim | 🟢 online<br><sub>100% · 39 ms</sub> |
| [BrasilAPI Taxas](https://brasilapi.com.br/docs) | Valores atuais de Selic, CDI e IPCA<br><sub>[exemplo](https://brasilapi.com.br/api/taxas/v1)</sub> | Não | Sim | 🟢 online<br><sub>100% · 41 ms</sub> |
| [Foxbit](https://docs.foxbit.com.br) | Mercados, cotações e livro de ofertas de criptomoedas em reais<br><sub>[exemplo](https://api.foxbit.com.br/rest/v3/markets)</sub> | Não | Sim | 🟢 online<br><sub>100% · 307 ms</sub> |
| [HG Brasil Finance](https://hgbrasil.com/docs) | Cotações de moedas, índices da bolsa e taxas como Selic e CDI | Chave grátis | Não | 🟢 online<br><sub>100% · 109 ms · 🔑 testada sem chave</sub> |
| [Ipeadata](http://www.ipeadata.gov.br/api/) | Milhares de séries econômicas, sociais e regionais do Ipea<br><sub>[exemplo](http://www.ipeadata.gov.br/api/odata4/Temas/)</sub> | Não | Sim | 🟡 lenta<br><sub>100% · 15140 ms</sub> |
| [Mercado Bitcoin](https://api.mercadobitcoin.net/api/v4/docs) | Pares negociados, cotações, livro de ofertas e candles de criptomoedas em reais<br><sub>[exemplo](https://api.mercadobitcoin.net/api/v4/symbols)</sub> | Não | Sim | 🟢 online<br><sub>100% · 627 ms</sub> |
| [SICONFI (Tesouro Nacional)](https://apidatalake.tesouro.gov.br/docs/siconfi/) | Relatórios fiscais e contábeis de estados e municípios (RREO, RGF, DCA)<br><sub>[exemplo](https://apidatalake.tesouro.gov.br/ords/siconfi/tt/entes)</sub> | Não | Não | 🟢 online<br><sub>100% · 69 ms</sub> |
| [Tesouro Nacional CUSTOS](https://apidatalake.tesouro.gov.br/docs/custos/) | Custos do governo federal por órgão, programa e natureza de despesa<br><sub>[exemplo](https://apidatalake.tesouro.gov.br/docs/custos/)</sub> | Não | Não | 🔵 documentação<br><sub>100% · 390 ms</sub> |
| [Tesouro Nacional SADIPEM](https://apidatalake.tesouro.gov.br/docs/sadipem/) | Operações de crédito e dívida pública de estados e municípios<br><sub>[exemplo](https://apidatalake.tesouro.gov.br/docs/sadipem/)</sub> | Não | Não | 🔵 documentação<br><sub>100% · 781 ms</sub> |
| [Tesouro Nacional Transferências Constitucionais](https://apiapex.tesouro.gov.br/aria/v1/transferencias_constitucionais/docs) | Repasses constitucionais da União a estados e municípios, como FPM e FPE<br><sub>[exemplo](https://apiapex.tesouro.gov.br/aria/v1/transferencias_constitucionais/docs)</sub> | Não | ? | 🛡️ bloqueou o robô<br><sub>HTTP 403</sub> |

**[⬆ voltar ao índice](#índice)**

### Governo, Legislativo e Justiça

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [Assembleia Legislativa de Minas Gerais](https://dadosabertos.almg.gov.br/ws/ajuda/sobre) | Deputados estaduais, proposições, votações e legislação mineira<br><sub>[exemplo](https://dadosabertos.almg.gov.br/ws/deputados/em_exercicio?formato=json)</sub> | Não | Sim | 🔴 fora do ar |
| [Brasil.IO](https://blog.brasil.io/2020/10/10/como-acessar-os-dados-do-brasil-io/) | Dados públicos tratados, como sócios de empresas, eleições e gastos | Chave grátis | ? | 🟢 online<br><sub>100% · 568 ms · 🔑 testada sem chave</sub> |
| [Câmara dos Deputados](https://dadosabertos.camara.leg.br/swagger/api.html) | Deputados, proposições, votações, despesas e eventos da Câmara<br><sub>[exemplo](https://dadosabertos.camara.leg.br/api/v2/deputados?itens=5)</sub> | Não | Sim | 🔴 fora do ar |
| [Compras.gov.br Dados Abertos](https://dadosabertos.compras.gov.br/swagger-ui/index.html) | Licitações, contratos, materiais, serviços e fornecedores do governo federal | Não | ? | 🔑 requer chave |
| [DataJud](https://datajud-wiki.cnj.jus.br/api-publica/) | Metadados de processos judiciais de todos os tribunais do país (CNJ) | Chave pública | ? | 🟢 online<br><sub>100% · 98 ms · 🔑 testada sem chave</sub> |
| [INLABS (Diário Oficial da União)](https://inlabs.in.gov.br) | Edições completas do Diário Oficial da União em XML | Chave grátis | ? | 🔑 requer chave |
| [LexML](https://www12.senado.leg.br/dados-abertos/legislativo/legislacao/acervo-do-portal-lexml) | Busca em leis, decretos, jurisprudência e proposições de todo o país (SRU, XML)<br><sub>[exemplo](https://www.lexml.gov.br/busca/SRU?operation=searchRetrieve&query=urn+any+lei&maximumRecords=1)</sub> | Não | Não | 🟣 não é API<br><sub>100% · 193 ms</sub> |
| [PNCP (Portal Nacional de Contratações Públicas)](https://pncp.gov.br/api/consulta/swagger-ui/index.html) | Contratações, atas e contratos de todos os entes públicos do país<br><sub>[exemplo](https://pncp.gov.br/api/consulta/v1/contratacoes/publicacao?dataInicial=20260101&dataFinal=20260102&codigoModalidadeContratacao=8&pagina=1)</sub> | Não | Sim | 🟢 online<br><sub>100% · 61 ms</sub> |
| [Portal Brasileiro de Dados Abertos](https://www.gov.br/conecta/catalogo/apis/api-portal-de-dados-abertos) | Catálogo nacional de conjuntos de dados abertos do governo (dados.gov.br) | Chave grátis | Não | 🟢 online<br><sub>100% · 39 ms · 🔑 testada sem chave</sub> |
| [Portal da Transparência](https://portaldatransparencia.gov.br/api-de-dados) | Gastos, contratos, servidores e benefícios do governo federal | Chave grátis | ? | 🟢 online<br><sub>100% · 34 ms · 🔑 testada sem chave</sub> |
| [Querido Diário](https://docs.queridodiario.ok.org.br/en/latest/using/public-api.html) | Busca textual em diários oficiais de municípios brasileiros<br><sub>[exemplo](https://api.queridodiario.ok.org.br/gazettes?querystring=educacao&size=1) · limite: Recomenda até 60 req/min</sub> | Não | ? | 🔴 fora do ar |
| [Senado Federal](https://legis.senado.leg.br/dadosabertos/docs/) | Senadores, matérias, votações e comissões do Senado<br><sub>[exemplo](https://legis.senado.leg.br/dadosabertos/senador/lista/atual.json)</sub> | Não | Sim | 🟢 online<br><sub>100% · 192 ms</sub> |
| [SIORG](https://estruturaorganizacional.dados.gov.br) | Estrutura organizacional dos órgãos do governo federal<br><sub>[exemplo](https://estruturaorganizacional.dados.gov.br)</sub> | Não | Sim | 🔵 documentação<br><sub>100% · 86 ms</sub> |
| [TCE-MG Dados Abertos](https://dadosabertos.tce.mg.gov.br/) | Dados fiscais e de contratações dos municípios de Minas Gerais<br><sub>[exemplo](https://dadosabertos.tce.mg.gov.br/)</sub> | Não | Não | 🟣 não é API<br><sub>100% · 89 ms · ⚠️ certificado SSL · 🇧🇷 só do Brasil</sub> |
| [TCE-PE Dados Abertos](https://www.tce.pe.gov.br/internet/index.php/dados-abertos) | Licitações, contratos, despesas e fornecedores fiscalizados pelo TCE de Pernambuco<br><sub>[exemplo](https://www.tce.pe.gov.br/internet/index.php/dados-abertos)</sub> | Não | Não | 🟣 não é API<br><sub>100% · 581 ms · ⚠️ certificado SSL</sub> |
| [TCE-RN Dados Abertos](https://apidadosabertos.tce.rn.gov.br/) | Licitações, contratos e órgãos fiscalizados pelo Tribunal de Contas do RN<br><sub>[exemplo](https://apidadosabertos.tce.rn.gov.br/)</sub> | Não | Sim | 🟣 não é API<br><sub>44% · 2237 ms</sub> |
| [TCM-CE Dados Abertos](https://api.tcm.ce.gov.br/) | Dados dos municípios cearenses fiscalizados pelo Tribunal de Contas<br><sub>[exemplo](https://api.tcm.ce.gov.br/)</sub> | Não | ? | 🔴 fora do ar |
| [TCU Dados Abertos](https://sites.tcu.gov.br/dados-abertos/) | Acórdãos, súmulas, jurisprudência e normas do Tribunal de Contas da União<br><sub>[exemplo](https://sites.tcu.gov.br/dados-abertos/)</sub> | Não | Não | 🟣 não é API<br><sub>100% · 37 ms</sub> |
| [Transferegov](https://api-publica.transferegov.gestao.gov.br/ted/docs) | Transferências da União, emendas especiais, fundo a fundo e parcerias<br><sub>[exemplo](https://api-publica.transferegov.gestao.gov.br/ted/docs)</sub> | Não | Não | 🛡️ bloqueou o robô<br><sub>HTTP 200</sub> |
| [TSE DivulgaCandContas](https://divulgacandcontas.tse.jus.br/divulga/) | Eleições, candidatos, bens declarados e prestação de contas de campanha<br><sub>[exemplo](https://divulgacandcontas.tse.jus.br/divulga/rest/v1/eleicao/ordinarias)</sub> | Não | Sim | 🛡️ bloqueou o robô<br><sub>HTTP 403</sub> |

**[⬆ voltar ao índice](#índice)**

### IBGE e Geografia

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [BrasilAPI IBGE](https://brasilapi.com.br/docs) | Estados e municípios do IBGE, funcionando também em servidores fora do Brasil<br><sub>[exemplo](https://brasilapi.com.br/api/ibge/uf/v1)</sub> | Não | Sim | 🟠 instável<br><sub>89% · 56 ms</sub> |
| [IBGE Agregados (SIDRA)](https://servicodados.ibge.gov.br/api/docs/agregados?versao=3) | Tabelas de pesquisas do IBGE, como PNAD, Censo e PIB<br><sub>[exemplo](https://servicodados.ibge.gov.br/api/v3/agregados)</sub> | Não | Sim | 🟢 online<br><sub>100% · 104 ms · 🇧🇷 só do Brasil</sub> |
| [IBGE Calendário](https://servicodados.ibge.gov.br/api/docs/calendario?versao=3) | Calendário de divulgações de pesquisas e eventos do IBGE<br><sub>[exemplo](https://servicodados.ibge.gov.br/api/v3/calendario/?qtd=1)</sub> | Não | Sim | 🟢 online<br><sub>100% · 105 ms · 🇧🇷 só do Brasil</sub> |
| [IBGE CNAE](https://servicodados.ibge.gov.br/api/docs/cnae?versao=2) | Classificação Nacional de Atividades Econômicas (seções, classes e subclasses)<br><sub>[exemplo](https://servicodados.ibge.gov.br/api/v2/cnae/secoes)</sub> | Não | Sim | 🟢 online<br><sub>100% · 89 ms · 🇧🇷 só do Brasil</sub> |
| [IBGE Geoserviços](https://geoservicos.ibge.gov.br/geoserver/web/) | Camadas geográficas oficiais do IBGE via GeoServer (WFS/WMS)<br><sub>[exemplo](https://geoservicos.ibge.gov.br/geoserver/ows?service=WFS&version=2.0.0&request=GetCapabilities)</sub> | Não | Não | 🟢 online<br><sub>100% · 894 ms</sub> |
| [IBGE Localidades](https://servicodados.ibge.gov.br/api/docs/localidades) | Regiões, estados, municípios e distritos com códigos oficiais<br><sub>[exemplo](https://servicodados.ibge.gov.br/api/v1/localidades/estados)</sub> | Não | Sim | 🟢 online<br><sub>100% · 78 ms · 🇧🇷 só do Brasil</sub> |
| [IBGE Malhas](https://servicodados.ibge.gov.br/api/docs/malhas?versao=3) | Contornos geográficos de estados e municípios em GeoJSON ou SVG<br><sub>[exemplo](https://servicodados.ibge.gov.br/api/v3/malhas/estados/SP?formato=application/vnd.geo+json)</sub> | Não | Sim | 🟢 online<br><sub>100% · 71 ms · 🇧🇷 só do Brasil</sub> |
| [IBGE Nomes](https://servicodados.ibge.gov.br/api/docs/nomes?versao=2) | Frequência e ranking de nomes por década, segundo o Censo<br><sub>[exemplo](https://servicodados.ibge.gov.br/api/v2/censos/nomes/maria)</sub> | Não | Sim | 🟢 online<br><sub>100% · 134 ms · 🇧🇷 só do Brasil</sub> |
| [IBGE Notícias](https://servicodados.ibge.gov.br/api/docs/noticias?versao=3) | Notícias e releases publicados pela Agência IBGE<br><sub>[exemplo](https://servicodados.ibge.gov.br/api/v3/noticias/?qtd=1)</sub> | Não | Sim | 🟢 online<br><sub>100% · 130 ms · 🇧🇷 só do Brasil</sub> |
| [IBGE Países](https://servicodados.ibge.gov.br/api/docs/paises) | Indicadores, histórico e dados gerais de países<br><sub>[exemplo](https://servicodados.ibge.gov.br/api/v1/paises/BR)</sub> | Não | Sim | 🟢 online<br><sub>100% · 62 ms · 🇧🇷 só do Brasil</sub> |
| [IBGE Pesquisas](https://servicodados.ibge.gov.br/api/docs/pesquisas) | Lista de pesquisas do IBGE e seus indicadores<br><sub>[exemplo](https://servicodados.ibge.gov.br/api/v1/pesquisas)</sub> | Não | Sim | 🔴 fora do ar |
| [IBGE Projeção da População](https://servicodados.ibge.gov.br/api/docs/projecoes) | Projeção da população brasileira em tempo real e por estado<br><sub>[exemplo](https://servicodados.ibge.gov.br/api/v1/projecoes/populacao/BR)</sub> | Não | ? | 🔴 fora do ar |
| [IBGE SIDRA](https://apisidra.ibge.gov.br/home/ajuda) | Valores das tabelas do SIDRA, como IPCA, PNAD, PIB e Censo<br><sub>[exemplo](https://apisidra.ibge.gov.br/values/t/7060/n1/all/v/63/p/last/c315/7169)</sub> | Não | Sim | 🟢 online<br><sub>100% · 88 ms</sub> |

**[⬆ voltar ao índice](#índice)**

### Calendário e Feriados

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [BrasilAPI Feriados](https://brasilapi.com.br/docs) | Feriados nacionais de um ano, incluindo os móveis<br><sub>[exemplo](https://brasilapi.com.br/api/feriados/v1/2026)</sub> | Não | Sim | 🟢 online<br><sub>100% · 86 ms</sub> |
| [Calendarific](https://calendarific.com/api-documentation) | Feriados nacionais, estaduais e datas comemorativas | Chave grátis | ? | 🟢 online<br><sub>100% · 487 ms · 🔑 testada sem chave</sub> |
| [Nager.Date](https://date.nager.at) | Feriados públicos do Brasil e de outros 100+ países<br><sub>[exemplo](https://date.nager.at/api/v3/PublicHolidays/2026/BR)</sub> | Não | Sim | 🟢 online<br><sub>100% · 238 ms</sub> |

**[⬆ voltar ao índice](#índice)**

### Clima e Tempo

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [BrasilAPI CPTEC](https://brasilapi.com.br/docs) | Previsão do tempo, condições nas capitais e ondas, com dados do CPTEC/INPE<br><sub>[exemplo](https://brasilapi.com.br/api/cptec/v1/clima/capital)</sub> | Não | ? | 🔴 fora do ar<br><sub>HTTP 500</sub> |
| [Climatempo Advisor](https://advisor.climatempo.com.br) | Previsão do tempo, condições atuais e alertas para cidades brasileiras | Chave grátis | ? | 🟠 instável<br><sub>88% · 255 ms · 🔑 testada sem chave</sub> |
| [CPTEC/INPE (XML)](http://servicos.cptec.inpe.br/XML/) | Previsão de 7 dias por cidade direto do serviço oficial do CPTEC, em XML<br><sub>[exemplo](http://servicos.cptec.inpe.br/XML/cidade/7dias/241/previsao.xml)</sub> | Não | Não | 🟢 online<br><sub>100% · 74 ms</sub> |
| [HG Brasil Weather](https://hgbrasil.com/docs) | Previsão do tempo para cidades brasileiras | Chave grátis | Não | 🟢 online<br><sub>100% · 312 ms · 🔑 testada sem chave</sub> |
| [INMET Alertas](https://portal.inmet.gov.br/noticias/saiba-como-acessar-os-dados-meteorol%C3%B3gicos-dispon%C3%ADveis-no-site-do-inmet) | Avisos meteorológicos oficiais em feed RSS<br><sub>[exemplo](https://apiprevmet3.inmet.gov.br/avisos/rss)</sub> | Não | Sim | 🟢 online<br><sub>100% · 588 ms</sub> |
| [INMET Estações](https://portal.inmet.gov.br/manual/manual-de-uso-da-api-esta%C3%A7%C3%B5es) | Dados horários e diários das estações meteorológicas automáticas e convencionais<br><sub>limite: Até cerca de 6 meses por consulta</sub> | Token grátis | ? | 🔑 requer chave |
| [Tábua de Marés](https://tabuamare.devtu.qzz.io/) | Previsão de marés dos portos brasileiros com base nas tábuas da Marinha<br><sub>[exemplo](https://tabuamare.devtu.qzz.io/)</sub> | Não | Não | 🛡️ bloqueou o robô<br><sub>HTTP 200</sub> |

**[⬆ voltar ao índice](#índice)**

### Veículos

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [BrasilAPI FIPE](https://brasilapi.com.br/docs) | Marcas, veículos, preços e tabelas de referência da FIPE<br><sub>[exemplo](https://brasilapi.com.br/api/fipe/marcas/v1/carros)</sub> | Não | Sim | 🟢 online<br><sub>100% · 127 ms</sub> |
| [FIPE (Parallelum)](https://github.com/deividfortuna/fipe) | Marcas, modelos, anos e preços da Tabela FIPE<br><sub>[exemplo](https://parallelum.com.br/fipe/api/v2/cars/brands)</sub> | Opcional | Sim | 🟢 online<br><sub>100% · 163 ms</sub> |
| [FIPE (site oficial)](https://veiculos.fipe.org.br) | Consulta oficial da Tabela FIPE por marca, modelo e ano (requisições POST) | Não | ? | 🔑 requer chave |

**[⬆ voltar ao índice](#índice)**

### Transporte

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [AISWEB (DECEA)](http://www.aisweb.aer.mil.br/api/doc/index.cfm) | Informações aeronáuticas oficiais, como cartas, NOTAM e dados de aeródromos | Chave grátis | ? | 🔑 requer chave |
| [OpenSky Network](https://openskynetwork.github.io/opensky-api/rest.html) | Posição em tempo real das aeronaves sobre o Brasil<br><sub>[exemplo](https://opensky-network.org/api/states/all?lamin=-34&lomin=-74&lamax=6&lomax=-34) · limite: Uso anônimo com cota diária menor</sub> | Opcional | Não | 🔴 fora do ar |
| [REDEMET (DECEA)](https://api-redemet.decea.mil.br/) | METAR, TAF, imagens de radar e satélite da meteorologia aeronáutica | Chave grátis | ? | 🟢 online<br><sub>100% · 95 ms · 🔑 testada sem chave</sub> |
| [SPTrans Olho Vivo](https://www.sptrans.com.br/desenvolvedores/api-do-olho-vivo-guia-de-referencia/documentacao-api/) | Posição dos ônibus, linhas, paradas e previsão de chegada em São Paulo | Token grátis | ? | 🟢 online<br><sub>100% · 140 ms · 🔑 testada sem chave</sub> |

**[⬆ voltar ao índice](#índice)**

### Saúde

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [OMS Global Health Observatory](https://www.who.int/data/gho/info/gho-odata-api) | Indicadores de saúde da OMS para o Brasil, como expectativa de vida e mortalidade<br><sub>[exemplo](https://ghoapi.azureedge.net/api/Dimension)</sub> | Não | ? | 🔴 fora do ar<br><sub>HTTP 500</sub> |
| [OpenDataSUS](https://opendatasus.saude.gov.br) | Catálogo de dados abertos do Ministério da Saúde (API CKAN)<br><sub>[exemplo](https://opendatasus.saude.gov.br/api/3/action/package_list)</sub> | Não | Não | 🟣 não é API<br><sub>100% · 553 ms</sub> |

**[⬆ voltar ao índice](#índice)**

### Comércio e Tributos

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [BrasilAPI NCM](https://brasilapi.com.br/docs) | Busca na Nomenclatura Comum do Mercosul usada em notas fiscais<br><sub>[exemplo](https://brasilapi.com.br/api/ncm/v1?search=3305)</sub> | Não | Sim | 🟢 online<br><sub>100% · 2070 ms</sub> |
| [Cosmos Bluesoft](https://cosmos.bluesoft.com.br) | Catálogo de produtos por GTIN/EAN e produtos por NCM | Chave grátis | ? | 🟢 online<br><sub>100% · 452 ms · 🔑 testada sem chave</sub> |
| [Mercado Livre](https://developers.mercadolivre.com.br/pt_br/api-docs-pt-br) | Categorias, produtos e vendedores do Mercado Livre Brasil | Token grátis | ? | 🟠 instável<br><sub>89% · 112 ms · 🔑 testada sem chave</sub> |
| [Open Food Facts Brasil](https://openfoodfacts.github.io/openfoodfacts-server/api/) | Ingredientes, tabela nutricional e Nutri-Score de alimentos pelo código de barras<br><sub>[exemplo](https://br.openfoodfacts.org/api/v2/product/7891000100103.json)</sub> | Não | Sim | 🟢 online<br><sub>100% · 892 ms</sub> |
| [SI5 Global](https://global.si5.com.br/documentacao) | Dados de produto, NCM e CEST a partir do código de barras (GTIN/EAN)<br><sub>limite: 100 consultas/dia no plano gratuito</sub> | Chave grátis | ? | 🟢 online<br><sub>100% · 261 ms · 🔑 testada sem chave</sub> |

**[⬆ voltar ao índice](#índice)**

### Internet, Telefonia e Domínios

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [BrasilAPI DDD](https://brasilapi.com.br/docs) | Estado e cidades atendidos por um DDD<br><sub>[exemplo](https://brasilapi.com.br/api/ddd/v1/11)</sub> | Não | Sim | 🟢 online<br><sub>100% · 55 ms</sub> |
| [BrasilAPI Registro.br](https://brasilapi.com.br/docs) | Situação e disponibilidade de domínios .br<br><sub>[exemplo](https://brasilapi.com.br/api/registrobr/v1/brasilapi.com.br)</sub> | Não | Sim | 🟢 online<br><sub>100% · 810 ms</sub> |
| [GNews](https://gnews.io/docs) | Busca de notícias em português e manchetes do Brasil | Chave grátis | ? | 🟠 instável<br><sub>88% · 357 ms · 🔑 testada sem chave</sub> |
| [NewsAPI](https://newsapi.org/docs) | Manchetes de veículos brasileiros e busca de notícias | Chave grátis | ? | 🟢 online<br><sub>100% · 165 ms · 🔑 testada sem chave</sub> |
| [Registro.br RDAP](https://rdap.registro.br) | Dados públicos de registro de domínios .br no padrão RDAP<br><sub>[exemplo](https://rdap.registro.br/domain/registro.br)</sub> | Não | Sim | 🟢 online<br><sub>100% · 58 ms</sub> |
| [TabNews](https://www.tabnews.com.br/GabrielSozinho/documentacao-da-api-do-tabnews) | Publicações e comentários da comunidade TabNews (leitura sem login)<br><sub>[exemplo](https://www.tabnews.com.br/api/v1/contents?per_page=1)</sub> | Não | Sim | 🟢 online<br><sub>100% · 309 ms</sub> |

**[⬆ voltar ao índice](#índice)**

### Livros, Cultura e Língua

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [A Bíblia Digital](https://github.com/omarciovsena/abibliadigital/blob/master/DOCUMENTATION.md) | Livros, capítulos e versículos da Bíblia em várias versões em português<br><sub>[exemplo](https://www.abibliadigital.com.br/api/books) · limite: 20 req/hora por endpoint sem token</sub> | Opcional | ? | 🔴 fora do ar<br><sub>HTTP 503</sub> |
| [Bible API (Almeida)](https://bible-api.com) | Versículos da Bíblia na tradução de João Ferreira de Almeida<br><sub>[exemplo](https://bible-api.com/john+3:16?translation=almeida)</sub> | Não | Sim | 🟢 online<br><sub>100% · 638 ms</sub> |
| [BrasilAPI ISBN](https://brasilapi.com.br/docs) | Dados de livros por ISBN, consultando várias fontes<br><sub>[exemplo](https://brasilapi.com.br/api/isbn/v1/9788545702870)</sub> | Não | Sim | 🟢 online<br><sub>100% · 534 ms</sub> |
| [Deezer](https://developers.deezer.com/api) | Busca de artistas, álbuns e músicas, incluindo prévias de 30 segundos<br><sub>[exemplo](https://api.deezer.com/search/artist?q=anitta)</sub> | Não | Não | 🟢 online<br><sub>100% · 292 ms</sub> |
| [Dicionário Aberto](https://api.dicionario-aberto.net/index.html) | Dicionário da língua portuguesa com definições e busca por prefixo e sufixo<br><sub>[exemplo](https://api.dicionario-aberto.net/word/casa)</sub> | Não | Sim | 🟢 online<br><sub>100% · 781 ms</sub> |
| [Google Books](https://developers.google.com/books/docs/v1/using) | Busca de livros por título, autor ou ISBN, com capa e descrição<br><sub>[exemplo](https://www.googleapis.com/books/v1/volumes?q=machado+de+assis&maxResults=1)</sub> | Opcional | ? | 🟢 online<br><sub>100% · 1119 ms</sub> |
| [Gutendex](https://gutendex.com) | Livros em domínio público do Projeto Gutenberg, com filtro para português<br><sub>[exemplo](https://gutendex.com/books/?languages=pt)</sub> | Não | Sim | 🔴 fora do ar |
| [Internet Archive](https://archive.org/developers/) | Busca no acervo digital do Internet Archive, com livros, áudios e vídeos em português<br><sub>[exemplo](https://archive.org/advancedsearch.php?q=language%3Apor&fl%5B%5D=identifier&rows=1&output=json)</sub> | Não | Sim | 🟢 online<br><sub>100% · 876 ms</sub> |
| [LanguageTool](https://languagetool.org/http-api/) | Correção ortográfica e gramatical de textos em português do Brasil<br><sub>[exemplo](https://api.languagetool.org/v2/languages) · limite: 20 req/min na API pública</sub> | Não | Sim | 🟢 online<br><sub>100% · 710 ms</sub> |
| [Mapas Culturais (MinC)](https://mapas.cultura.gov.br) | Espaços, agentes, eventos e projetos culturais cadastrados no Ministério da Cultura<br><sub>[exemplo](https://mapas.cultura.gov.br/api/space/find?@select=id,name&@limit=1)</sub> | Não | Não | 🔵 documentação<br><sub>100% · 1845 ms</sub> |
| [MusicBrainz](https://musicbrainz.org/doc/MusicBrainz_API) | Enciclopédia aberta de música com artistas e discografias brasileiras<br><sub>[exemplo](https://musicbrainz.org/ws/2/artist/?query=country:BR&fmt=json&limit=1) · limite: 1 req/s, exige User-Agent</sub> | Não | Sim | 🟠 instável<br><sub>89% · 638 ms</sub> |
| [Open Library](https://openlibrary.org/developers/api) | Catálogo aberto de livros e autores, incluindo literatura brasileira<br><sub>[exemplo](https://openlibrary.org/search.json?q=machado+de+assis&limit=1)</sub> | Não | Sim | 🟢 online<br><sub>100% · 2775 ms</sub> |
| [Radio Browser](https://api.radio-browser.info) | Milhares de rádios brasileiras com link de transmissão<br><sub>[exemplo](https://de1.api.radio-browser.info/json/stations/bycountrycodeexact/BR?limit=1)</sub> | Não | Sim | 🟠 instável<br><sub>89% · 811 ms</sub> |
| [TMDB](https://developer.themoviedb.org/docs) | Filmes e séries com títulos e sinopses em português | Chave grátis | ? | 🟢 online<br><sub>100% · 363 ms · 🔑 testada sem chave</sub> |
| [Vagalume](https://api.vagalume.com.br/docs/) | Letras, traduções, artistas e discografias de músicas | Chave grátis | ? | 🔴 fora do ar<br><sub>HTTP 503</sub> |
| [Wikcionário em Português](https://www.mediawiki.org/wiki/API:Main_page) | Verbetes do dicionário colaborativo da língua portuguesa<br><sub>[exemplo](https://pt.wiktionary.org/w/api.php?action=query&titles=casa&prop=info&format=json)</sub> | Não | Não | 🟢 online<br><sub>100% · 532 ms</sub> |
| [Wikidata](https://www.wikidata.org/wiki/Wikidata:Data_access) | Dados estruturados sobre pessoas, lugares e obras, como o item do Brasil (Q155)<br><sub>[exemplo](https://www.wikidata.org/wiki/Special:EntityData/Q155.json)</sub> | Não | Sim | 🟢 online<br><sub>100% · 976 ms</sub> |
| [Wikimedia Commons](https://www.mediawiki.org/wiki/API:Search) | Imagens e mídias livres sobre o Brasil, com licença e autoria<br><sub>[exemplo](https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch=Brasil&srnamespace=6&format=json&srlimit=1)</sub> | Não | Não | 🟢 online<br><sub>100% · 1615 ms</sub> |
| [Wikimedia Pageviews](https://doc.wikimedia.org/generated-data-platform/aqs/analytics-api/) | Artigos mais lidos e audiência da Wikipédia em português<br><sub>[exemplo](https://wikimedia.org/api/rest_v1/metrics/pageviews/top/pt.wikipedia/all-access/2026/10/01)</sub> | Não | Sim | 🟢 online<br><sub>100% · 458 ms</sub> |
| [Wikipédia em Português (busca)](https://www.mediawiki.org/wiki/API:Search) | Busca de artigos e conteúdo da Wikipédia lusófona pela API MediaWiki<br><sub>[exemplo](https://pt.wikipedia.org/w/api.php?action=query&list=search&srsearch=Brasil&format=json&srlimit=1)</sub> | Não | Não | 🟢 online<br><sub>100% · 433 ms</sub> |
| [Wikivoyage em Português](https://www.mediawiki.org/wiki/API:Main_page) | Guias de viagem colaborativos de cidades e destinos brasileiros<br><sub>[exemplo](https://pt.wikivoyage.org/w/api.php?action=query&list=search&srsearch=Salvador&format=json&srlimit=1)</sub> | Não | Não | 🟢 online<br><sub>100% · 509 ms</sub> |

**[⬆ voltar ao índice](#índice)**

### Ciência e Educação

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [BDTD (IBICT)](https://bdtd.ibict.br/vufind/) | Busca em teses e dissertações das universidades brasileiras<br><sub>[exemplo](https://bdtd.ibict.br/vufind/api/v1/search?lookfor=amazonia&limit=1)</sub> | Não | Sim | 🔴 fora do ar<br><sub>HTTP 400</sub> |
| [Crossref](https://www.crossref.org/documentation/retrieve-metadata/rest-api/) | Metadados de artigos com DOI, incluindo periódicos brasileiros<br><sub>[exemplo](https://api.crossref.org/works?query=brasil&rows=1)</sub> | Não | Sim | 🟢 online<br><sub>100% · 461 ms</sub> |
| [DOAJ](https://doaj.org/api/docs) | Revistas científicas de acesso aberto, com muitos periódicos brasileiros<br><sub>[exemplo](https://doaj.org/api/search/journals/brasil?pageSize=1)</sub> | Não | Sim | 🟢 online<br><sub>100% · 276 ms</sub> |
| [Europe PMC](https://europepmc.org/RestfulWebService) | Artigos de saúde e ciências da vida, incluindo pesquisas brasileiras<br><sub>[exemplo](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=brasil&format=json&pageSize=1)</sub> | Não | Sim | 🟢 online<br><sub>100% · 2072 ms</sub> |
| [Oasisbr (IBICT)](https://oasisbr.ibict.br/vufind/) | Busca na produção científica de acesso aberto do Brasil e de Portugal<br><sub>[exemplo](https://oasisbr.ibict.br/vufind/api/v1/search?lookfor=amazonia&limit=1)</sub> | Não | Sim | 🔴 fora do ar<br><sub>HTTP 503</sub> |
| [OpenAlex](https://docs.openalex.org) | Artigos, autores e instituições de pesquisa brasileiras<br><sub>[exemplo](https://api.openalex.org/institutions?filter=country_code:BR&per-page=1)</sub> | Não | Sim | 🟢 online<br><sub>100% · 1149 ms</sub> |
| [ORCID](https://info.orcid.org/documentation/api-tutorials/) | Identificadores de pesquisadores e suas afiliações, como USP e Unicamp<br><sub>[exemplo](https://pub.orcid.org/v3.0/expanded-search/?q=affiliation-org-name:%22Universidade%20de%20Sao%20Paulo%22&rows=1)</sub> | Não | Sim | 🟢 online<br><sub>100% · 716 ms</sub> |
| [Repositório do Ipea](https://repositorio.ipea.gov.br) | Publicações e estudos do Instituto de Pesquisa Econômica Aplicada<br><sub>[exemplo](https://repositorio.ipea.gov.br/server/api)</sub> | Não | ? | 🛡️ bloqueou o robô<br><sub>HTTP 403</sub> |
| [ROR (Research Organization Registry)](https://ror.readme.io/docs/rest-api) | Cadastro mundial de instituições de pesquisa, incluindo universidades brasileiras<br><sub>[exemplo](https://api.ror.org/v2/organizations?query=universidade%20de%20sao%20paulo)</sub> | Não | Sim | 🟢 online<br><sub>100% · 783 ms</sub> |
| [SciELO ArticleMeta](http://articlemeta.scielo.org) | Metadados de periódicos e artigos científicos da rede SciELO<br><sub>[exemplo](http://articlemeta.scielo.org/api/v1/journal/identifiers/?collection=scl&limit=1)</sub> | Não | Não | 🟢 online<br><sub>100% · 24 ms · 🇧🇷 só do Brasil</sub> |
| [Semantic Scholar](https://api.semanticscholar.org/api-docs/) | Artigos científicos, citações e autores, com busca por tema<br><sub>[exemplo](https://api.semanticscholar.org/graph/v1/paper/search?query=amazonia&limit=1) · limite: Compartilhado entre usuários sem chave</sub> | Não | ? | 🟢 online<br><sub>100% · 567 ms</sub> |

**[⬆ voltar ao índice](#índice)**

### Meio Ambiente

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [ANA Telemetria](https://www.snirh.gov.br/hidroweb/) | Níveis de rios, vazão e chuva das estações telemétricas da Agência Nacional de Águas<br><sub>[exemplo](https://telemetriaws1.ana.gov.br/ServiceANA.asmx)</sub> | Não | Sim | 🔵 documentação<br><sub>83% · 61 ms</sub> |
| [INPE Catálogo de Dados (GeoNetwork)](https://data.inpe.br/geonetwork/) | Catálogo de metadados de dados geoespaciais e de satélite do INPE<br><sub>[exemplo](https://data.inpe.br/geonetwork/srv/api/site)</sub> | Não | ? | 🔴 fora do ar<br><sub>HTTP 502</sub> |
| [MapBiomas Alerta](https://plataforma.alerta.mapbiomas.org/api) | Alertas de desmatamento validados, com laudos e imagens de satélite | Chave grátis | ? | 🔑 requer chave |
| [TerraBrasilis (INPE)](https://terrabrasilis.dpi.inpe.br/about/) | Desmatamento PRODES e alertas DETER via GeoServer (WFS/WMS)<br><sub>[exemplo](https://terrabrasilis.dpi.inpe.br/geoserver/ows?service=WFS&version=2.0.0&request=GetCapabilities)</sub> | Não | Sim | 🟠 instável<br><sub>94% · 164 ms</sub> |

**[⬆ voltar ao índice](#índice)**

### Agropecuária

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [Embrapa AgroAPI](https://www.agroapi.cnptia.embrapa.br/portal/) | APIs da Embrapa de clima agrícola, solos, cultivares, agrotóxicos e satélite | Chave grátis | ? | 🟢 online<br><sub>100% · 148 ms · 🔑 testada sem chave</sub> |
| [NASA POWER](https://power.larc.nasa.gov/docs/services/api/) | Radiação solar, temperatura e chuva diárias por coordenada, muito usadas no agro<br><sub>[exemplo](https://power.larc.nasa.gov/api/temporal/daily/point?parameters=T2M&community=AG&longitude=-47.06&latitude=-22.9&start=20250101&end=20250102&format=JSON)</sub> | Não | Sim | 🟢 online<br><sub>100% · 649 ms</sub> |

**[⬆ voltar ao índice](#índice)**

### Segurança Pública

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [Atlas da Violência (Ipea)](https://www.ipea.gov.br/atlasviolencia/) | Séries de homicídios, violência por gênero e raça e mortes por arma de fogo | Não | ? | 🔑 requer chave |
| [Fogo Cruzado](https://api.fogocruzado.org.br) | Tiroteios registrados nas regiões metropolitanas de Rio, Recife, Salvador e Belém | Chave grátis | ? | 🟢 online<br><sub>100% · 515 ms · 🔑 testada sem chave</sub> |
| [Fórum Brasileiro de Segurança Pública](https://publicacoes.forumseguranca.org.br) | Metadados das publicações do FBSP, como o Anuário de Segurança Pública<br><sub>[exemplo](https://publicacoes.forumseguranca.org.br/server/api)</sub> | Não | ? | 🛡️ bloqueou o robô<br><sub>HTTP 403</sub> |

**[⬆ voltar ao índice](#índice)**

### Esportes e Loterias

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [API-Futebol](https://www.api-futebol.com.br) | Campeonatos, tabelas, rodadas e partidas do futebol brasileiro | Chave grátis | ? | 🟢 online<br><sub>100% · 107 ms · 🔑 testada sem chave</sub> |
| [Cartola FC](https://github.com/giovanigenerali/cartrolandofc/blob/master/nova-api.md) | Status do mercado, atletas, clubes e partidas do fantasy game da Globo (API não oficial)<br><sub>[exemplo](https://api.cartola.globo.com/mercado/status)</sub> | Não | Não | 🟢 online<br><sub>100% · 42 ms</sub> |
| [football-data.org](https://www.football-data.org/documentation/quickstart) | Tabela, jogos e artilharia do Brasileirão Série A no plano gratuito | Chave grátis | ? | 🟢 online<br><sub>100% · 644 ms · 🔑 testada sem chave</sub> |
| [Jolpica F1 (Ergast)](https://github.com/jolpica/jolpica-f1) | Histórico da Fórmula 1, incluindo o circuito de Interlagos<br><sub>[exemplo](https://api.jolpi.ca/ergast/f1/circuits/interlagos.json)</sub> | Não | Sim | 🟢 online<br><sub>100% · 561 ms</sub> |
| [Loterias Caixa API](https://github.com/guto-alves/loterias-api) | Resultados da Mega-Sena, Lotofácil, Quina e demais loterias da Caixa<br><sub>[exemplo](https://loteriascaixa-api.herokuapp.com/api/megasena/latest)</sub> | Não | Sim | 🟢 online<br><sub>100% · 464 ms</sub> |
| [Resultado Mega](https://resultadomega.com.br/api/) | Todos os concursos da Mega-Sena desde 1996, próximo concurso e estatísticas<br><sub>[exemplo](https://resultadomega.com.br/api/ultimo.json)</sub> | Não | Sim | 🟢 online<br><sub>100% · 66 ms</sub> |
| [TheSportsDB](https://www.thesportsdb.com/free_sports_api) | Times, jogadores e partidas do Brasileirão e de outras ligas<br><sub>[exemplo](https://www.thesportsdb.com/api/v1/json/123/lookupleague.php?id=4351)</sub> | Não | Sim | 🟠 instável<br><sub>89% · 327 ms</sub> |

**[⬆ voltar ao índice](#índice)**

### Utilidades

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [Invertexto](https://api.invertexto.com) | Utilidades para devs brasileiros, como CEP, CNPJ, feriados e validação de documentos | Chave grátis | ? | 🟢 online<br><sub>100% · 481 ms · 🔑 testada sem chave</sub> |
| [IP-API](https://ip-api.com/docs) | Localização aproximada por IP, com nomes de cidades e estados em português<br><sub>[exemplo](http://ip-api.com/json/?lang=pt-BR) · limite: 45 req/min, uso não comercial</sub> | Não | Sim | 🟢 online<br><sub>100% · 288 ms</sub> |
| [QR Server](https://goqr.me/api/) | Geração de QR Codes, útil para códigos Pix copia e cola<br><sub>[exemplo](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=apis-publicas-brasil)</sub> | Não | Sim | 🟢 online<br><sub>100% · 850 ms</sub> |
| [Sunrise-Sunset](https://sunrise-sunset.org/api) | Horários de nascer e pôr do sol para qualquer coordenada<br><sub>[exemplo](https://api.sunrise-sunset.org/json?lat=-23.55&lng=-46.63)</sub> | Não | Sim | 🟢 online<br><sub>100% · 166 ms</sub> |
| [TimeAPI.io](https://timeapi.io/swagger/index.html) | Data e hora atuais nos fusos horários do Brasil<br><sub>[exemplo](https://timeapi.io/api/time/current/zone?timeZone=America/Sao_Paulo)</sub> | Não | Sim | 🟢 online<br><sub>100% · 679 ms</sub> |

**[⬆ voltar ao índice](#índice)**

### Portais de Dados Abertos (CKAN)

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [Acre Dados Abertos](https://dados.ac.gov.br) | Dados abertos do Governo do Acre<br><sub>[exemplo](https://dados.ac.gov.br/api/3/action/status_show)</sub> | Não | Não | 🟢 online<br><sub>100% · 1463 ms</sub> |
| [Alagoas Dados Abertos](https://dados.al.gov.br) | Dados abertos do Governo de Alagoas<br><sub>[exemplo](https://dados.al.gov.br/catalogo/api/3/action/status_show)</sub> | Não | ? | 🔴 fora do ar |
| [ANEEL Dados Abertos](https://dadosabertos.aneel.gov.br) | Geração de energia, geração distribuída, tarifas e bandeiras tarifárias<br><sub>[exemplo](https://dadosabertos.aneel.gov.br/api/3/action/status_show)</sub> | Não | Não | 🟢 online<br><sub>100% · 672 ms</sub> |
| [ANTT Dados Abertos](https://dados.antt.gov.br) | Rodovias concedidas, pedágios, ferrovias e transporte de passageiros<br><sub>[exemplo](https://dados.antt.gov.br/api/3/action/status_show)</sub> | Não | Não | 🔴 fora do ar |
| [Bahia Dados Abertos](https://dados.ba.gov.br) | Dados abertos do Governo da Bahia<br><sub>[exemplo](https://dados.ba.gov.br/api/3/action/status_show)</sub> | Não | Não | 🟢 online<br><sub>100% · 256 ms · ⚠️ certificado SSL</sub> |
| [BNDES Dados Abertos](https://dadosabertos.bndes.gov.br) | Operações de financiamento, desembolsos e instituições credenciadas do BNDES<br><sub>[exemplo](https://dadosabertos.bndes.gov.br/api/3/action/status_show)</sub> | Não | Não | 🟢 online<br><sub>100% · 129 ms</sub> |
| [CAPES Dados Abertos](https://dadosabertos.capes.gov.br) | Pós-graduação, bolsas, teses, dissertações e avaliação de programas<br><sub>[exemplo](https://dadosabertos.capes.gov.br/api/3/action/status_show)</sub> | Não | Não | 🔴 fora do ar |
| [CCEE Dados Abertos](https://dadosabertos.ccee.org.br) | Preços, geração, consumo e contratos do mercado de energia elétrica<br><sub>[exemplo](https://dadosabertos.ccee.org.br/api/3/action/status_show)</sub> | Não | Não | 🛡️ bloqueou o robô<br><sub>HTTP 403</sub> |
| [CVM Dados Abertos](https://dados.cvm.gov.br) | Fundos de investimento, companhias abertas e intermediários do mercado de capitais<br><sub>[exemplo](https://dados.cvm.gov.br/api/3/action/status_show)</sub> | Não | Não | 🟢 online<br><sub>100% · 70 ms</sub> |
| [Espírito Santo Dados Abertos](https://dados.es.gov.br) | Dados abertos do Governo do Espírito Santo<br><sub>[exemplo](https://dados.es.gov.br/api/3/action/status_show)</sub> | Não | Não | 🟢 online<br><sub>100% · 154 ms</sub> |
| [FNDE Dados Abertos](https://www.fnde.gov.br/dadosabertos) | Repasses da educação, como merenda escolar, transporte escolar e PDDE<br><sub>[exemplo](https://www.fnde.gov.br/dadosabertos/api/3/action/status_show)</sub> | Não | ? | 🛡️ bloqueou o robô<br><sub>HTTP 403</sub> |
| [Goiás Dados Abertos](https://dadosabertos.go.gov.br) | Dados abertos do Governo de Goiás<br><sub>[exemplo](https://dadosabertos.go.gov.br/api/3/action/status_show)</sub> | Não | ? | 🛡️ bloqueou o robô<br><sub>HTTP 403</sub> |
| [Governo Aberto SP](https://www.governoaberto.sp.gov.br) | Dados abertos do Governo do Estado de São Paulo, com mais de 400 conjuntos<br><sub>[exemplo](https://www.governoaberto.sp.gov.br/api/3/action/status_show)</sub> | Não | Não | 🔴 fora do ar<br><sub>HTTP 502</sub> |
| [IBAMA Dados Abertos](https://dadosabertos.ibama.gov.br) | Autos de infração, licenciamento, Cadastro Técnico Federal e biomas<br><sub>[exemplo](https://dadosabertos.ibama.gov.br/api/3/action/status_show)</sub> | Não | Não | 🟡 lenta<br><sub>100% · 6095 ms</sub> |
| [Minas Gerais Dados Abertos](https://dados.mg.gov.br) | Dados abertos do Governo de Minas Gerais<br><sub>[exemplo](https://dados.mg.gov.br/api/3/action/status_show)</sub> | Não | Não | 🟢 online<br><sub>100% · 59 ms</sub> |
| [ONS Dados Abertos](https://dados.ons.org.br) | Carga, geração e intercâmbio de energia do Sistema Interligado Nacional<br><sub>[exemplo](https://dados.ons.org.br/api/3/action/status_show)</sub> | Não | Não | 🟢 online<br><sub>100% · 350 ms</sub> |
| [Pernambuco Dados Abertos](https://dados.pe.gov.br) | Dados abertos do Governo de Pernambuco<br><sub>[exemplo](https://dados.pe.gov.br/api/3/action/status_show)</sub> | Não | Não | 🟢 online<br><sub>100% · 255 ms</sub> |
| [Prefeitura de Belo Horizonte Dados Abertos](https://dados.pbh.gov.br) | Dados abertos da cidade de Belo Horizonte, incluindo transporte e saúde<br><sub>[exemplo](https://dados.pbh.gov.br/api/3/action/status_show)</sub> | Não | Sim | 🟢 online<br><sub>100% · 172 ms</sub> |
| [Prefeitura de Fortaleza Dados Abertos](https://dados.fortaleza.ce.gov.br) | Dados abertos da cidade de Fortaleza<br><sub>[exemplo](https://dados.fortaleza.ce.gov.br/api/3/action/status_show)</sub> | Não | Não | 🟢 online<br><sub>100% · 286 ms</sub> |
| [Prefeitura de Porto Alegre Dados Abertos](https://dadosabertos.poa.br) | Dados abertos da cidade de Porto Alegre<br><sub>[exemplo](https://dadosabertos.poa.br/api/3/action/status_show)</sub> | Não | Sim | 🟢 online<br><sub>100% · 432 ms</sub> |
| [Prefeitura de São Paulo Dados Abertos](https://dados.prefeitura.sp.gov.br) | Dados abertos da cidade de São Paulo<br><sub>[exemplo](https://dados.prefeitura.sp.gov.br/api/3/action/status_show)</sub> | Não | Sim | 🟠 instável<br><sub>94% · 76 ms</sub> |
| [Prefeitura do Recife Dados Abertos](https://dados.recife.pe.gov.br) | Dados abertos da cidade do Recife<br><sub>[exemplo](https://dados.recife.pe.gov.br/api/3/action/status_show)</sub> | Não | Não | 🟢 online<br><sub>100% · 216 ms · 🇧🇷 só do Brasil</sub> |
| [Rio Grande do Sul Dados Abertos](https://dados.rs.gov.br) | Dados abertos do Governo do Rio Grande do Sul, com mais de 400 conjuntos<br><sub>[exemplo](https://dados.rs.gov.br/api/3/action/status_show)</sub> | Não | Não | 🟢 online<br><sub>100% · 111 ms</sub> |
| [Rondônia Dados Abertos](https://dados.ro.gov.br) | Dados abertos do Governo de Rondônia<br><sub>[exemplo](https://dados.ro.gov.br/api/3/action/status_show)</sub> | Não | Não | 🟢 online<br><sub>100% · 1865 ms</sub> |
| [Santa Catarina Dados Abertos](https://dados.sc.gov.br) | Dados abertos do Governo de Santa Catarina<br><sub>[exemplo](https://dados.sc.gov.br/api/3/action/status_show)</sub> | Não | Não | 🟢 online<br><sub>100% · 61 ms · ⚠️ certificado SSL</sub> |
| [STJ Dados Abertos](https://dadosabertos.web.stj.jus.br) | Decisões, estatísticas e dados administrativos do Superior Tribunal de Justiça<br><sub>[exemplo](https://dadosabertos.web.stj.jus.br/api/3/action/status_show)</sub> | Não | Não | 🟢 online<br><sub>100% · 526 ms</sub> |
| [TCE-RS Dados Abertos](https://dados.tce.rs.gov.br) | Educação, saúde e gestão fiscal dos municípios gaúchos<br><sub>[exemplo](https://dados.tce.rs.gov.br/api/3/action/status_show)</sub> | Não | Não | 🔴 fora do ar |
| [TRE-PR Dados Abertos](https://dadosabertos.tre-pr.jus.br) | Dados eleitorais e administrativos do Tribunal Regional Eleitoral do Paraná<br><sub>[exemplo](https://dadosabertos.tre-pr.jus.br/api/3/action/status_show)</sub> | Não | Não | 🛡️ bloqueou o robô<br><sub>HTTP 200</sub> |
| [TSE Dados Abertos](https://dadosabertos.tse.jus.br) | Resultados eleitorais, candidatos, eleitorado e prestação de contas<br><sub>[exemplo](https://dadosabertos.tse.jus.br/api/3/action/status_show)</sub> | Não | Não | 🟢 online<br><sub>100% · 74 ms</sub> |

**[⬆ voltar ao índice](#índice)**

### Internacionais com Dados do Brasil

| API | Descrição | Autenticação | CORS | Status |
|---|---|:---:|:---:|:---:|
| [Alpha Vantage](https://www.alphavantage.co/documentation/) | Cotações e histórico de ações, incluindo papéis da B3 (sufixo .SA) | Chave grátis | Sim | 🟢 online<br><sub>100% · 122 ms · 🔑 testada sem chave</sub> |
| [Banco Mundial](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392) | Indicadores econômicos e sociais do Brasil, como PIB, pobreza e educação<br><sub>[exemplo](https://api.worldbank.org/v2/country/BR/indicator/NY.GDP.MKTP.CD?format=json&per_page=1)</sub> | Não | Sim | 🟢 online<br><sub>100% · 374 ms</sub> |
| [Banco Mundial Projetos](https://projects.worldbank.org/en/projects-operations/projects-home) | Projetos financiados pelo Banco Mundial no Brasil<br><sub>[exemplo](https://search.worldbank.org/api/v2/projects?format=json&countrycode_exact=BR&rows=1)</sub> | Não | Não | 🟢 online<br><sub>100% · 337 ms</sub> |
| [CoinGecko](https://www.coingecko.com/pt/api/documentation) | Cotação de criptomoedas em reais e outras moedas<br><sub>[exemplo](https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=brl)</sub> | Opcional | Sim | 🟢 online<br><sub>100% · 193 ms</sub> |
| [CoinPaprika](https://api.coinpaprika.com) | Cotações de criptomoedas convertidas para reais<br><sub>[exemplo](https://api.coinpaprika.com/v1/tickers/btc-bitcoin?quotes=BRL)</sub> | Não | Sim | 🟢 online<br><sub>100% · 245 ms</sub> |
| [Currency API (fawazahmed0)](https://github.com/fawazahmed0/exchange-api) | Câmbio diário do real para moedas e criptomoedas, servido por CDN<br><sub>[exemplo](https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/brl.json)</sub> | Não | Sim | 🟢 online<br><sub>100% · 112 ms</sub> |
| [ExchangeRate-API (aberta)](https://www.exchangerate-api.com/docs/free) | Câmbio diário do real para mais de 150 moedas, sem chave<br><sub>[exemplo](https://open.er-api.com/v6/latest/BRL)</sub> | Não | Sim | 🟢 online<br><sub>100% · 150 ms</sub> |
| [FMI DataMapper](https://www.imf.org/external/datamapper/api/help) | Indicadores e projeções do FMI para o Brasil, como PIB, inflação e dívida<br><sub>[exemplo](https://www.imf.org/external/datamapper/api/v1/NGDP_RPCH/BRA)</sub> | Não | Não | 🟢 online<br><sub>100% · 531 ms</sub> |
| [Frankfurter](https://frankfurter.dev) | Câmbio do real e de outras moedas com base nas taxas do Banco Central Europeu<br><sub>[exemplo](https://api.frankfurter.app/latest?from=BRL)</sub> | Não | Sim | 🟢 online<br><sub>100% · 765 ms</sub> |
| [GBIF](https://techdocs.gbif.org/en/openapi/) | Registros de ocorrência de espécies no Brasil<br><sub>[exemplo](https://api.gbif.org/v1/occurrence/search?country=BR&limit=1)</sub> | Não | Sim | 🟢 online<br><sub>100% · 626 ms</sub> |
| [GeoNames](https://www.geonames.org/export/web-services.html) | Base geográfica com cidades, bairros e pontos de interesse do Brasil | Chave grátis | Sim | 🟢 online<br><sub>100% · 412 ms · 🔑 testada sem chave</sub> |
| [iNaturalist](https://api.inaturalist.org/v1/docs/) | Observações de fauna e flora feitas por cidadãos no Brasil<br><sub>[exemplo](https://api.inaturalist.org/v1/places/autocomplete?q=Brasil)</sub> | Não | Sim | 🟢 online<br><sub>100% · 1222 ms</sub> |
| [NASA EONET](https://eonet.gsfc.nasa.gov/docs/v3) | Eventos naturais em andamento, como queimadas e enchentes, com coordenadas<br><sub>[exemplo](https://eonet.gsfc.nasa.gov/api/v3/events?limit=1)</sub> | Não | Sim | 🟡 lenta<br><sub>100% · 6635 ms</sub> |
| [NASA FIRMS](https://firms.modaps.eosdis.nasa.gov/api/) | Focos de incêndio detectados por satélite em tempo quase real | Chave grátis | ? | 🔑 requer chave |
| [Nominatim (OpenStreetMap)](https://nominatim.org/release-docs/latest/api/Search/) | Geocodificação de endereços brasileiros e busca reversa por coordenadas<br><sub>[exemplo](https://nominatim.openstreetmap.org/search?q=Avenida%20Paulista&countrycodes=br&format=json&limit=1) · limite: 1 req/s, exige User-Agent</sub> | Não | Sim | 🟢 online<br><sub>100% · 301 ms</sub> |
| [ONU Objetivos de Desenvolvimento Sustentável](https://unstats.un.org/sdgapi/swagger/) | Metas e indicadores dos ODS da ONU, com séries do Brasil<br><sub>[exemplo](https://unstats.un.org/sdgapi/v1/sdg/Goal/List)</sub> | Não | Sim | 🟢 online<br><sub>100% · 981 ms</sub> |
| [Open Topo Data](https://www.opentopodata.org) | Altitude por coordenada a partir de modelos de relevo como o SRTM<br><sub>[exemplo](https://api.opentopodata.org/v1/srtm90m?locations=-22.95,-43.21) · limite: 1 req/s e 1.000 por dia</sub> | Não | Não | 🟢 online<br><sub>100% · 269 ms</sub> |
| [Open-Meteo](https://open-meteo.com/en/docs) | Previsão do tempo e histórico climático para qualquer coordenada do Brasil<br><sub>[exemplo](https://api.open-meteo.com/v1/forecast?latitude=-23.55&longitude=-46.63&current_weather=true)</sub> | Não | Sim | 🟢 online<br><sub>100% · 829 ms</sub> |
| [Open-Meteo Cheias](https://open-meteo.com/en/docs/flood-api) | Previsão de vazão de rios, incluindo a bacia amazônica<br><sub>[exemplo](https://flood-api.open-meteo.com/v1/flood?latitude=-3.1&longitude=-60.0&daily=river_discharge)</sub> | Não | Sim | 🟢 online<br><sub>100% · 892 ms</sub> |
| [Open-Meteo Clima Futuro](https://open-meteo.com/en/docs/climate-api) | Projeções climáticas até 2050 para qualquer coordenada<br><sub>[exemplo](https://climate-api.open-meteo.com/v1/climate?latitude=-23.55&longitude=-46.63&start_date=2050-01-01&end_date=2050-01-02&models=MRI_AGCM3_2_S&daily=temperature_2m_max)</sub> | Não | Sim | 🟢 online<br><sub>100% · 838 ms</sub> |
| [Open-Meteo Elevation](https://open-meteo.com/en/docs/elevation-api) | Altitude de qualquer coordenada do Brasil<br><sub>[exemplo](https://api.open-meteo.com/v1/elevation?latitude=-22.95&longitude=-43.21)</sub> | Não | Sim | 🟢 online<br><sub>100% · 178 ms</sub> |
| [Open-Meteo Ensemble](https://open-meteo.com/en/docs/ensemble-api) | Previsões por conjunto de modelos, com a incerteza da previsão<br><sub>[exemplo](https://ensemble-api.open-meteo.com/v1/ensemble?latitude=-23.55&longitude=-46.63&hourly=temperature_2m&models=icon_seamless)</sub> | Não | Sim | 🟢 online<br><sub>100% · 1027 ms</sub> |
| [Open-Meteo Geocoding](https://open-meteo.com/en/docs/geocoding-api) | Busca de cidades com coordenadas, população e fuso horário<br><sub>[exemplo](https://geocoding-api.open-meteo.com/v1/search?name=Campinas&language=pt&count=1)</sub> | Não | Sim | 🟢 online<br><sub>100% · 506 ms</sub> |
| [Open-Meteo Histórico](https://open-meteo.com/en/docs/historical-weather-api) | Clima histórico diário e horário desde 1940 para qualquer coordenada<br><sub>[exemplo](https://archive-api.open-meteo.com/v1/archive?latitude=-23.55&longitude=-46.63&start_date=2025-01-01&end_date=2025-01-02&daily=temperature_2m_max)</sub> | Não | Sim | 🟢 online<br><sub>100% · 828 ms</sub> |
| [Open-Meteo Marine](https://open-meteo.com/en/docs/marine-weather-api) | Altura, direção e período das ondas no litoral brasileiro<br><sub>[exemplo](https://marine-api.open-meteo.com/v1/marine?latitude=-22.97&longitude=-43.18&current=wave_height)</sub> | Não | Sim | 🟢 online<br><sub>100% · 889 ms</sub> |
| [Open-Meteo Qualidade do Ar](https://open-meteo.com/en/docs/air-quality-api) | Poluentes e índice de qualidade do ar para qualquer coordenada<br><sub>[exemplo](https://air-quality-api.open-meteo.com/v1/air-quality?latitude=-23.55&longitude=-46.63&current=pm10)</sub> | Não | Sim | 🟢 online<br><sub>100% · 897 ms</sub> |
| [OpenAQ](https://docs.openaq.org) | Medições de qualidade do ar de estações no Brasil e no mundo | Chave grátis | ? | 🟢 online<br><sub>100% · 70 ms · 🔑 testada sem chave</sub> |
| [OpenWeatherMap](https://openweathermap.org/api) | Clima atual e previsão para qualquer cidade do Brasil | Chave grátis | ? | 🟢 online<br><sub>100% · 357 ms · 🔑 testada sem chave</sub> |
| [Overpass API](https://wiki.openstreetmap.org/wiki/Overpass_API) | Consultas avançadas a pontos e vias do OpenStreetMap, como escolas ou ciclovias de uma cidade<br><sub>[exemplo](https://overpass-api.de/api/status)</sub> | Não | Sim | 🟡 lenta<br><sub>33% · 29276 ms</sub> |
| [Photon (Komoot)](https://photon.komoot.io) | Geocodificação com autocompletar sobre dados do OpenStreetMap<br><sub>[exemplo](https://photon.komoot.io/api/?q=Copacabana&limit=1)</sub> | Não | Sim | 🟢 online<br><sub>100% · 673 ms</sub> |
| [REST Countries](https://restcountries.com) | Dados gerais de países, como população, moeda, idiomas e fronteiras<br><sub>[exemplo](https://restcountries.com/v3.1/alpha/br)</sub> | Não | Não | 🟢 online<br><sub>100% · 467 ms</sub> |
| [USGS Terremotos](https://earthquake.usgs.gov/fdsnws/event/1/) | Abalos sísmicos registrados no Brasil e na América do Sul<br><sub>[exemplo](https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&minlatitude=-34&maxlatitude=6&minlongitude=-74&maxlongitude=-34&limit=1)</sub> | Não | Sim | 🟢 online<br><sub>100% · 465 ms</sub> |
| [Wikidata SPARQL](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service) | Consultas avançadas ao Wikidata, como capitais, municípios e personalidades brasileiras<br><sub>[exemplo](https://query.wikidata.org/sparql?query=SELECT%20%3Fx%20WHERE%20%7B%20wd%3AQ155%20wdt%3AP36%20%3Fx%20%7D&format=json)</sub> | Não | Sim | 🟢 online<br><sub>100% · 923 ms</sub> |
| [Wikipédia em Português](https://pt.wikipedia.org/api/rest_v1/) | Resumos, conteúdo e mídias de artigos da Wikipédia lusófona<br><sub>[exemplo](https://pt.wikipedia.org/api/rest_v1/page/summary/Brasil)</sub> | Não | Sim | 🟢 online<br><sub>100% · 39 ms</sub> |

**[⬆ voltar ao índice](#índice)**

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
