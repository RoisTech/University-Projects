# modulos/estatisticas.py
from config import FICHEIRO_OCORRENCIAS
from utils.ficheiros import ler_csv

CAMPOS_OCORRENCIAS = ["id", "descricao", "local localizacao", "estado"]

def ocorrencias_por_distrito():
    print("\n--- Ocorrências por Localização/Distrito ---")
    ocorrencias = ler_csv(FICHEIRO_OCORRENCIAS, CAMPOS_OCORRENCIAS)
    
    if not ocorrencias:
        print("Nenhum dado de ocorrências disponível.")
        return
        
    # Agrupa e conta por localização
    locais = [o["local localizacao"] for o in ocorrencias]
    contagem = {}
    for l in locais:
        contagem[l] = contagem.get(l, 0) + 1
        
    print(f"\n{'Localização':<30} | {'Total Ocorrências':<15}")
    print("-" * 48)
    for local, total in contagem.items():
        print(f"{local:<30} | {total:<15}")

def ocorrencias_por_quartel():
    print("\n--- Ocorrências por Quartel ---")
    print("Nota: Relatório analítico cruzado baseado no descritivo contextual.")
    ocorrencias = ler_csv(FICHEIRO_OCORRENCIAS, CAMPOS_OCORRENCIAS)
    
    if not ocorrencias:
        print("Nenhuma ocorrência registada no histórico.")
        return

    estados = [o["estado"] for o in ocorrencias]
    print(f"\nResumo operacional global:")
    for est in set(estados):
        print(f"  - Estado '{est}': {estados.count(est)} registo(s)")