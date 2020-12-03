from utilitarios import *
# **************************** Desafio 103 ************************** #
#                           Ficha do Jogador                          #
# Faça um programa que tenha uma função chamada ficha(), que receba   #
# dois parâmetros opcionais: o nome de um jogador e quantos gols ele  #
# marcou. O programa deverá ser capaz de mostrar a ficha do jogador,  #
# mesmo que algum dado não tenha sido informado corretamente.         #
# ******************************************************************* #
#
titulo(' Ficha do Jogador ')
# ******************************************************************* #
# Definindo a função:


def ficha(nome='', gol=0):
    """
    -> Mostra os dados do jogador
    :param nome: (opcional) Nome do jogador
    :param gol: (opcional) Gols marcados pelo jogador no campeonato
    :return: Dados do jogador
    """
    if nome in '':
        nome = '<desconhecido>'
    return print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')


# Rotina principal:
n = str(input("Nome do jogador: ")).title()
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.isnumeric():
    n = ''
ficha(n, gol=g)
