# ************************** Desafio 075 ************************** #
#                   Análise de dados em uma Tupla                   #
# Desenvolva um programa que leia quatro valores pelo teclado e     #
# guarde-os em uma tupla. No final, mostre:                         #
# A) Quantas vezes apareceu o valor 9.                              #
# B) Em que posição foi digitado o primeiro valor 3.                #
# C) Quais foram os números pares.                                  #
# ***************************************************************** #
titulo = ' \033[1;34mAnálise de dados em uma Tupla\033[m '
print(f'\n{titulo:=^60}\n')
for cont in range(0, 4):
    n = int(input(' Digite um número: '))
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
print('*'*60)
n1 = t.count(9)
if n1 == 0:
    n1 = ' Não foi digitado o valor 9'
else:
    n1 = f' O valor 9 foi digitado {t.count(9)} vez(ez)'
n2 = t.count(3)
if n2 != 0:
    n2 = f'O primeiro valor 3 foi digitado na posição {t.index(3)+1}'
else:
    n2 = 'Não foi digitado o valor 3'
cont = 0
for n in range(0, len(t)):
    if t[n] % 2 == 0:
        cont += 1
print(f'{n1}\n {n2}\n Foram digitados {cont} número(s) pares\n')
