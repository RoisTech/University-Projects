# modulos/estatisticas.py

from modulos.ocorrencias import carregar_ocorrencias

def ocorrencias_por_distrito():
    """
    Mostra o número de ocorrências por distrito.
    Cumpre a funcionalidade de resumo/estatística exigida no enunciado.
    """
    ocorrencias = carregar_ocorrencias()
    if not ocorrencias:
        print("Sem ocorrências.")
        return

    contagem = {}
    for o in ocorrencias:
        d = o["distrito"]
        contagem[d] = contagem.get(d, 0) + 1

    print("\n--- Ocorrências por distrito ---")
    for d, n in sorted(contagem.items()):
        print(f"{d}: {n}")

def ocorrencias_por_quartel():
    """
    Mostra o número de ocorrências por quartel (ID do quartel).
    """
    ocorrencias = carregar_ocorrencias()
    if not ocorrencias:
        print("Sem ocorrências.")
        return

    contagem = {}
    for o in ocorrencias:
        qid = o["quartel_id"]
        contagem[qid] = contagem.get(qid, 0) + 1

    print("\n--- Ocorrências por quartel ---")
    for qid, n in sorted(contagem.items()):
        print(f"{qid}: {n}")