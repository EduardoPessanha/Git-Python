from utilitarios import titulo
from utilidades.numero import leiaint, leiafloat
# ************************ Desafio 113 ************************* #
#                 Funções aprofundadas em Python                 #
#  Reescreva a função leiaInt() que fizemos no desafio 104,      #
#  incluindo agora a possibilidade da digitação de um número de  #
#  tipo inválido. Aproveite e crie também uma função leiaFloat() #
#  com a mesma funcionalidade.                                   #
# ************************************************************** #
titulo('Funções aprofundadas em Python')
# ************************************************************** #

nI = leiaint('Digite um número: ')
nR = leiafloat('Digite um número Real: ')
print(f'O número \"Inteiro\" digitado foi {nI} e o número \"Real\" foi {nR}')
