import os

def limpar_ecra():
    os.system('cls' if os.name == 'nt' else 'clear')

def ler_texto(msg):
    while True:
        v = input(msg).strip()
        if v: return v
        print("Erro: Este campo não pode ficar em branco.")

def ler_inteiro(msg):
    while True:
        try: return int(input(msg))
        except ValueError: print("Erro: Introduza um número inteiro válido.")

def ler_nota(msg):
    while True:
        try:
            n = float(input(msg))
            if 0 <= n <= 20: return n
            print("Erro: A nota deve situar-se estritamente entre 0.0 e 20.0.")
        except ValueError: print("Erro: Formato inválido. Use pontos para decimais.")

def menu_principal():
    print("\n" + "╠" + "═"*50 + "╣")
    print("║        SISTEMA DE GESTÃO DE FORMAÇÃO CORPORATIVA        ║")
    print("║                    BOMBEIROS 2026                       ║")
    print("╠" + "═"*50 + "╣")
    print("  1. 📚 Catálogo de Matérias Formativas")
    print("  2. 🧑‍🚒 Histórico de Classificações Práticas")
    print("  3. 📊 Painel Analítico e Estatísticas de Sucesso")
    print("  0. 💾 Terminar Sessão e Gravar Ficheiros")
    print("╚" + "═"*50 + "╝")

def submenu_materias():
    print("\n»» MÓDULO: CATÁLOGO DE MATÉRIAS ««")
    print("1. Registar Nova Matéria")
    print("2. Listar Todas as Matérias")
    print("3. Editar Informação de Matéria")
    print("4. Remover Matéria (Aviso: Apaga notas vinculadas)")
    print("0. Voltar")

def submenu_bombeiros():
    print("\n»» MÓDULO: HISTÓRICO DE CLASSIFICAÇÕES ««")
    print("1. Lançar Nota de Treino")
    print("2. Listagem Geral")
    print("3. Pesquisa Parametrizada (Nome ou Código)")
    print("4. Ordenar Pauta Prática")
    print("5. Eliminar Registo de Nota por ID")
    print("0. Voltar")

def mostrar_tabela_materias(lista):
    print(f"\n{'CÓDIGO':<8} | {'MATÉRIA FORMATIVA':<30} | {'HORAS':<7} | {'TIPOLOGIA':<15}")
    print("-" * 68)
    for m in lista:
        print(f"{m['cod']:<8} | {m['nome']:<30} | {m['horas']:<5} h | {m['tipo']:<15}")

def mostrar_tabela_bombeiros(lista_bombeiros, lista_materias):
    from logica import obter_nome_materia
    print(f"\n{'REGISTO':<8} | {'NOME DO BOMBEIRO':<25} | {'MATÉRIA':<20} | {'NOTA':<5}")
    print("-" * 68)
    for b in lista_bombeiros:
        nome_mat = obter_nome_materia(lista_materias, b['cod_materia'])
        nome_mat_resumo = (nome_mat[:17] + '...') if len(nome_mat) > 20 else nome_mat
        print(f"{b['id']:<8} | {b['nome']:<25} | {nome_mat_resumo:<20} | {b['nota']:<5.1f}")
