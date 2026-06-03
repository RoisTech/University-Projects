import csv

def carregar_materias(nome_ficheiro="materias_formativas.csv"):
    lista = []
    try:
        with open(nome_ficheiro, mode='r', encoding='utf-8') as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                linha['horas'] = int(linha['horas'])
                lista.append(linha)
    except FileNotFoundError:
        return [
            {'cod': 'MOD01', 'nome': 'Incêndios Urbanos', 'horas': 25, 'tipo': 'Prática'},
            {'cod': 'MOD02', 'nome': 'Desencarceramento', 'horas': 30, 'tipo': 'Prática'},
            {'cod': 'MOD03', 'nome': 'Suporte Básico de Vida', 'horas': 50, 'tipo': 'Teórico-Prática'}
        ]
    return lista

def carregar_bombeiros(nome_ficheiro="historico_formacao.csv"):
    lista = []
    try:
        with open(nome_ficheiro, mode='r', encoding='utf-8') as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                linha['id'] = int(linha['id'])
                linha['nota'] = float(linha['nota'])
                lista.append(linha)
    except FileNotFoundError:
        return []
    return lista

def guardar_tudo(lista_materias, lista_bombeiros):
    campos_mat = ['cod', 'nome', 'horas', 'tipo']
    with open("materias_formativas.csv", mode='w', encoding='utf-8', newline='') as f:
        escritor = csv.DictWriter(f, fieldnames=campos_mat)
        escritor.writeheader()
        escritor.writerows(lista_materias)
        
    campos_bom = ['id', 'nome', 'cod_materia', 'nota']
    with open("historico_formacao.csv", mode='w', encoding='utf-8', newline='') as f:
        escritor = csv.DictWriter(f, fieldnames=campos_bom)
        escritor.writeheader()
        escritor.writerows(lista_bombeiros)
