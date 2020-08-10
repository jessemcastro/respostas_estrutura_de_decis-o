#Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!",
# conforme o caso.

print ("Digite: M - para matutino")
print ("Digite: V - para vespertino")
print ("Digite: N - para noturno")

turno = str(input("Digite o turno"))

if turno == "M" or turno == "m":
    print("M - turno matutino")
elif turno == "V" or turno == "v":
    print("V - turno vespertino")
elif turno == "N" or turno == "n":
    print("N - turno noturno")
else:
    ("Turno Inválido")