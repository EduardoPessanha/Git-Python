def leiadinheiro(entrada):
	"""
	-> Fza a validação de dados para aceitar apenas
	valores monetários.
	:param entrada: Recebe o valor a ser validado.
	:return: retorna um valor no formato monetário
	"""
	from ex112.utilidadescev import cor
	while True:
		valor = str(input(entrada)).strip().replace(',', '.')
		if valor.isalpha() or valor == '':
			print(f'{cor.corletra("vm")}ERRO! \"{valor}\" é um PREÇO INVÁLIDO! Tente outra vez!{cor.corletra()}')
		else:
			break
	return float(valor)


# ************************* Desafio 112 ************************* #
#                   Entrada de dados monetários                   #
#  Dentro do pacote utilidadesCeV que criamos no desafio 111,     #
#  temos um módulo chamado dado. Crie uma função chamada          #
#  leiaDinheiro() que seja capaz de funcionar como a função       #
#  input(), mas com uma validação de dados para aceitar apenas    #
#  valores que seja monetários.                                   #
# *************************************************************** #

