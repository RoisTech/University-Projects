# Exercicio 1 = Sintaxe e Comentarios

"""
Nome: Sérgio Simões
UC: Programação de Computadores II
Data:19/03/2026
"""

print("A iniciar a ficha de exercicios")

# Exercicio 2 = Variaveis e Tipos
# Variaveis
nome_aluno = " Sérgio Simões"
idade = 53
nota_esperada = 16.5
inscrito_exame = True

"Mostrar tipo de cada variavel"
print(type(nome_aluno))
print(type(idade))
print(type(nota_esperada))
print(type(inscrito_exame))

# Exercicio 3 = Input e Apresentação
# Pedir dados ao utilizador
primeiro_nome = input("primeiro_nome: ")
apelido = input("apelido: ")
curso = input("curso: ")
idade = int(input("idade: "))

# Criar apresentação
apresentacao = (
    "Olá, eu sou "
    + primeiro_nome
    + " "
    + apelido
    + ", tenho "
    + str(idade)
    + " anos e estudo "
    + curso
    + "."
)


# Mostrar o Resultado
print(apresentacao)

# exercicio 4 = Conversão de Tipos
# Ler Numeros
num1 = int(input("digite o primeiro numero: "))
num2 = int(input("digite segundo numero: "))

# Soma
total = num1 + num2

# Mostra o Resultado
print("resultado da soma é: ", total)


# Exercicio 5 = Booleanos
limite_faltas = 5

faltas = int(input("numero de faltas: "))

# verificacao
situacao_regular = faltas <= limite_faltas

print(situacao_regular)

# Exercicio 6 = Area do Triangulo
# Ler Valores
base = float(input("digite a base do triangulo: "))
altura = float(input("digite a altura do triangulo: "))

# Calcular Area
area = (base * altura) / 2

# Mostrar Resultado
print("a area do triangulo é: ", area)
