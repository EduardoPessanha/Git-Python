# *************************** Desafio 092 ***************************** #
#                   Cadastro de Trabalhador em Python                   #
# Crie um programa que leia nome, ano de nascimento e carteira de       #
# trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a    #
# CTPS for diferente de ZERO, o dicionário receberá também o ano de     #
# contratação e o salário. Calcule e acrescente, além da idade, com     #
# quantos anos a pessoa vai se aposentar.                               #
# ********************************************************************* #
from datetime import datetime
linha = '++' * 24
linha1 = '\033[1;34m*=\033[m' * 24
título = ' \033[1;3;4;7;34mCadastro de Trabalhador em Python\033[m '
print(f'\n{título:*^64}\n')
print(linha)
# ********************************************************************* #
# cad = {'nome': '', 'idade': '', 'CTPS': ''}
# print(cad)
cad = dict()
cad['nome'] = str(input('Nome: ')).capitalize().strip()
cad['idade'] = datetime.now().year - (int(input('Ano de Nascimento: ')))
cad['CTPS'] = int(input('Carteira de Trabalho - CTPS (0 não tem): '))
if cad['CTPS'] != 0:
    cad['contratação'] = int(input('Ano de contratação: '))
    cad['salário'] = float(input('Salário: R$ '))
    # Para o exercício consideraremos a aposentadoria após 35 anos de trabalho
    cad['aposentadoria'] = cad['contratação'] + 35 - datetime.now().year + cad['idade']
print(linha1)
for k, v in cad.items():
    print(f'{"- ":>6} {k.capitalize()} tem o valor {v}')
print(linha1)
