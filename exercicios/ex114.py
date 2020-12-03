from utilitarios import titulo as cab
import urllib as ur # biblioteca para acessar a internet
# import urllib3.request as ur
# import urllib3
# ********************* Desafio 114 ********************** #
#                   Site está acessível?                   #
#  Crie um código em Python que teste se o site pudim está #
#  acessível pelo computador usado.   (www.pudim.com.br)   #
# ******************************************************** #
cab('Site está acessível?')
# ******************************************************** #

# url = 'www.pudim.com.br'
try:
    site = ur.urlopen('http://www.pudim.com.br')

except (FileNotFoundError, TypeError):
    print('O site pudim não esta acessível neste momento!!!')
else:
    print('O site pudim esta acessível!!!!')
    # print(site.read())  # exibe o conteúdo HTML do site que foi acessado.
