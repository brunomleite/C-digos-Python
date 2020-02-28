import emoji

x = int(input("Digite o valor da A: "))
y = int(input("Digite o valor de B: "))

div = int(x / y)
mod = int(x % y)

print(emoji.emojize("\n" + str(x) + " div " + str(y) + " = " + str(div) + " :jack_o_lantern:", use_aliases = True))
print(emoji.emojize(str(x) + " mod " + str(y) + " = " + str(mod) + " :ghost:", use_aliases = True))