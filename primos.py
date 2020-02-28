import math
import emoji

n = int(input(emoji.emojize("Digite o valor de :heavy_multiplication_x: : ", use_aliases = True)))

primos = list(range(2,n))

for i in range (2,int(math.sqrt(n) + 1)):
	if i in primos:
		for j in range(i**2, n , i):
			if j in primos: primos.remove(j)

if primos == []:
	print(emoji.emojize("não tem nenhum numero :speak_no_evil:", use_aliases = True))
else:
	print(emoji.emojize("Lista de primos:see_no_evil:\n" + str(primos) + "\ntotal de: " + str(len(primos)), use_aliases = True))