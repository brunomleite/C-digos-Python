import emoji

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
n = int(input("Digite o valor de N: "))

cong1 = int(a % n)
cong2 = int(b % n)

print(emoji.emojize("\n" + str(a) + " ≡ " + str(b) + " (mod " + str(n) +")", use_aliases = True))
print(str(n) + " | (" + str(a) + " - " + str(b) + ")\n")

if cong1 == cong2:
	print(emoji.emojize(str(a) + " mod " + str(n) + " = " + str(b) + " mod " + str(n) + " :sunglasses:", use_aliases = True))
	print(emoji.emojize(str(cong1) + " = " + str(cong2) + " :joy:", use_aliases = True))
else:
	print(emoji.emojize(str(a) + " mod " + str(n) + " ≠ " + str(b) + " mod " + str(n) + " :dizzy_face:", use_aliases = True))
	print(emoji.emojize("Os valores não são congruentes :rage: :no_entry_sign:", use_aliases = True))