# ************************** Desafio 089 **************************** #
#                  Boletim com listas compostas                       #
# Crie um programa que leia nome e duas notas de vários alunos e      #
# guarde tudo em uma lista composta. No final, mostre um boletim      #
# contendo a média de cada um e permita que o usuário possa mostrar   #
# as notas de cada aluno individualmente.                             #
# ******************************************************************* #
linha = '++' * 25
linha1 = '\033[1;34m*=\033[m' * 25
título = ' \033[1;36mBoletim com listas compostas\033[m '
print(f'\n{título:*^60}\n')
print(linha)
# ******************************************************************* #
boletim = list()
dados = list()
resp = ' '
while resp not in 'Nn':
    dados.insert(0, str(input('Nome do aluno: ')))
    dados.insert(1, float(input('Primeira nota: ')))
    dados.insert(2, float(input('Segunda nota: ')))
    dados.insert(3, (dados[1] + dados[2]) / 2)
    boletim.append(dados[:])
    dados.clear()
    while True:
        resp = str(input('Novo cadastro (S/N)? ')).upper().strip()[0]
        if resp not in 'SsNn':
            print('Entrada INVÁLIDA!.', end=' ')
        else:
            break
for i in boletim:
    print(f'{i}')
