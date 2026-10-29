# Verificador em São Paulo (AWS Lambda)

Algumas APIs do governo (IBGE, Prefeitura do Recife...) bloqueiam acessos vindos de fora do Brasil. Como os robôs do GitHub rodam nos EUA, essas APIs são testadas por uma função na AWS, na região de São Paulo.

```
GitHub Actions (EUA) ──► função na AWS (São Paulo) ──► APIs 🇧🇷
                    ◄── resultados ◄──
```

As APIs com `acesso: brasil` no `data/apis.yaml` passam por esse caminho. Sem a AWS configurada, elas aparecem no README como **🇧🇷 só do Brasil**, sem teste. O resto do robô funciona normalmente.

**Custo:** o plano gratuito permanente da AWS Lambda inclui 1 milhão de execuções e 400 mil GB-segundos por mês. O robô usa cerca de 30 execuções e algumas centenas de GB-segundos por mês, bem dentro do gratuito.

---

## 1. Criar a conta e um alerta de gastos

1. Crie uma conta em [aws.amazon.com](https://aws.amazon.com). A AWS pede um cartão de crédito no cadastro.
2. Por segurança, crie um alerta que avisa se qualquer gasto aparecer:
   1. Na barra de busca do console, procure **Budgets** e abra.
   2. Clique em **Create budget**.
   3. Escolha o modelo **Zero spend budget**, coloque seu e-mail e clique em **Create budget**.

## 2. Criar a função

1. No canto superior direito do console, troque a região para **América do Sul (São Paulo) sa-east-1**. **Esse passo é essencial:** a função precisa rodar no Brasil.
2. Na busca, procure **Lambda** e clique em **Create function**.
3. Preencha:
   - **Author from scratch**
   - **Function name:** `verificador-apis-brasil` (exatamente esse nome)
   - **Runtime:** Python 3.12 ou a versão de Python mais recente da lista
4. Clique em **Create function**.
5. Na aba **Code**, abra o arquivo `lambda_function.py`, apague todo o conteúdo e cole o conteúdo inteiro do arquivo [`scripts/verificacao.py`](../scripts/verificacao.py) deste repositório.
6. Clique em **Deploy**.
7. Vá em **Configuration → General configuration → Edit** e ajuste:
   - **Memory:** `256` MB
   - **Timeout:** `5` min `0` sec
8. Clique em **Save**.

### Testar a função

1. Na aba **Test**, em **Event JSON**, cole:
   ```json
   {"apis": {"IBGE Localidades": "https://servicodados.ibge.gov.br/api/v1/localidades/estados"}}
   ```
2. Clique em **Test**.

O resultado deve mostrar `"ok": true`. Se mostrar erro, o IBGE também está bloqueando os servidores da AWS. Nesse caso, abra uma issue com o erro.

## 3. Criar um usuário que só pode chamar essa função

O GitHub precisa de uma credencial para chamar a função. Ela vai ter permissão para **uma única coisa**: executar essa função.

1. Na busca, procure **IAM**. Vá em **Users → Create user**.
2. Em **User name**, coloque `github-verificador-apis`. Não marque o acesso ao console. Clique em **Next**, depois em **Next** de novo e em **Create user**.
3. Abra o usuário criado. Na aba **Permissions**, clique em **Add permissions → Create inline policy**.
4. Escolha a aba **JSON**, apague o conteúdo e cole:
   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": "lambda:InvokeFunction",
         "Resource": "arn:aws:lambda:sa-east-1:*:function:verificador-apis-brasil"
       }
     ]
   }
   ```
5. Clique em **Next**. Em **Policy name**, coloque `invocar-verificador-apis` e clique em **Create policy**.
6. Ainda no usuário, abra a aba **Security credentials** e clique em **Create access key**.
7. Escolha **Application running outside AWS**, clique em **Next** e depois em **Create access key**.
8. **Copie a Access key e a Secret access key agora.** A secret só aparece uma vez.

## 4. Guardar as chaves no GitHub

1. No repositório, vá em **Settings → Secrets and variables → Actions → New repository secret**.
2. Crie dois segredos:

| Name | Secret |
|---|---|
| `AWS_ACCESS_KEY_ID` | a Access key copiada |
| `AWS_SECRET_ACCESS_KEY` | a Secret access key copiada |

Os segredos ficam criptografados e nunca aparecem no código, nos logs nem para quem abre pull requests.

## 5. Rodar

Vá em **Actions → Verificar APIs → Run workflow**. No log do passo **Testar as APIs**, as APIs testadas pela AWS aparecem com `[testada do Brasil]`.

## Manutenção

- **Se o arquivo `scripts/verificacao.py` mudar no repositório,** cole a versão nova na função da AWS e clique em **Deploy**.
- **Para nunca mais usar a AWS,** apague os dois segredos do GitHub. As APIs 🇧🇷 voltam a ficar sem teste.
