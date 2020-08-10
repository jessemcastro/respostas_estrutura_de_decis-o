#Faça um programa que pergunte o preço de três produtos e
# informe qual produto você deve comprar, sabendo que a
# decisão é sempre pelo mais barato.

preco_1 = float(input("Digite o primeiro preço "))
preco_2 = float(input("Digite o primeiro preço"))
preco_3 = float(input("Digite o primeiro preço"))


if preco_1<preco_2 and preco_1<preco_3:
    print("O menor preço é ", preco_1, "compre esse produto")

elif preco_2<preco_1 and preco_2<preco_3:
    print("O menor preço é ", preco_2, "compre esse produto")

elif preco_3<preco_1 and preco_3<preco_2:
    print("O menor preço é ", preco_3,"compre esse produto")

else:
    print("Há produtos com preços iguais")
