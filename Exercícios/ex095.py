# **************************** Desafio 095 ************************* #
#                     Aprimorando os Dicionários                     #
# Aprimore o desafio 93 para que ele funcione com vários jogadores,  #
# incluindo um sistema de visualização de detalhes do aproveitamento #
# de cada jogador.                                                   #
# ****************************************************************** #
linha = '+=' * 24
linha1 = '\033[1;34m*=\033[m' * 26
título = ' \033[1;3;4;7;34mAprimorando os Dicionários\033[m '
print(f'\n{título:*^64}\n')
print(linha)
# ****************************************************************** #
cad = dict()
n_gols = list()
jogos = list()
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
    jogos.append(cad.copy())
    if resp == 'N':
        break
# Fim do cadastro
print(linha1)
#  Exibindo a listagem geral dos jogadores:
print(f"{'Cod':^6}{'Nome':<12}{'Gols':<18}{'Total':^6}")
print(linha)
for k, v in enumerate(jogos):
    print(f"{(k + 1):^6}{v['nome']:<12}{str(v['gols']):<18}{v['total']:}")
print(linha1)
# Exibindo os dados do jogador:
while True:
    cod = int(input('Mostrar dados de qual jogador? (999 para sair) '))
    if cod == 999:
        break
    elif cod <= partidas:
        # O indice da lista jogos corresponde a um dicionário que contém os dados dos jogadores:
        i = cod - 1
        print(f"-- LEVANTAMENTO DO JOGADOR {jogos[i]['nome']} --")
        # O números de partidas corresponde aos gols que estão na chave 'gols' do dicionário que contém os
        # dados do jogador print(jogos[i]['gols'])
        for k in range(len(jogos[i]['gols'])):
            print(f"Na partida {k + 1} fez ", end='')
            print(f"{jogos[i]['gols'][k]} gols.")
        print(linha1)
    else:
        print(f'NÃO EXISTE jogador com código {cod}. Tente outra vez!!!')
print(linha1)
print(f'{"< << << << PROGRAMA ENCERRADO >> >> >> >":^52}')

'''
ordenando raciocínio:
jogos é a lista que contém os dicionários (cad) com os dados dos jogadores.

jogos = [{'nome': 'A', 'gols': [1, 2, 3, 4], 'total': 10}, {'nome': 'B', 'gols': [1, 2, 3], 'total': 6},
         {'nome': 'C', 'gols': [1, 2], 'total': 3}]

Então cada indice de jogos corresponde as dados de um jogador:

jogos[0] = {'nome': 'A', 'gols': [1, 2, 3, 4], 'total': 10}

logo o nome do jogador x  será o valor do campo 'nome' de jogos[x]


#     item                item            item
#  ___________   ___________________   __________
# {'nome': 'T', 'gols': [2, 1, 2, 3], 'total': 8}
'''
