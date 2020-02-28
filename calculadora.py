import math
import emoji
import os
import time

x = float(input(emoji.emojize(":tophat: Digite o valor do X: ", use_aliases = True)))

menu = 0
while menu != 9:
	print("\nX: " + str(x) + "\n")
	menu = float(input(emoji.emojize("(1) - Soma +\n(2) - Subtração -\n(3) - Multiplicação x\n(4) - Divizão ÷\n(5) - Resto de Divizão %\n(6) - Potenciação x¹\n(7) - Raiz Quadrada √\n(8) - Novo Valor de X\n(9) Sair\n:arrows_counterclockwise: -> ", use_aliases = True)))
	
	os.system("clear")
	print("\nX: " + str(x) + "\n")
	if menu == 1:
		print(emoji.emojize("(1) Soma\n:new_moon_with_face: x + y = z", use_aliases = True))
		y = float(input("Digite o valor do Y: "))
		z = x + y
		print(emoji.emojize(str(x) + " + " + str(y) + " = " + str(z) + " :full_moon_with_face:", use_aliases = True))
		x = z
	elif menu == 2:
		print(emoji.emojize("(2) Subtração\n:new_moon_with_face: x - y = z", use_aliases = True))
		y = float(input("Digite o valor do Y: "))
		z = x - y
		print(emoji.emojize(str(x) + " - " + str(y) + " = " + str(z) + " :full_moon_with_face:", use_aliases = True))
		x = z
	elif menu == 3:
		print(emoji.emojize("(3) Multiplicação\n:new_moon_with_face: x * y = z", use_aliases = True))
		y = float(input("Digite o valor do Y: "))
		z = x * y
		print(emoji.emojize(str(x) + " * " + str(y) + " = " + str(z) + " :full_moon_with_face:", use_aliases = True))
		x = z
	elif menu == 4:
		print(emoji.emojize("(4) Divisão\n:new_moon_with_face: x / y = z", use_aliases = True))
		y = float(input("Digite o valor do Y: "))
		z = x / y
		print(emoji.emojize(str(x) + " / " + str(y) + " = " + str(z) + " :full_moon_with_face:", use_aliases = True))
		x = z
	elif menu == 5:
		print(emoji.emojize("(5) Resto de Divisão\n:new_moon_with_face: x % y = z", use_aliases = True))
		y = float(input("Digite o valor do Y: "))
		z = x % y
		print(emoji.emojize(str(x) + " % " + str(y) + " = " + str(z) + " :full_moon_with_face:", use_aliases = True))
		x = z
	elif menu == 6:
		print(emoji.emojize("(6) Potenciação\n:new_moon_with_face: x ** y = z", use_aliases = True))
		y = float(input("Digite o valor do Y: "))
		z = math.pow(x, y)
		print(emoji.emojize(str(x) + " ** " + str(y) + " = " + str(z) + " :full_moon_with_face:", use_aliases = True))
		x = z
	elif menu == 7:
		print(emoji.emojize("(7) Raiz Quadrada\n:new_moon_with_face: √x = z", use_aliases = True))
		z = math.sqrt(x)
		print(emoji.emojize("√" + str(x) + " = " + str(z) + " :full_moon_with_face:", use_aliases = True))
		x = z
	elif menu == 8:
		x = float(input(emoji.emojize("(8) Novo Valor de X\n:tophat: Digite o valor do X: ", use_aliases = True)))
	elif menu == 9:
		pass
	else:
		print(emoji.emojize("Comando inválido. :rage:", use_aliases = True))

	if menu != 9:
		input(emoji.emojize("\n->press any key :blush:", use_aliases = True))
	os.system("clear")