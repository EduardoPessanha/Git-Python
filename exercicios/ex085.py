# ************************** Desafio 085 ***************************** #
#                   Listas com pares e ímpares                         #
# Crie um programa onde o usuário possa digitar sete valores numéricos #
# e cadastre-os em uma lista única que mantenha separados os valores   #
# pares e ímpares. No final, mostre os valores pares e ímpares em      #
# ordem crescente.                                                     #
# ******************************************************************** #
linha = '++' * 25
linha1 = '\033[1;34m*=\033[m'*25
título = ' \033[1;32mListas com pares e ímpares\033[m '
print(f'\n{título:*^60}\n')
print(linha)
# ******************************************************************* #
geral = [[], []]
for n in range(0, 7):
    num = int(input(f'Digite o {n + 1}º valor: '))  # Lendo os 7 números:
    if num % 2 != 0:    # Número digitado é ímpar
        geral[1].append(num)
    else:   # Número digitado é par
        geral[0].append(num)
geral[1].sort()
geral[0].sort()
print(linha1)
print(f'Os valores pares digitados foram: {geral[0]}')
print(f'Os valores ímpares digitados foram: {geral[1]}')
