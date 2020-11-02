matriz = list()
'''
lin = nº de linhas
col = nº de colunas
valor = valor do elemento da matriz
'''
print()
lin = int(input('Digite o número de linhas da matriz: '))
col = int(input('Digite o número de colunas da matriz: '))
print()
for l in range(0, lin):
    # Cria as linhas da matriz
    linha = []
    for c in range(0, col):
        # Cria as colunas da matriz e recebe o valor
        linha.append(int(input('Digite o valor para [' + str(l) +'][' + str(c) +']: ')))
    matriz.append(linha)
for l, v in enumerate(matriz):
    print()
    for l1, vi in enumerate(v):
        print(f'[{vi:^6}]', end='')
print()
