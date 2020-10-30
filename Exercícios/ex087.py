# ************************** Desafio 087 **************************** #
#                    Mais sobre Matriz em Python                      #
# Aprimore o desafio anterior, mostrando no final:                    #
# A) A soma de todos os valores pares digitados.                      #
# B) A soma dos valores da terceira coluna.                           #
# C) O maior valor da segunda linha.                                  #
#                        0 [] [] []                                   #
#                        1 [] [] []                                   #
#                        2 [] [] []                                   #
#                          0  1  2                                    #
# ******************************************************************* #
linha = '++' * 25
linha1 = '\033[1;34m*=\033[m' * 25
título = ' \033[1;34mMais sobre Matriz em Python\033[m '
print(f'\n{título:*^60}\n')
print(linha)
# ******************************************************************* #
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = col3 = 0
lin2 = list()
for lin in range(0, 3):
    for col in range(0, 3):
        matriz[lin][col] = int(input(f'Digite um valor para a posição [{lin},{col}]: '))
        if matriz[lin][col] % 2 == 0:
            spar += matriz[lin][col]
        if col == 2:
            col3 += matriz[lin][col]
        if lin == 1:
            lin2.append(matriz[lin][col])
print(linha1)
for lin in range(0, 3):
    for col in range(0, 3):
        print(f'[{matriz[lin][col]:^5}]', end='')
    print()
print(linha1)
print(f'A soma de todos os valores pares digitados é igual a {spar}.')
print(f'A soma dos valores da terceira coluna é igual a {col3}.')
print(f'O maior valor da segunda linha é igual a {max(lin2)}.')
