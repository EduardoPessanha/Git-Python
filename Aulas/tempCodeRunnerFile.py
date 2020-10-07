valor = list()
for cont in range(0, 5):
    # inserindo os elementos da lista pelo teclado!
    valor.append(int(input('Digite um valor: ')))
for c, v in enumerate(valor):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')
