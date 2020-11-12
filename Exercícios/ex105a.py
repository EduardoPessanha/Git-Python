from utilitarios import titulo

# **************************** Desafio 105 *************************** #
#                   Analisando e gerando Dicionários                   #
# Faça um programa que tenha uma função notas() que pode receber       #
# várias notas de alunos e vai retornar um dicionário com as seguintes #
# informações:                                                         #
#                                                                      #
# - Quantidade de notas                                                #
# - A maior nota                                                       #
# - A menor nota                                                       #
# - A média da turma                                                   #
# - A situação (opcional)                                              #
#                                                                      #
# Adicione também as docstrings dessa função para consulta pelo        #
# desenvolvedor.                                                       #
# ******************************************************************** #
#
titulo(' Analisando e gerando Dicionários ')

# Resumindo o exercício ex105:
# ******************************************************************** #


# Dfinindo a função:
def notas(*n, sit=False):
    """
    ->Recebe várias notas de alunos, e retorna o número
      de notas (aceita várias), a maior e menor nota,
      a média e a situação (opcional)
    :param n: uma ou mais notas
    :param sit: (opcional) indica a situação do aluno
    :return: dicionário com as informações
    """
    informa = dict()
    informa['total'] = len(n)
    informa['maior'] = max(n)
    informa['menor'] = min(n)
    média = float(sum(n) / len(n))
    informa['média'] = f'{média:.2f}'
    if sit:
        if média < 5:
            situação = 'RUÍM'
        elif média < 7:
            situação = 'RAZOÁVEL'
        else:
            situação = 'BOA'
        informa['situação'] = situação
    return informa


# Rotina principal
help(notas)
print('*'*75)
resp = notas(5.5, 3.9, 2, 6.5)
print(resp)
resp = notas(5.5, 3.9, 2, 6.5, sit=True)
print(resp)
