def calcular_subtotal(quantidade, preco):
    return quantidade * preco


def calcular_desconto(subtotal):
    if subtotal >= 100:
        return subtotal * 0.10
    else:
        return 0


def calcular_total_final(subtotal, desconto):
    return subtotal - desconto


def calcular_media_por_participante(total, quantidade):
    return total / quantidade


if __name__ == "__main__":

    subtotal = calcular_subtotal(10, 15)
    print(f"Subtotal: {subtotal:.2f} €")

    desconto = calcular_desconto(subtotal)
    print(f"Desconto: {desconto:.2f} €")

    total = calcular_total_final(subtotal, desconto)
    print(f"Total Final: {total:.2f} €")

    media = calcular_media_por_participante(total, 10)
    print(f"Média por participante: {media:.2f} €")