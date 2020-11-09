# **************************** Desafio 101 ************************** #
#                         Funções para votação                        #
# Crie um programa que tenha uma função chamada voto() que vai receber#
# como parâmetro o ano de nascimento de uma pessoa, retornando um     #
# valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e   #
# OBRIGATÓRIO nas eleições.                                           #
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


titulo('Funções para votação')
# ****************************************************************** #
