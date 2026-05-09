"""
Nome: Sérgio Simões
UC: Programação de Computadores II
Data:23/04/2026
"""

#Exercício 1 – Pedido de Apoio Pedagógico
nome = input("Nome completo: ").strip()
email = input("Email: ").strip()
idade = int(input("Idade: "))
mensagem = input("Mensagem: ").strip()

print(" Tratamento ")
print("Maiúsculas:", nome.upper())
print("Minúsculas:", nome.lower())
print("Nº caracteres:", len(nome))

# Booleanos
maior_idade = idade >= 18
nome_longo = len(nome) > 15
tem_python = "python" in mensagem.lower()

# Urgência
nivel = int(input("Nível de urgência (1-4): "))

if nivel == 1:
    urgencia = "Reduzido"
elif nivel == 2:
    urgencia = "Moderado"
elif nivel == 3:
    urgencia = "Elevado"
elif nivel == 4:
    urgencia = "Muito elevado"
else:
    urgencia = "Inválido"

# Tema
tema = input("Código do tema (A-D): ").upper()

match tema:
    case "A":
        tema_nome = "Estruturas condicionais"
    case "B":
        tema_nome = "Ciclos"
    case "C":
        tema_nome = "Estruturas de dados"
    case "D":
        tema_nome = "Revisão geral"
    case _:
        tema_nome = "Inválido"

# Resumo
print("\n--- RESUMO ---")
print(f"Nome: {nome}")
print(f"Email: {email}")
print(f"Maior de idade: {maior_idade}")
print(f"Nome longo: {nome_longo}")
print(f"Mensagem tem 'python': {tem_python}")
print(f"Urgência: {urgencia}")
print(f"Tema: {tema_nome}")

#xercício 2 – Rotina de Estudo
dias = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")
horas = []

i = 0
while i < len(dias):
    h = float(input(f"Horas de estudo em {dias[i]}: "))
    horas.append(h)
    i += 1

total = 0
dias_sem_estudo = 0
dias_2h = 0

for h in horas:
    total += h
    if h == 0:
        dias_sem_estudo += 1
    if h >= 2:
        dias_2h += 1

media = total / len(horas)
maximo = max(horas)

print("\nDias com mais estudo:")
for i in range(len(horas)):
    if horas[i] == maximo:
        print(dias[i])

# Classificação
if total < 5:
    classificacao = "Insuficiente"
elif total <= 9:
    classificacao = "Suficiente"
elif total <= 14:
    classificacao = "Bom"
else:
    classificacao = "Muito bom"

print("\n--- RELATÓRIO ---")
for i in range(len(dias)):
    print(dias[i], ":", horas[i])

print("Total:", total)
print("Média:", media)
print("Dias sem estudo:", dias_sem_estudo)
print("Dias >=2h:", dias_2h)
print("Classificação:", classificacao)


#Exercício 3 – Organização de Materiais
materiais = []

while True:
    item = input("Material (fim para terminar): ")
    if item.lower() == "fim":
        break
    materiais.append(item)

print("\nLista:", materiais)
print("Total:", len(materiais))

if materiais:
    print("Primeiro:", materiais[0])
    print("Último:", materiais[-1])

# Pesquisa
pesquisa = input("Material a procurar: ")
existe = pesquisa in materiais
print("Existe:", existe)

# Conjunto
conjunto = set(materiais)
print("Conjunto:", conjunto)

if len(conjunto) != len(materiais):
    print("Há repetidos")
else:
    print("Sem repetidos")

# Remover
remover = input("Material a remover: ")
if remover in materiais:
    materiais.remove(remover)
else:
    print("Não existe")

# Vogais
vogais = "aeiou"
lista_vogais = []

for m in materiais:
    if m[0].lower() in vogais:
        lista_vogais.append(m)

print("Final:", materiais)
print("Começam por vogal:", lista_vogais)

#Exercício 4 – Preferências Tecnológicas
registos = {}
n = int(input("Quantos registos: "))

for i in range(n):
    nome = input("Nome: ")
    tech = input("Tecnologia: ")
    registos[nome] = tech

print("\nRegistos:")
for k, v in registos.items():
    print(k, "=>", v)

# Menu
op = input("1-Consultar 2-Alterar 3-Remover 4-Mostrar: ")

match op:
    case "1":
        nome = input("Nome: ")
        print(registos.get(nome, "Não encontrado"))
    case "2":
        nome = input("Nome: ")
        if nome in registos:
            registos[nome] = input("Nova tecnologia: ")
    case "3":
        nome = input("Nome: ")
        registos.pop(nome, None)
    case "4":
        for k, v in registos.items():
            print(k, "=>", v)

# Tecnologias únicas
tecnologias = set(registos.values())
print("Tecnologias:", tecnologias)

tem_python = "Python" in tecnologias
print("Tem Python:", tem_python)

# Contagem
contagem = {}
for t in registos.values():
    if t in contagem:
        contagem[t] += 1
    else:
        contagem[t] = 1

print("Contagem:")
for k, v in contagem.items():
    print(k, "=>", v)

#Exercício 5 – Perfil de Aprendizagem    
nome = input("Nome: ")
num = int(input("Nº exercícios resolvidos: "))
dificil = input("Estrutura mais difícil: ")

dominados = []
for i in range(3):
    dominados.append(input("Tema dominado: "))

dificuldades_input = input("Temas em dificuldade (separados por vírgula): ")
partes = dificuldades_input.split(",")

dificuldades = set()
for p in partes:
    dificuldades.add(p.strip().lower())

# Dicionário
perfil = {
    "nome": nome,
    "exercicios": num,
    "dificil": dificil,
    "dominados": dominados,
    "dificuldades": dificuldades
}

print("\nPerfil:")
for k, v in perfil.items():
    print(k, "=>", v)

# Classificação
if num < 5:
    progresso = "Inicial"
elif num <= 9:
    progresso = "Em desenvolvimento"
else:
    progresso = "Consistente"

print("Progresso:", progresso)

# Booleanos
tem_listas = "listas" in dificuldades
tem_dict = "dicionarios" in dificuldades
tem_conj = "conjuntos" in dificuldades

print("Dificuldade em listas:", tem_listas)
print("Dificuldade em dicionários:", tem_dict)
print("Dificuldade em conjuntos:", tem_conj)

# Comparação
repetidos = []
for t in dominados:
    if t in dificuldades:
        repetidos.append(t)

if repetidos:
    print("Temas inconsistentes:", repetidos)
else:
    print("Aprendizagem consistente")

