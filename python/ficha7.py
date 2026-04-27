#Exercicio 1-Validação de Inscricão

nome = input("Introduza o nome completo: ").strip().capitalize()
idade = int(input("Introduza a idade: "))
email = input("Introduza o email: ").strip().lower()
tipo_inscricao = input("Introduza o tipo de inscrição: ").strip().lower()
valor_pago = float(input("Introduza o valor pago (€): "))

maiorIdade = idade >= 18
if valor_pago == 0:
  classificacao_pagamento = "Gratuita"
elif valor_pago >0 and valor_pago < 10:
  classificacao_pagamento = "reduzida"
elif valor_pago >= 10:
  classificacao_pagamento = "normal"
  

 
   