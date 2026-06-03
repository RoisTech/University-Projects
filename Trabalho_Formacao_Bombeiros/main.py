import ficheiros
import logica
import interface
import testes

def fluxo_materias(materias, bombeiros):
    while True:
        interface.submenu_materias()
        op = input("Opção: ").strip()
        if op == "1":
            cod = interface.ler_texto("Código da Matéria (Ex: MOD05): ")
            nome = interface.ler_texto("Nome Descritivo: ")
            horas = interface.ler_inteiro("Carga Horária (h): ")
            tipo = interface.ler_texto("Regime (Prática / Teórica): ")
            sucesso, msg = logica.inserir_materia(materias, cod, nome, horas, tipo)
            print(msg)
        elif op == "2":
            interface.mostrar_tabela_materias(materias)
        elif op == "3":
            cod = interface.ler_texto("Introduza o Código da matéria que pretende alterar: ")
            if logica.materia_existe(materias, cod):
                n_nome = interface.ler_texto("Novo Nome: ")
                n_horas = interface.ler_inteiro("Novas Horas: ")
                n_tipo = interface.ler_texto("Novo Regime: ")
                logica.editar_materia(materias, cod, n_nome, n_horas, n_tipo)
                print("Catálogo atualizado com sucesso.")
            else:
                print("Matéria não encontrada.")
        elif op == "4":
            cod = interface.ler_texto("Código da matéria a eliminar definitivamente: ")
            confirmacao = input(f"Aviso: Isto eliminará todas as notas associadas ao código {cod}. Confirmar? (s/n): ")
            if confirmacao.lower() == 's':
                if logica.remover_materia_e_vinculos(materias, bombeiros, cod):
                    print("Matéria e notas associadas removidas com sucesso.")
                else:
                    print("Código não encontrado.")
        elif op == "0":
            break

def fluxo_bombeiros(bombeiros, materias):
    while True:
        interface.submenu_bombeiros()
        op = input("Opção: ").strip()
        if op == "1":
            if not materias:
                print("Catálogo vazio. Impossível registar classificações sem matérias existentes.")
                continue
            nome = interface.ler_texto("Nome Completo do Bombeiro: ")
            interface.mostrar_tabela_materias(materias)
            cod_mat = interface.ler_texto("Código da Matéria Aplicada: ")
            nota = interface.ler_nota("Nota Obtida no Treino Prático: ")
            sucesso, msg = logica.matricular_e_avaliar(bombeiros, materias, nome, cod_mat, nota)
            print(msg)
        elif op == "2":
            interface.mostrar_tabela_bombeiros(bombeiros, materias)
        elif op == "3":
            print("Pesquisar por: 1 - Nome do Bombeiro | 2 - Código da Matéria")
            escolha = input("Escolha: ").strip()
            criterio = "nome" if escolha == "1" else "materia"
            termo = interface.ler_texto("Termo de pesquisa: ")
            resultados = logica.pesquisa_linear_bombeiro(bombeiros, termo, criterio)
            interface.mostrar_tabela_bombeiros(resultados, materias)
        elif op == "4":
            print("1 - Ordenar por maior classificação (Decrescente) | 2 - Ordenar por menor classificação (Crescente)")
            tipo_ord = input("Escolha: ").strip()
            asc = True if tipo_ord == "2" else False
            dados_ordenados = logica.ordenar_por_nota_bubble(bombeiros, ascendente=asc)
            interface.mostrar_tabela_bombeiros(dados_ordenados, materias)
        elif op == "5":
            id_rem = interface.ler_inteiro("ID do registo de avaliação a remover: ")
            if logica.remover_avaliacao(bombeiros, id_rem):
                print("Avaliação eliminada com sucesso.")
            else:
                print("Registo não encontrado.")
        elif op == "0":
            break

def main():
    interface.limpar_ecra()
    testes.executar_testes_sistema()
    
    materias = ficheiros.carregar_materias()
    bombeiros = ficheiros.carregar_bombeiros()
    
    while True:
        interface.menu_principal()
        opcao = input("Selecione o módulo de trabalho: ").strip()
        
        if opcao == "1":
            fluxo_materias(materias, bombeiros)
        elif opcao == "2":
            fluxo_bombeiros(bombeiros, materias)
        elif opcao == "3":
            print("\n" + "="*40)
            print("   PAINEL DE DESEMPENHO OPERACIONAL")
            print("="*40)
            estat = logica.calcular_estatisticas_avancadas(bombeiros)
            if not estat:
                print("Sem dados suficientes para processar análises de rendimento.")
            else:
                print(f" * Total de Ações Formativas Avaliadas : {estat['total_treinos']}")
                print(f" * Média de Classificação da Corporação: {estat['media_global']} / 20 valores")
                print(f" * Operacionais Aptos para Intervenção : {estat['aptos']}")
                print(f" * Operacionais com Classificação Negativa: {estat['nao_aptos']}")
                print(f" * Taxa Global de Sucesso no Treino    : {estat['taxa_sucesso']}%")
                print(f" * Nota Máxima Registada no Corpo Ativo: {estat['melhor_nota']} valores")
            print("="*40)
        elif opcao == "0":
            print("\nA compactar e a guardar os dados operacionais nos arquivos CSV...")
            ficheiros.guardar_tudo(materias, bombeiros)
            print("Sessão encerrada com sucesso. Bom trabalho, operacional!")
            break
        else:
            print("Comando desconhecido. Tente novamente.")

if __name__ == "__main__":
    main()
