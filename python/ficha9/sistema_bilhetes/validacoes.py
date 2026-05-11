# Função para validar participantes
def quantidade_valida(quantidade):
    return quantidade > 0


# Função para validar preço do bilhete
def preco_valido(preco):
    return preco >= 0


# Função para validar custo de transporte
def transporte_valido(transporte):
    return transporte >= 0


# Testes do módulo
if __name__ == "__main__":
    print("=== TESTE validacoes.py ===")

    print(quantidade_valida(10))   # True
    print(quantidade_valida(0))    # False

    print(preco_valido(15.5))      # True
    print(preco_valido(-5))        # False

    print(transporte_valido(50))   # True
    print(transporte_valido(-1))   # False