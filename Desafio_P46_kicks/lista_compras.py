carrinho = []
sair = False
print("Olá, vamos iniciar as compras?")



def adicionar_produto(nome, preco, quantidade):
    carrinho.append({"nome": nome, "preco": preco, "quantidade": quantidade})
    print(f"{quantidade}x {nome} adicionado ao carrinho.")

def exibir_carrinho():
    if not carrinho:
        print("Carrinho está vazio.")
    else:
        print("Carrinho de Compras:")
        for item in carrinho:
            print(f"{item['quantidade']}x {item['nome']} - R${item['preco'] * item['quantidade']:.2f}")

def calcular_total():
    total = sum(item["preco"] * item["quantidade"] for item in carrinho)
    print(f"\nTotal: R${total:.2f}")


while (sair == False):
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o valor do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    adicionar_produto(nome, preco, quantidade)
    exibir_carrinho()
    rsp = input("Gostaria de adicionar mais um item?\n1-SIM\n2-NÃO\n")
    if rsp == 'NÃO' or rsp == '2':
        print("\n\n\nCompras finalizadas!!\n")
        exibir_carrinho()
        calcular_total()
        sair = True

                                                                                                                      