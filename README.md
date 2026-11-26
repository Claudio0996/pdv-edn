# PDV — Ponto de Venda em Python

Um programa de terminal que funciona como o caixa de uma loja:

1. você informa os produtos e os preços;
2. ele aplica um desconto que cresce com o valor da compra;
3. imprime o cupom;
4. pergunta a forma de pagamento e, se for dinheiro, calcula o troco.

## Como executar

É preciso ter o Python 3 instalado. No terminal, dentro da pasta do projeto:

```bash
python pdv.py
```

> Use ponto nos preços (`12.50`), não vírgula (`12,50`).

## Exemplo de uso

```
Nome do produto: arroz
Preço (ex: 12.50): abc
Erro: digite um número.
Preço (ex: 12.50): 0
Erro: o preço deve ser maior que zero.
Preço (ex: 12.50): 50
Adicionar mais itens? (s/n): s
Nome do produto: feijao
Preço (ex: 12.50): 70
Adicionar mais itens? (s/n): n

========== CUPOM ==========
arroz  R$ 50.00
feijao  R$ 70.00
---------------------------
Subtotal:  R$ 120.00
Desconto:  R$ 12.00
Total:     R$ 108.00
===========================
Forma de pagamento (dinheiro/cartao): dinheiro
Valor pago: 100
Erro: o valor é menor que o total.
Valor pago: 150
Troco: R$ 42.00
```

## Roteiro do código

O código está dividido em 5 partes, marcadas no arquivo com `# ===== PARTE N =====`.

### Parte 1: Preparação

```python
itens = []
subtotal = 0
continuar = "s"
```

Cria o que o programa precisa **lembrar** durante a compra:

- `itens`: lista vazia, onde cada produto vai entrar.
- `subtotal`: começa em zero e vai somando os preços.
- `continuar`: começa com `"s"` para o laço da parte 2 rodar pelo menos uma vez.

Essas variáveis ficam **antes** do `while`. Se ficassem dentro, seriam zeradas a cada produto e a compra perderia os itens anteriores.

### Parte 2: Cadastrar os produtos

```python
while continuar == "s":
    nome = input("Nome do produto: ")

    preco = 0
    while preco <= 0:
        try:
            preco = float(input("Preço (ex: 12.50): "))
            if preco <= 0:
                print("Erro: o preço deve ser maior que zero.")
        except ValueError:
            print("Erro: digite um número.")

    itens.append({"nome": nome, "preco": preco})
    subtotal = subtotal + preco

    continuar = input("Adicionar mais itens? (s/n): ").strip().lower()
```

O programa continua **enquanto** o usuário responder `s`. A cada volta, ele:

1. **Pergunta o nome** do produto.
2. **Pergunta o preço até ele ser válido.** O preço começa em `0` para forçar a entrada no `while` de dentro. Esse `while` só termina quando vem um número maior que zero:
   - `float()` transforma o texto em número. `input()` sempre devolve texto, e com texto não dá para fazer conta.
   - Se o usuário digitar letras, `float()` gera um `ValueError`. O `except` captura esse erro e mostra a mensagem, sem o programa quebrar.
   - Se o número for `0` ou negativo, o `if` mostra a mensagem e o `while` pergunta de novo.
3. **Guarda o produto** na lista. Cada produto é um dicionário com `"nome"` e `"preco"`.
4. **Soma o preço** no subtotal.
5. **Pergunta se quer continuar.** `.strip()` tira os espaços e `.lower()` deixa a resposta em minúsculas, então `S` também vale.

### Parte 3: Desconto progressivo

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

| Subtotal | Desconto |
|---|---|
| até R$ 50,00 | sem desconto |
| acima de R$ 50,00 | 5% |
| acima de R$ 100,00 | 10% |
| acima de R$ 200,00 | 15% |

- **A ordem vai do maior para o menor.** Uma compra de R$ 250 também é maior que 100 e que 50. Se o teste de 50 viesse primeiro, ela ganharia só 5%.
- **`elif` quer dizer "senão, se".** Só um dos blocos roda.
- **O `else` garante `desconto = 0`.** Assim a variável sempre existe, mesmo sem desconto, e o cupom não quebra.
- **O sinal é `>`, não `>=`.** R$ 100,00 fica na faixa de 5%; R$ 100,01 já ganha 10%.

> **Atenção:** o teste "Exatamente 100" da tarefa 9 espera desconto R$ 0,00, porque usa a regra antiga (10% só acima de R$ 100). Com o desconto progressivo, essa compra recebe R$ 5,00 de desconto.

### Parte 4: Cupom

```python
for item in itens:
    print(f"{item['nome']}  R$ {item['preco']:.2f}")
```

O `for` passa por cada produto da lista e imprime o nome e o preço. Depois vêm o subtotal, o desconto e o total.

- **O `f` antes das aspas** (f-string) coloca o valor das variáveis dentro do texto.
- **`:.2f`** mostra o número com 2 casas decimais (`50.00` em vez de `50.0`).

### Parte 5: Pagamento e troco

```python
pagamento = input("Forma de pagamento (dinheiro/cartao): ").strip().lower()

if pagamento == "dinheiro":
    valor_pago = 0
    while valor_pago < total:
        try:
            valor_pago = float(input("Valor pago: "))
            if valor_pago < total:
                print("Erro: o valor é menor que o total.")
        except ValueError:
            print("Erro: digite um número.")

    troco = valor_pago - total
    print(f"Troco: R$ {troco:.2f}")
else:
    print("Pagamento no cartão.")
```

- **Se for dinheiro:** pergunta quanto o cliente pagou e repete até o valor cobrir o total. É a mesma ideia da validação do preço na parte 2. No fim, mostra o troco (`valor_pago - total`).
- **Qualquer outra resposta** cai no `else` e é tratada como cartão.

## Variáveis

| Variável | Tipo | O que guarda |
|---|---|---|
| `itens` | lista | Todos os produtos da compra. |
| `subtotal` | número | A soma dos preços. |
| `continuar` | texto | A resposta para "Adicionar mais itens?". |
| `nome` | texto | O nome do produto atual. |
| `preco` | número | O preço do produto atual. |
| `desconto` | número | O valor do desconto. |
| `total` | número | O que o cliente paga: subtotal menos desconto. |
| `pagamento` | texto | A forma de pagamento: `"dinheiro"` ou `"cartao"`. |
| `valor_pago` | número | Quanto o cliente entregou em dinheiro. |
| `troco` | número | Valor pago menos total. |

## Conceitos de Python usados

| Conceito | Para que serve | Onde aparece |
|---|---|---|
| `input()` | Ler o que o usuário digita | Partes 2 e 5 |
| `float()` | Transformar texto em número | Partes 2 e 5 |
| `while` | Repetir enquanto algo for verdade | Partes 2 e 5 |
| `try` / `except` | Não quebrar quando o usuário digita letras | Partes 2 e 5 |
| `if` / `elif` / `else` | Escolher um caminho | Partes 3 e 5 |
| Lista e `append()` | Guardar vários produtos | Partes 1 e 2 |
| Dicionário | Juntar nome e preço de um produto | Parte 2 |
| `for` | Passar por cada item da lista | Parte 4 |
| `.strip().lower()` | Limpar a resposta do usuário | Partes 2 e 5 |
| f-string com `:.2f` | Mostrar dinheiro com 2 casas | Partes 4 e 5 |
