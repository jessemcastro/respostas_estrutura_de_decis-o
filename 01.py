#Faça um Programa que peça dois números e imprima o maior deles.

numero_1 = float(input("Digite o primeiro numero"))
numero_2 = float(input("Digite o segundo numero"))

if numero_1 > numero_2:
    print("O maior número é", numero_1)
elif numero_1 == numero_2:
    print("Os número são iguais")
else:
    print("O maior número é ", numero_2)