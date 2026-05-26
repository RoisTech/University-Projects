# main.py
from gui import FireCommandGUI
from interface.menu import menu_principal
from database.db import iniciar_bd   # ← agora vem de db.py# ajusta o nome do módulo/função se for diferente


def main():
    # inicializar base de dados (criar BD/tabelas se necessário)
    iniciar_bd()

    print("1 - Interface gráfica (GUI)")
    print("2 - Interface consola")
    opcao = input("Escolha o modo (1/2): ").strip()

    if opcao == "2":
        menu_principal()
    else:
        sistema = FireCommandGUI()
        sistema.iniciar()


if __name__ == "__main__":
    main()
