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
def pyhelp(nome):
    from time import sleep
    texto = f"Acessando o manual do comando '{nome}'"
    print(f'\033[1;30;44m*' * (len(nome) + 37))
    print(f'{texto:>38}')
    print('*' * (len(nome) + 37))
    print('\033[m\033[1;7;30m')
    help(nome)
    sleep(2)


# Rotina principal
while True:
    print(f'\033[m\033[1;30;42m*' * 28)
    print(f'{"SISTEMA DE AJUDA PyHELP:":^28}')
    print(f"{'*' * 28}")
    func = (str(input('\033[mFunção de Biblioteca -> ')))
    if func == 'fim':
        break
    else:
        pyhelp(func)
print(f'\033[m\033[1;30;41m*' * 14)
print(f'{"ATÉ LOGO!:":^14}')
print(f"{'*' * 14}")
