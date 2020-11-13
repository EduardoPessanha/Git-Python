def lin():
    print('+=' * 24)


def lin1():
    print('\033[1;34m*=\033[m' * 26)


def cor(tipo):
    """
    Altera a cor do texto:
    br = branca, vm = vermelho, vd = verde, am = amarelo, az = azul
    ma = magenta, ci = ciânico, cz = cinza, 0 = restaura cor padrão
    :param tipo: indica qual a cor desejada:
    :return: retorna o código da cor escolhida
    função criada por Eduardo A. M. Pessanha
    """
    if tipo == 0:
        tipo = '\033[m'
    elif tipo == 'br':
        tipo = '\033[1;30m'
    elif tipo == 'vm':
        tipo = '\033[1;31m'
    elif tipo == 'vd':
        tipo = '\033[1;32m'
    elif tipo == 'am':
        tipo = '\033[1;33m'
    elif tipo == 'az':
        tipo = '\033[1;34m'
    elif tipo == 'mg':
        tipo = '\033[1;35m'
    elif tipo == 'ci':
        tipo = '\033[1;36m'
    elif tipo == 'cz':
        tipo = '\033[1;37m'
    return tipo


def titulo(msg):
    """
    Exibe uma mensagem formatada.
    :param msg: texto a ser exibido
    """
    # print('\033[1;3;34m*' * 48)
    # print(f'{"*"}{"*":>47}')
    texto = f'\033[1;3;4;7;34m{msg}\033[m\033[1;3;34m'
    a = len(msg) + 4
    print('\033[1;3;34m*' * a)
    print(f'{"*":<2}{texto:^{a}}{"*":>2}')
    # print(f'{"*"}{"*":>47}')
    print('*' * a)
    print('\033[m')


def leiaint(texto):
    """
    -> Lê uma string de entrada e faz a validação
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
            print(f'\033[1;31mERRO: Digite um número inteiro válido.\033[m')
    return n
