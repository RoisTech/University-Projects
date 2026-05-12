lista_produtos = []
 
def adicionar_produto(nome, quantidade, preco):

    produto = {
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }
    lista_produtos.append(produto)
    print(f"Produto '{nome}' adicionado com sucesso!")
 
 
def listar_produtos():

    if len(lista_produtos) == 0:
        print("A lista de compras está vazia.")
        return  
 
    print("\n=== Lista de Produtos ===")
 
    for produto in lista_produtos:
        subtotal = produto["quantidade"] * produto["preco"]

        print(f"Nome: {produto['nome']}")
        print(f"  Quantidade: {produto['quantidade']}")
        print(f"  Preço unitário: {produto['preco']:.2f}€")
        print(f"  Subtotal: {subtotal:.2f}€")
        print("-" * 25)
 
 
def calcular_total():
   
    total = 0
 

    for produto in lista_produtos:
        subtotal = produto["quantidade"] * produto["preco"]
        total = total + subtotal

    return total
 
 
def pesquisar_produto(nome_pesquisa):

    encontrado = False 
 
    for produto in lista_produtos:
        if produto["nome"].lower() == nome_pesquisa.lower():
            print("Produto encontrado!")
            print(f"Nome: {produto['nome']}")
            print(f"Quantidade: {produto['quantidade']}")
            print(f"Preço: {produto['preco']:.2f}€")
            encontrado = True
            break  
 
    if not encontrado:
        print(f"Produto '{nome_pesquisa}' não encontrado na lista.")
 
 
def produto_mais_caro():

    if len(lista_produtos) == 0:
        print("A lista está vazia.")
        return

    mais_caro = lista_produtos[0]
 
    for produto in lista_produtos:
        if produto["preco"] > mais_caro["preco"]:
            mais_caro = produto 
 
    print(f"Produto mais caro: {mais_caro['nome']} — {mais_caro['preco']:.2f}€")
 
 
if __name__ == "__main__":
    print("=== Testes de compras.py ===")
 
    adicionar_produto("Arroz", 2, 1.50)
    adicionar_produto("Leite", 3, 0.89)
    adicionar_produto("Pão", 1, 1.20)
 
    listar_produtos()
 
    total = calcular_total()
    print(f"Total da compra: {total:.2f}€")
 
    pesquisar_produto("Leite")
    pesquisar_produto("Manteiga")
 
    produto_mais_caro()