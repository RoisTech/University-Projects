# modulos/ocorrencias.py
from config import FICHEIRO_OCORRENCIAS
from utils.ficheiros import ler_csv, gravar_csv
from utils.validacao import ler_str

# Sincronizado com os campos definidos no ficheiro anterior: id, descricao, local localizacao, estado
CAMPOS = ["id", "descricao", "local localizacao", "estado"]

def inserir_ocorrência_manual(id_ocorrencia, descricao, localizacao, estado):
    """Função utilitária interna para criar registo estruturado."""
    return {
        "id": str(id_ocorrencia),
        "descricao": descricao,
        "local localizacao": localizacao,
        "estado": estado
    }

def inserir_ocorrencia():
    print("\n--- Inserir Ocorrência ---")
    ocorrencias = ler_csv(FICHEIRO_OCORRENCIAS, CAMPOS)
    
    proximo_id = 1
    if ocorrencias:
        try:
            proximo_id = max(int(o["id"]) for o in ocorrencias) + 1
        except ValueError:
            proximo_id = len(ocorrencias) + 1

    descricao = ler_str("Descrição da Ocorrência (ex: Incêndio Urbano): ")
    localizacao = ler_str("Localização/Distrito/Quartel Responsável: ")
    estado = "Ativa"
    
    nova = inserir_ocorrência_manual(proximo_id, descricao, localizacao, estado)
    ocorrencias.append(nova)
    
    if gravar_csv(FICHEIRO_OCORRENCIAS, ocorrencias, CAMPOS):
        print(f"Ocorrência #{proximo_id} inserida com sucesso!")

def listar_ocorrencias():
    ocorrencias = ler_csv(FICHEIRO_OCORRENCIAS, CAMPOS)
    if not ocorrencias:
        print("\nNenhuma ocorrência registada.")
        return
        
    print(f"\n{'ID':<5} | {'Descrição':<35} | {'Localização':<20} | {'Estado':<10}")
    print("-" * 78)
    for o in ocorrencias:
        print(f"{o['id']:<5} | {o['descricao']:<35} | {o['local localizacao']:<20} | {o['estado']:<10}")

def editar_ocorrência_campos(o, nova_desc, novo_local, novo_estado):
    """Aplica as alterações nos campos da ocorrência."""
    if nova_desc: o["descricao"] = nova_desc
    if novo_local: o["local localizacao"] = novo_local
    if novo_estado: o["estado"] = novo_estado

def editar_ocorrencia():
    print("\n--- Editar Ocorrência ---")
    id_alvo = ler_str("Introduza o ID da ocorrência a editar: ")
    ocorrencias = ler_csv(FICHEIRO_OCORRENCIAS, CAMPOS)
    
    encontrado = False
    for o in ocorrencias:
        if o["id"] == id_alvo:
            encontrado = True
            print(f"\nEncontrada: {o['descricao']} em {o['local localizacao']} [{o['estado']}]")
            
            nova_desc = input("Nova descrição (Enter para manter): ").strip()
            novo_local = input("Nova localização (Enter para manter): ").strip()
            
            print("Estados possíveis: 1 - Ativa, 2 - Em Curso, 3 - Resolvida")
            op_est = input("Escolha o novo estado (Enter para manter): ").strip()
            novo_estado = ""
            if op_est == "1": novo_estado = "Ativa"
            elif op_est == "2": novo_estado = "Em Curso"
            elif op_est == "3": novo_estado = "Resolvida"
            
            editar_ocorrência_campos(o, nova_desc, novo_local, novo_estado)
            break
            
    if encontrado:
        gravar_csv(FICHEIRO_OCORRENCIAS, ocorrencias, CAMPOS)
        print("Ocorrência atualizada com sucesso!")
    else:
        print("Ocorrência não encontrada.")

def remover_ocorrencia():
    print("\n--- Remover Ocorrência ---")
    id_alvo = ler_str("ID da ocorrência a remover: ")
    ocorrencias = ler_csv(FICHEIRO_OCORRENCIAS, CAMPOS)
    
    tamanho_original = len(ocorrencias)
    ocorrencias = [o for o in ocorrencias if o["id"] != id_alvo]
    
    if len(ocorrencias) < tamanho_original:
        gravar_csv(FICHEIRO_OCORRENCIAS, ocorrencias, CAMPOS)
        print("Ocorrência removida com sucesso!")
    else:
        print("Ocorrência não encontrada.")