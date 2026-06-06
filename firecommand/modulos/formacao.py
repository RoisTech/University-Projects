# modulos/formacao.py
import os
from config import FORMACAO_PATH
from utils.validacao import ler_str

def consultar_formacao():
    """Verifica e detalha a estrutura de pastas formativas local."""
    print("\n--- 📚 DIRETÓRIO DE FORMAÇÃO ---")
    if os.path.exists(FORMACAO_PATH):
        print(f"Pasta de formação localizada em: {FORMACAO_PATH}")
        print("\nSubpastas disponíveis para consulta:")
        for item in os.listdir(FORMACAO_PATH):
            full_p = os.path.join(FORMACAO_PATH, item)
            if os.path.isdir(full_p):
                print(f"  - [{item.upper()}] contendo {len(os.listdir(full_p))} ficheiro(s)")
    else:
        print("Aviso: A pasta física de formação não foi detetada no BASE_PATH.")
    
    ler_str("\nPressione Enter para continuar...")