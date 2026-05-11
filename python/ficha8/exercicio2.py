# Função para calcular a média
def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3


# Função para obter a situação do estudante
def obter_situacao(media):
    if media >= 9.5:
        return "Aprovado"
    else:
        return "Reprovado"


# Função para mostrar o resultado
def mostrar_resultado(nome, media, situacao):
    print("\n--- Resultado Final ---")
    print(f"Nome do estudante: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")


# Programa principal
nome = input("Digite o nome do estudante: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Cálculos
media = calcular_media(nota1, nota2, nota3)
situacao = obter_situacao(media)

# Mostrar resultado
mostrar_resultado(nome, media, situacao)