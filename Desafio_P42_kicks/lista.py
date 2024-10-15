'''Não foi usado estruturas de repetição como pedido'''


print("Olá! Seja Bem Vindo(a) a lista de exercícios, por gentileza digite o número do desafio desejado:")
rsp = input("\n1) Faça um programa em que o usuário digita dois valores e o resultado da soma é exibido na tela.\n2) Faça um programa em que o usuário precisa cadastrar nome, idade, telefone e e-mail. Depois mostre os valores digitados na tela.\n3) Faça um programa no qual o usuário precisa cadastrar as informações de dois produto: código, nome, quantidade e preço. No final o programa deve mostrar as informações cadastradas e exibir o valor total das compras.\n4) Faça um programa que converte Grau Celsius em Grau Fahrenheit.\n5) Faça um programa que calcule a área de um quadrado/retângulo.\n")

if rsp == '1':
    som_num1 = input("Digite o primeiro valor: ")
    som_num2 = input("Digite o segundo valor: ")
    soma = int(som_num1) + int(som_num2)
    print(f"{som_num1} + {som_num2} = {soma}")

if rsp == '2':
    nome = input("Digite o seu nome: ")
    idade = input("Digite o sua idade: ")
    telefone = input("Digite o seu telefone: ")
    email = input("Digite o seu e-mail: ")
    print(f"Os dados passados foram\n Nome: {nome}\n Idade: {idade}\n Telefone: {telefone}\n E-mail: {email}")

if rsp == '3':
    codigo1 = input("Digite o código do primeiro produto: ")
    nome1 = input("Digite o nome do primeiro produto: ")
    quantidade1 = input("Digite a quantidade: ")
    preço1 = input("Digite o preço: ")
    print("Ok! Agora vamos para o segundo")
    codigo2 = input("Digite o código do primeiro produto: ")
    nome2 = input("Digite o nome do primeiro produto: ")
    quantidade2 = input("Digite a quantidade: ")
    preço2 = input("Digite o preço: ")
    print(f"Os produtos cadastrados foram\n\n\n Nome: {nome1}\n Cógido: {codigo1}\n Quantidade: {quantidade1}\n Preço: {preço1}\n\n Nome: {nome2}\n Cógido: {codigo2}\n Quantidade: {quantidade2}\n Preço: {preço2}")

if rsp == '4':
    celsius = int(input("Digite o valor em celsius: "))
    resultado =  (celsius*1.8)+32
    print(f"A conversão de {celsius}º para Fahrenheit = {resultado}")

if rsp == '5':
    larg = int(input("Digite a altura: "))
    alt = int(input("Digite a largura: "))
    area  = larg*alt
    print(f"A área do seu quadrado/retângulo de altura {alt}  largura {larg} deu {area}m²")
