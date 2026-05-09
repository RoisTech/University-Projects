"""
Nome: Sérgio Simões
UC: Programação de Computadores II
Data:19/03/2026
"""

#Exercício 1 – While + For (Contagem e Soma)
n = int(input("Introduza um número inteiro positivo: "))

# While (contagem)23
i = 1
while i <= n:
    print(i)
    i += 1

# For (soma)
soma = 0
for i in range(1, n + 1):
    soma += i

print("Soma total:", soma)

#Exercício 2 – Análise de Frase
frase = input("Introduza uma frase: ")

vogais = "aeiou"
num_vogais = 0
num_espacos = 0

for c in frase:
    if c.lower() in vogais:
        num_vogais += 1
    if c == " ":
        num_espacos += 1

print("Total caracteres:", len(frase))
print("Vogais:", num_vogais)
print("Espaços:", num_espacos)

#Exercício 3 – Manipulação de Lista
lista = []

for i in range(5):
    num = int(input("Introduza um número: "))
    lista.append(num)

print("Lista:", lista)
print("Primeiro:", lista[0])
print("Último:", lista[-1])
print("Índice 1 a 3:", lista[1:4])

for valor in lista:
    print(valor)

novo = int(input("Novo número: "))
if novo in lista:
    print("Pertence à lista.")
else:
    print("Não pertence à lista.")

lista.append(novo)

lista[1] = 0

remover = int(input("Valor a remover: "))
if remover in lista:
    lista.remove(remover)

print("Lista final:", lista)

#Exercício 4 – Lista de Compras (While)
compras = []

while True:
    item = input("Produto (ou 'fim'): ")
    if item.lower() == "fim":
        break
    compras.append(item)

print("Total produtos:", len(compras))
print("Lista:", compras)

if compras:
    print("Primeiro:", compras[0])
    print("Último:", compras[-1])

#Exercício 5 – Dias da Semana (Tupla)
dias = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")

num = int(input("Introduza um número (1-7): "))

if 1 <= num <= 7:
    print("Dia:", dias[num - 1])
else:
    print("Valor inválido.")

#Exercício 6 – Coordenadas (Tupla)
x = int(input("Coordenada X: "))
y = int(input("Coordenada Y: "))

ponto = (x, y)
print("Ponto:", ponto)

if x == 0 and y == 0:
    print("Origem")
elif y == 0:
    print("Eixo X")
elif x == 0:
    print("Eixo Y")
else:
    print("Posição geral")

#Exercício 7 – Pares e Ímpares
lista = []

for i in range(8):
    num = int(input("Introduza um número: "))
    lista.append(num)

pares = []
impares = []

for num in lista:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Lista original:", lista)
print("Pares:", pares)
print("Ímpares:", impares)
print("Quantidade pares:", len(pares))
print("Quantidade ímpares:", len(impares))

