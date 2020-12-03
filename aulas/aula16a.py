# -*- coding: utf-8 -*-
# ***************************************************** #
#                  Python 3 - Aula 016                  #
#                        Tuplas                         #
# ***************************************************** #

# Variáveis Compostas:

# Existem 3 tipos de variáveis compostas no Python, a
# saber:
#       - Tuplas
#       - Listas
#       - Dicionários

# Tuplas:

# DEFINIÇÃO DE TUPLA

# Tupla é uma Lista imutável,  já que após definida, não permite
# a adição ou remoção de elementos, é uma lista que restringe a
# adição, alteração, remoção e o ordenamento do elementos.
# Tuplas são estruturas de dados heterogêneas. Em outras palavras,
# numa Tupla, os elementos podem ser de tipos distintos, por exemplo,
# uma Tupla pode conter o dia, o dia da semana, o mês e o ano.
t = ("10", "segunda-feira", "Fevereiro", 2022)
lanche = ('hambúrguer', 'suco', 'pizza', 'pudim', 'batata frita')
print()
type(lanche)
print('\n', lanche)
print(lanche[2])
print()
print(lanche[0:2], '\n')
print(lanche[1:])
print('\n', lanche[-1])
l = len(lanche)
print('O tamanho da Tupla lanche é {}'.format(l))


# lanche[1] = 'Refigerante' # Vai dar erro, porque as Tuplas são imutáveis!!!!!

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!!!\n')

# Usando range do for:

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

# Outra forma, usando enumaerate():
print('\nUsando o for com "enumerate()":')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print()

# usando o método sorted():
print(sorted(lanche))
print(lanche)

print()
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(f'a = {a} e b = {b}\n')
print(f'c = a + b = {c}\n')
c = b+a
print(f'c = b + a = {c}\n')
# usando o metodo count() para verificar o número de ocorrencias
# de um elemento dentro de uma Tupla:
print(f'O número 5 aparece {c.count(5)} vezes na tupla c\n')
# Usando o metodo index() para verificar o indice de um elemento
# em uma tupla (o index() mostra sempre a primeira ocorrência):
print(
    f'A primeira vez que o número 4 aparece na tupla "c" é na posição {c.index(4)}')

# Para apagar uma tupla podemos usar o comando del()
