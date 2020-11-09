# **************************** Desafio 098 ************************* #
#                          Função de Contador                        #
#  Faça um programa que tenha uma função chamada contador(), que     #
#  receba três parâmetros: início, fim e passo. Seu programa tem que #
#  realizar três contagens através da função criada:                 #
#                                                                    #
# a) de 1 até 10, de 1 em 1                                          #
# b) de 10 até 0, de 2 em 2                                          #
# c) uma contagem personalizada                                      #
# ****************************************************************** #
#
# Definindo as funções:
def lin():
    print('+=' * 24)


def lin1():
    print('\033[1;34m*=\033[m' * 26)


def titulo(msg):
    lin()
    texto = f' \033[1;3;4;7;34m{msg}\033[m '
    print(f'\n{texto:*^64}\n')
    lin()
    print()


titulo('Função de Contador')


# ****************************************************************** #
# def exibe(início, fim, passo):
#     print(f'Contagem de {início} até {fim} de {passo} em {passo}:')


def contador(ini, fim, p):
    if p < 0:
        p = -p
    if p == 0:
        p = 1
    print(f'Contagem de {ini} até {fim} de {p} em {p}:')
    if ini < fim:
        for c in range(ini, fim + 1, p):
            print(c, end=' ')
    else:
        for c in range(ini, fim - 1, -p):
            print(c, end=' ')
    print('FIM!.')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
