# *************************** Desafio 093 ******************************** #
#                    Cadastro de Jogador de Futebol                        #
# Crie um programa que gerencie o aproveitamento de um jogador de futebol. #
# O programa vai ler o nome do jogador e quantas partidas ele jogou.       #
# Depois vai ler a quantidade de gols feitos em cada partida. No final,    #
# tudo isso será guardado em um dicionário, incluindo o total de gols      #
# feitos durante o campeonato.                                             #
# ************************************************************************ #
lin = '+=' * 24
lin1 = '\033[1;34m*=\033[m' * 30
título = ' \033[1;3;4;7;34mCadastro de Jogador de Futebol\033[m '
print(f'\n{título:*^64}\n')
print(lin)
# ************************************************************************ #
jogador = {}    # guarda os dados do jogador
partida = []    # guarda os dados da partida do jogador
# Cadastrando os dados do jogador:
jogador['nome'] = str(input('Nome do jogador: ')).capitalize()  # chave nome = nome do jogador
tot = int(input(f"Quantas partidas {jogador['nome']} jogou? "))    # guarda o número de partidas
# Guardando os gols marcados pelo jogador em cada partida:
total = 0   # guarda o total de gols marcados pelo jogador
for c in range(tot):
    partida.append(int(input(f"Quantos gols {jogador['nome']} marcou na partida {c + 1}? ")))
    total += partida[c]
jogador['gols'] = partida
jogador['total'] = total
# fim do cadastro
# Exibindo os dados do jogador:
print(lin1)
print(jogador)
print(lin1)
