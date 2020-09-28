# ************************** Desafio 073 ************************** #
#                    Tuplas com Times de Futebol                    #
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela #
# do Campeonato Brasileiro de Futebol, na ordem de colocação.       #
# Depois mostre:                                                    #
# a) Os 5 primeiros times.                                          #
# b) Os últimos 4 colocados.                                        #
# c) Times em ordem alfabética.                                     #
# d) Em que posição está o time do Flamengo (da Chapecoense).       #
# ***************************************************************** #
titulo = '\033[1;32m Tuplas com Times de Futebol de 2020 \033[m'
linha = '¬'*60
print(f'\n{titulo:@^70}\n')
t = ('Atlético-MG', 'Internacional', 'São Paulo', 'Palmeiras',
     'Vasco da Gama', 'Flamengo', 'Sport Recife', 'Santos',
     'Fortaleza', 'Athletico-PR', 'Fluminense', 'Ceará SC',
     'Grêmio', 'Corinthians', 'Atlético-GO', 'Coritiba',
     'Bragantino-SP', 'Botafogo', 'Bahia', 'Goias')
print(linha)
print(f'Os cinco primeiros colocados:\n{t[0:5]}')
print(linha)
print(f'Os quatros últimos colocados:\n{t[-4:]}')
print(linha)
print(f'Times em ordem alfabética:\n{sorted(t)}')
print(linha)
print(f'O Flamengo está na {t.index("Flamengo") + 1}ª posição no campeonato')
print(linha)
# print(t.index(t[0])+1, 'º lugar', '.'*38, t[0])
# O usuário deverá escolher um time para verificar a sua colocação
# no campeonato.
# Se o time escolhido não estiver na tabela, informar ao usuário.
