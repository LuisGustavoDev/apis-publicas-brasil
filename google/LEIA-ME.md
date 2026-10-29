# Verificador em São Paulo (Google Cloud)

Algumas APIs do governo (IBGE, Prefeitura do Recife...) bloqueiam acessos vindos de fora do Brasil. Como os robôs do GitHub rodam nos EUA, essas APIs são testadas por uma função no Google Cloud, na região de São Paulo.

```
GitHub Actions (EUA) ──► função no Google Cloud (São Paulo) ──► APIs 🇧🇷
                    ◄── resultados ◄──
```

As APIs com `acesso: brasil` no `data/apis.yaml` passam por esse caminho. Sem a função configurada, elas aparecem no README como **🇧🇷 só do Brasil**, sem teste. O resto do robô funciona normalmente.

**Custo:** o nível gratuito permanente do Cloud Run inclui 2 milhões de requisições e 180 mil vCPU-segundos por mês. O robô faz cerca de 30 chamadas por mês, de poucos segundos cada. Contas novas também ganham um período de teste com créditos, durante o qual nada é cobrado sem você ativar a conta paga.

**Segurança:** a função tem um endereço público, mas só trabalha para quem envia a senha certa (o "token"). Sem a senha, ela responde "não autorizado" e não faz nada.

---

## 1. Criar a conta

1. Acesse [cloud.google.com/free](https://cloud.google.com/free) e clique em **Comece a usar gratuitamente**.
2. Entre com sua conta Google, preencha os dados e o cartão de crédito.
3. Ao final, você cai no **console do Google Cloud**, com um projeto já criado (geralmente chamado "My First Project").

## 2. Criar um alerta de gastos

1. Na busca do topo, digite **Faturamento** (Billing) e abra.
2. No menu da esquerda, clique em **Orçamentos e alertas** (Budgets & alerts) → **Criar orçamento**.
3. Dê o nome `alerta`, avance, coloque o valor **R$ 5** e mantenha os alertas sugeridos (50%, 90%, 100%).
4. Clique em **Concluir**. Você recebe e-mail se os gastos se aproximarem desse valor.

## 3. Criar a senha (token)

No PowerShell do seu computador, rode:

```powershell
[guid]::NewGuid().ToString("N") + [guid]::NewGuid().ToString("N")
```

Ele mostra um texto aleatório de 64 letras e números. **Guarde esse texto**: ele é a senha que o GitHub vai usar para chamar a função.

## 4. Criar a função

1. Na busca do topo do console, digite **Cloud Run** e abra.
2. Se pedir para ativar APIs, clique em **Ativar** (Enable) e aguarde.
3. Clique em **Escrever uma função** (Write a function).
4. Preencha:
   - **Nome do serviço:** `verificador-apis-brasil`
   - **Região:** `southamerica-east1 (São Paulo)` ← **essencial**
   - **Ambiente de execução (Runtime):** Python 3.12 ou o Python mais novo da lista
   - **Autenticação:** **Permitir acesso público** (Allow public access)
5. Abra a seção **Contêineres, volumes, rede, segurança** (Containers, Volumes, Networking, Security), mais abaixo:
   - Em **Variáveis e secrets** (Variables & Secrets), clique em **Adicionar variável**: nome `TOKEN_VERIFICADOR`, valor = a senha criada no passo 3.
   - Se aparecer **Número máximo de instâncias** (Maximum number of instances), coloque `1`.
6. Clique em **Criar** (Create) e aguarde. A tela muda para a aba **Origem** (Source), com o código da função.

## 5. Colocar o código

1. Na aba **Origem**, clique em **Editar origem** (Edit source), se aparecer.
2. No campo **Ponto de entrada da função** (Function entry point), apague o que estiver lá e escreva: `verificar_http`
3. Na lista de arquivos, clique em **main.py**, apague todo o conteúdo e cole o conteúdo inteiro do arquivo [`scripts/verificacao.py`](../scripts/verificacao.py) deste repositório.
4. **Não mexa** no arquivo `requirements.txt`.
5. Clique em **Salvar e reimplantar** (Save and redeploy) e aguarde alguns minutos.
6. Quando terminar, copie o endereço que aparece ao lado de **URL**, no topo da página. Ele termina em `.run.app`.

## 6. Testar (passo decisivo)

No PowerShell, troque os dois valores entre aspas e rode:

```powershell
$url = "COLE_A_URL_DA_FUNCAO"
$token = "COLE_A_SENHA_DO_PASSO_3"
Invoke-RestMethod -Method Post -Uri $url -Headers @{Authorization = "Bearer $token"} -ContentType "application/json" -Body '{"apis": {"IBGE Localidades": "https://servicodados.ibge.gov.br/api/v1/localidades/estados"}}' | ConvertTo-Json -Depth 5
```

Se aparecer `"ok": true`, funcionou: o IBGE aceita a função em São Paulo. Se aparecer `"ok": false`, o IBGE também bloqueia servidores de nuvem e não vale a pena continuar.

## 7. Guardar a URL e a senha no GitHub

No repositório, vá em **Settings → Secrets and variables → Actions → New repository secret** e crie dois segredos:

| Name | Secret |
|---|---|
| `GCP_VERIFICADOR_URL` | a URL da função (passo 5) |
| `GCP_VERIFICADOR_TOKEN` | a senha (passo 3) |

Depois, vá em **Actions → Verificar APIs → Run workflow**. No log do passo **Testar as APIs**, as APIs do IBGE e do Recife devem aparecer com `[testada do Brasil]`.

## Manutenção

- **Se o arquivo `scripts/verificacao.py` mudar no repositório,** abra a função no Cloud Run, cole a versão nova no `main.py` e clique em **Salvar e reimplantar**.
- **Para trocar a senha,** gere uma nova (passo 3), atualize a variável `TOKEN_VERIFICADOR` da função (**Editar e implantar nova revisão**) e o segredo `GCP_VERIFICADOR_TOKEN` no GitHub.
- **Para desligar,** apague os dois segredos do GitHub e exclua o serviço no Cloud Run. As APIs 🇧🇷 voltam a ficar sem teste.
