# modulos/quarteis.py
from config import FICHEIRO_QUARTEIS
from utils.ficheiros import ler_csv, gravar_csv
from utils.validacao import ler_str, ler_distrito

CAMPOS = ["id", "nome", "distrito"]

def carregar_quarteis():
    return ler_csv(FICHEIRO_QUARTEIS, CAMPOS)

def guardar_quarteis(quarteis):
    gravar_csv(FICHEIRO_QUARTEIS, quarteis, CAMPOS)

def gerar_novo_id(quarteis):
    """
    Gera um novo ID do tipo 'Q1', 'Q2', ... com base nos IDs existentes.
    """
    if not quarteis:
        return "Q1"
    nums = [
        int(q["id"][1:])
        for q in quarteis
        if q["id"].startswith("Q") and q["id"][1:].isdigit()
    ]
    novo = max(nums) + 1 if nums else 1
    return f"Q{novo}"

def inserir_quartel():
    quarteis = carregar_quarteis()
    novo_id = gerar_novo_id(quarteis)
    print(f"ID atribuído: {novo_id}")
    nome = ler_str("Nome do quartel: ")
    distrito = ler_distrito()
    quarteis.append({"id": novo_id, "nome": nome, "distrito": distrito})
    guardar_quarteis(quarteis)
    print("Quartel inserido com sucesso.")

def listar_quarteis():
    quarteis = sorted(carregar_quarteis(), key=lambda q: q["distrito"])
    if not quarteis:
        print("Sem quarteis registados.")
        return
    print("\n--- Lista de Quartéis ---")
    for q in quarteis:
        print(f'{q["id"]} - {q["nome"]} ({q["distrito"]})')

def procurar_quarteis_por_distrito():
    """
    Pesquisa simples por distrito (critério exigido pelo enunciado).
    """
    distrito = ler_str("Distrito a pesquisar: ")
    quarteis = carregar_quarteis()
    encontrados = [q for q in quarteis if q["distrito"].lower() == distrito.lower()]
    if not encontrados:
        print("Nenhum quartel encontrado nesse distrito.")
        return
    for q in encontrados:
        print(f'{q["id"]} - {q["nome"]}')

def editar_quartel():
    quarteis = carregar_quarteis()
    if not quarteis:
        print("Sem quarteis.")
        return
    listar_quarteis()
    qid = ler_str("ID do quartel a editar: ")
    quartel = next((q for q in quarteis if q["id"] == qid), None)
    if not quartel:
        print("Quartel não encontrado.")
        return

    novo_nome = input(f"Nome [{quartel['nome']}]: ").strip()
    print(f"Distrito atual: {quartel['distrito']}")
    mudar_distrito = input("Alterar distrito? (s/n): ").strip().lower()

    if novo_nome:
        quartel["nome"] = novo_nome
    if mudar_distrito == "s":
        quartel["distrito"] = ler_distrito()

    guardar_quarteis(quarteis)
    print("Quartel atualizado.")

def remover_quartel():
    quarteis = carregar_quarteis()
    if not quarteis:
        print("Sem quarteis.")
        return
    listar_quarteis()
    qid = ler_str("ID do quartel a remover: ")
    nova_lista = [q for q in quarteis if q["id"] != qid]
    if len(nova_lista) == len(quarteis):
        print("Quartel não encontrado.")
        return
    guardar_quarteis(nova_lista)
    print("Quartel removido.")