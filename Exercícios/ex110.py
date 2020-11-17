from utilitarios import titulo
from pcex110 import moeda
# ************************** Desafio 110 ************************** #
#                 Reduzindo ainda mais seu programa                 #
#  Adicione o módulo moeda.py criado nos desafios anteriores, uma   #
#  função chamada resumo(), que mostre na tela algumas informações  #
#  geradas pelas funções que já temos no módulo criado até aqui.    #
# ***************************************************************** #
titulo('Reduzindo ainda mais seu programa')
# ***************************************************************** #

#     " Solução na pasta pcex110 "


num = str(input('Digite o preço: R$ '))
moeda.resumo(num, 25, 15)
