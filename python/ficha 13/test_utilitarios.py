import pytest
from utilitarios import e_impar, menor_que_cem, produto, subtrair, valida_nome


def test_produto():
    assert produto(3, 4) == 12
    assert produto(-2, 5) == -10
    assert produto(0, 10) == 0

def test_e_impar():
    assert e_impar(3) is True
    assert e_impar(4) is False
    assert e_impar(0) is False
    assert e_impar(-5) is True

def test_menor_que_cem():
    assert menor_que_cem(99) is True
    assert menor_que_cem(-50) is True
    assert menor_que_cem(100) is False
    assert menor_que_cem(101) is False

def test_subtrair():
    assert subtrair(10, 5) == 5
    assert subtrair(5, 5) == 0
    assert subtrair(5, 10) == "Erro: resultado negativo"

def test_valida_nome():
    assert valida_nome("João") == "João"
    
    with pytest.raises(ValueError, match="Nome inválido"):
        valida_nome("")
        
    with pytest.raises(ValueError, match="Nome inválido"):
        valida_nome("   ")

if __name__ == "__main__":
    pytest.main(["-v", __file__])
