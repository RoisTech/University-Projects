from calculos import (
    calcular_media,
    obter_maior_nota,
    obter_menor_nota,
    nota_valida
)


def main():
    # Pedir nome do estudante
    nome = input("Digite o nome do estudante: ")

    notas = []
    erro = False

    # Pedir 3 notas
    for i in range(1, 4):
        nota = float(input(f"Digite a nota {i}: "))

        # Validar nota
        if nota_valida(nota):
            notas.append(nota)
        else:
            print("Nota inválida.")
            erro = True
            break

    # Só calcula se não houver erro
    if not erro:
        media = calcular_media(notas)
        maior = obter_maior_nota(notas)
        menor = obter_menor_nota(notas)

        # Mostrar resultados
        print("\n--- Resultado Final ---")
        print(f"Nome do estudante: {nome}")
        print(f"Lista de notas: {notas}")
        print(f"Média: {media:.2f}")
        print(f"Maior nota: {maior}")
        print(f"Menor nota: {menor}")


if __name__ == "__main__":
    main()