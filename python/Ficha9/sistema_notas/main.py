from calculos import (
    calcular_media,
    obter_maior_nota,
    obter_menor_nota
)


def main():
    nome = input("Nome do estudante: ")

    notas = []

    for i in range(1, 4):
        nota = float(input(f"Introduza a nota {i}: "))
        notas.append(nota)

    media = calcular_media(notas)
    maior_nota = obter_maior_nota(notas)
    menor_nota = obter_menor_nota(notas)

    print("\n===== RESULTADO FINAL =====")
    print(f"Nome do estudante: {nome}")
    print(f"Lista de notas: {notas}")
    print(f"Média: {media:.2f}")
    print(f"Maior nota: {maior_nota}")
    print(f"Menor nota: {menor_nota}")


if __name__ == "__main__":
    main()