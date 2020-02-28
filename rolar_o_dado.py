import random

nota1 = []
nota2 = []

for x in range(0, 51):
	dado1 = random.randint(0, 10)
	dado2 = random.randint(1, 10)
	ajuda = dado1 / 10

	nota1.append(ajuda)
	nota2.append(dado2)

for x in range(0, 51):
	print(str(nota1[x]) + " x " + str(nota2[x]))