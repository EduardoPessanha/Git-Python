from ex111.utilidadescev import moeda
from utilitarios import titulo

# ************************ Desafio 111 ************************* #
#                Transformando módulos em pacotes                #
#  Crie um pacote chamado utilidadesCeV que tenha dois módulos   #
#  internos chamados moeda e dado. Transfira todas as funções    #
#  utilizadas nos desafios 107, 108 e 109 para o primeiro pacote #
#  e mantenha tudo funcionando.                                  #
# ************************************************************** #
titulo('Transformando módulos em pacotes')
# ************************************************************** #

num = float(input('Digite o preço: R$ '))
moeda.resumo(num, 25, 15)
