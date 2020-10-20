print('\nLei de Ohm -> V = I x R\n')
fim = ' '
while fim not in 'N':
    print('''Qual a unidade você quer calcular:

        V = Tensão
        I = Corrente
        R = Resistencia
        ''')
    while True:
        opcao = str(input('Escolha a sua opção (V/I/R): ')).upper().strip()[0]
        if opcao not in 'VIR':
            print('Entrada INVÁLIDA.', end=' ')
        else:
            break
    if opcao == 'V':
        I = float(input('Informe o valor da corrente em Aperes: '))
        R = float(input('Informe o valor da resistencia em Ohms: '))
        V = I*R
        print(f'O valor da tensão é {V:.2f} Volts\n')
    elif opcao == 'I':
        V = float(input('Informe o valor da tensão em Volts: '))
        R = float(input('Informe o valor da resistencia em Ohms: '))
        I = V/R
        print(f'O valor da corrente é {I:.2f} Aperes\n')
    elif opcao == 'R':
        V = float(input('Informe o valor da tensão em Volts: '))
        I = float(input('Informe o valor da corrente em Aperes: '))
        R = V/I
        print(f'O valor da resistencia é {R:.2f} Ohms\n')
    while True:
        fim = str(input('Deseja continuar (S/N): ')).upper().strip()[0]
        if fim not in 'SN':
            print('Opção INVÁLIDA.', end=' ')
        else:
            break
    if fim == 'N':
        print()
        break
    else:
        print('-='*30, '\n')
