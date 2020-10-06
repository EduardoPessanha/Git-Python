# ************************** Desafio 081 ************************** #
#                    Extraindo dados de uma Lista                   #
# Crie um programa que vai ler vários números e colocar em uma      #
# lista. Depois disso, mostre:                                      #
# A) Quantos números foram digitados.                               #
# B) A lista de valores, ordenada de forma decrescente.             #
# C) Se o valor 5 foi digitado e está ou não na lista.              #
# ***************************************************************** #
linha = '=+'*25
titulo = ' \033[1;35mExtraindo dados de uma Lista\033[m '
print(f'\n{titulo:*^60}\n')
print(linha)
# ***************************************************************** #
listaNum = list()
continua = ' '
while True:
    listaNum.append(int(input('Digite um número: ')))
    while continua not in 'nNsS':
        continua = str(input('Deseja continuar (S/N)? ')).upper().strip()[0]
        if continua not in 'sSnN':
            print('Entrada inválida!', end=' ')
    if continua in 'nN':
        break
    else:
        continua=' '
cont = listaNum.count(5)
print(f'\n{linha}')
print('O número 5 foi digitado', end =' ')
if cont == 0:
    print(f'{cont} vez(es)!!', end='')
else:
    listaNum.sort(reverse=True)
    print(f'{cont} vez(es) e ficaram na posição', end=' ')
    for pos, num in enumerate(listaNum):
        if num == 5:
            print(f'{pos + 1}', end=' ')
quant = len(listaNum)
print(f'\nForam digiados {quant} números')
print(listaNum)
