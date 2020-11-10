# **************************** Desafio 100 ************************** #
#                     Funções para sortear e somar                    #
# Faça um programa que tenha uma lista chamada números e duas funções #
# chamadas sorteia() e somaPar(). A primeira função vai sortear 5     #
# números e vai colocá-los dentro da lista e a segunda função vai     #
# mostrar a soma entre todos os valores pares sorteados pela função   #
# anterior.                                                           #
# ******************************************************************* #
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


titulo('Funções para sortear e somar')
# ****************************************************************** #
def sorteia():
    from random import randint
    sorteado = list()
    for n in range(5):
        sorteado.append(randint(0, 10))
    print('Sorteando 5 valores da lista: ', end='')
    for v in sorteado:
        print(v, end=' ')
    print('PRONTO!')
    somapar(sorteado)


def somapar(*v):
    sp = 0
    for i in v:
        for n in i:
            if n % 2 == 0:      # número par
                sp += n
    print(sp)



sorteia() 


