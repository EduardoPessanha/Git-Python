# *************************** Desafio 093 ******************************** #
#                    Cadastro de Jogador de Futebol                        #
# Crie um programa que gerencie o aproveitamento de um jogador de futebol. #
# O programa vai ler o nome do jogador e quantas partidas ele jogou.       #
# Depois vai ler a quantidade de gols feitos em cada partida. No final,    #
# tudo isso será guardado em um dicionário, incluindo o total de gols      #
# feitos durante o campeonato.                                             #
# ************************************************************************ #
linha = '+=' * 24
linha1 = '\033[1;34m*=\033[m' * 30
título = ' \033[1;3;4;7;34mCadastro de Jogador de Futebol\033[m '
print(f'\n{título:*^64}\n')
print(linha)
# ************************************************************************ #
cad = dict()
n_gols = list()
cad['nome'] = str(input('Nome do jogador: ')).capitalize().strip()
partidas = int(input(f'Quantas partidas o {cad["nome"]} jogou? '))
for c in range(partidas):
    n_gols.append(int(input(f'{" ":>3}Quantos gols {cad["nome"]} marcou na partida {c + 1}? ')))
cad['gols'] = n_gols[:]
cad['total'] = sum(n_gols)
print(linha1)
print(cad)
print(linha1)
for k, v in cad.items():
    print(f"O campo {k} tem o valor {v}.")
print(linha1)
print(f"O jogador {cad['nome']} jogou {partidas} partidas:")
# No lugar de partidas poderia usar len(cad['gols'])
for i, v in enumerate(cad['gols']):
    print(f"{'=> ':>6}Na partida {i + 1}, fez {v} gols")
print(f"Fez um total de {cad['total']} gols.")
print(linha1)
