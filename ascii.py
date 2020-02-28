import emoji
import math

ajuda = []
ajuda2 = []
mensagem = str(input(emoji.emojize(":sunglasses: Digite um texto :fire:: ", use_aliases = True)))

print(emoji.emojize("Normal:fries: / ASCII:cake:", use_aliases = True))
for i in range(0, len(mensagem)):
	ajuda.append(ord(mensagem[i]))

for i in range(0, len(mensagem)):
	ajuda2.extend(chr(ajuda[i]))

for i in range(0, len(mensagem)):
	print(str(ajuda2[i]) + " = " + str(ajuda[i]))