# ************************** Desafio 088 ***************************** #
#                    Palpites para a Mega Sena                         #
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. #
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 #
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista   #
# composta.                                                            #
# ******************************************************************** #
from random import randint
from time import sleep
linha = '++' * 25
linha1 = '\033[1;34m*=\033[m' * 25
título = ' Palpites para a Mega Sena '
print(linha)
print(f'\033[1;34m{título.upper():*^50}\033[m')
print(linha)
# ******************************************************************* #
palpite = list()
mega = [[], [], [], [], [], []]
n = 0
quant = int(input('Quantos jogos você quer sortear? '))
for jogo in range(0, quant):
    for lin in range(0, 6):
        if lin == 0:
            n = randint(1, 60)
        else:
            while True:
                n = randint(1, 60)
                if mega.count(n) != 0:  # número repetido !!!
                    n = 0
                else:
                    break
        mega[lin] = n
    mega.sort()
    palpite.append(mega[:])
print('\033[1;34m*=' * 7, f' SORTEANDO {quant} JOGOS ', '*=' * 7, '\033[m')
for lin in range(0, quant):
    print(f'Jogo {lin + 1}: {palpite[lin]}')
    sleep(1)
print('\033[1;34m*=' * 9, ' BOA SORTE!!', '*=' * 9, '\033[m')

# **************************** SOLUÇÃO DO GUSTAVO GUANABARA ****************************
# jogo = list()
# quant = int(input('Quantos jogos você quer sortear? '))
# print('\033[1;34m*=' * 7, f' SORTEANDO {quant} JOGOS ', '*=' * 7, '\033[m')
# tot = 1
# palpite = list()
# while tot <= quant:
#     cont = 0
#     # ****** Sorteando os números:
#     while True:
#         num = randint(1, 60)
#         if num not in jogo:
#             jogo.append(num)
#             cont += 1
#         if cont >= 6:
#             break
#     # ****************************
#     tot += 1
#     jogo.sort()
#     palpite.append(jogo[:])
#     jogo.clear()
# for i, j in enumerate(palpite):
#     print(f'Jogo n.º {i + 1}: {j}')
#     sleep(1)
# # print('.*' * 19)
# print('\033[1;34m*=' * 9, ' BOA SORTE!!', '*=' * 9, '\033[m')
