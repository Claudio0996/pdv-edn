itens = []
continuar = "s"
subtotal = 0


while continuar == "s":
    nome = input("Qual o nome do produto ? ")
    preco = 0
    while preco <=0:
        texto = input("Qual o preço ? ")
        try:
            preco = float(texto)
        except ValueError:
            print("Erro: Digite um número.")
            preco = 0

    item = {"nome":nome,"preco":preco}
    itens.append(item)
    subtotal = subtotal + item["preco"]

    continuar = input("Deseja adicionar mais itens?: ").strip().lower()


print(f"O valor sem o desconto é ${subtotal}")