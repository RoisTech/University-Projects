# interface/menu.py

from utils.validacao import ler_int
from modulos.quarteis import (
    inserir_quartel,
    listar_quarteis,
    procurar_quarteis_por_distrito,
    editar_quartel,
    remover_quartel,
)
from modulos.ocorrencias import (
    inserir_ocorrencia,
    listar_ocorrencias,
    editar_ocorrencia,
    remover_ocorrencia,
)
from modulos.estatisticas import (
    ocorrencias_por_distrito,
    ocorrencias_por_quartel,
)

def menu_principal():
    """
    Menu principal da aplicação FireCommand em modo consola.
    Permite aceder a Quartéis, Ocorrências e Estatísticas.
    """
    while True:
        print("\n=== FireCommand (Consola) ===")
        print("1 - Gestão de Quartéis")
        print("2 - Gestão de Ocorrências")
        print("3 - Estatísticas")
        print("0 - Sair")
        op = ler_int("Opção: ", 0, 3)

        if op == 1:
            menu_quarteis()
        elif op == 2:
            menu_ocorrencias()
        elif op == 3:
            menu_estatisticas()
        elif op == 0:
            print("Até à próxima.")
            break

def menu_quarteis():
    while True:
        print("\n--- Quartéis ---")
        print("1 - Inserir")
        print("2 - Listar")
        print("3 - Pesquisar por distrito")
        print("4 - Editar")
        print("5 - Remover")
        print("0 - Voltar")
        op = ler_int("Opção: ", 0, 5)

        if op == 1:
            inserir_quartel()
        elif op == 2:
            listar_quarteis()
        elif op == 3:
            procurar_quarteis_por_distrito()
        elif op == 4:
            editar_quartel()
        elif op == 5:
            remover_quartel()
        elif op == 0:
            break

def menu_ocorrencias():
    while True:
        print("\n--- Ocorrências ---")
        print("1 - Inserir")
        print("2 - Listar")
        print("3 - Editar")
        print("4 - Remover")
        print("0 - Voltar")
        op = ler_int("Opção: ", 0, 4)

        if op == 1:
            inserir_ocorrencia()
        elif op == 2:
            listar_ocorrencias()
        elif op == 3:
            editar_ocorrencia()
        elif op == 4:
            remover_ocorrencia()
        elif op == 0:
            break

def menu_estatisticas():
    while True:
        print("\n--- Estatísticas ---")
        print("1 - Ocorrências por distrito")
        print("2 - Ocorrências por quartel")
        print("0 - Voltar")
        op = ler_int("Opção: ", 0, 2)

        if op == 1:
            ocorrencias_por_distrito()
        elif op == 2:
            ocorrencias_por_quartel()
        elif op == 0:
            break