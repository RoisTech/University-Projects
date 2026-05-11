# Função para calcular a média
def calcular_media(notas):
    return sum(notas) / len(notas)


# Função para obter a maior nota
def obter_maior_nota(notas):
    return max(notas)


# Função para obter a menor nota
def obter_menor_nota(notas):
    return min(notas)


# Função para validar nota
def nota_valida(nota):
    return 0 <= nota <= 20


# Teste protegido
if __name__ == "__main__":
    notas_teste = [10, 15, 8]

    print("=== TESTE DO calculos.py ===")
    print(f"Notas: {notas_teste}")
    print(f"Média: {calcular_media(notas_teste):.2f}")
    print(f"Maior nota: {obter_maior_nota(notas_teste)}")
    print(f"Menor nota: {obter_menor_nota(notas_teste)}")

    # Teste da validação
    print(f"Nota 15 válida? {nota_valida(15)}")
    print(f"Nota 25 válida? {nota_valida(25)}")