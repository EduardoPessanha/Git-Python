# **************************** Desafio 095 ************************* #
#                     Aprimorando os Dicionários                     #
# Aprimore o desafio 93 para que ele funcione com vários jogadores,  #
# incluindo um sistema de visualização de detalhes do aproveitamento #
# de cada jogador.                                                   #
# ****************************************************************** #
linha = '+=' * 24
linha1 = '\033[1;34m*=\033[m' * 24
título = ' \033[1;3;4;7;34mAprimorando os Dicionários\033[m '
print(f'\n{título:*^64}\n')
print(linha)
# ****************************************************************** #
cad = dict()
n_gols = list()
lista = list()
# Cadastrando os jogadores:
while True:
    cad.clear()
    cad['nome'] = str(input('Nome do jogador: ')).capitalize().strip()
    partidas = int(input(f'Quantas partidas o {cad["nome"]} jogou? '))
    for c in range(partidas):
        n_gols.append(int(input(f'{" ":>3}Quantos gols {cad["nome"]} marcou na partida {c + 1}? ')))
    cad['gols'] = n_gols[:]
    cad['total'] = sum(n_gols)
    n_gols.clear()
    while True:
        resp = str(input('Deseja continuar (S/N)? ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('Entrada INVÁLIDA. ', end='')
    lista.append(cad.copy())
    if resp == 'N':
        break
# Fim do cadastro
print(linha1)
#  Exibindo a listagem geral dos jogadores:
print(f"{'Cod':^6}{'Nome':<12}{'Gols':<18}{'Total':^6}")
print(linha)
for k, v in enumerate(lista):
    print(f"{(k + 1):^6}{v['nome']:<12}{str(v['gols']):<18}{v['total']:}")
print(linha1)
# Exibindo a listagem por jogador:

