# ************************** Desafio 075 ************************** #
#                   Análise de dados em uma Tupla                   #
# Desenvolva um programa que leia quatro valores pelo teclado e     #
# guarde-os em uma tupla. No final, mostre:                         #
# A) Quantas vezes apareceu o valor 9.                              #
# B) Em que posição foi digitado o primeiro valor 3.                #
# C) Quais foram os números pares.                                  #
# ***************************************************************** #

for cont in range(0, 4):
    n = int(input('Digit um número: '))
    if cont == 0:
        t1 = n
    elif cont == 1:
        t2 = n
    elif cont == 2:
        t3 = n
    else:
        t4 = n
    cont += 1

t = (t1, t2, t3, t4)
print(f'{type(t)} => {t}')
