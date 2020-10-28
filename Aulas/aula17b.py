azul = '\033[1;34m'
amarelo = '\033[1;33m'
normal = '\033[m'
print(f'''{azul}
# ***************************************************** #
#                  Python 3 - Aula 017                  #
#        VARIÁVEIS COMPOSTAS - LISTAS (Parte 2)         #
# ***************************************************** #
  
# LISTAS COMPOSTAS:
\033[1m
pessoas = list()

pessoas:
----------------------------------------------------------
| ................ | ................ | ................ |
| : 'Pedro' : 25 : | : 'Maria' : 25 : | : 'João'  : 23 : |
| :.........:....: | :.........:....: | :.........:....: |
|     0       1    |    0        1    |     0       1    |
----------------------------------------------------------
          0                 1                  2       \033[m{normal}''')

dados = list()
dados.append('Pedro')
dados.append(25)
# pessoas.append(dados[:])
# print(dados[0])
# print(dados[1])
# print()

pessoas = [['Pedro', 25], ['Maria', 19], ['João', 23]]

print(f'''{amarelo}
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 23]]

print(pessoas) =>{normal} ''', end=' ')
print(pessoas)
print(f'''{amarelo}
print(pessoas[0][0]) =>{normal} ''', end=' ')
print(pessoas[0][0])
print(f'''{amarelo}
print(pessoas[1][1]) =>{normal} ''', end=' ')
print(pessoas[1][1])
print(f'''{amarelo}
print(pessoas[2][0]) =>{normal} ''', end=' ')
print(pessoas[2][0])
print(f'''{amarelo}
print(pessoas[1]) =>{normal} ''', end=' ')
print(pessoas[1])
print()
teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)
galera = list()
# Desta forma estamos fazendo uma ligação entre teste e galera!!!!
galera.append(teste)
print(galera)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)

galera.pop()
galera.pop()
teste[0] = 'Gustavo'
teste[1] = 40
# desta forma (teste[:]) estamos COPIANDO teste para galera!!!!
galera.append(teste[:])
print(galera)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
print()
galera1 = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera1:
    print(f'{p[0]} tem {p[1]} anos de idade')

galera2 = list()
dados = list()
totMaior = totMenor = 0
for c in range(0, 3):
    dados.append(str(input('None: ')))
    dados.append(int(input('Idade: ')))
    galera2.append(dados[:])
    dados.clear()
# print(galera2)

for p in galera2:
    if p[1] > 21:
        print(f'{p[0]} é maior de idade!')
        totMaior += 1
    else:
        print(f'{p[0]} é menor de idade!')
        totMenor += 1

print(f'Temos {totMaior} maiores e {totMenor} menores de idade')
print()
