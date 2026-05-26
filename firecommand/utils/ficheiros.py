# utils/ficheiros.py
import os
import csv

def garantir_pasta(path):
    if path:
        os.makedirs(path, exist_ok=True)

def ler_csv(caminho, campos):
    """
    Lê um ficheiro CSV e devolve uma lista de dicionários.
    """
    if not os.path.exists(caminho):
        return []
    with open(caminho, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, fieldnames=campos, delimiter=";")
        linhas = list(reader)
    # remover cabeçalho se existir
    if linhas and linhas[0][campos[0]] == campos[0]:
        linhas = linhas[1:]
    return linhas

def gravar_csv(caminho, registos, campos):
    """
    Escreve uma lista de dicionários num CSV com cabeçalho.
    """
    garantir_pasta(os.path.dirname(caminho))
    with open(caminho, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=campos, delimiter=";")
        writer.writeheader()
        writer.writerows(registos)