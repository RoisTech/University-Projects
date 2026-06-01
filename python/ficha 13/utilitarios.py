def produto (a, b):
    return a * b

def e_impar(n):
    return n % 2 != 0

def menor_que_cem(n):
    return n < 100

def subtrair(a, b):
    if a < b:
        return "Erro: resultado negativo"
    return a - b

def valida_nome(nome):
    if isinstance(nome, str) and nome.strip() != "":
        return nome
    raise ValueError("Nome inválido")

if __name__ == "__main__":
    print("A iniciar testes manuais...")
    
    # Testes para a função produto
    assert produto(3, 4) == 12, "Erro: produto(3, 4) deveria devolver 12"
    assert produto(-2, 5) == -10, "Erro: produto(-2, 5) deveria devolver -10"
    
    # Testes para a função e_impar
    assert e_impar(3) is True, "Erro: e_impar(3) deveria devolver True"
    assert e_impar(4) is False, "Erro: e_impar(4) deveria devolver False"
    
    # Testes para a função menor_que_cem
    assert menor_que_cem(99) is True, "Erro: menor_que_cem(99) deveria devolver True"
    assert menor_que_cem(100) is False, "Erro: menor_que_cem(100) deveria devolver False"
    
    # Testes para a função subtrair
    assert subtrair(10, 5) == 5, "Erro: subtrair(10, 5) deveria devolver 5"
    assert subtrair(5, 10) == "Erro: resultado negativo", "Erro: subtrair(5, 10) deveria devolver string de erro"
    
    # Testes para a função valida_nome
    assert valida_nome("João") == "João", "Erro: valida_nome('João') deveria devolver 'João'"
    
    # Testar o lançamento do erro (ValueError) para uma string vazia
    try:
        valida_nome("")
        assert False, "Erro: valida_nome('') deveria ter lançado um ValueError"
    except ValueError as e:
        assert str(e) == "Nome inválido", "Erro: A mensagem da exceção deveria ser 'Nome inválido'"

    # Testar o lançamento do erro (ValueError) para espaços em branco
    try:
        valida_nome("   ")
        assert False, "Erro: valida_nome('   ') deveria ter lançado um ValueError"
    except ValueError as e:
        assert str(e) == "Nome inválido", "Erro: A mensagem da exceção deveria ser 'Nome inválido'"
        
    print("Todos os testes passaram.")