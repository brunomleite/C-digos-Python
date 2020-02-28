import math
#Pegando valores
mensagem = []
mensagem_cod = []
mensagem_decod = []
ajuda = []
n = int(input("Digite o valor de N: "))
e = int(input("Digite o valor de E: "))
inv_e = 0
p = 0
q = 0
phi = 0
x = e
primos = list(range(2,n))
#descobrindo os primos de 2 - n
for i in range (2,int(math.sqrt(n) + 1)):
	if i in primos:
		for j in range(i**2, n , i):
			if j in primos: primos.remove(j)

for x in range (0, len(primos)):
	for y in range (0,len(primos)):
		if primos[x] * primos[y] == n:
			p = primos[x]
			q = primos[y]
		if p == 0 and q == 0:
			p = 1
			q = n
phi = ((p - 1) * (q - 1))
print("\np = " + str(p) + ", q = " + str(q))
print("\nphi(n) = " + str(phi))
y = phi
#checando se tem inverso
#euclides
resto = e % phi

if resto != 1:
	while resto != 1:
		x = y
		y = resto
		resto = x % y
if resto == 1:
#descobrindo o inverso de n no grupo de phi
	for x in range(0, phi - 1):
		if (e * x) % phi == 1:
			inv_e = x
			print("\nO inverso de (" + str(e) + ") na base (" + str(phi) + ") é: "+str(inv_e) + "\n")
elif resto != 1 :
	print(str(e) + " não possui inverso em " + str(phi))
#mensagem
coisa = str(input("Digite a mensagem a ser codificada: "))
for x in range (0,len(coisa)):
	mensagem.append(ord(coisa[x]))
for x in range (0,len(mensagem)):
	codzin = pow(mensagem[x],e) % n
	mensagem_cod.append(codzin)
	ajuda.append(codzin)
for x in range (0,len(ajuda)):
	mensagem_cod[x] = chr(mensagem_cod[x])
print("\nMensagem Codificada -> " + str(mensagem_cod) + "\n")

for x in range(0,len(ajuda)):
	dedcodzin = pow(ajuda[x],inv_e) % n
	mensagem_decod.append(dedcodzin)
print("Mensagem na tabela ASCII -> " + str(mensagem_decod) + "\n")
for x in range(0,len(ajuda)):
	mensagem_decod[x] = chr(mensagem_decod[x])
print("Mensagem Decodificada -> " + str(mensagem_decod) + "\n")