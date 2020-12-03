def cor(tipo):
    if tipo == 0:
        tipo = '\033[m'
    elif tipo == 'br':
        tipo = '\033[1;30m'
    elif tipo == 'vm':
        tipo = '\033[1;31m'
    elif tipo == 'vd':
        tipo = '\033[1;32m'
    elif tipo == 'am':
        tipo = '\033[1;33m'
    elif tipo == 'az':
        tipo = '\033[1;34m'
    elif tipo == 'mg':
        tipo = '\033[1;35m'
    elif tipo == 'ci':
        tipo = '\033[1;36m'
    elif tipo == 'cz':
        tipo = '\033[1;37m'
    return tipo


print('\n')
print('\033[1;30;41m-=-' * 10, ' CORES NO TERMINAL ', '-=-' * 10, '\033[m')
print(f""" \nPadrão ANSI - escape sequence
\n \033[1mSTYLE               TEXT      BACKGROUND\033[m
   0  = none          30           40 => {cor('br')}Branca{cor(0)}
   1  = Bold          31           41 => {cor('vm')}Vermelho{cor(0)}
   3  = Itálico       32           42 => {cor('vd')}Verde{cor(0)}
   4  = Underline     33           43 => {cor('am')}Amarelo{cor(0)}
   7  = Negative      34           44 => {cor('az')}Azul{cor(0)}
                      35           45 => {cor('mg')}Magenta (Roxo){cor(0)}
                      36           46 => {cor('ci')}Ciânico{cor(0)} 
                      37           47 => {cor('cz')}Cinza{cor(0)}

 \033[1;7;30m sintaxe ->\O33[STYLE;TEXT;BACKGROUNDm -> Ex.: \O33[1;33;46m \033[m

""")
