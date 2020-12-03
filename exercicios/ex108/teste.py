# import ex108.moeda
# from ex108.moeda import metade, dobro, aumentar, diminuir, moeda
from ex108 import moeda

p = float(input('Digite o preço: R$ '))

print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando em 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Reduzindo em 20%, temos {moeda.moeda(moeda.diminuir(p, 20))}')

# print(f'A metade de {moeda(p)} é {moeda(metade(p))}')
# print(f'O dobro de {moeda(p)} é {moeda(dobro(p))}')
# print(f'Aumentando em 10%, temos {moeda(aumentar(p, 10))}')
# print(f'Reduzindo em 20%, temos {moeda(diminuir(p, 20))}')
