

itens = []
continuar = "s"
subtotal = 0

while continuar == "s":
    nome_do_produto = input("Qual o nome do produto? ")
    preco_do_produto = 0

    while preco_do_produto <= 0:
        preco_digitado_pelo_usuario = input("Qual o preço? ")

        try:
            preco_do_produto = float(preco_digitado_pelo_usuario)
        except ValueError:
            print("Erro: Digite um número.")
            preco_do_produto = 0

    produto = {
        "nome_do_produto": nome_do_produto,
        "preco_do_produto": preco_do_produto
    }

    itens.append(produto)

    continuar = input(
        "Deseja adicionar mais itens? (s/n): "
    ).strip().lower()

# Calcular subtotal
for produto in itens:
    subtotal += produto["preco_do_produto"]

# Valores do cupom
desconto = 0
total = subtotal

# Tarefa 8: Montar o cupom
print("\n========== CUPOM ==========")

for produto in itens:
    print(
        f"{produto['nome_do_produto']} - "
        f"R$ {produto['preco_do_produto']:.2f}"
    )

print("---------------------------")
print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total a pagar: R$ {total:.2f}")
print("===========================")
