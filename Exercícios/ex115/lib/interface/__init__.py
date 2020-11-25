from utilidades.cor import *
from utilidades.numero import leiaint


def linha(simb='=', tam=40):
	return simb * tam


def texto(msg='', tam=0):
	print(linha("*"))
	print(msg.upper().center(40))
	print(linha('*'))
	return


def menuprincipal(opc, tam=0):
	texto('MENU PRINCIPAL')
	for c in range(len(opc)):
		print(f'{c+1:>3}- {corletra("az")}{opc[c]}{corletra()}')
	print(linha('*'))
	return leiaint(f'{corletra("vd")}Sua opção: {corletra()}')


def opcao(num=1):
	texto(num)
	return
