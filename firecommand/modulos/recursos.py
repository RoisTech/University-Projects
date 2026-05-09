from utils.ficheiros import guardar_csv, ler_csv

# Caminho do ficheiro
FICHEIRO = "dados/recursos.csv"

# =========================
# GUARDAR RECURSO (usado na GUI)
# =========================

def guardar_recurso(recurso):
    """
    Guarda um recurso no ficheiro CSV
    recurso = {
        "bombeiros": int,
        "veiculos": int
    }
    """
    guardar_csv(FICHEIRO, recurso)

# =========================
# LISTAR RECURSOS (opcional)
# =========================

def listar_recursos():
    """
    Devolve lista de recursos
    """
    return ler_csv(FICHEIRO)