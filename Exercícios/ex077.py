# ************************** Desafio 077 ************************** #
#                     Contando vogais em Tupla                      #
# Crie um programa que tenha uma tupla com várias palavras (não     #
# usar acentos). Depois disso, você deve mostrar, para cada palavra,#
# quais são as suas vogais.                                         #
# ***************************************************************** #
titulo = ' \033[1;36mContando vogais em Tupla\033[m '
linha = '*-' * 25
print(f'\n{titulo:+^60}')
palavra = ('carro', 'aviao', 'churrasco', 'teclado', 'computador',
           'aprender', 'programar', 'linguagem', 'Python', 'curso',
           'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'futuro')
for nome in palavra:
    print(f'\nNa palavra {nome.upper()} temos as vogais:', end=' ')
    for vogal in nome:
        if vogal.lower() in 'aeiou':
            print(vogal, end=' ')
print(f'\n{linha}\n')
