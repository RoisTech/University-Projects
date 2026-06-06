# utils/ficheiros.py
import os
import csv

def garantir_pasta(path):
    """
    Garante que a pasta especificada no caminho existe.
    """
    if path:
        os.makedirs(path, exist_ok=True)

def ler_csv(caminho, campos):
    """
    Lê um ficheiro CSV e devolve uma lista de dicionários.
    """
    if not os.path.exists(caminho):
        return []
        
    try:
        with open(caminho, encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f, fieldnames=campos, delimiter=";")
            linhas = list(reader)
        
        # Remover cabeçalho se ele corresponder aos nomes dos campos
        if linhas and linhas[0][campos[0]] == campos[0]:
            linhas = linhas[1:]
        return linhas
    except Exception as erro:
        print(f"Erro ao ler o ficheiro CSV ({caminho}): {erro}")
        return []

def gravar_csv(caminho, registos, campos):
    """
    Escreve uma lista de dicionários num CSV com cabeçalho.
    """
    try:
        garantir_pasta(os.path.dirname(caminho))
        with open(caminho, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=campos, delimiter=";")
            writer.writeheader()
            writer.writerows(registos)
        return True
    except Exception as erro:
        print(f"Erro ao gravar o ficheiro CSV ({caminho}): {erro}")
        return False