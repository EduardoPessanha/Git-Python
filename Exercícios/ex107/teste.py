# import ex107.moeda
from ex107.moeda import metade, dobro, aumentar, diminuir

p = float(input('Digite o preço: R$ '))

# print(f'A metade de {p} é {ex107.moeda.metade(p)}')
# print(f'O dobro de {p} é {ex107.moeda.dobro(p)}')
# print(f'Aumentando em 10%, temos {ex107.moeda.aumentar(p, 10)}')
# print(f'Reduzindo em 20%, temos {ex107.moeda.diminuir(p, 20)}')

print(f'A metade de {p} é {metade(p)}')
print(f'O dobro de {p} é {dobro(p)}')
print(f'Aumentando em 10%, temos {aumentar(p, 10)}')
print(f'Reduzindo em 20%, temos {diminuir(p, 20)}')
