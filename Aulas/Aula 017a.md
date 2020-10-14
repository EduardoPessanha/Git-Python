# ***************************************************** #
#                  Python 3 - Aula 017                  #
#        VARIÁVEIS COMPOSTAS - LISTAS (Parte 1)         #
# ***************************************************** #

# Sintaxe das Listas -> as Listas são declaradas atravez de colchetes [] (ou usando a função "list")
# A diferença básica entre as Listas e as Tuplas é que as Listas PODEM SER ALTERADAS"

lanche = ['hamburger', 'suco', 'pizza', 'pudim']
print(f'lanche = {lanche}')
print('Tipo "lanche" -> ', type(lanche))

# Podemos substituir, eliminar (del(), pop(), remove()) e adicionar (append(), insert())

print('\nSubstituindo pudim por picolé:\n')
lanche[3] = 'picolé'
print(f'lanche = {lanche}')

print('\nAdicionando pudim ao lanche:\n')
# O método append() adiciona o elemento no final da lista
lanche.append('pudim')
print(f'lanche = {lanche}')

print('\nAdicionando cachorro-quente antes de hamburger ao lanche:\n')
# O método insert() adiciona o elemento em uma posição definida
lanche.insert(0, 'cachorro-quente')
print(f'lanche = {lanche}')

print('\nApagando "pizza" de lanche com o metodo del:\n')
# O método del apaga o elemento da lista conforme o indice definido
del lanche[3]
print(f'lanche = {lanche}')

print('\nApagando "pizza" de lanche com o metodo pop():\n')
lanche.insert(3, 'pizza')
# O método pop('indice') apaga o elemento da lista conforme o indice definido
lanche.pop(3)
print(f'lanche = {lanche}')

print('\nApagando último elemento de lanche com o metodo pop():\n')
lanche.insert(3, 'pizza')
lanche.pop()  # O método pop() apaga o último elemento da lista
print(f'lanche = {lanche}')

print('\nApagando "pizza" de lanche com o metodo remove("pizza"):\n')
lanche.append('picolé')
# O método remove('elemento') apaga a primeira ocorrência do 'elemento' que encontrar na lista
lanche.remove('pizza')
print(f'lanche = {lanche}')

# Podemos criar listas atravez de range() e a função list():

valores = list(range(4, 11))
print(f'\nvalores = {valores}')
valores.sort(reverse=True)
print(f'\nvalores na ordem inversa = {valores}')
maior = max(valores)
print(f'Maior valor = {maior} usando o método "max()"')
print(f'Menor valor = {min(valores)} usando o método "min()"')
print(f'Tamanho de lista = {len(valores)} usando o método "len()"')

num = [7, 5, 2, 3, 2, 1]
print(num)
num.remove(2)
print(num)
if 8 in num:
    num.remove(8)
    print(f'O número 8 foi removido da lista {num}\n')
else:
    print(f'Não existe o número 8 na lista {num}\n')

# valor = []  # ou valor = list() -> lista vazia
# valor = list()
# # valor.append(5)
# # valor.append(9)
# # valor.append(4)
# # print(valor)
# for cont in range(0, 5):
#     # inserindo os elementos da lista pelo teclado!
#     valor.append(int(input('Digite um valor: ')))
# for c, v in enumerate(valor):
#     print(f'Na posição {c} encontrei o valor {v}!')
# print('Cheguei ao final da lista')

a = [2, 3, 4, 7, 1, 5]
print(f'Lista a: {a}')
b = a
print('\nIgualando listas( b = a):')
print(f'Lista b: {b}\n')
b[2] = 8 # A partir do momento que igualamos listas, é criado uma
         # ligação entre elas, assim, ao se alterar uma lista a outra
         # também será alterada da mesma forma.
print(f'Lista a: {a}')
print(f'Lista b: {b}, na lista b fizemos b[2] = 8')
print('\nCopiando listas (b = a[:]):')
b = a[:] # Nesse caso, estamos copiando para lista b os valores da lista a.
b[2]= 7
print(f'Lista a: {a}')
print(f'Lista b: {b}, na lista b, fizemos b[2] = 7')
print(b.count(7))
