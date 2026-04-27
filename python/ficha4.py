"""
Nome: Sérgio Simões
UC: Programação de Computadores II
Data:19/03/2026
"""

#Exercício 1 – Tratamento de Nome
nome = input("Introduza o seu nome completo: ").strip()

print("Maiúsculas:", nome.upper())
print("Minúsculas:", nome.lower())
print("Número de caracteres:", len(nome))

nome_longo = len(nome) > 15
print("Nome longo:", nome_longo)


#Exercício 2 – Maior de IdadecMSFPkefpwe
idade = int(input("Introduza a sua idade: "))

if idade >= 18:
    print("É maior de idade.")
else:
    print("É menor de idade.")


 #Exercício 3 – Classificação de Nota
nota = float(input("Introduza a nota (0 a 20): "))

if nota >= 18:
    print("Excelente")
elif nota >= 14:
    print("Bom")
elif nota >= 10:
    print("Suficiente")
else:
    print("Insuficiente")

#xercício 4 – Operadores Lógicos
idade = int(input("Introduza a sua idade: "))

if idade >= 18 and idade <= 25:
    print("Está entre 18 e 25 anos.")
else:
    print("Não está entre 18 e 25 anos.")

resposta = input("Pretende continuar? (s/n): ")

if resposta == "s" or resposta == "S":
    print("Continuar...")
else:
    print("Parar...")

#Exercício 5 – Strings e Decisão
nome = input("Introduza um nome: ").strip()

if nome.lower().startswith("a"):
    print("O nome começa com A.")
else:
    print("O nome não começa com A.")

frase = input("Introduza uma frase: ")

if "python" in frase.lower():
    print("A palavra 'python' está presente.")
else:
    print("A palavra 'python' não está presente.")

#Exercício 6 – Validação de Comando
comando = input("Introduza um comando: ").strip().lower()

if comando == "iniciar":
    print("Sistema iniciado.")
elif comando == "parar":
    print("Sistema parado.")
elif comando == "ajuda":
    print("Ajuda disponível.")
else:
    print("Comando inválido.")


#Exercício 7 – Match-Case
opcao = input("Escolha uma opção (1-Consultar, 2-Inserir, 3-Sair): ")

match opcao:
    case "1":
        print("Consultar...")
    case "2":
        print("Inserir...")
    case "3":
        print("Sair...")
    case _:
        print("Opção inválida.")

#Exercício 8 – Positivo, Negativo ou Zero
num = int(input("Introduza um número inteiro: "))

# Positivo / Negativo / Zero
if num > 0:
    tipo = "positivo"
elif num < 0:
    tipo = "negativo"
else:
    tipo = "zero"

# Par ou ímpar
if num % 2 == 0:
    paridade = "par"
else:
    paridade = "ímpar"

print(f"O número é {tipo} e {paridade}.")

