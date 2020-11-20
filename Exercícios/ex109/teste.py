# import ex109.moeda
# from ex109.moeda import metade, dobro, aumentar, diminuir, moeda
from ex109 import moeda

p = float(input('Digite o preço: R$ '))

print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando em 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo em 20%, temos {moeda.diminuir(p, 20, True)}')

# print(f'A metade de {moeda(p)} é {moeda(metade(p))}')
# print(f'O dobro de {moeda(p)} é {moeda(dobro(p))}')
# print(f'Aumentando em 10%, temos {moeda(aumentar(p, 10))}')
# print(f'Reduzindo em 20%, temos {moeda(diminuir(p, 20))}')
