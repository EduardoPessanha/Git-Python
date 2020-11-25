from utilitarios import titulo, leiaint

# ************************ Desafio 115a *********************** #
#                      Arquivos com Python                      #
#  Vamos ver como fazer acesso a arquivos usando o Python.      #
# ************************************************************* #
titulo('Arquivos com Python')
# ************************************************************* #


def linha(simb='=', comp=40):
    return print(simb * comp)


def texto(msg=''):
    return print(f'{msg.upper():^40}')


def menuprincipal():
    texto('MENU PRINCIPAL')
    linha('*')
    print(f"{'  1 - Ver pessoas cadastradas'}\n{'  2 - Cadastrar nova pessoa'}\n{'  3 - Sair do Sistema'}")
    linha('*')
    return


def opcao(num=1):
    linha('*')
    texto(f'Opção {num}')
    linha('*')
    return


# Rotina principal:

linha('*')
menuprincipal()
while True:
    while True:
        op = leiaint('Sua opção: ')
        if op > 3:
            print(f'ERRO! Opção inválida. Tente outra vez.')
        else:
            break
    if op == 3:
        linha('*')
        texto('Saindo do sistema')
        break
    opcao(op)
    menuprincipal()
