# ************************** Desafio 080 ************************** #
#                   Lista ordenada sem repetições                   #
# Crie um programa onde o usuário possa digitar cinco valores       #
# numéricos e cadastre-os em uma lista, já na posição correta de    #
# inserção (sem usar o sort()). No final, mostre a lista ordenada   #
# na tela.                                                          #
# ***************************************************************** #
linha = '-=' * 25
título = ' \033[1;34mLista ordenada sem repetições\033[m '
print(f'\n{título:*^60}\n')
print(linha)
# ***************************************************************** #
lista = list()
for cont in range(0, 5):
    valor = int(input('Digite um valor: '))
    if cont == 0:
        lista.insert(0, valor)
        print(f'O valor {valor}, foi adiconado no final da lista!')
    elif cont == 1:
        if valor > lista[0]:
            lista.insert(1, valor)
            indice = lista.index(valor)
            print(f'O valor {valor}, foi adiconado no final da lista!')
        else:
            lista.insert(0, valor)
            indice = lista.index(valor)
            print(f'Adicionado na posição {indice}')
    elif cont == 2:
        if valor > lista[1]:
            lista.insert(2, valor)
            indice = lista.index(valor)
            print(f'O valor {valor}, foi adiconado no final da lista!')
        elif valor < lista[0]:
            lista.insert(0, valor)
            indice = lista.index(valor)
            print(f'Adicionado na posição {indice}')
        else:
            lista.insert(1, valor)
            indice = lista.index(valor)
            print(f'Adicionado na posição {indice}')
    elif cont == 3:
        if valor > lista[2]:
            lista.insert(3, valor)
            indice = lista.index(valor)
            print(f'O valor {valor}, foi adiconado no final da lista!')
        elif valor < lista[0]:
            lista.insert(0, valor)
            indice = lista.index(valor)
            print(f'Adicionado na posição {indice}')
        elif valor > lista[1]:
            lista.insert(2, valor)
            indice = lista.index(valor)
            print(f'Adicionado na posição {indice}')
        else:
            lista.insert(1, valor)
            indice = lista.index(valor)
            print(f'Adicionado na posição {indice}')
    elif cont == 4:
        if valor > lista[3]:
            lista.insert(4, valor)
            indice = lista.index(valor)
            print(f'O valor {valor}, foi adiconado no final da lista!')
        elif valor < lista[0]:
            lista.insert(0, valor)
            indice = lista.index(valor)
            print(f'Adicionado na posição {indice}')
        elif valor > lista[2]:
            lista.insert(3, valor)
            indice = lista.index(valor)
            print(f'Adicionado na posição {indice}')
        elif valor > lista[1]:
            lista.insert(2, valor)
            indice = lista.index(valor)
            print(f'Adicionado na posição {indice}')
        else:
            lista.insert(1, valor)
            indice = lista.index(valor)
            print(f'Adicionado na posição {indice}')
print(f'\n{linha}')
print(f'Os números digitados foram {lista}')

# ***************************************************************** #
#                 Solução do Gustavo Guanabara                      #
# ***************************************************************** #
# lista = list()
# for c in range(0, 5):
#     num = int(input("Digite um valor: "))
#     if c == 0 or num > lista[-1]:  # lista[-1] é o mesmo que lista[len(lista) - 1] => é a última posição da lista
#         lista.append(num)
#         print('Adicionado no final da lista!')
#     # if num > lista[-1]:
#     #     lista.append(num)
#     else:                        # O valor digitado estará entre a primeira e última posição
#         pos = 0
#         while pos < len(lista):  # Percorre a lista de posição em posição até o final
#             if num <= lista[pos]:
#                 lista.insert(pos, num)
#                 print(f'Adiconado na posição {pos} da lista!')
#                 break
#             pos += 1
# print(f'\n{linha}')
# print(f'Os valores digitados em ordem foram: {lista}')
