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
lista=list()
for cont in range(0,5):
    valor = int(input('Digite um valor: '))
    lista.append(valor)
print(lista)