# ======================================================
# Exercício 1 - Inscrição num Evento
# ======================================================

nome = input("Nome: ")
email = input("Email: ")
idade = int(input("Idade: "))
preco = float(input("Preço da inscrição (€): "))

resposta = input("Inscrição paga? (sim/não): ").lower()
inscricao_paga = resposta == "sim"

print("\n--- RESUMO ---")
print(f"{nome}, {idade} anos, email {email}, inscrição de {preco:.2f}€.")
print(f"Pagamento efetuado: {inscricao_paga}")


# ======================================================
# Exercício 2 - Orçamento de Material Escolar
# ======================================================

artigo = input("\nNome do artigo: ")
preco_unitario = float(input("Preço unitário (€): "))
quantidade = int(input("Quantidade: "))

subtotal = preco_unitario * quantidade
total = subtotal * 1.23  # IVA 23%

print("\n--- ORÇAMENTO ---")
print(f"Artigo: {artigo}")
print(f"Subtotal: {subtotal:.2f}€")
print(f"Total com IVA: {total:.2f}€")


# ======================================================
# Exercício 3 - Estimativa de Consumo de Água
# ======================================================

mes = input("\nMês: ")
consumo_diario = float(input("Consumo diário (litros): "))

consumo_mensal = consumo_diario * 30
consumo_m3 = consumo_mensal / 1000

print("\n--- CONSUMO ---")
print(f"No mês de {mes}, consumiu {consumo_mensal:.2f} litros ({consumo_m3:.2f} m³).")


# ======================================================
# Exercício 4 - Pagamento de Serviço
# ======================================================

servico = input("\nNome do serviço: ")
horas = float(input("Número de horas: "))
valor_hora = float(input("Valor por hora (€): "))

total_receber = horas * valor_hora
maior_100 = total_receber > 100

print("\n--- PAGAMENTO ---")
print(f"Serviço: {servico}")
print(f"Total a receber: {total_receber:.2f}€")
print(f"Valor superior a 100€: {maior_100}")


# ======================================================
# Exercício 5 - Avaliação de uma Unidade Curricular
# ======================================================

uc = input("\nNome da UC: ")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

media = (nota1 + nota2 + nota3) / 3
aprovado = media >= 10

print("\n--- AVALIAÇÃO ---")
print(f"UC: {uc}")
print(f"Média: {media:.2f}")
print(f"Aprovado: {aprovado}")
