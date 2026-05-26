# modulos/ocorrencias.py
from config import FICHEIRO_OCORRENCIAS
from utils.ficheiros import ler_csv, gravar_csv
from utils.validacao import ler_str, ler_distrito
from modulos.quarteis import carregar_quarteis, listar_quarteis

CAMPOS = ["id", "descricao", "distrito", "quartel_id"]

def carregar_ocorrencias():
    return ler_csv(FICHEIRO_OCORRENCIAS, CAMPOS)

def guardar_ocorrencias(ocorrencias):
    gravar_csv(FICHEIRO_OCORRENCIAS, ocorrencias, CAMPOS)

def gerar_novo_id(ocorrencias):
    """
    Gera novo ID do tipo O1, O2, ...
    """
    if not ocorrencias:
        return "O1"
    nums = [
        int(o["id"][1:])
        for o in ocorrencias
        if o["id"].startswith("O") and o["id"][1:].isdigit()
    ]
    novo = max(nums) + 1 if nums else 1
    return f"O{novo}"

def escolher_quartel():
    """
    Mostra lista de quarteis e devolve o ID escolhido.
    """
    quarteis = carregar_quarteis()
    if not quarteis:
        print("Não existem quarteis. Registe primeiro.")
        return None
    listar_quarteis()
    qid = ler_str("ID do quartel responsável: ")
    if any(q["id"] == qid for q in quarteis):
        return qid
    print("Quartel não encontrado.")
    return None

def inserir_ocorrencia():
    """
    Inserção de nova ocorrência (cumpre 'inserção de registos').
    """
    ocorrencias = carregar_ocorrencias()
    novo_id = gerar_novo_id(ocorrencias)
    print(f"ID da ocorrência: {novo_id}")
    desc = ler_str("Descrição: ")
    distrito = ler_distrito()
    qid = escolher_quartel()
    if qid is None:
        return
    ocorrencias.append({
        "id": novo_id,
        "descricao": desc,
        "distrito": distrito,
        "quartel_id": qid
    })
    guardar_ocorrencias(ocorrencias)
    print("Ocorrência registada.")

def listar_ocorrencias():
    """
    Listagem de ocorrências, ordenadas por distrito.
    """
    ocorrencias = sorted(carregar_ocorrencias(), key=lambda o: o["distrito"])
    if not ocorrencias:
        print("Sem ocorrências.")
        return
    print("\n--- Lista de Ocorrências ---")
    for o in ocorrencias:
        print(f'{o["id"]} - {o["descricao"]} ({o["distrito"]}) -> {o["quartel_id"]}')

def editar_ocorrencia():
    """
    Edição de ocorrência (cumpre 'edição de registos').
    """
    ocorrencias = carregar_ocorrencias()
    if not ocorrencias:
        print("Sem ocorrências.")
        return
    listar_ocorrencias()
    oid = ler_str("ID da ocorrência a editar: ")
    oc = next((o for o in ocorrencias if o["id"] == oid), None)
    if not oc:
        print("Ocorrência não encontrada.")
        return

    nova_desc = input(f"Descrição [{oc['descricao']}]: ").strip()
    print(f"Distrito atual: {oc['distrito']}")
    mudar_distrito = input("Alterar distrito? (s/n): ").strip().lower()
    mudar_quartel = input("Alterar quartel? (s/n): ").strip().lower()

    if nova_desc:
        oc["descricao"] = nova_desc
    if mudar_distrito == "s":
        oc["distrito"] = ler_distrito()
    if mudar_quartel == "s":
        qid = escolher_quartel()
        if qid:
            oc["quartel_id"] = qid

    guardar_ocorrencias(ocorrencias)
    print("Ocorrência atualizada.")

def remover_ocorrencia():
    """
    Remoção de ocorrência (cumpre 'remoção de registos').
    """
    ocorrencias = carregar_ocorrencias()
    if not ocorrencias:
        print("Sem ocorrências.")
        return
    listar_ocorrencias()
    oid = ler_str("ID da ocorrência a remover: ")
    nova_lista = [o for o in ocorrencias if o["id"] != oid]
    if len(nova_lista) == len(ocorrencias):
        print("Ocorrência não encontrada.")
        return
    guardar_ocorrencias(nova_lista)
    print("Ocorrência removida.")