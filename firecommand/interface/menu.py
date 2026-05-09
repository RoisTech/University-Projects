from modulos.incidentes import adicionar_incidente, listar_incidentes
from modulos.recursos import adicionar_recurso, listar_recursos
from core.simulador import simular
from modulos.analise import estatisticas

def menu():
    while True:
        print("\n=== FIRECOMMAND ===")
        print("1. Novo Incidente")
        print("2. Ver Incidentes")
        print("3. Adicionar Recursos")
        print("4. Ver Recursos")
        print("5. Simular Operação")
        print("6. Estatísticas")
        print("0. Sair")

        op = input("Escolha: ")

        if op == "1":
            adicionar_incidente()
        elif op == "2":
            listar_incidentes()
        elif op == "3":
            adicionar_recurso()
        elif op == "4":
            listar_recursos()
        elif op == "5":
            simular()
        elif op == "6":
            estatisticas()
        elif op == "0":
            break
