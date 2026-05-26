# utils/validacao.py
from config import DISTRITOS

def ler_int(msg, minimo=None, maximo=None):
    """
    Lê um inteiro do utilizador, com validação opcional de intervalo.
    """
    while True:
        try:
            valor = int(input(msg))
            if minimo is not None and valor < minimo:
                print(f"Valor mínimo é {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"Valor máximo é {maximo}.")
                continue
            return valor
        except ValueError:
            print("Introduza um número inteiro válido.")

def ler_str(msg, obrigatorio=True):
    """
    Lê uma string do utilizador, opcionalmente obrigatória.
    """
    while True:
        texto = input(msg).strip()
        if obrigatorio and not texto:
            print("Este campo é obrigatório.")
        else:
            return texto

def ler_distrito():
    """
    Mostra a lista de distritos definidos em config.DISTRITOS e devolve o selecionado.
    """
    print("Distritos disponíveis:")
    for i, d in enumerate(DISTRITOS, start=1):
        print(f"{i} - {d}")
    idx = ler_int("Escolha o número do distrito: ", 1, len(DISTRITOS))
    return DISTRITOS[idx - 1]