# *************************** Desafio 092 ***************************** #
#                   Cadastro de Trabalhador em Python                   #
# Crie um programa que leia nome, ano de nascimento e carteira de       #
# trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a    #
# CTPS for diferente de ZERO, o dicionário receberá também o ano de     #
# contratação e o salário. Calcule e acrescente, além da idade, com     #
# quantos anos a pessoa vai se aposentar..                              #
# ********************************************************************* #
from random import randint
from time import sleep
from operator import itemgetter
linha = '++' * 24
linha1 = '\033[1;34m*=\033[m' * 24
título = ' \033[1;3;4;7;33mCadastro de Trabalhador em Python\033[m '
print(f'\n{título:*^64}\n')
print(linha)
# ********************************************************************* #
