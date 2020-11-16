def aumentar(n, taxa=0, fm=False):
    res = n + (n * taxa / 100)
    # if fm:
    #     return moeda(res)
    # return res              ou:
    # return res if fm is False else moeda(res)    ou:
    # return res if not fm else moeda(res)  ou:
    return moeda(res) if fm else res


def diminuir(n=0, taxa=0, fm=False):
    res = n - (n * taxa / 100)
    if fm:
        return moeda(res)
    return res


def dobro(n=0, fm=False):
    res = n * 2
    if fm:
        return moeda(res)
    return res


def metade(n, fm=False):
    res = n / 2
    if fm:
        return moeda(res)
    return res


def moeda(n, m='R$'):
    res = f'{m} {n:.2f}'.replace(".", ",")
    return res
