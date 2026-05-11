from calculos import (
    calcular_subtotal,
    calcular_desconto,
    calcular_total_final,
    calcular_media_participante
)

from validacoes import (
    quantidade_valida,
    preco_valido,
    transporte_valido
)


def main():
    # Nome da visita
    nome_visita = input("Digite o nome da visita de estudo: ")

    # Dados
    quantidade = int(input("Digite a quantidade de participantes: "))
    preco = float(input("Digite o preço unitário do bilhete (€): "))
    transporte = float(input("Digite o custo total de transporte (€): "))

    # Validações
    if not quantidade_valida(quantidade):
        print("Dados inválidos.")
        return

    if not preco_valido(preco):
        print("Dados inválidos.")
        return

    if not transporte_valido(transporte):
        print("Dados inválidos.")
        return

    # Cálculos
    subtotal = calcular_subtotal(quantidade, preco)
    desconto = calcular_desconto(subtotal)
    total_final = calcular_total_final(
        subtotal,
        desconto,
        transporte
    )

    media = calcular_media_participante(
        total_final,
        quantidade
    )

    # Resultados
    print("\n--- Resultado Final ---")
    print(f"Visita de estudo: {nome_visita}")
    print(f"Quantidade de participantes: {quantidade}")
    print(f"Preço unitário do bilhete: {preco:.2f} €")
    print(f"Subtotal: {subtotal:.2f} €")
    print(f"Desconto: {desconto:.2f} €")
    print(f"Transporte: {transporte:.2f} €")
    print(f"Total Final: {total_final:.2f} €")
    print(f"Valor médio por participante: {media:.2f} €")


if __name__ == "__main__":
    main()