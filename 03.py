#Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

print ("Digite: F - para sexo feminino")
print ("Digite: M - para sexo masculino")

sexo = str(input("Digite o sexo"))

if sexo == "F" or sexo == "f":
    print("F - Sexo Feminino")
elif sexo =="M" or sexo == "m":
    print("M - Sexo Masculino")
else:
    ("Sexo inválido")