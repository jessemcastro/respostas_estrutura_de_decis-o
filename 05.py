#Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota_1 = float(input("Digite sua nota parcial 1"))
nota_2 = float(input("Digite sua nota parcial 2"))

media = (nota_1+nota_2)/2


if media == 10:
    print("A média foi ", media, "e o aluno está APROVADO COM DISTINÇÃO")
elif media>= 7.0 and media<10:
    print("A média foi ", media, "e o aluno está APROVADO")
elif media< 7.0:
    print("A média foi ", media, "e o aluno esta REPROVADO")
else:
    print("Notas inválidas")
