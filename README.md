# PDV — Ponto de Venda em Python

Um programa simples de terminal que funciona como o caixa de uma loja: você informa os produtos e os preços, e no final ele mostra o valor total da compra (ainda sem desconto).

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
Qual o preço ? 10.5
Deseja adicionar mais itens?(s/n): s
Qual o nome do produto ? feijao
Qual o preço ? 8
Deseja adicionar mais itens?(s/n): n
O valor sem o desconto é $18.5
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

### 8. Mostrar o resultado

```python
print(f"O valor sem o desconto é ${subtotal}")
```

A f-string (o `f` antes das aspas) coloca o valor de `subtotal` dentro do texto, no lugar de `{subtotal}`.

## Conceitos de Python usados

- **`input()`**: ler dados digitados pelo usuário
- **`float()`**: converter texto em número decimal
- **`while`**: repetir enquanto uma condição for verdadeira
- **`for`**: percorrer os elementos de uma lista
- **`try` / `except`**: tratar erros sem travar o programa
- **Listas** (`[]`, `.append()`): guardar vários valores em ordem
- **Dicionários** (`{"chave": valor}`): agrupar dados com nomes
- **Métodos de texto** (`.strip()`, `.lower()`): limpar e padronizar respostas
- **f-strings**: montar textos com valores de variáveis


