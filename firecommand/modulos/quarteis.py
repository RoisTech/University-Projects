# modulos/quarteis.py
from config import FICHEIRO_QUARTEIS
from utils.ficheiros import ler_csv, gravar_csv
from utils.validacao import ler_str, ler_distrito

CAMPOS = ["nome", "tipo", "distrito", "latitude", "longitude"]

def inserir_quartel():
    print("\n--- Inserir Quartel ---")
    nome = ler_str("Nome do Quartel: ")
    
    # Validação simples de duplicados
    quarteis = ler_csv(FICHEIRO_QUARTEIS, CAMPOS)
    for q in quarteis:
        if q["nome"].lower() == nome.lower():
            print("Erro: Já existe um quartel com esse nome.")
            return

    print("Tipos: 1 - Voluntários, 2 - Sapadores, 3 - Municipais")
    tipo_op = ler_str("Escolha o tipo (1-3): ")
    tipo = "Voluntários"
    if tipo_op == "2":
        tipo = "Sapadores"
    elif tipo_op == "3":
        tipo = "Municipais"
        
    distrito = ler_distrito()
    
    # Valores geográficos padrão para a consola
    latitude = "39.5"
    longitude = "-8.0"
    
    quarteis.append({
        "nome": nome,
        "tipo": tipo,
        "distrito": distrito,
        "latitude": latitude,
        "longitude": longitude
    })
    
    if gravar_csv(FICHEIRO_QUARTEIS, quarteis, CAMPOS):
        print("Quartel inserido com sucesso!")

def listar_quarteis():
    quarteis = ler_csv(FICHEIRO_QUARTEIS, CAMPOS)
    if not quarteis:
        print("\nNenhum quartel registado.")
        return
        
    print(f"\n{'Nome':<30} | {'Tipo':<15} | {'Distrito':<20}")
    print("-" * 70)
    for q in quarteis:
        print(f"{q['nome']:<30} | {q['tipo']:<15} | {q['distrito']:<20}")

def procurar_quarteis_por_distrito():
    print("\n--- Pesquisar por Distrito ---")
    distrito_alvo = ler_distrito()
    quarteis = ler_csv(FICHEIRO_QUARTEIS, CAMPOS)
    
    filtrados = [q for q in quarteis if q["distrito"].lower() == distrito_alvo.lower()]
    
    if not filtrados:
        print(f"\nNenhum quartel encontrado no distrito de {distrito_alvo}.")
        return
        
    print(f"\nQuartéis em {distrito_alvo}:")
    print(f"{'Nome':<30} | {'Tipo':<15}")
    print("-" * 48)
    for q in filtrados:
        print(f"{q['nome']:<30} | {q['tipo']:<15}")

def editar_quartel():
    print("\n--- Editar Quartel ---")
    nome_alvo = ler_str("Introduza o nome do quartel a editar: ")
    quarteis = ler_csv(FICHEIRO_QUARTEIS, CAMPOS)
    
    encontrado = False
    for q in quarteis:
        if q["nome"].lower() == nome_alvo.lower():
            encontrado = True
            print(f"\nQuartel encontrado: {q['nome']} ({q['tipo']} - {q['distrito']})")
            
            novo_nome = input(f"Novo nome [{q['nome']}]: ").strip()
            if novo_nome:
                q["nome"] = novo_nome
                
            print("Tipos: 1 - Voluntários, 2 - Sapadores, 3 - Municipais")
            novo_tipo_op = input(f"Novo tipo (Enter para manter): ").strip()
            if novo_tipo_op == "1": q["tipo"] = "Voluntários"
            elif novo_tipo_op == "2": q["tipo"] = "Sapadores"
            elif novo_tipo_op == "3": q["tipo"] = "Municipais"
            
            mudar_dist = ler_str("Deseja alterar o distrito? (s/n): ", obrigatorio=False)
            if mudar_dist.lower() == "s":
                q["distrito"] = ler_distrito()
            break
            
    if encontrado:
        gravar_csv(FICHEIRO_QUARTEIS, quarteis, CAMPOS)
        print("Quartel atualizado com sucesso!")
    else:
        print("Quartel não encontrado.")

def remover_quartel():
    print("\n--- Remover Quartel ---")
    nome_alvo = ler_str("Nome do quartel a remover: ")
    quarteis = ler_csv(FICHEIRO_QUARTEIS, CAMPOS)
    
    tamanho_original = len(quarteis)
    quarteis = [q for q in quarteis if q["nome"].lower() != nome_alvo.lower()]
    
    if len(quarteis) < tamanho_original:
        gravar_csv(FICHEIRO_QUARTEIS, quarteis, CAMPOS)
        print("Quartel removido com sucesso!")
    else:
        print("Quartel não encontrado.")