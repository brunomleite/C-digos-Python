import time
import os
import emoji

def subtrai_a(x, y):
	print(emoji.emojize("subtrai_:a:: (" + str(x) + "-1, " + str(y)+ ")", use_aliases = True))
	x -= 1
	return x

def adiciona_b(x, y):
	print(emoji.emojize("adiciona_:b:: (" + str(x) + ", " + str(y)+ "+1)", use_aliases = True))
	y += 1
	return y

def a_zero(x):
	if x == 0:
		return True
	else:
		return False


def dorme():
	time.sleep(1)
	print(emoji.emojize(".....", use_aliases = True))
	time.sleep(1)

a = int(input(emoji.emojize("Digite o valor do Registrador A :innocent: : ", use_aliases = True)))
b = 0

escolha = int(input(emoji.emojize("\nEscolha uma opção abaixo :arrow_heading_down: :\n1 - Copia :cake:\n2 - Soma 2 :fries:\n3 - Multiplica 2 :pizza:\n4 - Divide 2 :hamburger:\n->", use_aliases = True)))
os.system("clear")

#Copia
if escolha == 1:
	print(emoji.emojize("Cópia :heavy_check_mark:\n", use_aliases = True))
	while (True):
		print(emoji.emojize(":new_moon_with_face: (" + str(a) + ", " + str(b) + ") :full_moon_with_face:", use_aliases = True))
		dorme()
		print(emoji.emojize("testendo a_zero :sunglasses:", use_aliases = True))
		dorme()
		if a == 0:
			print(emoji.emojize(str(a_zero(a)) + " :heart_eyes:", use_aliases = True))
			dorme()
			break
		print(emoji.emojize(str(a_zero(a)) + " :cold_sweat:", use_aliases = True))
		dorme()
		a = subtrai_a(a, b)
		dorme()
		b = adiciona_b(a, b)
		dorme()

#Soma
if escolha == 2:
	print(emoji.emojize("Soma 2 :heavy_plus_sign:\n", use_aliases = True))
	while(True):
		print(emoji.emojize(":new_moon_with_face: (" + str(a) + ", " + str(b) + ") :full_moon_with_face:", use_aliases = True))
		dorme()
		print(emoji.emojize("testendo a_zero :sunglasses:", use_aliases = True))
		dorme()
		if a == 0:
			print(emoji.emojize(str(a_zero(a)) + " :heart_eyes:", use_aliases = True))
			dorme()
			b = adiciona_b(a, b)
			dorme()
			b = adiciona_b(a, b)
			dorme()
			break
		print(emoji.emojize(str(a_zero(a)) + " :cold_sweat:", use_aliases = True))
		dorme()
		a = subtrai_a(a, b)
		dorme()
		b = adiciona_b(a, b)
		dorme()

#Multiplicação
if escolha == 3:
	print(emoji.emojize("Multiplicação 2 :heavy_multiplication_x:\n", use_aliases = True))
	while(True):
		print(emoji.emojize(":new_moon_with_face: (" + str(a) + ", " + str(b) + ") :full_moon_with_face:", use_aliases = True))
		dorme()
		print(emoji.emojize("testendo a_zero :sunglasses:", use_aliases = True))
		dorme()
		if a == 0:
			print(emoji.emojize(str(a_zero(a)) + " :heart_eyes:", use_aliases = True))
			dorme()
			break
		print(emoji.emojize(str(a_zero(a)) + " :cold_sweat:", use_aliases = True))
		dorme()
		a = subtrai_a(a, b)
		dorme()
		b = adiciona_b(a, b)
		dorme()
		b = adiciona_b(a, b)
		dorme()

#Divisão
if escolha == 4:
	print(emoji.emojize("Divisão 2 :heavy_division_sign:\n", use_aliases = True))
	while(True):
		print(emoji.emojize(":new_moon_with_face: (" + str(a) + ", " + str(b) + ") :full_moon_with_face:", use_aliases = True))
		dorme()
		print(emoji.emojize("testendo a_zero :sunglasses:", use_aliases = True))
		dorme()
		if a == 0:
			print(emoji.emojize(str(a_zero(a)) + " :heart_eyes:", use_aliases = True))
			dorme()
			break
		print(emoji.emojize(str(a_zero(a)) + " :cold_sweat:", use_aliases = True))
		dorme()
		a = subtrai_a(a, b)
		dorme()
		if a == 0:
			pass
		else:
			print(emoji.emojize("testendo a_zero :sunglasses:", use_aliases = True))
			dorme()
			print(emoji.emojize(str(a_zero(a)) + " :cold_sweat:", use_aliases = True))
			dorme()
			a = subtrai_a(a, b)
			dorme()
			b = adiciona_b(a, b)
			dorme()

print(emoji.emojize("Resultado :muscle: : (" + str(a) + ", " + str(b) + ")", use_aliases = True))