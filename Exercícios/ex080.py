# ************************** Desafio 080 ************************** #
#                   Lista ordenada sem repetições                   #
# Crie um programa onde o usuário possa digitar cinco valores       #
# numéricos e cadastre-os em uma lista, já na posição correta de    #
# inserção (sem usar o sort()). No final, mostre a lista ordenada   #
# na tela.                                                          #
# ***************************************************************** #
linha = '-='*25
titulo = ' \033[1;34mLista ordenada sem repetições\033[m '
print(f'\n{titulo:*^60}\n')
print(linha)
# ***************************************************************** #
lista = list()
for cont in range(0, 5):
    valor = int(input('Digite um valor: '))
    if cont == 0:
        lista.insert(0, valor)
        print(f'O valor {valor}, foi adiconado no final da lista!')
        # indice = lista.index(valor)
        # print('O tamanho da lista é ', len(lista))
    elif cont == 1:                     #valor not in lista:
        if valor > max(lista):
            lista.insert(len(lista), valor)
            indice = list.index(valor)
            print(f'Adiconado na posição {indice}')
        else:
            lista.insert(0, valor)
            indice = lista.index(valor)
            print(f'Adicionado na posição {indice}')
        # print('O tamanho da lista é ', len(lista))
    elif cont == 2:
        if lista[0] < valor < lista[1]:
            lista.insert(1, valor)
            indice = lista.index(valor)
            print(f'Adicionado na posição {indice}')
        elif valor> lista[1]:
            lista.insert(1,valor)
            indice = lista.index(valor)
            print(f'Adicionado na posição {indice}')
        else:
            lista.insert(0,valor)
            indice = lista.index(valor)
            print(f'Adicionado na posição {indice}')
    elif cont == 3:
        if valor > lista[2]:
            lista.insert(2, valor)
            indice = lista.index(valor)
            print(f'Adicionado na posição {indice}')
        elif valor < lista[0]:
            lista.insert(lista[0], valor)
            indice = lista.index(valor)
            print(lista.index(valor))
        elif lista[1] < valor < lista[2]:
            lista.insert(2, valor)
            indice = lista.index(valor)
            print(f'Adicionado na posição {indice}')
    else:
        if valor > lista[3]:
            lista.insert(3, valor)
            indice = lista.index(valor)
            print(f'Adicionado na posição {indice}')
        elif valor < lista[0]:
            lista.insert(lista[0], valor)
            indice = lista.index(valor)
            print(f'Adicionado na posição {indice}')
        elif lista[2] < valor < lista[3]:
            lista.insert(2, valor)
            indice = lista.index(valor)
            print(f'Adicionado na posição {indice}')
        else:                                           
            lista.insert(3, valor)
            indice = lista.index(valor)
            print(f'Adicionado na posição {indice}')
print(linha)
print(lista)
