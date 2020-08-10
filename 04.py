#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input("Digite uma letra para determinar se é uma vogal"))

if letra == "a" or letra =="e" or letra =="i" or letra =="o" or letra=="u":
    print("A letra ",letra," é uma vogal")
else:
    print("A letra ",letra, " é uma consoante")


