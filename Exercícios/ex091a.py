from random import randint
from time import sleep
from operator import itemgetter
jogo = dict()
quant = int(input('\nInforme o número de jogadores: '))

# Definindo o dicionário jogo:

for c in range(quant):
    jogo[f'jogador{c+1}'] = randint(1, 6)

# Exibindo o dicionário jogo:

print('\nValores sorteados:\n')
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(0.75)
print()
print('\033[1;34m*=\033[m'*24)
print(f"\033[1;34m{'== RANKING DOS JOGADORES ==':^48}\033[m")
print('\033[1;34m*=\033[m'*24)
# para ordenar o dicionário foi usado a função "itemgetter()", obtida da biblioteca "operator"
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
sleep(0.75)
for i, v in enumerate(ranking):
    print(f'{i+1:>8}º lugar: {v[0]} com {v[1]} pontos')
print('\033[1;34m*=\033[m'*24)
