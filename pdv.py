itens = []
continuar = "s"
subtotal = 0

while continuar == "s":
    nome_do_produto = input("Qual o nome do produto ? ")
    quantidade = int(input("Qual a quantidade do produto? "))
    preco_do_produto = 0
    while preco_do_produto <= 0:
        preco_digitado_pelo_usuario = input("Qual o preço ? ")
        try:
            preco_do_produto = float(preco_digitado_pelo_usuario)
        except ValueError:
            print("Erro: Digite um número.")
            preco_do_produto = 0

    produto = {"nome_do_produto": nome_do_produto, "preco_do_produto": preco_do_produto, "quantidade": quantidade}
    itens.append(produto)
    continuar = input("Deseja adicionar mais itens?(s/n): ").strip().lower()

for produto in itens:
    subtotal = subtotal + (produto["preco_do_produto"]* produto["quantidade"])


print(f"O valor sem o desconto é ${subtotal}")


print(f"O valor sem o desconto é R$ {subtotal:.2f}")

# Desafio 3: desconto progressivo
# 5% acima de R$ 50, 10% acima de R$ 100 e 15% acima de R$ 200
if subtotal > 200:
    desconto = subtotal * 0.15
elif subtotal > 100:
    desconto = subtotal * 0.10
elif subtotal > 50:
    desconto = subtotal * 0.05
else:
    desconto = 0

total = subtotal - desconto

print()
print("========== CUPOM ==========")
for produto in itens:
    print(f"{produto['nome_do_produto']}  R$ {produto['preco_do_produto']:.2f}")
print("---------------------------")
print(f"Subtotal:  R$ {subtotal:.2f}")
print(f"Desconto:  R$ {desconto:.2f}")
print(f"Total:     R$ {total:.2f}")
print("===========================")

# Desafio 2: forma de pagamento e troco
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
