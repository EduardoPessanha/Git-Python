# ************************** Desafio 083 **************************** #
#                  Validando expressões matemáticas                   #
# Crie um programa onde o usuário digite uma expressão qualquer que   #
# use parênteses. Seu aplicativo deverá analisar se a expressão       #
# passada está com os parênteses abertos e fechados na ordem correta. #
# ******************************************************************* #
linha = '++'*25
título = ' \033[1;7;31mValidando expressões matemáticas\033[m '
print(f'\n{título:*^60}\n')
print(linha)
# ******************************************************************* #
expressão = str(input('Digite uma expressão com parênteses: '))
abre = expressão.count('(')
fecha = expressão.count(')')
if abre != fecha:
    print('Expressão INVÁLIDA!')
else:
    print('Expressão OK!')
