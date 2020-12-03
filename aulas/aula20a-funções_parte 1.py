azul = '\033[1;34m'
amarelo = '\033[1;33m'
normal = '\033[m'
print(f'''{azul}
# ***************************************************** #
#                  Python 3 - Aula 020                  #
#                   FUNÇÕES - PARTE 1                   #
# ***************************************************** #
''')
#
# Ao sair e entrar de novo no interpretador Python, as definições anteriores (funções e variáveis) são perdidas.
# Portanto, se quiser escrever um programa maior, será mais eficiente usar um editor de texto para preparar as
# entradas para o interpretador, e executá-lo usando o arquivo como entrada. Isso é conhecido como criar um
# script. Se o programa se torna ainda maior, é uma boa prática dividi-lo em arquivos menores, para facilitar
# a manutenção. Também é preferível usar um arquivo separado para uma função que você escreveria em vários
# programas diferentes, para não copiar a definição de função em cada um deles.
#
# Para permitir isso, o Python tem uma maneira de colocar as definições em um arquivo e então usá-las em um
# script ou em uma execução interativa do interpretador. Tal arquivo é chamado de módulo; definições de um
# módulo podem ser importadas para outros módulos, ou para o módulo principal (a coleção de variáveis a que você
# tem acesso num script executado como um programa e no modo calculadora).
#
# Um módulo é um arquivo contendo definições e instruções Python. O nome do arquivo é o nome do módulo acrescido
# do sufixo .py. Dentro de um módulo, o nome do módulo (como uma string) está disponível como o valor de
# variável global
# Um módulo pode conter tanto instruções executáveis quanto definições de funções e classes. Essas instruções
# servem para inicializar o módulo. Eles são executados somente na primeira vez que o módulo é encontrado em uma
# instrução de importação. [1] (Também rodam se o arquivo é executado como um script.)
# [1] Na verdade, definições de funções também são ‘instruções’ que são ‘executados’; a execução da definição de
# uma função coloca o nome da função na tabela de símbolos global do módulo.
#

# A função está ligada a palavra rotina!!! São coisas que se faz repetidamente!
# Por exemplo:
# Mostrar uma linha na tela - podemos criar uma função para isso: mostralinha()
# print('-----------------------------------------------')
# print('              SISTEMA DE ALUNOS                ')
# print('-----------------------------------------------')
#
# print('-----------------------------------------------')
# print('           CADASTRO DE FUNCIONÁRIOS            ')
# print('-----------------------------------------------')
#
# print('-----------------------------------------------')
# print('               ERRO DO SISTEMA                 ')
# print('-----------------------------------------------')
#
# Assim percebemos que repetimos várias vezes o mesmo comando print('-----------------------------------------------')
# Logo podemos criar uma rotina para executar o comando:
#
# def mostralinha():
# print('-----------------------------------------------')
#
#
# mostralinha()
# print('              SISTEMA DE ALUNOS                ')
# mostralinha()
#
# mostralinha()
# print('           CADASTRO DE FUNCIONÁRIOS            ')
# mostralinha()
#
# mostralinha()
# print('               ERRO DO SISTEMA                 ')
# mostralinha()

print('-' * 30)
print(f'{"CURSO EM VIDEO":^30}')
print('-' * 30)
print('-' * 30)
print(f"{'APRENDENDO PYTHON':^30}")
print('-' * 30)
print(f"{'GUSTAVO GUANABARA':^30}")
print('-' * 30)


def lin():  # Exibe uma linha com 30 caracteres
    print('-' * 30)


# Rotina principal:
lin()
print(f'{"CURSO EM VIDEO":^30}')
lin()
print(f"{'APRENDENDO PYTHON':^30}")
lin()
print(f"{'GUSTAVO GUANABARA':^30}")
lin()


#  Podemos personalizar ainda mais:
#
# print('-----------------------------------------------')
# print('           CADASTRO DE FUNCIONÁRIOS            ')
# print('-----------------------------------------------')
#
# def mensagem(msg)
#   print('-----------------------------------------------')
#   print(msg)
#   print('-----------------------------------------------')
#
#
# mensagem('SISTEMA DE ALUNOS')
#


def mensagem(msg):
    print('-' * 30)
    print(f'{msg:^30}')
    print('-' * 30)


#  Rotina principal:
mensagem('SISTEMA DE ALUNOS')

# Alguns exemplos

a = 5
b = 6
s = a + b
print(s)

a = 7
b = 3
s = a + b
print(s)

a = 5
b = 9
s = a + b
print(s)


def soma(a, b):
    print(a + b)


# Rotina principal:
lin()
soma(5, 6)
soma(7, 3)
soma(5, 9)
lin()


# se fizermos assim:
# soma(3, 5, 6)    # Vai gerar um ERRO! -> a função soma criada só recebe 2 parâmetros!!!!!
# Empacotamento de parâmetros:
#
# def contador(*num):   # * -> é o símblo de desempacotar!!!!
#
#
# contador(5,7,6,3,1,4)
# contador(3,2,1)
#
# Deste modo de desempacotamento iremos gerar tuplas!


def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print()
    print('FIM!')
    tam = len(num)
    print(f"Recebi os valores {num} e são ao todo {tam} números")


lin()
# Rotina principal:
contador(2, 1, 7)
contador(8, 9)
contador(4, 4, 7, 6, 2)

lin()
# Podemos também trabalhar com listas:

valores = [7, 2, 5, 2, 4]
print(valores)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


dobra(valores)
print(valores)


def soma(*num):
    s = 0
    for v in num:  # para cada valor(v) em num:
        s += v
    print(f'A soma de {num} é igual a {s}')


lin()
soma(5, 2)
soma(2, 9, 4)
