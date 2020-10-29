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
# ******************************************************************* #
L0 = [[], [], []]
L1 = [[], [], []]
L2 = [[], [], []]
matriz = list()
for c in range(0, 9):
    if c <= 2:
        valor = int(input(f'Digite um valor para a posição [0, {c}]: '))
        L0[c].append(valor)
    elif c <= 5:
        valor = int(input(f'Digite um valor para a posição [1, {c - 3}]: '))
        L1[c - 3].append(valor)
    else:
        valor = int(input(f'Digite um valor para a posição [2, {c - 6}]: '))
        L2[c - 6].append(valor)
matriz.append(L0)
matriz.append(L1)
matriz.append(L2)
print(linha1)
for c in matriz:
    print(f'[ {c[0][0]} ][ {c[1][0]} ][ {c[2][0]} ]')
print(linha1)
