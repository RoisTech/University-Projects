# Função para calcular subtotal
def calcular_subtotal(quantidade, preco):
    return quantidade * preco


# Função para calcular desconto
def calcular_desconto(subtotal):
    if subtotal >= 100:
        return subtotal * 0.10
    return 0


# Função para calcular total final
def calcular_total_final(subtotal, desconto, transporte):
    return subtotal - desconto + transporte


# Função para calcular valor médio por participante
def calcular_media_participante(total, quantidade):
    return total / quantidade


# Testes do módulo
if __name__ == "__main__":
    print("=== TESTE calculos.py ===")

    subtotal = calcular_subtotal(10, 15)
    desconto = calcular_desconto(subtotal)
    total = calcular_total_final(subtotal, desconto, 20)
    media = calcular_media_participante(total, 10)

    print(f"Subtotal: {subtotal:.2f} €")
    print(f"Desconto: {desconto:.2f} €")
    print(f"Total Final: {total:.2f} €")
    print(f"Média por participante: {media:.2f} €")