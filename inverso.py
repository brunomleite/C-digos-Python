import emoji

a = int(input(emoji.emojize(":point_right: Digite o valor de A: ", use_aliases = True)))
b = int(input(emoji.emojize(":point_right: Digite o valor de B: ", use_aliases = True)))

for x in range(0, b - 1):
		if (a * x) % b == 1:
			inv_e = x
			print(emoji.emojize("O inverso de " + str(a) + " na base " + str(b) + " é :sunglasses: : "+str(inv_e), use_aliases = True))