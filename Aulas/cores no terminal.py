print('\n')
print('\033[1;30;41m-=-' * 10, ' CORES NO TERMINAL ', '-=-' * 10, '\033[m')
print(""" \nPadrão ANSI - escape sequence
\n \033[1mSTYLE               TEXT      BACKGROUND\033[m
   0  = none          30           40 = Branca
   1  = Bold          31           41 = Vermelho
   3  = Itálico       32           42 = Verde
   4  = Underline     33           43 = Amarelo
   7  = Negative      34           44 = Azul
                      35           45 = Magenta (Roxo)
                      36           46 = Ciânico 
                      37           47 = Cinza

 \033[1;7;30m sintaxe ->\O33[STYLE;TEXT;BACKGROUNDm -> Ex.: \O33[1;33;46m \033[m

""")
