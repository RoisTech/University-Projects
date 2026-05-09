import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def get_path(rel_path):
    return os.path.join(BASE_DIR, rel_path)

def guardar_csv(ficheiro, dados):
    caminho = get_path(ficheiro)
    existe = os.path.isfile(caminho)

    with open(caminho, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=dados.keys())
        if not existe:
            writer.writeheader()
        writer.writerow(dados)

def ler_csv(ficheiro):
    caminho = get_path(ficheiro)

    if not os.path.exists(caminho):
        return []

    with open(caminho, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))



















        