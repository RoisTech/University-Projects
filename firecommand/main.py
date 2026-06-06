# main.py
"""
Ponto de Entrada Central do Sistema FireCommand Pro Tático.
Gerencia a inicialização operacional, a bateria de testes de asserção (Requisito UC),
e o carregamento das interfaces (Gráfica vs. Consola).
"""

import sys

# Importações de configuração e backend
from config import BASE_PATH, DB_CONFIG
from database.db import iniciar_bd
from gui import FireCommandGUI
from interface.menu import menu_principal

# Importação do módulo de validação de testes académicos (Requisito estrito com Assert)
from tests import executar_testes_sistema


def main():
    print("🚒 FireCommand Pro — Centro Operacional Tático de Gestão de Emergências")
    print("----------------------------------------------------------------------")
    print(f"Base de Dados: {DB_CONFIG['host']} - {DB_CONFIG['database']}")
    print(f"Diretório Raiz: {BASE_PATH}\n")
    
    # 1. BLOCO OPERACIONAL OBRIGATÓRIO (Requisito do Enunciado):
    # Executa a bateria de testes automáticos com a estrutura condicional assert
    # antes de carregar a interface. Isto garante a fiabilidade do sistema.
    try:
        executar_testes_sistema()
    except AssertionError as ae:
        print(f"\n❌ ERRO CRÍTICO NA VALIDAÇÃO DOS TESTES TÁTICOS OPERACIONAIS (Assert):")
        print(f"==> Detalhe do Erro: {ae}")
        print("A aplicação não pode ser iniciada até que o módulo de testes seja corrigido.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erro desconhecido durante a execução dos testes: {e}")
        sys.exit(1)

    # 2. BLOCO DE PERSISTÊNCIA HÍBRIDA (Requisito do Enunciado):
    # Inicializa o MySQL e gera/sincroniza a cópia local obrigatória em formato CSV (bombeiros_backup.csv)
    print("\n🚀 A sincronizar persistência híbrida (MySQL + Cópia Local CSV)...")
    try:
        iniciar_bd()
        # Nota: A função iniciar_bd() já chama internamente a rotina sincronizar_dados_para_csv()
    except Exception as e:
        print(f"⚠️  Aviso ao inicializar Base de Dados: {e}")
        # Dependendo da política operacional, podes decidir sair (sys.exit) ou continuar apenas com CSV.
        print("Tentando continuar a aplicação com a persistência de dados disponível.")

    # 3. BLOCO DE INTERFACE:
    # Mantém o teu sistema de escolha profissional de interface (Consola vs. Gráfica com Mapeamento)
    print("\n----------------------------------------------------------------------")
    print("1 — Interface Gráfica Avançada (GUI com Mapas Interativos Folium/TkinterMapView)")
    print("2 — Interface de Consola (Operações procedimentais básicas — Requisito UC)")
    
    # Valida a entrada do utilizador
    while True:
        opcao = input("\nEscolha o modo operacional (1/2) ou 'S' para Sair: ").strip().upper()
        
        if opcao == "1":
            print("\n🚀 A carregar Interface Gráfica Avançada...")
            sistema = FireCommandGUI()
            sistema.iniciar()
            break
        elif opcao == "2":
            print("\n📋 A carregar Interface de Consola procedimental...")
            menu_principal()
            break
        elif opcao == "S":
            print("\nSair do sistema. Desmobilizando operações.")
            break
        else:
            print("❌ Opção inválida. Por favor, escolha 1 para GUI, 2 para Consola, ou 'S' para Sair.")


if __name__ == "__main__":
    main()