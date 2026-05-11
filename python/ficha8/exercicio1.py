# Função para calcular o subtotal
def calcular_subtotal(preco, quantidade):
    return preco * quantidade


# Função para calcular o IVA (23%)
def calcular_iva(subtotal):
    return subtotal * 0.23


# Função para calcular o total final
def calcular_total(subtotal, iva):
    return subtotal + iva


# Programa principal
nome_produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço unitário (€): "))
quantidade = int(input("Digite a quantidade: "))

# Cálculos
subtotal = calcular_subtotal(preco, quantidade)
iva = calcular_iva(subtotal)
total = calcular_total(subtotal, iva)

# Resultados
print("\n--- Resumo da Compra ---")
print(f"Produto: {nome_produto}")
print(f"Subtotal: {subtotal:.2f} €")
print(f"IVA (23%): {iva:.2f} €")
print(f"Total Final: {total:.2f} €")