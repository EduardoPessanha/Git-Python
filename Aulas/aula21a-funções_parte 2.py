from funcCor import cor
print(f'''{cor('am')}
# ***************************************************** #
#                  Python 3 - Aula 021                  #
#                   FUNÇÕES - PARTE 2                   #
# ***************************************************** #
\033[1m{cor('az')}''')
#
#   - interactive Help
#   - docstrings
#   - Argumentos opcionais
#   - Escopo de variáveis
#   - Retorno de Resultados
#
#  - interactive help (ajuda interativa):
#
# interactive help => help()  => mostra o manual de qualquer função ou biblioteca do
#                                Python (para sair, digite 'q' ou quit)
# Exemplo:
# help(input)
print('Exemplo => help(input):')
print(f'\033[7m{cor("ci")}')
help(input)
print(f'{cor(0)}\033[1m{cor("az")}')
# help()
#
# Outra forma de se obter ajuda é usar: print(função.__doc__)
# Exemplo: print(input.__doc__)
print('Exemplo => print(input.__doc__):')
print(f'\033[7m{cor("ci")}{input.__doc__}{cor(0)}\033[1m{cor("az")}')


#
#
# - docstring:
#
#
# def contador(i, f, p):          # => O docstring é toda a informação contida entre as 3 aspas duplas
#     """                         #    logo abaixo da definição da função.
#     Faz uma contagem e mostra na tela.
#     :param i: início da contagem
#     :param f: fim da contagem
#     :param p: passo da contagem
#     :return: sem retorno
#     """
#     c = i
#     while c <= f:
#         print(f'{c}', end=' ')
#         c += p
#     print('FIM!')
#
# contador(10,100,10)
#
# - Parâmetros opcionais:
#
# def somar(a=0, b=0, c=0):     # Ao definirmos o valor 0 para os parâmetros da função, os tornamos opcionais.
#   s = a + b + c
#   print(f'A soma vale {s}')
#
# Os exemplos a seguir, não dariam erro algum na execução da função:
#
# somar(3, 2, 5)
# somar(8, 4)
# somar()
#
def somar(a=0, b=0, c=0):
    """
    -> Faz a soma e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    Função criada pr Gustavo Guanabara no canal CursoemVídeo.
    """
    s = a + b + c
    print(f'A soma vale {s}.')


print('somar(3, 2, 5) => ', end='')
somar(3, 2, 5)
print('somar(3, 2) => ', end='')
somar(3, 2)
print('somar() => ', end='')
somar()
print('somar(c=4, a=2) => ', end='')
somar(c=4, a=2)
#


def teste():
    x = 8
    print(f'{cor("br")}Na função teste, n vale {n}.')
    print(f'Na função teste, x vale {x}.{cor("az")}')


print("""\n
# - Escopo de variáveis:
# 
# É o local onde uma variável existe ou o local onde uma variável não existe!!!
#
def teste(): 
    x = 8
    print(f'Na função teste, n vale {n}.')
    print(f'Na função teste, x vale {x}.')
# 
# 
# Programa principal:
print('n = 2')
print("print(f'No programa principal n vale {n}.') => """, end='')
n = 2
print(f'{cor("br")}No programa principal n vale {n}.{cor("az")}')
print('''teste() :''')
teste()
print('''print(f'No programa principal x vale {x}.') => dará erro, porque a variável x foi declarada na função teste(),
#                                              assim ela só existe nesta função.
# A variável x é uma variável local, porque ela só existe na função de teste(), enquanto a variável n é uma 
# variável global, que foi declarada no programa principal. \n''')


def teste1(b):
    # global a      # O comando 'global' permite que uma variável global possa ser usada dentro das funções.
    a = 8
    b += 4
    c = 2
    print(f'{cor("br")}Na função teste1(), a dentro(local) vale {a}.')
    print(f'{cor("br")}Na função teste1(), b dentro(local) vale {b}.')
    print(f'{cor("br")}Na função teste1(), c dentro(local) vale {c}.')


a = 5
teste1(a)
print(f'No programa principal, a fora(global) vale {a}.{cor("az")}')
#
# - Retorno de resultados: => return
#
print('''\n
# - Retorno de valores:
# 
# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     return s
# 
# 
# r1 = somar(3, 2, 5)
# r2 = somar(2, 2)
# r3 = somar(6)
# print(f'Os resultados foram {r1}, {r2} e {r3}') => ''', end='')


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'{cor("br")}Os resultados foram {r1}, {r2} e {r3}{cor("az")}')
