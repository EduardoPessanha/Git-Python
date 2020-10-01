#            VARIÁVEIS CPOMPOSTAS - LISTAS (Parte 1)

# Sintaxe das Listas -> as Listas são declaradas atravez de colchetes [] (ou usando a função "list")
# A diferença básica entre as Listas e as Tuplas é que as Listas PODEM SER ALTERADAS"

lanche = ['hamburger', 'suco', 'pizza', 'pudim']
print(f'lanche = {lanche}')
print('Tipo "lanche" -> ', type(lanche))

# Podemos substituir, eliminar (del(), pop(), remove()) e adicionar (append(), insert()),

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
# O método pop('indice') aapaga o elemento da lista conforme o indice definido
lanche.pop(3)
print(f'lanche = {lanche}')

print('\nApagando último elemento de lanche com o metodo pop():\n')
lanche.insert(3, 'pizza')
lanche.pop()  # O método pop() aapaga o último elemento da lista
print(f'lanche = {lanche}')

print('\nApagando "pizza" de lanche com o metodo remove("pizza"):\n')
lanche.append('picolé')
# O método remove('elemento') aapaga 'elemento' da lista
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
