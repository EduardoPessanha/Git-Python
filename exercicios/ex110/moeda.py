def aumentar(preco=0, taxa=0, formato=False):
	"""
	-> Calcula o aumento de um determinado preço,
	retornando o resultado com ou sem formatação.
	:param preco: o preço que se quer reajustar.
	:param taxa: é a porcentagem do aumento.
	:param formato: determina se a saída será formatada ou não.
	:return: o valor reajustado, com ou sem formato
	"""
	res = preco + (preco * taxa / 100)
	# if formato:                             ___
	#     return moeda(res)                      |__ ou:
	# return res                              ___|
	# return res if formato is False else moeda(res) ou:
	# return res if not formato else moeda(res)      ou:
	return moeda(res) if formato else res


def diminuir(preco=0, taxa=0, formato=False):
	"""
	-> Calcula a redução de um determinado preço,
	retornando o resultado com ou sem formatação.
	:param preco: o preço que se quer reajustar.
	:param taxa: é a porcentagem de redução.
	:param formato: determina se a saída será formatada ou não.
	:return: o valor reajustado, com ou sem formato
	"""
	res = preco - (taxa * preco / 100)
	return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
	"""
	-> Calcula o dobro de um determinado preço,
	retornando o resultado com ou sem formatação.
	:param preco: o preço que se quer reajustar.
	:param formato: determina se a saída será formatada ou não.
	:return: o valor reajustado, com ou sem formato
	"""
	res = preco * 2
	return res if not formato else moeda(res)


def metade(preco=0, formato=False):
	"""
	-> Calcula a metade de um determinado preço,
	retornando o resultado com ou sem formatação.
	:param preco: o preço que se quer reajustar.
	:param formato: determina se a saída será formatada ou não.
	:return: o valor reajustado, com ou sem formato
	"""
	res = preco / 2
	return moeda(res) if formato else res


def moeda(preco=0, moeda="R$"):
	"""
	-> Faz a formatação de um determinado preço.
	:param preco: o preço a ser formatado.
	:param moeda: determina o formato a ser aplicado.
	:return: o valor formato
	"""
	return f'{moeda} {preco:>.2f}'.replace('.', ',')


def resumo(preco=0, taxaa=0, taxar=0):
	"""
	-> Faz uma analisa um determinado preço, calculando
	o aumento, redução, dobro e a metade do preço.
	:param preco: o preço a ser analisado.
	:param taxaa: a porcentagem de aumento do preço.
	:param taxar: a porcentagem de redução do preço.
	:return: retorna a analise do preço informado.
	"""
	print('*' * 30)
	print(f'{"RESUMO DO VALOR":^30}')
	print('*' * 30)
	print(f'Preço analisado: \t{moeda(preco)}')  # \t -> faz a tabulação
	print(f'Dobro do preço: \t{dobro(preco, True)}')
	print(f'Metade do preço: \t{metade(preco, True)}')
	print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
	print(f'{taxar}% de redução: \t{diminuir(preco, taxar, True)}')
	print('*' * 30)
	return
