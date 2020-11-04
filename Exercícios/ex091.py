# *************************** Desafio 091 ***************************** #
#                      Jogo de Dados em Python                          #
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados  #
# aleatórios. Guarde esses resultados em um dicionário em Python. No    #
# final, coloque esse dicionário em ordem, sabendo que o vencedor tirou #
# o maior número no dado.                                               #
# ********************************************************************* #
from random import randint
from time import sleep
from operator import itemgetter
linha = '++' * 24
linha1 = '\033[1;34m*=\033[m' * 24
título = ' \033[1;3;4;7;33mJogo de Dados em Python\033[m '
print(f'\n{título:*^64}\n')
print(linha)
# ********************************************************************* #
jogo = list()
dado = {}
jog = pontos = " "
for c in range(1, 5):
    dado['jogador'] = f'jogador{c}'
    dado['resultado'] = randint(1, 6)
    jogo.append(dado.copy())
print('Valores sorteados:')
ranking = []
for d in jogo:
    for k, v in d.items():
        if k == 'jogador':
            print(f'O {v} tirou ', end='')
            jog = v
        else:
            print(f'{v} no dado.')
            pontos = v
    sleep(0.75)
    item = (jog, pontos)
    ranking.append(item)
    del item
print(linha1)
print(f"{'== RANKING DOS JOGADORES ==':^48}")
jogo = sorted(ranking, key=itemgetter(1), reverse=True)
for i, v in enumerate(jogo):
    print(f'{i + 1}º Colocado: {v[0]} com {v[1]} pontos')
print(linha1)

# ************************************************************************************************************** #

# ************************** SOLUÇÃO DO GUSTAVO GUANABARA  **************************
# print()
# # Definindo o dicionário:
# jogo = {'jogador1': randint(1, 6),
#         'jogador2': randint(1, 6),
#         'jogador3': randint(1, 6),
#         'jogador4': randint(1, 6)
#         }
# Exibindo o dicionário jogo:
# print('Valores sorteados:')
# for k, v in jogo.items():
#     print(f'O {k} tirou {v} no dado.')
#     sleep(0.75)
# print(linha1)
# print(f"{'== RANKING DOS JOGADORES ==':^48}")
# # para ordenar, conforme solicitado, foi usado a função "itemgetter()", obtida da biblioteca "operator"
# ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# for i, v in enumerate(ranking):
#     print(f'{i+1}º lugar: {v[0]} com {v[1]} pontos')
#     sleep(0.75)
