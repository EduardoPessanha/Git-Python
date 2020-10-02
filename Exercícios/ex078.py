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
valores = []
for valor in range(0, 5):
    valores.append(int(input('Digite um número inteiro: ')))
print(f'\n{linha}')
print('\nOs números digitados foram: ', end='')
for n in range(0, len(valores)):
    if n < len(valores)-1:
        print(f'{valores[n]}', end=' ')
    else:
        print(f'{valores[n]}\n')
maior = max(valores)
menor = min(valores)
posM = valores.index(maior)+1
posm = valores.index(menor)+1
print(f"O maior valor digitado foi {maior}, na posição {posM}!")
print(f'O menor valor digitado foi {menor}, na posição {posm}!\n')

# ************************************************************ #

# for pos, c in enumerate(valores):
#     print(f'Na posição {pos+1} encontrei {c}')
