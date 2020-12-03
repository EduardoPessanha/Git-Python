from utilitarios import titulo
# **************************** Desafio 106 ************************** #
#                Sistema interativo de ajuda em Python                #
# Faça um mini-sistema que utilize o Interactive Help do Python. O    #
# usuário vai digitar o comando e o manual vai aparecer. Quando o     #
# usuário digitar a palavra 'FIM', o programa se encerrará.           #
# Importante: use cores.                                              #
# ******************************************************************* #
#
titulo(' Sistema interativo de ajuda em Python ')
# ******************************************************************* #


# Definindo as funções:
def pyhelp():
    while True:
        texto = "SISTEMA DE AJUDA PyHELP:"
        t = len(texto) + 4
        print(f'\033[m\033[1;30;42m*' * t)
        print(f'{texto:^{t}}')
        print(f"{'*' * t}")
        func = (str(input('\033[mFunção de Biblioteca -> ')))
        if func.upper() == 'FIM':
            break
        else:
            manual(func)
    saida()


def manual(nome):
    from time import sleep
    texto = f"Acessando o manual do comando '{nome}'"
    t = len(texto) + 4
    print(f'\033[1;30;44m*' * t)
    print(f'{texto:^{t}}')
    print('*' * t)
    print('\033[m\033[1;7;30m')
    help(nome)
    sleep(2)


def saida():
    texto = '"ATÉ LOGO!:"'
    t = len(texto) + 4
    print(f'\033[m\033[1;30;41m*' * t)
    print(f'{texto:^{t}}')
    print(f"{'*' * t}")


# Rotina principal:
pyhelp()
