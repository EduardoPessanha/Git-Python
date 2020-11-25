def arqexiste(arq):
	"""
	-> Verifica se existe o arquivo arq
	:param arq: Nome do arquivo a ser testado.
	:return: retorna True se o arquivo for encontrado,
	caso contrário False
	"""
	try:
		a = open(arq)
	except FileNotFoundError:  # O arquivo não foi encontrado
		print('Arquivo não encontrado!')
		return False
	else:
		return True


def criaarq(arq):
	try:
		a = open(arq, 'wt+')
	except:
		print('ERRO! Não foi possivel criar o arquivo')
	else:
		print('Arquivo criado com sucesso!')
		a.close()
	return


def lerarq(arq):
	try:
		a = open(arq, 'rt')
	except:
		print(f'ERRO ao abrir o arquivo {arq}')
	else:
		for item in a:
			dado = item.split(';')
			dado[1] = dado[1].replace('\n', '')
			print(f"{dado[0]:<30} {dado[1]:>6}")
	finally:
		a.close()
	return


def cadarq(arq, nome='desconhecido', idade=0):
	try:
		a = open(arq, 'at')
	except:
		print('ERRO ao abrir o arquivo')
	else:
		# a.write(f'{nome};')
		# a.write(f'{idade}\n')
		a.write(f'{nome};{idade}\n')
		print(f'Novo registro de {nome} adicionado com sucesso')
	finally:
		a.close()
	return
