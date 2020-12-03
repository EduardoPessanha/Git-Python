# from utilidades import cor
from Exercícios.utilidades.cor import corletra


def leiaint(texto):
    """
    -> Lê um valor de entrada e faz a validação
    para aceitar apenas um valor numérico.
    :param texto: recebe o valor a ser validada.
    :return: retorna um valor Inteiro.
    """
    while True:
        try:
            num = int(input(texto))
        except (ValueError, TypeError):
            print(
                f'{corletra("vm")}ERRO! Digite um número \"Inteiro\" válido!.{corletra()}')
            continue
        except (KeyboardInterrupt, EOFError):
            print(
                f'\n{corletra("az")}O usuário preferiu não digitar esse valor!{corletra()}')
            return 0
        else:
            return num


def leiafloat(texto):
    """
    -> Lê um valor de entrada e faz a validação
    para aceitar apenas um valor Real.
    :param texto: recebe o valor a ser validado.
    :return: retorna um valor Real.
    """
    while True:
        try:
            num = str(input(texto)).replace(',', '.')
            num = float(num)
        except (ValueError, TypeError):
            print(
                f'{corletra("vm")}ERRO! Digite um número \"Real\" válido!.{corletra()}')
            continue
        except (KeyboardInterrupt, EOFError):
            print(
                f'\n{corletra("az")}O usuário preferiu não digitar esse valor!{corletra()}')
            return 0
        else:
            return num


def leiaintold(texto):
    """
    -> Lê uma string de entrada e faz a validação
    para aceitar apenas um valor numérico.
    :param texto: String a ser validada.
    :return: retorna um valor Inteiro.
    """
    while True:
        n = str(input(texto))
        if n.isnumeric():  # Retorna True se houver apenas caracteres numéricos (inteiros),
            # caso contrário retorna False
            n = int(n)
            break
        else:
            print(
                f'{corletra("vm")}ERRO: Digite um número \"Inteiro\" válido. Tente outra vez!{corletra()}')
    return n


def leiafloatold(texto):
    """
    -> Lê uma string de entrada e faz a validação
    para aceitar apenas um valor Real.
    :param texto: Recebe o valor a ser validado.
    :return: retorna um valor Real.
    """
    while True:
        valor = str(input(texto)).strip().replace(',', '.')
        if valor.isalpha() or valor == '' or valor.isnumeric():
            print(
                f'{corletra("vm")}ERRO! Digite um número \"Real\" válido! Tente outra vez!{corletra()}')
        else:
            break
    return f'{float(valor):.2f}'
