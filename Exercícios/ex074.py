# ************************** Desafio 074 ************************** #
#                  Maior e menor valores em Tupla                   #
# Crie um programa que vai gerar cinco números aleatórios e colocar #
# em uma tupla. Depois disso, mostre a listagem de números gerados  #
# e também indique o menor e o maior valor que estão na tupla.      #
# ***************************************************************** #
from random import randint
titulo = ' \033[1;36mMaior e menor valores em Tupla\033[m '
print(f"\n{titulo:*^60}\n")
t = (randint(0, 10), randint(0, 10), randint(
    0, 10), randint(0, 10), randint(0, 10))
for cont in range(0, len(t)):
    n = t[cont]
    if cont == 0:
        maior = menor = t[cont]
    if n > maior:
        maior = t[cont]
    if n < menor:
        menor = t[cont]
print(f'Foram gerados os seguintes números: {t}')
print(f'\nO maior valor foi {maior}')
print(f'O menor valor foi {menor}\n')
