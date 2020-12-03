# ************************** Desafio 084 **************************** #
#                Lista composta e análise de dados                    #
# Faça um programa que leia nome e peso de várias pessoas, guardando  #
# tudo em uma lista. No final, mostre:                                #
# A) Quantas pessoas foram cadastradas.                               #
# B) Uma listagem com as pessoas mais pesadas.                        #
# C) Uma listagem com as pessoas mais leves.                          #
# ******************************************************************* #
linha = '++' * 25
linha1 = '\033[1;34m*\033[m' * 50
título = ' \033[1;31mLista composta e análise de dados\033[m '
print(f'\n{título:*^60}\n')
print(linha)
# ******************************************************************* #
cad = list()
dados = list()
# nomeMaiorPeso = list()
# nomeMenorPeso = list()
resp = ' '
maiorPeso = menorPeso = cont = 0

# Criando o cadastro:
while resp not in 'Nn':
    dados.append(str(input('Qual é o seu nome: ')))
    dados.append(float(input('Qual é o seu peso? ')))
    # Cadastrando o maior e menor peso:
    if len(cad) == 0:
        maiorPeso = menorPeso = dados[1]
    elif dados[1] > maiorPeso:
        maiorPeso = dados[1]
    elif dados[1] < menorPeso:
        menorPeso = dados[1]
    cad.append(dados[:])
    dados.clear()
    while True:
        resp = str(input('Deseja continuar (S/N)? ')).upper().strip()[0]
        if resp not in 'SsNn':
            print('Entrada inválida!', end=' ')
        else:
            break

# Verificando o maior e menor peso:
# for p in cad:
#     # print(p)
#     if cont == 0:
#         maiorPeso = menorPeso = p[1]
#         cont += 1
#     elif p[1] > maiorPeso:
#         maiorPeso = p[1]
#     elif p[1] < menorPeso:
#         menorPeso = p[1]

# for i in cad:
#     if maiorPeso == i[1]:
#         nomeMaiorPeso.append(i[0])
#     elif menorPeso == i[1]:
#         nomeMenorPeso.append(i[0])

print(linha1, '\n')
print(f'Ao todo, foram cadastradas {len(cad)} pessoas')
print(f'O maior peso cadastrado foi {maiorPeso:.2f} Kg. Peso de ', end='')
for p in cad:
    if maiorPeso == p[1]:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso cadastrado foi {menorPeso:.2f} Kg. Peso de ', end='')
for p in cad:
    if menorPeso == p[1]:
        print(f'[{p[0]}] ', end='')
print()
# Na solução do Gustavo Guanabara, ele já fez a verificação do maior e menor Peso
# no momento do cadastro, antes de adicionar na lista principal,
# o que reduziu o tamanho do programa.
