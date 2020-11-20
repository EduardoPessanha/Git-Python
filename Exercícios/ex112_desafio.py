from utilitarios import titulo
from ex112.utilidadescev import moeda, dado
# ************************* Desafio 112 ************************* #
#                   Entrada de dados monetários                   #
#  Dentro do pacote utilidadesCeV que criamos no desafio 111,     #
#  temos um módulo chamado dado. Crie uma função chamada          #
#  leiaDinheiro() que seja capaz de funcionar como a função       #
#  input(), mas com uma validação de dados para aceitar apenas   #
#  valores que seja monetários.                                   #
# *************************************************************** #
titulo('Entrada de dados monetários')
# *************************************************************** #

p = dado.leiadinheiro('Digite o preço: R$ ')
moeda.resumo(p, 20, 12)