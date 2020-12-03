# **************************** Desafio 100 ************************** #
#                     Funções para sortear e somar                    #
# Faça um programa que tenha uma lista chamada números e duas funções #
# chamadas sorteia() e somaPar(). A primeira função vai sortear 5     #
# números e vai colocá-los dentro da lista e a segunda função vai     #
# mostrar a soma entre todos os valores pares sorteados pela função   #
# anterior.                                                           #
# ******************************************************************* #
#
from time import sleep


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


titulo('Funções para sortear e somar')


# ****************************************************************** #


def sorteia(lista):     # Sorteia 5 valores aleatórios e coloca em uma lista
    from random import randint
    for n in range(5):
        números.append(randint(0, 10))
    print('Sorteando 5 valores da lista: ', end='', flush=True)
    sleep(.6)
    for valor in números:
        print(valor, end=' ', flush=True)
        sleep(.35)
    print('PRONTO!')


def somapar(v):
    spar = 0
    for n in v:
        if n % 2 == 0:  # número par
            spar += n
    print(f'Somando os valores pares de {v} temos: {spar}')


números = list()
sorteia(números)
somapar(números)
