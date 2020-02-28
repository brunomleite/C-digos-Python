import emoji

a = int(input(emoji.emojize(":pencil2: Digite o valor de A: ", use_aliases = True)))
b = int(input(emoji.emojize(":pencil2: Digite o valor de B: ", use_aliases = True)))
c = a % b

x = 0
y = 0
cont = 1
while c != 0:
	x = b
	y = c
	c = x % y
	cont += 1

print(emoji.emojize("\n:sunglasses: M.D.C(" + str(a) + "," + str(b)+") = " + str(y), use_aliases = True))
print(emoji.emojize("Em " + str(cont) + " divisões.:heavy_division_sign:", use_aliases = True))