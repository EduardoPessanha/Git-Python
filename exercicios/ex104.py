from utilitarios import titulo, cor
# **************************** Desafio 104 ************************** #
#                 Validando entrada de dados em Python                #
# Crie um programa que tenha a função leiaInt(), que vai funcionar de #
# forma semelhante 'a função input() do Python, só que fazendo a      #
# validação para aceitar apenas um valor numérico.                    #
# Ex: n = leiaInt('Digite um n: ')                                    #
# ******************************************************************* #
#
titulo(' Validando entrada de dados em Python ')
# ******************************************************************* #


# definindo a função:
def leiaint(texto):
    """
    -> Le uma string de entrada e faz a validação
    para aceitar apenas um valor numérico.
    :param texto: String a ser validada
    :return: n
    """
    while True:
        n = str(input(texto))
        if n.isnumeric():
            n = int(n)
            break
        else:
            print(f'{cor("vm")}ERRO: Digite um número inteiro válido.{cor(0)}')
    return n


# Rotina principal:
n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')
