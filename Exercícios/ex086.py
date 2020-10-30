# ************************** Desafio 086 **************************** #
#                         Matriz em Python                            #
# Crie um programa que declare uma matriz de dimensão 3x3 e preencha  #
# com valores lidos pelo teclado. No final, mostre a matriz na tela,  #
# com a formatação correta.                                           #
#                        0 [] [] []                                   #
#                        1 [] [] []                                   #
#                        2 [] [] []                                   #
#                          0  1  2                                    #
# ******************************************************************* #
linha = '++' * 25
linha1 = '\033[1;34m*=\033[m' * 25
título = ' \033[1;33mMatriz em Python\033[m '
print(f'\n{título:*^60}\n')
print(linha)
# # ******************************************************************* #
L0 = [[], [], []]
L1 = [[], [], []]
L2 = [[], [], []]
matriz = list()
for c in range(0, 9):
    print('Digite um valor para a posição ', end='')
    if c <= 2:
        valor = int(input(f'[0, {c}]: '))
        L0[c].append(valor)
    elif c <= 5:
        valor = int(input(f'[1, {c - 3}]: '))
        L1[c - 3].append(valor)
    else:
        valor = int(input(f'[2, {c - 6}]: '))
        L2[c - 6].append(valor)
matriz.append(L0)
matriz.append(L1)
matriz.append(L2)
print(linha1)
for c in matriz:
    print(f'[{c[0][0]:^5}][{c[1][0]:^5}][{c[2][0]:^5}]')
print(linha1)

# ********************* Solução do Gustavo Guanabara *********************

# Declarando a matriz:
#
# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # A matriz foi declarada como uma lista, que tem três (elementos) listas
# # dentro, e dentro de cada lista, iremos ter três valores.
# # Fazendo um laço dentro de outro para preencher os valores da matriz:
# for lin in range(0, 3):  # Laço para preencher as linhas
#     for col in range(0, 3):  # laço para preencher as colunas
#         matriz[lin][col] = int(input(f'Digite um valor para a posição [{lin}, {col}]: '))
# print(linha1)
# for lin in range(0, 3):
#     for col in range(0, 3):
#         print(f'[{matriz[lin][col]:^5}]', end=' ')
#     print()
# print(linha1)
