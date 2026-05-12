def validar_nome(nome):

    return nome.strip() != ""
 
 
def validar_quantidade(quantidade):

    return quantidade >= 0
 
 
def validar_preco(preco):

    return preco >= 0
 
 

if __name__ == "__main__":
    print("=== Testes de validacoes.py ===")
 
    print(validar_nome("Arroz"))    # True  — nome válido
    print(validar_nome(""))         # False — nome vazio
    print(validar_nome("   "))      # False — só espaços
 
    print(validar_quantidade(2))    # True  — quantidade válida
    print(validar_quantidade(0))    # True  — zero é válido
    print(validar_quantidade(-1))   # False — negativo é inválido
 
    print(validar_preco(1.50))      # True  — preço válido
    print(validar_preco(0))         # True  — grátis é válido
    print(validar_preco(-5))        # False — preço negativo inválido