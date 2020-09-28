# ************************** Desafio 074 ************************** #
#                  Maior e menor valores em Tupla                   #
# Crie um programa que vai gerar cinco números aleatórios e colocar #
# em uma tupla. Depois disso, mostre a listagem de números gerados  #
# e também indique o menor e o maior valor que estão na tupla.      #
# ***************************************************************** #
from random import randint

titulo = '\033[1;33m  Maior e menor valores em Tupla \033[m'
t = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(t)
# print(type(t))
