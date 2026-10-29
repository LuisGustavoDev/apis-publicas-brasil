# Verificador em São Paulo (Vercel) — recomendado

Algumas APIs do governo (IBGE, Prefeitura do Recife...) bloqueiam acessos vindos de fora do Brasil. Como os robôs do GitHub rodam nos EUA, essas APIs são testadas por uma função na **Vercel**, rodando em **São Paulo** (região `gru1`).

```
GitHub Actions (EUA) ──► função na Vercel (São Paulo) ──► APIs 🇧🇷
                    ◄── resultados ◄──
```

- O código da função está neste repositório, em [`api/verificar.py`](../api/verificar.py), e usa a mesma lógica do robô ([`scripts/verificacao.py`](../scripts/verificacao.py)).
- A região de São Paulo já está definida no [`vercel.json`](../vercel.json).
- A cada `git push` que mude a função, a Vercel atualiza tudo sozinha. Os commits diários do robô não geram novas publicações.

**Custo:** o plano gratuito (Hobby) não pede cartão e inclui 1 milhão de chamadas por mês. O robô faz cerca de 30. Sem cartão cadastrado, não existe cobrança possível.

**Segurança:** a função tem um endereço público, mas só trabalha para quem envia a senha certa. Sem ela, responde "não autorizado".

---

## 1. Criar a senha

No PowerShell do seu computador, rode:

```powershell
[guid]::NewGuid().ToString("N") + [guid]::NewGuid().ToString("N")
```

Copie o texto que aparecer (64 letras e números) e guarde. Essa é a senha.

## 2. Criar a conta na Vercel

1. Acesse [vercel.com/signup](https://vercel.com/signup).
2. Escolha **Hobby** (uso pessoal, gratuito).
3. Clique em **Continue with GitHub** e autorize com a sua conta do GitHub.

## 3. Importar o repositório

1. No painel da Vercel, clique em **Add New… → Project**.
2. Na lista **Import Git Repository**, encontre `apis-publicas-brasil` e clique em **Import**.
   - Se ele não aparecer, clique em **Adjust GitHub App Permissions** (ou **Configure GitHub App**) e dê acesso a esse repositório.
3. Na tela de configuração:
   - **Framework Preset:** `Other`
   - Não mexa em **Root Directory** nem em **Build and Output Settings**.
   - Abra **Environment Variables** e adicione:
     - **Key:** `TOKEN_VERIFICADOR`
     - **Value:** a senha do passo 1
4. Clique em **Deploy** e aguarde até aparecer a tela de parabéns.

## 4. Descobrir o endereço da função

1. Clique em **Continue to Dashboard** (ou abra o projeto no painel).
2. Em **Domains**, copie o endereço curto do projeto, por exemplo `apis-publicas-brasil.vercel.app`. Use esse endereço curto, e não o endereço longo com letras aleatórias, que pode exigir login.
3. O endereço da função é esse domínio seguido de `/api/verificar`, por exemplo:
   ```
   https://apis-publicas-brasil.vercel.app/api/verificar
   ```
4. Abra esse endereço no navegador. Deve aparecer `{"status": "no ar", ...}`.

**Confira a região:** em **Settings → Functions**, a **Function Region** deve mostrar **São Paulo, Brazil (gru1)**. Se mostrar outra, troque para São Paulo, salve e faça um novo deploy (**Deployments → ⋯ → Redeploy**).

## 5. Testar (passo decisivo)

No PowerShell, troque os dois valores entre aspas e rode:

```powershell
$url = "https://SEU-PROJETO.vercel.app/api/verificar"
$token = "COLE_A_SENHA_DO_PASSO_1"
Invoke-RestMethod -Method Post -Uri $url -Headers @{Authorization = "Bearer $token"} -ContentType "application/json" -Body '{"apis": {"IBGE Localidades": "https://servicodados.ibge.gov.br/api/v1/localidades/estados"}}' | ConvertTo-Json -Depth 5
```

Se aparecer `"ok": true`, funcionou: o IBGE aceita a função em São Paulo. Se aparecer `"ok": false`, o IBGE também bloqueia servidores de nuvem e não vale a pena continuar.

## 6. Guardar o endereço e a senha no GitHub

No repositório, vá em **Settings → Secrets and variables → Actions → New repository secret** e crie dois segredos:

| Name | Secret |
|---|---|
| `VERIFICADOR_BR_URL` | o endereço da função (passo 4) |
| `VERIFICADOR_BR_TOKEN` | a senha (passo 1) |

Depois, vá em **Actions → Verificar APIs → Run workflow**. No log do passo **Testar as APIs**, as APIs do IBGE e do Recife devem aparecer com `[testada do Brasil]`.

## Manutenção

- **Atualizações:** nada a fazer. Quando `api/`, `scripts/verificacao.py` ou `vercel.json` mudarem no GitHub, a Vercel publica a nova versão sozinha.
- **Trocar a senha:** gere uma nova (passo 1), atualize `TOKEN_VERIFICADOR` em **Settings → Environment Variables** na Vercel, faça um **Redeploy** e atualize o segredo `VERIFICADOR_BR_TOKEN` no GitHub.
- **Desligar:** apague os dois segredos do GitHub e exclua o projeto na Vercel (**Settings → Advanced → Delete Project**). As APIs 🇧🇷 voltam a ficar sem teste.
