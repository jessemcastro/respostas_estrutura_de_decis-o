#Faça um Programa que leia três números e mostre-os em ordem decrescente.

numero_1 = float(input("Digite o primeiro numero"))
numero_2 = float(input("Digite o primeiro numero"))
numero_3 = float(input("Digite o primeiro numero"))

if numero_1>numero_2 and numero_1>numero_3 and numero_2>numero_3:
    print("Em ordem ",numero_1," - ",numero_2, " - ", numero_3)

elif numero_1>numero_2 and numero_1>numero_3 and numero_3>numero_2:
    print("Em ordem ",numero_1," - ",numero_3, " - ", numero_2)

if numero_2 > numero_1 and numero_2 > numero_3 and numero_1 > numero_3:
    print("Em ordem ", numero_2, " - ", numero_1, " - ", numero_3)

elif numero_2 > numero_1 and numero_2 > numero_3 and numero_3 > numero_1:
    print("Em ordem ", numero_2, " - ", numero_3, " - ", numero_1)

if numero_3 > numero_1 and numero_3 > numero_2 and numero_1 > numero_2:
    print("Em ordem ", numero_3, " - ", numero_1, " - ", numero_2)

elif numero_3 > numero_1 and numero_3 > numero_2 and numero_2 > numero_1:
    print("Em ordem ", numero_3, " - ", numero_2, " - ", numero_1)