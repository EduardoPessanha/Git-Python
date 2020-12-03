from utilitarios import corlinha
print(f'''{corlinha('vd')}
# ***************************************************** #
#                  Python 3 - Aula 022                  #
#                   Módulos e Pacotes                   #
# ***************************************************** #
{corlinha('az')}''')


# ****************************************************************************** #
# Modularização (é o ato de construir módulos): -> "Dividir para Conquistar"
#     - Surgiu no início da década de 60
#     - Sistemas ficando cada vez maiores
#
# Foco:
#     - Dividir programas grandes em menores
#     - Aumentar a legibilidade
#     - Facilitar a manutenção do sistema
#
# Vantagens da modularização:
#     - organização do código
#     - facilidade na manutenção
#     - ocultação do código detalhado
#     - reutilização em outros projetos


def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f


num = int(input('Digite um número para calcular o seu fatorial: '))
print("""

def fatorial(n):
    f = 1
    for c in range(1, n +1):
        f *= c
    return f


num = int(input('Digite um número para calcular o seu fatorial: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}') -> """, end='')
fat = fatorial(num)
print(corlinha(), end='')
print(f'O fatorial de {num} é {fat}')
print(corlinha('az'))

#  Os pacotes precisam ser criados dentro do projeto
print("""
# As funções foram separadas do programa princial e foram colocadas
# dentro do arquivo uteis.py, que passa a ser chamado de módulo:
#
#                ************** uteis.py **************
#                *                                    *
#                *   def fatorial(n):                 *
#                *       f = 1                        *
#                *       for c in range(1, n + 1):    *
#                *           f *= c                   *
#                *       return f                     *
#                *                                    *
#                *                                    *
#                *   def dobro(n):                    *
#                *       return n * 2                 *
#                *                                    *
#                *                                    *
#                *   def triplo(n):                   *
#                *       return n * 3                 *
#                *                                    *
#                **************************************
#
# Pacotes (em outras linguagens de programação são as bibliotecas):
#
# São junções de módulos separados por assuntos
#
# Todo arquivo .py pode ser potencialmente um módulo!
#
# Dentro de um projeto python toda pasta é considerada um pacote, ou seja 
# o PACOTE é uma pasta que contém módulos! 
#
# Criando um pacote:
#
# Se dentro do projeto nós temos um módulo, basta criar uma pasta
# com o nome do módulo e teremos agora um pacote.
# Por exemplo:
# Criamos uma pasta chamada uteis, e dentro dela criamos outras
# pastas chamdas cores, datas, números, strings
# os nomes dos arquivos dentro dos pacotes tem um nome especial: __init__.py""")
