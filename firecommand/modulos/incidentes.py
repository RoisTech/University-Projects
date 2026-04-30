from utils.ficheiros import guardar_csv, ler_csv

# Caminho do ficheiro
FICHEIRO = "dados/incidentes.csv"

# =========================
# GUARDAR INCIDENTE (GUI)
# =========================

def guardar_incidente(incidente):
    """
    incidente = {
        "tipo": str,
        "gravidade": int,
        "vento": int,
        "temperatura": int,
        "x": int,
        "y": int
    }
    """
    guardar_csv(FICHEIRO, incidente)

# =========================
# LISTAR INCIDENTES
# =========================

def listar_incidentes():
    return ler_csv(FICHEIRO)