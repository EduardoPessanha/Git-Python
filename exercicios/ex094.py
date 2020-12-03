# **************************** Desafio 094 ********************************* #
#                     Unindo dicionários e listas                            #
# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando  #
# os dados de cada pessoa em um dicionário e todos os dicionários em uma     #
# lista. No final, mostre:                                                   #
# A) Quantas pessoas foram cadastradas                                       #
# B) A média de idade                                                        #
# C) Uma lista com as mulheres                                               #
# D) Uma lista de pessoas com idade acima da média                           #
# ************************************************************************** #
linha = '+=' * 24
linha1 = '\033[1;34m*=\033[m' * 30
título = ' \033[1;3;4;7;34mUnindo dicionários e listas\033[m '
print(f'\n{título:*^64}\n')
print(linha)
# ************************************************************************** #
cad = dict()
lista = list()
while True:
    # Cadastrando as informações:
    cad['nome'] = str(input('Nome: ')).capitalize().strip()
    while True:
        cad['sexo'] = str(input('Sexo (M/F): ')).upper().strip()[0]
        if cad['sexo'] not in "MF":
            print('Entrada INVÁLIDA.', end=' ')
        else:
            break
    cad['idade'] = int(input('Idade: '))
    lista.append(cad.copy())
    while True:
        resp = str(input('Deseja continuar (S/N)? ')).upper().strip()[0]
        if resp not in "SN":
            print('Entrada INVÁLIDA.', end=' ')
        else:
            break
    if resp == 'N':
        break
# Fim do cadastro.
print(f'\n{linha1}')
# Calculando o total de pessoas cadastradas:
print(f"A) Ao todo foram cadastradas {len(lista)} pessoas.")
# Calculando A média de idade:
tot = 0
for i, v in enumerate(lista):
    tot += v['idade']
média = tot / len(lista)
print(f'B) A média de idades cadastradas foi de {média:.2f} anos.')
# Exibindo uma lista com as mulheres cadastradas:
cont = 0
print('C) As mulheres cadastradas foram: ', end='')
for i, v in enumerate(lista):
    if v['sexo'] in 'F':
        print(f"{v['nome']}", end=' ')
        cont += 1
if cont == 0:
    print('Não houve cadastro de mulheres!')
print()
# Exibindo uma lista de pessoas com idade acima da média:
print('D) Lista de pessoas com idade acima da média:')
for i, d in enumerate(lista):
    if d['idade'] > média:
        print(f"    nome = {d['nome']}; sexo = {d['sexo']}; idade = {d['idade']}")
print(linha1)
print(f'{"<< ENCERRADO >>":^60}')
