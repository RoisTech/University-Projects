def calcular_media(notas):
    return sum(notas) / len(notas)


def obter_maior_nota(notas):
    return max(notas)


def obter_menor_nota(notas):
    return min(notas)


def nota_valida(nota):
    return 0 <= nota <= 20


if __name__ == "__main__":
    notas_teste = [10, 15, 12]

    print("Notas:", notas_teste)
    print("Média:", calcular_media(notas_teste))
    print("Maior nota:", obter_maior_nota(notas_teste))
    print("Menor nota:", obter_menor_nota(notas_teste))

    print("Nota 15 válida:", nota_valida(15))
    print("Nota 25 válida:", nota_valida(25))