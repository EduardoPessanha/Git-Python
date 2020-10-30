# ************************** Desafio 088 ***************************** #
#                    Palpites para a Mega Sena                         #
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. #
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 #
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista   #
# composta.                                                            #
# ******************************************************************** #
from random import randint
linha = '++' * 25
linha1 = '\033[1;34m*=\033[m' * 25
título = ' \033[1;35mPalpites para a Mega Sena\033[m '
print(f'\n{título:*^60}\n')
print(linha)
# ******************************************************************* #
palpite = list()
mega = [[], [], [], [], [], []]
quant = 10
for jogo in range(0, quant):
    for lin in range(0, 6):
        # for col in range(0, 6):
        mega[lin] = randint(1, 60)
    mega.sort()
    palpite.append(mega[:])
print(linha1)
for lin in range(0, quant):
    print(f'Jogo {lin + 1}: {palpite[lin]}')
print(linha1)

# video: 32:56
