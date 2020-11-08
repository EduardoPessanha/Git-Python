# **************************** Desafio 096 ************************* #
#                           Um print especial                        #
# Faça um programa que tenha uma função chamada escreva(), que       #
# receba um texto qualquer como parâmetro e mostre uma mensagem com  #
# tamanho adaptável.                                                 #
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
# ****************************************************************** #


# Rotina principal
titulo('Um print especial')
