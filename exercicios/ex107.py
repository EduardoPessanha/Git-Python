from pcex107 import moeda           # pcex107 = pacote que contém o módulo moeda
from utilitarios import titulo
# *************************** Desafio 107 *************************** #
#                    Exercitando módulos em Python                    #
#  Crie um módulo chamado moeda.py que tenha as funções incorporadas  #
#  aumentar(), diminuir(), dobro() e metade(). Faça também um         #
#  programa que importe esse módulo e use algumas dessas funções.     #
# ******************************************************************* #
titulo('Exercitando módulos em Python')
# ******************************************************************* #

num = float(input('Digite o preço: R$'))
print(f'a metade de {num} é {moeda.metade(num)}')
print(f'O dobro de R${num} é {moeda.dobro(num)}')
print(f'Aumentando 10%, temos {moeda.aumentar(num, 10)}')
print(f'Reduzindo 10%, temos {moeda.diminuir(num, 10)}')

# " Ver solução na pasta pcex107 "
