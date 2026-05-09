from calculos import (
    calcular_subtotal,
    calcular_desconto,
    calcular_total_final,
    calcular_media_por_participante
)

from validacoes import (
    validar_participantes,
    validar_preco
)


def main():

        participantes = int(input("Quantidade de participantes: "))
        preco = float(input("Preço unitário do bilhete: "))

        if (
            not validar_participantes(participantes)
            or not validar_preco(preco)
        ):
            print("Dados inválidos.")
            return

        subtotal = calcular_subtotal(participantes, preco)

        desconto = calcular_desconto(subtotal)

        total_final = calcular_total_final(
            subtotal,
            desconto
        )

        media = calcular_media_por_participante(
            total_final,
            participantes
        )

        print(f"Participantes: {participantes}")
        print(f"Preço do bilhete: {preco:.2f} €")
        print(f"Subtotal: {subtotal:.2f} €")
        print(f"Desconto: {desconto:.2f} €")
        print(f"Total final: {total_final:.2f} €")
        print(f"Valor médio por participante: {media:.2f} €")

if __name__ == "__main__":
    main()