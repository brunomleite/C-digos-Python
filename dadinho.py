import random
import os
import emoji

dice = []

rodada = True
jogo = True
while(jogo == True):
    num = int(input(emoji.emojize("Digite o numero de :game_die:: ", use_aliases = True)))
    mao = int(input(emoji.emojize("Digite a quantidade de :game_die: na sua :hand:: ", use_aliases = True)))
    rodada = True
    while(rodada == True):
        for x in range(0, mao):
            dice.append(random.randint(1, 6))

        print(emoji.emojize("\nTotal de :game_die: -> " + str(num) + "\nSua :hand: -> " + str(dice), use_aliases = True))

        lose = int(input(emoji.emojize("Voce perdeu a rodada? (1-sim/resto-não)", use_aliases = True)))

        if lose == 1:
            mao -= 1
            num -= 1
            dice = []
            os.system("clear")

            if ((num > 0) and (mao <= 0)):
                escolha = int(input(emoji.emojize("Voce Perdeu\nNovo jogo? (1-sim/resto-não)", use_aliases = True)))
                if escolha == 1:
                    rodada = False
                    dice = []
                else:
                    rodada = False
                    jogo = False
            if (num == mao):
                escolha = int(input(emoji.emojize("Voce Ganhou\nNovo jogo? (1-sim/resto-não)", use_aliases = True)))
                if escolha == 1:
                    rodada = False
                    dice = []
                else:
                    rodada = False
                    jogo = False
        else:
            num -= 1
            dice = []
            os.system("clear")

            if ((num > 0) and (mao <= 0)):
                escolha = int(input(emoji.emojize("Voce Perdeu\nNovo jogo? (1-sim/resto-não)", use_aliases = True)))
                if escolha == 1:
                    rodada = False
                    dice = []
                else:
                    rodada = False
                    jogo = False
            if (num == mao):
                escolha = int(input(emoji.emojize("Voce Ganhou\nNovo jogo? (1-sim/resto-não)", use_aliases = True)))
                if escolha == 1:
                    rodada = False
                    dice = []
                else:
                    rodada = False
                    jogo = False
