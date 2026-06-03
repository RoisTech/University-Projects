def materia_existe(lista_materias, cod_materia):
    for m in lista_materias:
        if m['cod'].upper() == cod_materia.upper():
            return True
    return False

def obter_nome_materia(lista_materias, cod_materia):
    for m in lista_materias:
        if m['cod'].upper() == cod_materia.upper():
            return m['nome']
    return "Desconhecida"

def inserir_materia(lista_materias, cod, nome, horas, tipo):
    if materia_existe(lista_materias, cod):
        return False, "Erro: Já existe uma matéria com esse código!"
    nova = {
        'cod': cod.upper().strip(),
        'nome': nome.strip(),
        'horas': int(horas),
        'tipo': tipo.strip()
    }
    lista_materias.append(nova)
    return True, "Matéria adicionada com sucesso ao catálogo!"

def editar_materia(lista_materias, cod, novo_nome, novas_horas, novo_tipo):
    for m in lista_materias:
        if m['cod'].upper() == cod.upper():
            m['nome'] = novo_nome.strip()
            m['horas'] = int(novas_horas)
            m['tipo'] = novo_tipo.strip()
            return True
    return False

def remover_materia_e_vinculos(lista_materias, lista_bombeiros, cod_materia):
    removido = False
    for i, m in enumerate(lista_materias):
        if m['cod'].upper() == cod_materia.upper():
            lista_materias.pop(i)
            removido = True
            break
    if removido:
        for i in range(len(lista_bombeiros) - 1, -1, -1):
            if lista_bombeiros[i]['cod_materia'].upper() == cod_materia.upper():
                lista_bombeiros.pop(i)
        return True
    return False

def matricular_e_avaliar(lista_bombeiros, lista_materias, nome, cod_materia, nota):
    if not materia_existe(lista_materias, cod_materia):
        return False, "Erro: Código de matéria inexistente!"
    novo_id = max([b['id'] for b in lista_bombeiros]) + 1 if lista_bombeiros else 1001
    novo_registo = {
        'id': novo_id,
        'nome': nome.strip(),
        'cod_materia': cod_materia.upper().strip(),
        'nota': float(nota)
    }
    lista_bombeiros.append(novo_registo)
    return True, "Avaliação registada com sucesso!"

def remover_avaliacao(lista_bombeiros, id_registo):
    for i, b in enumerate(lista_bombeiros):
        if b['id'] == id_registo:
            lista_bombeiros.pop(i)
            return True
    return False

def pesquisa_linear_bombeiro(lista_bombeiros, termo, criterio="nome"):
    resultados = []
    for b in lista_bombeiros:
        if criterio == "nome" and termo.lower() in b['nome'].lower():
            resultados.append(b)
        elif criterio == "materia" and termo.lower() in b['cod_materia'].lower():
            resultados.append(b)
    return resultados

def ordenar_por_nota_bubble(lista_bombeiros, ascendente=False):
    lista_ordenada = list(lista_bombeiros)
    n = len(lista_ordenada)
    for i in range(n):
        for j in range(0, n - i - 1):
            condicao = (lista_ordenada[j]['nota'] > lista_ordenada[j + 1]['nota']) if ascendente else (lista_ordenada[j]['nota'] < lista_ordenada[j + 1]['nota'])
            if condicao:
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]
    return lista_ordenada

def calcular_estatisticas_avancadas(lista_bombeiros):
    if not lista_bombeiros:
        return {}
    total = len(lista_bombeiros)
    total_notas = sum(b['nota'] for b in lista_bombeiros)
    media_global = total_notas / total
    aptos = sum(1 for b in lista_bombeiros if b['nota'] >= 9.5)
    taxa_sucesso = (aptos / total) * 100
    melhor_nota = max(b['nota'] for b in lista_bombeiros)
    return {
        'total_treinos': total,
        'media_global': round(media_global, 2),
        'aptos': aptos,
        'nao_aptos': total - aptos,
        'taxa_sucesso': round(taxa_sucesso, 1),
        'melhor_nota': melhor_nota
    }
