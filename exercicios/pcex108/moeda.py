def aumentar(n, taxa=0):
    res = n + (n * taxa / 100)
    return res  # moeda(res)
    # return res


def diminuir(n=0, taxa=0):
    res = n - (n * taxa / 100)
    return res  # moeda(res)


def dobro(n=0):
    res = n * 2
    return res  # moeda(res)


def metade(n):
    res = n / 2
    return res  # moeda(res)


def moeda(n, m='R$'):
    res = f'{m} {n:.2f}'.replace(".", ",")
    return res
