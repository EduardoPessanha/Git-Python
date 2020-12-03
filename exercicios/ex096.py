# **************************** Desafio 096 ************************* #
#                       Função que calcula área                      #
# Faça um programa que tenha uma função chamada área(), que receba   #
# as dimensões de um terreno retangular (largura e comprimento) e    #
# mostre a área do terreno.                                          #
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


def area(larg, comp): # Calcula a área
    s = larg * comp
    print(f'A área do terreno é igual a {s:.2f}m²')


# ****************************************************************** #
# Rotina principal
titulo('Função que calcula área')
# larg = float(input("Qual a largura do terreno? "))
# comp = float(input('Qual o comprimento do terreno? '))
area(float(input("Qual a largura do terreno? ")), float(input('Qual o comprimento do terreno? ')))
lin1()
