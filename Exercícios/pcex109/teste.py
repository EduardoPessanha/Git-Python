from pcex109 import moeda

num = float(input('Digite o preço: R$ '))
print(f'a metade de {moeda.moeda(num)} é {moeda.metade(num, True)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}')
print(f'Aumentando 15%, temos {moeda.aumentar(num, 15, True)}')
print(f'Reduzindo 10%, temos {moeda.diminuir(num, 10, True)}')
