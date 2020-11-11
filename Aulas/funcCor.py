def cor(tipo):
    """
    Altera a cor do texto.
    :param tipo: indica qual a cor desejada:
    br = branca, vm = vermelho, vd = verde, am = amarelo, az = azul
    ma = magenta, ci = ciânico, cz = cinza, 0 = restaura cor padrão
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

