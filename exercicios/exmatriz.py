linha = '++' * 25
linha1 = '\033[1;34m*=\033[m' * 21
título = ' \033[1;33mMatriz em Python\033[m '
print(f'\n{título:*^60}\n')
print(linha)
# # ******************************************************************* #
matriz = list()
'''
lin = nº de linhas
col = nº de colunas
valor = valor do elemento da matriz
'''
print()
lin = int(input('Digite o número de linhas da matriz: '))
col = int(input('Digite o número de colunas da matriz: '))
print(linha1)
for l in range(0, lin):
    # Cria as linhas da matriz
    linha = []
    for c in range(0, col):
        # Cria as colunas da matriz e recebe o valor
        linha.append(int(input(f'Digite o valor para a posição [{l}][{c}]: ')))
    matriz.append(linha)
print(linha1)
for l in range(lin):
    for c in range(col):
        print(f'[{matriz[l][c]:^6}]', end=' ')
    print()
print(linha1)
