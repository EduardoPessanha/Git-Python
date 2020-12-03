# ************************** Desafio 090 **************************** #
#                        Dicionário em Python                         #
# Faça um programa que leia nome e média de um aluno, guardando       #
# também a situação em um dicionário. No final, mostre o conteúdo da  #
# estrutura na tela.                                                  #
# ******************************************************************* #
linha = '++' * 24
título = ' \033[1;3;4;7;37mDicionário em Python\033[m '
print(f'\n{título:*^64}\n')
print(linha)
# ******************************************************************* #
boletim = dict()
boletim['aluno'] = str(input('Nome do aluno: ')).capitalize()
boletim['média'] = float(input(f'Média de {boletim["aluno"]}: '))
if boletim['média'] < 5 :
    boletim['situação'] = 'REPROVADO'
elif boletim['média'] < 7:
    boletim['situação'] = 'RECUPERAÇÃO'
else:
    boletim['situação'] = 'APROVADO'
print(linha)
# print(f'O nome do aluno é {boletim["aluno"]}')
# print(f'A média é igual a {boletim["media"]}')
# print(f'Situação é igual a {boletim["situação"]}')
for k, v in boletim.items():
    print(f'- {k.capitalize()} é igual a {v}')
print(linha)
