azul = '\033[1;34m'
amarelo = '\033[1;33m'
normal = '\033[m'
print(f'''{azul}
# ***************************************************** #
#                  Python 3 - Aula 019                  #
#        VARIÁVEIS COMPOSTAS - DICIONÁRIOS              #
# ***************************************************** #

# Ao contrário das sequências, que são indexadas por um intervalo de números, # os dicionários são
# indexados por chaves (keys), que podem ser de qualquer tipo IMUTÁVEL; strings e números
# sempre podem ser chaves. Tuplas podem ser usadas como chaves se contiverem apenas strings, números
# ou tuplas; se uma tupla contém qualquer objeto mutável direta ou indiretamente, ela não pode ser
# usada como uma chave (key).
#
# Você NÃO PODE USAR listas COMO CHAVES, já que as listas podem ser # modificadas no local usando
# atribuições de índice, atribuições de fatias ou métodos como e .append() e .extend()
#
# Um dicionário é formado por um conjunto de pares "chave: valor" ("key: value"), com o requisito 
# de que as chaves sejam exclusivas ( dentro de um dicionário ).
#
# Um par de chaves cria um dicionário vazio: {'{}'}.
#
# Colocar uma lista separada por vírgulas de pares "chave: valor" entre colchetes adiciona pares "chave:
# valor" inicial ao dicionário; esta também é a forma como os dicionários são escritos na saída.
#
# As principais operações em um dicionário são armazenar um valor com alguma chave e extrair o valor
# fornecido pela chave. Também é possível excluir um par "chave: valor" com del. Se você armazenar
# usando uma chave que já está em uso, o valor antigo associado a essa chave será esquecido ( substituído ). 
#
# É um erro extrair um valor usando uma chave inexistente.
# 
# Aqui está um pequeno exemplo usando um dicionário :

tel = {"{'jack': 4098, 'sape': 4139}"} => \033[m''', end='')
tel = {'jack': 4098, 'sape': 4139}
print(tel)
print('''\n\033[1;34mInserindo um elemento no dicionário:
tel['guido'] = 4127 => \033[m''', end='')
tel['guido'] = 4127
print(tel)
print('''\n\033[1;34mExtraindo o valor de uma chave do dicionário:
print(tel['jack']) => \033[m''', end='')
print(tel['jack'])
print('''\n\033[1;34mApagando um elemento do dicionário:
del tel['sape']
print(tel) => \033[m''', end='')
del tel['sape']
print(tel)
print('''\n\033[1;34mOrdenando os elementos do dicionário:
tel['irv'] = 4127
print(list(tel)) => \033[m''', end='')
tel['irv'] = 4127
list(tel)
print(list(tel))
print('''\033[1;34mprint(sorted(tel)) => \033[m''', end='')
print(sorted(tel))
print('''\n\033[1;34mVerificando se existe o elemento no dicionário:
print('guido' in tel) => \033[m''', end='')
print('guido' in tel)
print('''\033[1;34mprint('jack' not in tel) => \033[m''', end='')
print('jack' not in tel)

# Outros exemplos:

# Declarando dicionários:

dados = {}  # Dicionário declarado com uma estrutura vazia
print('\ndados = {}\ntype(dados) => ', end='')
print(type(dados))
print('print(dados) => ', end='')
print(dados)
dados = {'nome': 'Pedro', 'idade': 25}
print(f"dados = {{'nome': 'Pedro', 'idade': 25}}\nprint(dados) => ", end='')
print(dados)
print("dados = dict([('nome', 'Pedro'), ('idade', 25), ('sexo', 'masculino'),"
      " ('peso', 78)])\nprint(dados) => ", end='')
dados = dict([('nome', 'Pedro'), ('idade', 25), ('sexo', 'masculino'), ('peso', 78)])
print(dados)

# Exibindo dicionários e seus elementos:

print(f"O {dados['nome']} tem {dados['idade']} anos"
      f" de idade, é do sexo {dados['sexo']} e pesa {dados['peso']:.2f} Kg.")
# Nos dicionários o append() não funciona.
print(f'''filme = {{'titulo': 'star Wars',"
        'ano': 1977,"
        'diretor': 'George Lucas'
        }}\nprint(filme.values()) => ''', end='')
filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'
         }
print(filme.values())
print('print(filme.keys() => ', end='')
print(filme.keys())
print('print(filme.items()) => ', end='')
print(filme.items())

print('''\nfor k,v in filme.items():
    print(f'O {} é {}')''')
for k, v in filme.items():
    print(f'O {k} é {v}')
print('''
locadora = [{'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'},
            {'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedom'},
            {'titulo': 'Matrix', 'ano': 1999, 'diretor': 'Wachowski'}
            ]
print(locadora[0]['ano']) => ''', end='')
locadora = [{'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'},
            {'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedom'},
            {'titulo': 'Matrix', 'ano': 1999, 'diretor': 'Wachowski'}
            ]

print(locadora[0]['ano'])
print("print(locadora[2]['titulo']) => ", end='')
print(locadora[2]['titulo'])

# video: 16:29
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 25}
print(pessoas)
print(pessoas['nome'])
# Na hora de se referenciar os elementos do dicionário  usa-se colchetes:
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
#  Nos dicionários não usamos o enumerate(), nos usamos o items():
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()
pessoas['nome'] = 'Leandro'
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')

# Criando um dicionário dentro de uma lista:
print()

estado1 = {'uf': 'Rio de janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
Brasil = list()
Brasil.append(estado1)
Brasil.append(estado2)
print(estado1)
print()
print(estado2)
print()
print(Brasil)
print()
print(Brasil[0])
print()
print(Brasil[0]['uf'])

# estado = dict()
# Brasil = list()
# print()

# for c in range(3):
#     estado['uf'] = str(input('Unidade Federativa: '))
#     estado['sigla'] = str(input('Sigla do Estado: '))
#     Brasil.append(estado)   # Não vai funcionar corretamente!!!!
# print(Brasil)
# print()

estado = dict()
Brasil = list()
for c in range(3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    Brasil.append(estado.copy())  # No caso dos diconarios deve-se usar o comando copy()!
print(Brasil)

for e in Brasil:  # Para cada estado em Brasil que é uma lista
    # print(e)        # mostra o estado que é um dicionário
    for k, v in e.items():  # chave (k) e valor (v) em objeto gerado pelo for anterior -> 'e', que é um dicionário
        print(f'O campo {k} vale {v}')

for e in Brasil:  # Esse laço se refere a lista
    for v in e.values():  # Esse laço se refere ao dicionário
        print(v, end=' ')
    print()
