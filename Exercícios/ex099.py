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
def maior(*valor):
    from time import sleep
    n = 0
    lin1()
    # Analisando qual o maior valor passado
    for c in valor:     # para cada item em valor:
        if c == 0:
            n = c
        elif c >= n:
            n = c
    # Exibindo o resultado da função:
    print('Analisando os valores passados ...')
    for v in valor:
        print(f'{v}', end=' ', flush=True)
        sleep(.5)
    print(f'Foram informados {len(valor)} valores ao todo.')
    print(f'O maior valor informado foi {n}.')


# Rotina principal
maior(5, 7, 9, 4, 2, 1)
maior(23, 567, 8, 1234, 20)
maior(-5, -6, 0, -12)
maior(1, 2, 4, 7, 9, 3)
maior(1)
maior()
