# ************************** Desafio 082 ************************** #
#                 Dividindo valores em várias listas                #
# Crie um programa que vai ler vários números e colocar em uma      #
# lista. Depois disso, crie duas listas extras que vão conter       #
# apenas os valores pares e os valores ímpares digitados,           #
# respectivamente. Ao final, mostre o conteúdo das três listas      #
# geradas                                                           #
# ***************************************************************** #
linha = '=+' * 25
título = ' \033[1;36mDividindo valores em várias listas\033[m '
print(f'\n{título:*^60}\n')
print(linha)
# ***************************************************************** #
listaFonte = list()
listaPar = list()
listaÍmpar = list()
continua = ' '
while True:
    listaFonte.append(int(input('Digite um número inteiro: ')))
    while continua not in 'SN':
        continua = str(input('Deseja continuar (S/N)? ')).upper().strip()[0]
        if continua not in 'SN':
            print('Entrada inválida!', end=' ')
    if continua == 'N':
        break
    else:
        continua = ' '
for n in range(0, len(listaFonte)):
    if listaFonte[n] % 2 == 0:
        listaPar.append(listaFonte[n])
    else:
        listaÍmpar.append(listaFonte[n])
print(f'\n{linha}')
print(f'O números digitados foram: {listaFonte}')
print(f'Os números pares digitados foram: {listaPar}')
print(f'Os números ímpares digitados foram: {listaÍmpar}')
print(f'{linha}\n')
