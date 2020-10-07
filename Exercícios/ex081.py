# ************************** Desafio 081 ************************** #
#                    Extraindo dados de uma Lista                   #
# Crie um programa que vai ler vários números e colocar em uma      #
# lista. Depois disso, mostre:                                      #
# A) Quantos números foram digitados.                               #
# B) A lista de valores, ordenada de forma decrescente.             #
# C) Se o valor 5 foi digitado e está ou não na lista.              #
# ***************************************************************** #
linha = '=+' * 25
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
        continua = ' '
cont = listaNum.count(5)
listaNum.sort(reverse=True)
quant = len(listaNum)
print(f'\n{linha}')
print(f'Os números digitados em ordem decrescente foram:{listaNum}')
print(f'Foram digitados {quant} números')
print('O número 5', end=' ')
if cont == 0:
    print(f'não foi digitado! Não faz parte da lista!')
else:
    print(f'foi digitado {cont} vez(es) na posição:', end=' ')
    for pos, num in enumerate(listaNum):
        if num == 5:
            print(f'{pos + 1}', end=' ')
print(f'\n{linha}\n')

# ***************************************************************** #
#                 Solução do Gustavo Guanabara                      #
# ***************************************************************** #
# Na solução apresentada pelo professor, para saber se o número 5
# faz parte ou não da lista, foi usando um if con o operador "in":
#
# if 5 in listaNum:      # se o valor 5 ESTÁ EM (in) listaNum
#     print('O valor 5 faz parte da lista!')
# else:                  # se não:
#     print('O valor 5 não foi encontrado na lista!')
#
# O operador "in", no Python, faz buscas em coleções, listas. etc.
