# **************************** Desafio 095 ************************* #
#                     Aprimorando os Dicionários                     #
# Aprimore o desafio 93 para que ele funcione com vários jogadores,  #
# incluindo um sistema de visualização de detalhes do aproveitamento #
# de cada jogador.                                                   #
# ****************************************************************** #
lin = '+=' * 20
lin1 = '\033[1;34m*=\033[m' * 26
título = ' \033[1;3;4;7;34mAprimorando os Dicionários\033[m '
print(f'\n{título:*^64}\n')
print(lin)
# ****************************************************************** #
jogador = dict()    # Guarda os dados do jogador
partida = list()    # Guarda os dados das partidas dos jogadores => gols
lista = list()      # Guarda os dados de todos os jogadores cadastrados

# Cadastrando os dados dos jogadores:

while True:
    jogador['nome'] = str(input('Nome do jogador: ')).capitalize().strip()    # chave nome = nome do jogador
    tot = int(input(f"Quantas partidas {jogador['nome']} jogou? "))           # guarda a quantidade de partidas
    # Guardando os gols marcados pelo jogador em cada partida:
    for c in range(tot):
        partida.append(int(input(f"{' ':>3}Quantos gols {jogador['nome']} marcou na partida {c + 1}? ")))
    jogador['gol'] = partida[:]          # Guardando as partidas aos dados do jogador
    jogador['total'] = sum(partida)      # Guardando o total de gols do jogador
    while True:
        resp = str(input('Deseja continuar (S/N)? ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('Entrada INVÁLIDA. ', end='')
    lista.append(jogador.copy())   # Guarda os dados dos jogadores
    partida.clear()                # Apaga os dados do último jogador cadastrado
    if resp == 'N':
        break

# Fim do cadastro

# Exibindo os dados dos jogadores:

print(lin1)
# print(f"{'COD':^6}{'NOME':<15}{'GOLS':<15}{'TOTAL'}")    # minha solução

# Solução do Gustavo Guanabara:
print(f'{"COD":^6}', end='')
for k in jogador.keys():                # para cada chave em chave de jogador
    print(f"{k.upper():<15}", end='')   # exibe o nome da chave
print()
print(lin1)
for i, it in enumerate(lista):      # para cada indice e item na lista 'lista'
    print(f'{i + 1:^6}', end='')    # exibe o indice da lista
    for k, v in it.items():         # para cada chave e valor nos itens (jogador) da lista
        print(f"{str(v):<15}", end='')   # exibe o valor da chave
    print()

# Exibindo o ranking de um jogador:

while True:
    print(lin1)
    cod = int(input('Mostrar dados de qual jogador? (999 para sair) '))
    if cod == 999:
        break
    if cod > len(lista):
        print(f'ERRO! Não existe jogador com código {cod}')
    else:
        print(lin1)
        print(f">> > LEVANTAMENTO DO JOGADOR {lista[cod - 1]['nome'].upper()}:")
        for i, it in enumerate(lista[cod-1]['gol']):    # para cada indice e item na lista no campo 'gol',
            # dentro de 'jogador'
            print(f"{'* ':>7}Na partida {i + 1} {' => '} {it} gols.")
        print(f"{' ':>5}Total de gols marcados => {sum(lista[cod - 1]['gol'])}")
        média = sum(lista[cod - 1]['gol']) / (len(lista[cod-1]['gol']))
        print(f"{' ':>5}Média de gols por partida => {média:.2f}")
print(lin1)
print(f'{"<< PROGRAMA ENCERRADO >>":^52}')
saída = '\033[1;3;7;34m< << VOLTE SEMPRE >> >\033[m'
print(f"{saída:^66}")
