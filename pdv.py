# ===== PARTE 1: PREPARAÇÃO =====
itens = []        
subtotal = 0      
continuar = "s"   

# ===== PARTE 2: CADASTRAR OS PRODUTOS =====
while continuar == "s":
    nome = input("Nome do produto: ")

    # Repete a pergunta até o preço ser um número maior que zero
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

# ===== PARTE 3: DESCONTO PROGRESSIVO =====
if subtotal > 200:
    desconto = subtotal * 0.15
elif subtotal > 100:
    desconto = subtotal * 0.10
elif subtotal > 50:
    desconto = subtotal * 0.05
else:
    desconto = 0

total = subtotal - desconto

# ===== PARTE 4: CUPOM =====
print()
print("========== CUPOM ==========")
for item in itens:
    print(f"{item['nome']}  R$ {item['preco']:.2f}")
print("---------------------------")
print(f"Subtotal:  R$ {subtotal:.2f}")
print(f"Desconto:  R$ {desconto:.2f}")
print(f"Total:     R$ {total:.2f}")
print("===========================")

# ===== PARTE 5: PAGAMENTO E TROCO =====
pagamento = input("Forma de pagamento (dinheiro/cartao): ").strip().lower()

if pagamento == "dinheiro":
    # Repete a pergunta até o valor cobrir o total
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
