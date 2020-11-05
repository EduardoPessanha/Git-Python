from tkinter import *

janela = Tk()

label_1 = Label(janela, text='Teste de Interface Gráfica', font='Arial:20')


label_1.place(x=200, y=200)

janela.geometry('800x600+0+0')
janela.mainloop()