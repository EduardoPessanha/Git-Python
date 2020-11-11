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


# Definindo a função:
def voto(ano):
    """
    -> Recebe o ano de nascimento de uma pessoa
    e analisa a condição de voto de acordo com
    a idade.
    :param ano: ano de nascimento
    :return: idade e status
    Criado por EAMP
    """
    from datetime import datetime
    idade = datetime.now().year - ano
    if idade < 16:
        status = 'NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        status = 'VOTO OPCIONAL'
    else:
        status = 'VOTO OBRIGATÓRIO'
    return idade, status


# Rotina principal:
a = voto(int(input('Em que ano você nasceu? ')))
print(f'Com {a[0]} anos: {a[1]}.')

# # Solução do Gustavo Guanabara:
#
# def voto(ano):
#     from datetime import date
#     atual = date.today().year
#     idade = atual - ano
#     if idade < 16:
#         return print(f'Com {idade} anos: NÃO VOTA.')
#     elif 16 <= idade < 18 or idade > 65:
#         return print(f'Com {idade} anos: VOTO OPCIONAL.')
#     else:
#         return print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
#
#
# nasc = int(input('Em que ano você nasceu? '))
# voto(nasc)
