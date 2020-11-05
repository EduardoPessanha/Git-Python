from tkinter import *

janela = Tk()

texto = "Olá Mundo!, cheguei!"
label_1 = Label(janela, text=texto, font='Arial:20')


label_1.place(x=200, y=200)

janela.geometry('800x600+0+0')
janela.mainloop()
