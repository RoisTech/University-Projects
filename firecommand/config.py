# =====================================================
# FIRECOMMAND - CONFIGURAÇÕES
# =====================================================

import os

# ------------------------------
# Base path do projeto
# ------------------------------

# Diretório onde está este ficheiro (config.py)
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# ------------------------------
# Configuração da base de dados (MySQL - opcional)
# ------------------------------

DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "12345678",
    "database": "firecommand_db",
}

# ------------------------------
# Aplicação / GUI
# ------------------------------

APP_NAME = "FireCommand Pro"

WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900

THEME = "darkly"

# ------------------------------
# Pastas de formação (ppt, pdf, vídeos, etc.)
# ------------------------------

FORMACAO_PATH = os.path.join(BASE_PATH, "formacao")

PPT_PATH = os.path.join(FORMACAO_PATH, "ppt")
PDF_PATH = os.path.join(FORMACAO_PATH, "pdf")
VIDEOS_PATH = os.path.join(FORMACAO_PATH, "videos")
IMAGENS_PATH = os.path.join(FORMACAO_PATH, "imagens")
DOCUMENTOS_PATH = os.path.join(FORMACAO_PATH, "documentos")

# ------------------------------
# Dados (ficheiros CSV) - exigência do enunciado
# ------------------------------

DADOS_DIR = os.path.join(BASE_PATH, "dados")

FICHEIRO_QUARTEIS = os.path.join(DADOS_DIR, "quarteis.csv")
FICHEIRO_OCORRENCIAS = os.path.join(DADOS_DIR, "ocorrencias.csv")

# ------------------------------
# Distritos de Portugal
# ------------------------------

DISTRITOS = [
    "Viana do Castelo", "Braga", "Vila Real", "Bragança",
    "Porto", "Aveiro", "Viseu", "Guarda",
    "Coimbra", "Castelo Branco",
    "Leiria", "Santarém",
    "Lisboa", "Portalegre",
    "Évora", "Setúbal",
    "Beja", "Faro",
]