# **************************** Desafio 099 ************************* #
#                     Função que descobre o maior                    #
# Faça um programa que tenha uma função chamada maior(), que receba  #
# vários parâmetros com valores inteiros. Seu programa tem que       #
# analisar todos os valores e dizer qual deles é o maior.            #
# ****************************************************************** #
#
# Definindo as funções:
def lin():
    print('+=' * 24)


def lin1():
    print('\033[1;34m*=\033[m' * 26)


def titulo(msg):
    lin()
    texto = f' \033[1;3;4;7;34m{msg}\033[m '
    print(f'\n{texto:*^64}\n')
    lin()
    print()


titulo('Função que descobre o maior')
# ****************************************************************** #
