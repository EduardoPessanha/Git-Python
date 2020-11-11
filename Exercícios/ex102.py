from utilitarios import *

# **************************** Desafio 102 ************************** #
#                         Função para Fatorial                        #
# Crie um programa que tenha uma função fatorial() que receba dois    #
# parâmetros: o primeiro que indique o número a calcular e outro      #
# chamado show, que será um valor lógico (opcional) indicando se será #
# mostrado ou não na tela o processo de cálculo do fatorial.          #
# ******************************************************************* #
#
titulo(' Função para Fatorial ')


# ******************************************************************* #


# Definindo a função:

def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostra o processo do cálculo
    :return: O valor do fatorial do número n
    """
    fat = 1
    # print('~' * 30)
    for c in range(n, 0, -1):
        if show:
            if c == 1:
                print(c, end=' = ')
            else:
                print(c, end=' x ')
        fat *= c
    return fat


# Rotina Principal
help(fatorial)
print('~'*44)
n = int(input('Escolha um número para calcular o fatorial: '))
while True:
    s = str(input('Mostrar o cálculo (S/N)? ')).upper().strip()[0]
    if s not in 'SN':
        print('Entrada INVÁLIDA! ', end='')
    else:
        break
if s == "S":
    s = True
else:
    s = False
print(f'O valor de {n} fatorial é igual a: {n}! = ', end='')
print(f'{fatorial(n, s)}')

