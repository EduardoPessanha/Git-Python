from utilitarios import *
# **************************** Desafio 101 ************************** #
#                         Funções para votação                        #
# Crie um programa que tenha uma função chamada voto() que vai receber#
# como parâmetro o ano de nascimento de uma pessoa, retornando um     #
# valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e   #
# OBRIGATÓRIO nas eleições.                                           #
# ******************************************************************* #
#
titulo(' Funções para votação ')
# ****************************************************************** #
# Definindo as funções:


def voto(ano):
    """
    Recebe o ano de nascimento de uma pessoa
    e analisa a condição de voto de acordo
    com a idade.
    :param ano: ano de nascimento
    :teste: somente um teste
    :return: idade e status
    """
    from datetime import datetime
    idade = datetime.now().year - ano
    if idade < 16:
        status = 'NÃO VOTA'
    elif 16 <= idade < 18 or idade >= 65:
        status = 'VOTO OPCIONAL'
    else:
        status = 'VOTO OBRIGATÓRIO'
    return idade, status


a = voto(int(input('Em que ano você nasceu? ')))
print(f'Com {a[0]} anos: {a[1]}')
