#Exercicio 1-Validação de Inscricão

#leitura dos dados do participante
nome = input("Introduza o nome completo: ").strip().capitalize()
idade = int(input("Introduza a idade: "))
email = input("Introduza o email: ").strip().lower()
tipo_inscricao = input("Introduza o tipo de inscrição: ").strip().lower()
valor_pago = float(input("Introduza o valor pago (€): "))

#verificação de maioridade
maiorIdade = idade >= 18

#classificação do pagamento
if valor_pago < 0:
    classificacao = "Valor Inválido"
    print("Erro: O valor pago não pode ser negativo.")
elif valor_pago == 0:
    classificacao = "Gratuita"
elif valor_pago < 10:
    classificacao = "Reduzida"
else:
    classificacao = "Normal"

#guardar dados num dicionário
participante = {
    "nome": nome,
    "idade": idade,
    "email": email,
    "tipo_inscricao": tipo_inscricao,
    "valor_pago": valor_pago,
    "maior_idade": maiorIdade,
    "classificacao_pagamento": classificacao
}

 #apresentacao da sintaxe clara 
print(f"Nome: {participante['nome']}")
print(f"Email: {participante['email']}")
print(f"Maior de idade: {'Sim' if participante['maior_idade'] else 'Não'}")
print(f"Classificação: {participante['classificacao_pagamento']}")
print("---------------------------\n")

#consulta de chave no dicionário#
chave_consulta = input("Introduza a chave que deseja consultar (ex: nome, idade, email, valor_pago): ")
resultado = participante.get(chave_consulta, "Essa chave não existe no registo.")

print(f"Resultado da consulta: {resultado}")



#Exercício 2 – Escolha de Sessão

#criacao da tupla com as sessões disponíveis
sessoes = ("Introdução ao Python","Segurança Informática", "Desenvolvimento Web", "Base de Dados")
print("Sessões disponíveis:")

#percurrer a tupla e apresentar as sessões
for i in range(len(sessoes)):
    print(f"{i+1}. {sessoes[i]}")

#pedir a escolha do utilizador
escolha = (input("Escolha uma sessão (1-4): "))

#tratamento da escolha com match-case e variavel booleana
sessao_escolhida = ""
opcao_valida = True

match escolha:
    case "1":
        sessao_escolhida = sessoes[0]
    case "2":
        sessao_escolhida = sessoes[1]
    case "3":
        sessao_escolhida = sessoes[2]
    case "4":
        sessao_escolhida = sessoes[3]
    case _:
        opcao_valida = False

 #Mensagem de confirmação ou erro
if opcao_valida:
    print(f"Confirmação: Inscrito na sessão '{sessao_escolhida}'.")
else:
    print("Erro: Opção inválida.")

#Mensagem final de resumo
resp_cert = input("Pretende certificado? (s/n): ").strip().lower()
quer_certificado = resp_cert == "s"

print(f"\nSessão: {sessao_escolhida if opcao_valida else 'Nenhuma'}")
print(f"Certificado: {'Sim' if quer_certificado else 'Não'}")