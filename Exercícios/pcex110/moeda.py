def aumentar(n, taxa=0, fm=False):
    res = n + (n * taxa / 100)
    # if fm:                             ___
    #     return moeda(res)                 |__ ou:
    # return res                         ___|
    # return res if fm is False else moeda(res) ou:
    # return res if not fm else moeda(res)      ou:
    return moeda(res) if fm else res


def diminuir(n, taxa=0, fm=False):
    res = n - (n * taxa / 100)
    if fm:
        return moeda(res)
    return res


def dobro(n, fm=False):
    res = n * 2
    if fm:
        return moeda(res)
    return res


def metade(n, fm=False):
    res = n / 2
    if fm:
        return moeda(res)
    return res


def moeda(n, fm=True, m='R$'):
    if fm:
        res = f'{m} {n:.2f}'.replace(".", ",")
    else:
        res = f'{n:.2f}'
    return res


def resumo(n=0, am=0, dm=0, fm=True, m='R$'):
    """
    Calcula e formata valores para o padrão monetário
    brasileiro.
    :param n: valor
    :param am: valor do aumento
    :param dm: valor do decréscimo
    :param fm: formatação -> padrão: False
    :param m: formato da moeda -> padrão: R$
    :return: sem retorno
    """
    if not n:
        n = 0
    n = float(str(n).replace(',', '.'))
    print('*' * 30)
    print(f'{"RESUMO DO VALOR":>22}')
    print('*' * 30)
    # print(f'{"Preço analisado:":<20}{moeda(n, fm, m)}') (\t -> faz a tabulação) ou:
    print(f'Preço analisado: \t{moeda(n, fm, m)}')
    print(f'Dobro do preço: \t{moeda(dobro(n), fm, m)}')
    print(f'Metade do preço: \t{moeda(metade(n), fm, m)}')
    print(f'{am} % de aumento: \t{moeda(aumentar(n, am), fm, m)}')
    print(f'{dm} % de redução: \t{moeda(diminuir(n, dm), fm, m)}')
    print('*' * 30)
    return
