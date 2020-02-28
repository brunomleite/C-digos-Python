import emoji

a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
x = 0
y = 0
cont = 0
c = (a % b)

ajuda1 = a * (-1)
ajuda2 = b * (-1)

while c != 0:
	x = b
	y = c
	c = (x % y)
	cont = cont + 1

print(emoji.emojize("\n:sunglasses: M.D.C(" + str(a) + "," + str(b)+") = " + str(y), use_aliases = True))
print(emoji.emojize("Em " + str(cont) + " divisões.:heavy_division_sign:\n", use_aliases = True))

for ajuda1 in range (int(a * -1), int(a + 1)):
	for ajuda2 in range(0, int(a - 1)):
		if ((a * ajuda1) + (b * ajuda2)) == y:
			print(emoji.emojize(str(a) + "(" + str(ajuda1) + ") + " + str(b) + "(" + str(ajuda2) + ") = " + str(y) + " :see_no_evil:", use_aliases = True))