# PDV — Ponto de Venda em Python

Um programa simples de terminal que funciona como o caixa de uma loja: você informa os produtos e os preços, e no final ele aplica um desconto progressivo, imprime o cupom e pergunta a forma de pagamento. Se o pagamento for em dinheiro, ele calcula o troco.

## Como executar

É preciso ter o Python 3 instalado. No terminal, dentro da pasta do projeto:

```bash
python pdv.py
```

## Exemplo de uso

```
Qual o nome do produto ? arroz
Qual o preço ? abc
Erro: Digite um número.
Qual o preço ? 50
Deseja adicionar mais itens?(s/n): s
Qual o nome do produto ? feijao
Qual o preço ? 70
Deseja adicionar mais itens?(s/n): n
O valor sem o desconto é R$ 120.00

========== CUPOM ==========
arroz  R$ 50.00
feijao  R$ 70.00
---------------------------
Subtotal:  R$ 120.00
Desconto:  R$ 12.00
Total:     R$ 108.00
===========================
Qual a forma de pagamento? (dinheiro/cartao): dinheiro
Quanto o cliente pagou? 100
Erro: o valor é menor que o total.
Quanto o cliente pagou? 150
Troco: R$ 42.00
```

> Use ponto como separador decimal (`10.5`), não vírgula (`10,5`). Com vírgula, o Python não consegue converter o texto em número e o programa pede o preço de novo.

## Variáveis

| Variável | Tipo | O que guarda |
|---|---|---|
| `itens` | lista (`list`) | Todos os produtos adicionados na compra. Começa vazia (`[]`). |
| `continuar` | texto (`str`) | A resposta do usuário à pergunta "Deseja adicionar mais itens?". Começa com `"s"` para o laço rodar pelo menos uma vez. |
| `subtotal` | número (`float`) | A soma dos preços de todos os produtos. Começa em `0`. |
| `nome_do_produto` | texto (`str`) | O nome que o usuário digitou para o produto atual. |
| `preco_do_produto` | número (`float`) | O preço do produto atual, já convertido para número. |
| `preco_digitado_pelo_usuario` | texto (`str`) | O preço exatamente como foi digitado, antes de virar número. |
| `produto` | dicionário (`dict`) | Um produto com dois campos: `"nome_do_produto"` e `"preco_do_produto"`. |
| `desconto` | número (`float`) | O valor do desconto, calculado a partir do subtotal. |
| `total` | número (`float`) | O valor a pagar: subtotal menos desconto. |
| `forma_de_pagamento` | texto (`str`) | A forma de pagamento digitada: `"dinheiro"` ou `"cartao"`. |
| `valor_digitado_pelo_usuario` | texto (`str`) | O valor pago exatamente como foi digitado, antes de virar número. |
| `valor_pago` | número (`float`) | Quanto o cliente entregou em dinheiro. |
| `troco` | número (`float`) | O que o caixa devolve: valor pago menos total. |

## Como o código funciona, passo a passo

### 1. Preparação

```python
itens = []
continuar = "s"
subtotal = 0
```

Cria a lista vazia de produtos, define `continuar` como `"s"` para entrar no laço logo de início e zera o subtotal.

### 2. Laço principal: cadastrar produtos

```python
while continuar == "s":
```

Enquanto o usuário responder `"s"`, o programa continua pedindo produtos.

### 3. Ler o nome

```python
nome_do_produto = input("Qual o nome do produto ? ")
```

`input()` mostra a pergunta e devolve, como texto, o que o usuário digitou.

### 4. Ler e validar o preço

```python
preco_do_produto = 0
while preco_do_produto <= 0:
    preco_digitado_pelo_usuario = input("Qual o preço ? ")
    try:
        preco_do_produto = float(preco_digitado_pelo_usuario)
    except ValueError:
        print("Erro: Digite um número.")
        preco_do_produto = 0
```

- O preço começa em `0` para forçar a entrada no laço de validação.
- O laço se repete enquanto o preço for zero ou negativo.
- `float()` tenta transformar o texto em número decimal.
- Se o texto não for um número (ex.: `"abc"`), o Python gera um `ValueError`. O bloco `try/except` captura esse erro, mostra uma mensagem e pede o preço de novo, sem o programa travar.

### 5. Guardar o produto

```python
produto = {"nome_do_produto": nome_do_produto, "preco_do_produto": preco_do_produto}
itens.append(produto)
```

Monta um dicionário com o nome e o preço e o adiciona ao final da lista `itens` com `append()`.

### 6. Perguntar se quer continuar

```python
continuar = input("Deseja adicionar mais itens?(s/n): ").strip().lower()
```

- `.strip()` remove espaços extras antes e depois da resposta.
- `.lower()` deixa tudo em minúsculas, então `"S"` também vale como `"s"`.

Qualquer resposta diferente de `"s"` encerra o laço.

### 7. Calcular o subtotal

```python
for produto in itens:
    subtotal = subtotal + produto["preco_do_produto"]
```

Percorre cada produto da lista e soma o seu preço ao `subtotal`.

### 8. Mostrar o subtotal

```python
print(f"O valor sem o desconto é R$ {subtotal:.2f}")
```

A f-string (o `f` antes das aspas) coloca o valor de `subtotal` dentro do texto, no lugar de `{subtotal}`. O `:.2f` mostra o número com 2 casas decimais (`120.00` em vez de `120.0`).

### 9. Calcular o desconto progressivo

```python
if subtotal > 200:
    desconto = subtotal * 0.15
elif subtotal > 100:
    desconto = subtotal * 0.10
elif subtotal > 50:
    desconto = subtotal * 0.05
else:
    desconto = 0

total = subtotal - desconto
```

O desconto depende do valor da compra:

| Subtotal | Desconto |
|---|---|
| até R$ 50,00 | sem desconto |
| acima de R$ 50,00 | 5% |
| acima de R$ 100,00 | 10% |
| acima de R$ 200,00 | 15% |

- O `if` testa do **maior** valor para o **menor**. A ordem importa: uma compra de R$ 250 também é maior que 100 e maior que 50. Se o teste de 50 viesse primeiro, ela ganharia só 5%.
- O `elif` ("senão, se") só é testado quando as condições de cima deram falso. Assim, só um dos blocos roda.
- O sinal é `>` (maior que), não `>=`. Uma compra de exatamente R$ 100,00 fica na faixa de 5%, e uma de R$ 100,01 já ganha 10%.
- No fim, o total é o subtotal menos o desconto.

> **Atenção:** com o desconto progressivo, o teste "Exatamente 100" da tarefa 9 dá desconto de R$ 5,00, e não R$ 0,00. A tabela da tarefa 9 usa a regra antiga (10% só acima de R$ 100).

### 10. Imprimir o cupom

```python
print("========== CUPOM ==========")
for produto in itens:
    print(f"{produto['nome_do_produto']}  R$ {produto['preco_do_produto']:.2f}")
print("---------------------------")
print(f"Subtotal:  R$ {subtotal:.2f}")
print(f"Desconto:  R$ {desconto:.2f}")
print(f"Total:     R$ {total:.2f}")
```

O `for` passa por cada produto da lista e imprime uma linha com o nome e o preço. Depois vêm o subtotal, o desconto e o total, todos com 2 casas decimais. Quando não há desconto, a linha aparece como `R$ 0.00`.

Dentro da f-string, as chaves do dicionário usam aspas simples (`'nome_do_produto'`), porque o texto já está entre aspas duplas.

### 11. Forma de pagamento e troco

```python
forma_de_pagamento = input("Qual a forma de pagamento? (dinheiro/cartao): ").strip().lower()

if forma_de_pagamento == "dinheiro":
    valor_pago = 0
    while valor_pago < total:
        valor_digitado_pelo_usuario = input("Quanto o cliente pagou? ")
        try:
            valor_pago = float(valor_digitado_pelo_usuario)
            if valor_pago < total:
                print("Erro: o valor é menor que o total.")
        except ValueError:
            print("Erro: Digite um número.")
            valor_pago = 0
    troco = valor_pago - total
    print(f"Troco: R$ {troco:.2f}")
else:
    print("Pagamento no cartão.")
```

- O programa pergunta a forma de pagamento. Como no "continuar", `.strip().lower()` aceita `"Dinheiro"` ou `" dinheiro "`.
- **Se for dinheiro:** pede quanto o cliente pagou. É a mesma ideia da validação do preço:
  - `valor_pago` começa em `0` para entrar no laço;
  - o laço repete enquanto o valor não cobrir o total;
  - letras geram `ValueError` e o `except` mostra a mensagem de erro;
  - valor menor que o total mostra outra mensagem e pergunta de novo.
- Quando vem um valor suficiente, o troco é `valor_pago - total`. Se o cliente pagar o valor exato, o troco é `R$ 0.00`.
- **Qualquer outra resposta** (`cartao`, `pix`, um erro de digitação) cai no `else` e é tratada como cartão.

## Conceitos de Python usados

- **`input()`**: ler dados digitados pelo usuário
- **`float()`**: converter texto em número decimal
- **`while`**: repetir enquanto uma condição for verdadeira
- **`for`**: percorrer os elementos de uma lista
- **`if` / `elif` / `else`**: escolher um caminho entre vários
- **`try` / `except`**: tratar erros sem travar o programa
- **Listas** (`[]`, `.append()`): guardar vários valores em ordem
- **Dicionários** (`{"chave": valor}`): agrupar dados com nomes
- **Métodos de texto** (`.strip()`, `.lower()`): limpar e padronizar respostas
- **f-strings**: montar textos com valores de variáveis (`:.2f` para 2 casas decimais)
