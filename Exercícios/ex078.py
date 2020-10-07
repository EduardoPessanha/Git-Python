# ************************** Desafio 078 ************************** #
#                  Maior e Menor valores na Lista                   #
# Faça um programa que leia 5 valores numéricos e guarde-os em uma  #
# lista. No final, mostre qual foi o maior e o menor valor digitado #
# e as suas respectivas posições na lista.                          #
# ***************************************************************** #
titulo = ' \033[1;32mMaior e Menor valores na Lista\033[m '
linha = '*'*60
print(f'\n{titulo:#^70}\n')
print(f'{linha}\n')
# ***************************************************************** #
valores = []
cont = 1
for valor in range(0, 5):
    valores.append(int(input(f'Digite o {cont}º valor: ')))
    cont += 1
print(f'\n{linha}')
print('Os números digitados foram: ', end='')
for n in range(0, len(valores)):
    if n < len(valores)-1:
        print(f'{valores[n]}', end=' ')
    else:
        print(f'{valores[n]}')
maior = max(valores)
posM = valores.index(maior) + 1
menor = min(valores)
posm = valores.index(menor)+1
print(f"O maior valor digitado foi {maior}, nas posições ", end='')
for pos, c in enumerate(valores):
    if c == maior:
        print(f'{pos + 1}', end=' ')
print(f'\nO menor valor digitado foi {menor}, nas posições ', end='')
for pos, c in enumerate(valores):
    if c == menor:
        print(f'{pos + 1}', end=' ')
print(f'\n{linha}\n')
