# from tkinter import *

# janela = Tk()

# texto = "Olá Mundo!, cheguei!"
# label_1 = Label(janela, text = texto, font='Arial:20')


# label_1.place(x=200, y=200)

# janela.geometry('800x600+0+0')
# janela.mainloop()

# ***************************************************************** #

def lin():
    print('+=' * 24)
    print()


def lin1():
    print('\033[1;34m*=\033[m' * 21)
    print()


def titulo(msg):
    print()
    msg = f' \033[1;3;4;7;34m{msg}\033[m '
    # n = int(len(msg))/2
    # lin2 = '+=' * int(n)
    lin()
    # print(lin2)
    # print()
    print(f'{msg:*^64}\n')
    # print(lin2)
    lin()


# ***************************************************************** #
# import linha
# n = len(' Usando Funções em Python ')
# print(type(n))
titulo(' Usando Funções em Python ')
titulo('Olá Mundo')
lin1()
# linha.lin1()
