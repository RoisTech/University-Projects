def validar_participantes(quantidade):
    return quantidade > 0


def validar_preco(preco):
    return preco >= 0


if __name__ == "__main__":

    print("=== TESTES VALIDACOES ===")

    print(validar_participantes(10))
    print(validar_participantes(0))

    print(validar_preco(15.5))
    print(validar_preco(-5))