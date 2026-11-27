
itens = []        
subtotal = 0      
continuar = "s"   


while continuar == "s":
    nome_do_produto = input("Qual o nome do produto ? ")
    quantidade = 0
    while quantidade <= 0:
        quantidade_digitada_pelo_usuario = input("Qual a quantidade do produto? ")
        try:
            quantidade = int(quantidade_digitada_pelo_usuario)
            if quantidade <= 0:
                print("Erro: a quantidade deve ser maior que zero.")
        except ValueError:
            print("Erro: Digite um número inteiro.")
            quantidade = 0
    preco_do_produto = 0
    while preco_do_produto <= 0:
        preco_digitado_pelo_usuario = input("Qual o preço ? (ex: 12.50) ")
        try:
            preco_do_produto = float(preco_digitado_pelo_usuario)
            if preco_do_produto <= 0:
                print("Erro: o preço deve ser maior que zero.")
        except ValueError:
            print("Erro: Digite um número.")
            preco_do_produto = 0

    produto = {
        "nome_do_produto": nome_do_produto,
        "preco_do_produto": preco_do_produto,
        "quantidade": quantidade
    }
    itens.append(produto)
    continuar = input("Deseja adicionar mais itens?(s/n): ").strip().lower()

for produto in itens:
    subtotal = subtotal + (produto["preco_do_produto"] * produto["quantidade"])


print(f"O valor sem o desconto é R$ {subtotal:.2f}")

if subtotal > 200:
    desconto = subtotal * 0.15
elif subtotal > 100:
    #desconto = 137 * 0.10 = 13.7
    desconto = subtotal * 0.10
elif subtotal > 50:
    desconto = subtotal * 0.05
else:
    desconto = 0

total = subtotal - desconto

print("========== CUPOM ==========")
for item in itens:
    valor_do_item = item["preco_do_produto"] * item["quantidade"]
    print(f"{item['nome_do_produto']}  {item['quantidade']}x  R$ {valor_do_item:.2f}")
print("---------------------------")
print(f"Subtotal:  R$ {subtotal:.2f}")
#print(f"Subtotal:  R$ 137")
print(f"Desconto:  R$ {desconto:.2f}")
#print(f"Desconto:  R$ 13.7")
print(f"Total:     R$ {total:.2f}")
#print(f"Total:     R$ 123.3")
print("===========================")


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
