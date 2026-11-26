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


