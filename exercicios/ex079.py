# ************************** Desafio 079 ************************** #
#                    Valores únicos em uma Lista                    #
# Crie um programa onde o usuário possa digitar vários valores      #
# numéricos e cadastre-os em uma lista. Caso o número já exista lá  #
# dentro, ele não será adicionado. No final, serão exibidos todos   #
# os valores únicos digitados, em ordem crescente.                  #
# ***************************************************************** #
linha = '-='*25
titulo = ' \033[1;33mValores únicos em uma Lista\033[m '
print(f'\n{titulo:*^60}\n')
print(linha)
# ***************************************************************** #
listaValores = list()
continua = ' '
while True:
    num = int(input('Digite um número inteiro: '))
    cont = listaValores.count(num)
    if cont != 0:
        print(
            f'O número {num} já foi adicionado! Não será adicionado novamente.')
    else:
        listaValores.append(num)
        print('valor adiconado com sucesso!')
    while continua not in 'SN':
        continua = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
        if continua not in 'SN':
            print('Entrada incorreta! ', end='')
    if continua in 'N':
        break
    else:
        continua = ' '
print(linha)
listaValores.sort()
print(f'Os valores digitados foram: {listaValores}')

# ***************************************************************** #
#                 Solução do Gustavo Guanabara                      #
# ***************************************************************** #
# números = list()
# while True:
#     n = int(input('Digite um valor: '))
#     if n not in números:
#         números.append(n)
#         print('Valor adiconado com sucesso ...')
#     else:
#         print('Valor duplicado! Não vou adicionar ,,,')
#     r = str(input('Deseja continuar? [S/N] '))
#     if r in "Nn":
#         break
# print('-='*30)
# números.sort()
# print(f'Você digitou os valores: {números}')
