itens = [{"nome":"bola","preco":29.00},{"nome":"lapis","preco":5.00},{"nome":"caderno","preco":25.00}]
subtotal = 0
for item in itens:
    subtotal = subtotal + item["preco"]
print(subtotal)    
