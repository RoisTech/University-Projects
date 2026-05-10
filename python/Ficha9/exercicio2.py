def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media


def obter_situacao(media):
    if media >= 9.5:
        return "Aprovado"
    else:
        return "Reprovado"


def mostrar_resultado(nome, media, situacao):
    print("\n===== RESULTADO FINAL =====")
    print(f"Nome do estudante: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")


def main():
    nome = input("Nome do estudante: ")

    nota1 = float(input("Introduza a nota 1: "))
    nota2 = float(input("Introduza a nota 2: "))
    nota3 = float(input("Introduza a nota 3: "))

    media = calcular_media(nota1, nota2, nota3)
    situacao = obter_situacao(media)

    mostrar_resultado(nome, media, situacao)


if __name__ == "__main__":
    main()