from compras import (
    adicionar_produto,
    calcular_total,
    listar_produtos,
    pesquisar_produto,
    produto_mais_caro,
)
from validacoes import validar_nome, validar_preco, validar_quantidade


def mostrar_menu():

    print("=============================")
    print("   LISTA DE COMPRAS")
    print("=============================")
    print("1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Calcular total da compra")
    print("4 - Pesquisar produto")
    print("5 - Produto mais caro")
    print("0 - Sair")
    print("=============================")
 
 
def main():
  
    while True:
        mostrar_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")

            try:
                quantidade = int(input("Quantidade: "))
                preco = float(input("Preço unitário: "))
            except ValueError:

                print("Dados inválidos.")
                continue  

            if validar_nome(nome) and validar_quantidade(quantidade) and validar_preco(preco):
                adicionar_produto(nome, quantidade, preco)
            else:
                print("Dados inválidos.")

        elif opcao == "2":
            listar_produtos()

        elif opcao == "3":
            total = calcular_total()
            print(f"\nTotal da compra: {total:.2f}€")

        elif opcao == "4":
            nome = input("Nome do produto a pesquisar: ")
            pesquisar_produto(nome)

        elif opcao == "5":
            produto_mais_caro()
 
        elif opcao == "0":
            print("Até logo!")
            break 

        else:
            print("Opção inválida. Tenta novamente.")

if __name__ == "__main__":
    main()