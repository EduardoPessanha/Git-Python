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
while True:
    nome.append(str(input('Nome do aluno: ')).capitalize())
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
    if resp in 'Nn':
        break
print(linha1)
print(f'{"Nº":<4}{"Nome":<20}{"Média"}')
print('=' * 30)
boletim.sort()
for ind, el in enumerate(boletim):
    print(f'{ind + 1:<4}{el[0]:<20}{el[2]:>5.2f}')
print(linha1)
while True:
    nAluno = int(input('Mostrar as notas de qual aluno (999 interrompe)? '))
    if nAluno == 999:
        print(linha1)
        print('<<<< VOLTE SEMPRE >>>>')
        break
    if nAluno <= len(boletim):
        print(f'As notas de {boletim[nAluno - 1][0]} são: {boletim[nAluno - 1][1]}')
        print(linha1)

# *************************** SOLUÇÃO DO GUSTAVO GUANABARA ***************************
# boletim = list()
# while True:
#     nome = str(input('Nome: ')).capitalize()
#     nota1 = float(input('Nota 1: '))
#     nota2 = float(input('Nota 2: '))
#     media = (nota1 + nota2) / 2
#     boletim.append([nome, [nota1, nota2], media])
#     while True:
#         resp = str(input('Deseja continuar (S/N)? ')).upper().strip()[0]
#         if resp not in "SsNn":
#             print('Entrada INVÁLIDA!. ', end='')
#         else:
#             break
#     if resp in 'Nn':
#         break
# boletim.sort()
# print(linha1)
# print(f"{'N.º':<4}{'Nome':<20}{'Média':^6}")
# print('-=' * 15)
# for i in range(0, len(boletim)):
#     print(f'{(i + 1):<4}{boletim[i][0]:<20}{boletim[i][2]:^6.2f}')
# print(linha1)
# while True:
#     nAluno = int(input('Mostrar as notas de qual aluno (999 interrompe)? '))
#     if nAluno == 999:
#         print(linha1)
#         print('<<<< VOLTE SEMPRE >>>>')
#         break
#     if nAluno <= len(boletim):
#         print(f'As notas de {boletim[nAluno - 1][0]} são: {boletim[nAluno - 1][1]}')
#         print(linha1)
