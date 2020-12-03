from pcex107 import moeda
# import pcex107.moeda
num = float(input('Digite o preço: R$'))
print(f'a metade de R${num} é {moeda.metade(num)}')
print(f'O dobro de R${num} é {moeda.dobro(num)}')
print(f'Aumentando 10%, temos {moeda.aumentar(num, 10)}')
print(f'Reduzindo 10%, temos {moeda.diminuir(num, 10)}')
