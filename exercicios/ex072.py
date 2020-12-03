# ************************* Desafio 072 ************************* #
#                       Número por Extenso                        #
# Crie um programa que tenha uma Tupla totalmente preenchida com  #
# uma contagem por extenso, de zero até vinte.                    #
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e #
# mostrá-lo por extenso                                           #
# *************************************************************** #
titulo = ' Número por Extenso '
cor = '\033[1;36m'
linha = '='*60
print(f"\n{cor}{titulo:#^60}\033[m\n")
resp = ' '
extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis',
           'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
           'dezoito', 'dezenove', 'vinte')
while resp not in 'Nn':
    while True:
        n = int(input('Digite um número inteiro entre 0 e 20: '))
        if n < 0 or n > 20:
            print('O número deve estar entre 0 e 20. Tente outra vez!\n')
        else:
            break
    print(f'\nO número digitado foi {extenso[n]}\n')
    while True:
        resp = str(input('Deseja escolher outro número? (S/N) ')
                   ).upper().strip()[0]
        print(f'{linha}')
        if resp not in 'SsNn':
            print('Por favor digite S/N. Tente outra vez!')
        else:
            break
print('\nPrograma encerrado! Volte sempre!\n')
