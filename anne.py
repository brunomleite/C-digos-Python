import emoji

escolha = -1

def adiciona_b(x,y):
    y = y + 1
    return y

def subtrai_a(x,y):
    if x != 0:
        x = x - 1
    return x

def a_zero(x,y):
    if x == 0:
        return False
    else:
        return True


while(True):
    try:
        a = int(input(emoji.emojize("\nDigite seu input :sunglasses: : ", use_aliases = True)))
        b = 0
        escolha = int(input("Escolha:\n[0]Copia\n[1]Soma_2\n[2]Multiplica_por_2\n[3]Divide_por_2\n[4]Fim\nR="))
        print("\nINICIO      A: " + str(a) + " B: " + str(b))
    except:
        print("")


    if escolha == 0:
        while(a_zero(a,b)):
            print("a_zero:     " + str(a_zero(a, b)))
            a = subtrai_a(a, b)
            print("subtrai_a:  A: " + str(a) + " B: " + str(b))
            b = adiciona_b(a, b)
            print("adiciona_b: A: " + str(a) + " B: " + str(b))
        else:
            print("a_zero:     " + str(a_zero(a, b)))
        print(emoji.emojize("FIM :blush:", use_aliases = True))

    elif escolha == 1:
        while (a_zero(a, b)):
            print("a_zero:     " + str(a_zero(a, b)))
            a = subtrai_a(a, b)
            print("subtrai_a:  A: " + str(a) + " B: " + str(b))
            b = adiciona_b(a, b)
            print("adiciona_b: A: " + str(a) + " B: " + str(b))
        else:
            print("a_zero:     " + str(a_zero(a, b)))
            b = adiciona_b(a, b)
            print("adiciona_b: A: " + str(a) + " B: " + str(b))
            b = adiciona_b(a, b)
            print("adiciona_b: A: " + str(a) + " B: " + str(b))
        print(emoji.emojize("FIM :blush:", use_aliases = True))

    elif escolha == 2:
        while (a_zero(a, b)):
            print("a_zero:     " + str(a_zero(a, b)))
            a = subtrai_a(a, b)
            print("subtrai_a:  A: " + str(a) + " B: " + str(b))
            b = adiciona_b(a, b)
            print("adiciona_b: A: " + str(a) + " B: " + str(b))
            b = adiciona_b(a, b)
            print("adiciona_b: A: " + str(a) + " B: " + str(b))
        else:
            print("a_zero:     " + str(a_zero(a, b)))
        print(emoji.emojize("FIM :blush:", use_aliases = True))
    elif escolha == 3:
        while (a_zero(a, b)):
            print("a_zero:     " + str(a_zero(a, b)))
            a = subtrai_a(a, b)
            print("subtrai_a:  A: " + str(a) + " B: " + str(b))
            if a_zero(a,b) == False:
                print("a_zero:     " + str(a_zero(a, b)))
                a = subtrai_a(a, b)
                print("subtrai_a:  A: " + str(a) + " B: " + str(b))
                b = adiciona_b(a, b)
                print("adiciona_b: A: " + str(a) + " B: " + str(b))
        else:
            print("a_zero:     " + str(a_zero(a, b)))
        print(emoji.emojize("FIM :blush:", use_aliases = True))
    elif escolha == 4:
        exit()
    else:
        print(emoji.emojize("INPUT INVÁLIDO!:rage: \n", use_aliases = True))
