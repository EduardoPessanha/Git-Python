# ************************* Desafio 071 ************************* #
#                 Simulador de Caixa Eletronico                   #
# Crie um programa que simule o funcionamento de um caixa         #
# eletronico. No início, pergunte ao usuário qual será o valor    #
# a ser sacado (número inteiro) e o programa vai informar quantas #
# cédulas de cada valor serão entregues.                          #
#                                                                 #
# OBS:                                                            #
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1. #
# *************************************************************** #

# Inicializando variáveis:*******************************
título, banco = ' Simulador de Caixa Eletrônico ', 'BANCO POPPEPE'
l1, l2 = '@' * 36, '~' * 36
cedula = 50
# quant = 0
# ********************************************************
print(f'\n\033[1;34m{título:$^60}\033[m\n')
print(f'{l1}\n{banco:^36}\n{l1}\n')
num = int(input('Qual valor você quer sacar? R$'))
print(f'{l2}')
while True:
    quant = num // cedula
    if quant != 0:
        print(f'Total de cédulas de R${cedula:>5.2f} = {quant}')
    num = num - quant * cedula
    if cedula == 50:
        cedula = 20
    elif cedula == 20:
        cedula = 10
    elif cedula == 10:
        cedula = 1
    elif num == 0:
        break
print(f'{l2}')
print('Volte sempre. Tenha um bom dia!!!\n')

# ################################################################## #
#          SOLUÇÃO DO EXERCÍCIO SEM USAR LAÇO DE REPETIÇÃO           #
# ################################################################## #

# c50, c20, c10, c1 = 50, 20, 10, 1
# cedula50, cedula20, cedula10, cedula1 = 0, 0, 0, 0
# cedula50 = num // c50
# if cedula50 != 0:
#     print(f'Total de cédulas de R${c50:.2f} = {cedula50}')
#     num = num - cedula50 * c50
# cedula20 = num // c20
# if cedula20 != 0:
#     print(f'Total de cédulas de R${c20:.2f} = {cedula20}')
#     num = num - cedula20 * c20
# cedula10 = num // c10
# if cedula10 != 0:
#     print(f'Total de cédulas de R${c10:.2f} = {cedula10}')
#     num = num - cedula10 * c10
# cedula1 = num // c1
# if cedula1 != 0:
#     num = num - cedula1 * c1
#     print(f'Total de cédulas de R$ {c1:.2f} = {cedula1}')
# print(f'{linha}')
# print('Volte sempre.  Tenha um bom dia!\n')

# ################################################################## #
#                   SOLUÇÃO DO GUSTAVO GUANABARA                     #
# ################################################################## #

# print('='*30)
# print(f'{" BANCO CEV ":^30}')
# print('='*30)
# valor = int(input('Qual valor você quer sacar? R$'))
# total = valor
# ced = 50
# totced = 0
# while True:
#     if total >= ced:
#         total -= ced
#         totced += 1
#     else:
#         if totced > 0:
#             print(f'Total de {totced} cédulas de R${ced}')
#         if ced == 50:
#             ced = 20
#         elif ced == 20:
#             ced = 10
#         elif ced == 10:
#             ced = 1
#         totced = 0
#         if total == 0:
#             break
# print('='*30)
# print('Volte sempre ao BANCO CEV! Tenha um bom dia!')                
