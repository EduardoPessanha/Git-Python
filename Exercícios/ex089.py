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
nome = list()
nota = list()
resp = ' '
while resp not in 'Nn':
    nome.append(str(input('Nome do aluno: ')))
    for n in range(1, 3):
        nota.append(float(input(f'Nota {n}: ')))
    media = ((nota[0] + nota[1]) / 2)
    nome.insert(1, nota[:])
    nome.insert(2, media)
    boletim.append(nome[:])
    nome.clear()
    nota.clear()
    while True:
        resp = str(input('Novo cadastro (S/N)? ')).upper().strip()[0]
        if resp not in 'SsNn':
            print('Entrada INVÁLIDA!.', end=' ')
        else:
            break
print(linha1)
print('Nº   Nome       Média')
for id, el in enumerate(boletim):
    print(f'{id:<4} {el[0]:<10} {el[2]:.2f}')


# 'Mostrar as notas de qual aluno (999 interrompe)? '
