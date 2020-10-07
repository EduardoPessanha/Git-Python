# ************************** Desafio 083 **************************** #
#                  Validando expressões matemáticas                   #
# Crie um programa onde o usuário digite uma expressão qualquer que   #
# use parênteses. Seu aplicativo deverá analisar se a expressão       #
# passada está com os parênteses abertos e fechados na ordem correta. #
# ******************************************************************* #
linha = '++' * 25
título = ' \033[1;7;31mValidando expressões matemáticas\033[m '
print(f'\n{título:*^60}\n')
print(linha)
# ******************************************************************* #
expressão = str(input('Digite uma expressão: '))
pilha = list()
# *******************************************************************
# O código a seguir NÃO está correto!!!!
# abre = expressão.count('(')
# fecha = expressão.count(')')
# if abre != fecha:
#     print('Expressão INVÁLIDA!')
# else:
#     print('Expressão OK!')
# *******************************************************************
for carc in expressão:
    if carc == '(':
        pilha.append(carc)
    elif carc == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(carc)
            break
if len(pilha) == 0:
    print('Sua expressão está correta')
else:
    print('Sua expressão está errada!')

# ***************************************************************** #
#                 Solução do Gustavo Guanabara                      #
# ***************************************************************** #
# expr = str(input('Digite uma expressão: '))
# pilha = list()
# for simb in expr:
#     if simb == '(':
#         pilha.append(simb)
#     elif simb == ')':
#         if len(pilha) > 0:
#             pilha.pop()
#         else:
#             pilha.append(simb)
#             break
# if len(pilha) == 0:
#     print('Sua expressão está válida!')
# else:
#     print('Sua expressão não é válida!')
