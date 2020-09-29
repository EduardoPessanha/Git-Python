# ************************** Desafio 076 ************************** #
#                     Lista de Preços com Tupla                     #
# Crie um programa que tenha uma tupla única com nomes de produtos  #
# e seus respectivos preços, na sequência. No final, mostre uma     #
# listagem de preços, organizando os dados em forma tabular.        #
# ***************************************************************** #
titulo = ' \033[1;35mLista de Preços com Tupla\033[m '
linha = '=-'*25
print()
print(linha)
print(f'{titulo:$^60}')
print(linha)
produto = ('Lapis', 1.75, 'Borracha', 2.50, 'Caderno', 12.90,
           'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
           'Mochila', 120.32, 'Canetas', 27.00, 'Livro', 34.90)
for n in range(0, len(produto), 2):
    print(f'{produto[n]:.<40}R$ {produto[n+1]:>7.2f}')
print(linha, '\n')

#             Solução do Gustavo Guanabara:

for i in range(0, len(produto)):
    if i % 2 == 0:
        print(f'{produto[i]:.<40}', end='')
    else:
        print(f'R${produto[i]:>7.2f}')
print(linha, '\n')
