#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

print("Determinar se um número é positivo ou negativo")

valor = float(input("Digite um valor"))

if valor>0:
    print(valor," é um número positivo")
elif valor<0:
    print(valor, "é um número negativo")
else:
    print("Número 0")