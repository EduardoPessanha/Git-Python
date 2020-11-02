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
