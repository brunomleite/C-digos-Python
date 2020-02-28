import emoji
import time

n = int(input(emoji.emojize("Digite um valor de N, onde N > 0: ", use_aliases = True)))
a = int(input(emoji.emojize("Digite um valor de A: ", use_aliases = True)))
b = int(input(emoji.emojize("Digite um valor de B: ", use_aliases = True)))

menu = int(input(emoji.emojize("(1) - Adição Modular.\n(2) - Subtração Modular.\n(3) - Multiplicação Modular.\n->", use_aliases = True)))

if menu == 1:
	print(emoji.emojize("a :heavy_plus_sign: b = (a + b) mod n\n", use_aliases = True))
	ajuda = a + b
	somam = (a + b) % n

	print(emoji.emojize("(" + str(a) + " + " + str(b) + ") mod " + str(n), use_aliases = True))
	time.sleep(1)
	print(emoji.emojize("\n(" + str(ajuda) + ") mod " + str(n) + " = " + str(somam) + " :heart_eyes:", use_aliases = True))
elif menu == 2:
	print(emoji.emojize("a :heavy_minus_sign: b = (a - b) mod n\n", use_aliases = True))
	ajuda = a - b
	subm = (a - b) % n

	print(emoji.emojize("(" + str(a) + " - " + str(b) + ") mod " + str(n), use_aliases = True))
	time.sleep(1)
	print(emoji.emojize("\n(" + str(ajuda) + ") mod " + str(n) + " = " + str(subm) + " :wink:", use_aliases = True))
elif menu == 3:
	print(emoji.emojize("a :x: b = (a * b) mod n\n", use_aliases = True))
	ajuda = a * b
	multm = (a * b) % n

	print(emoji.emojize("(" + str(a) + " * " + str(b) + ") mod " + str(n), use_aliases = True))
	time.sleep(1)
	print(emoji.emojize("\n(" + str(ajuda) + ") mod " + str(n) + " = " + str(multm) + " :innocent:", use_aliases = True))
else:
	print(emoji.emojize("Opção Inválida", use_aliases = True))