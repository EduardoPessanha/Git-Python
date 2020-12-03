#usr/bin/python3
from time import sleep
from ex115.lib.arquivo import *
from ex115.lib.interface import *

arq = 'cadastro.txt'
if not arqexiste(arq):
	criaarq(arq)

txt = ['Ver pessoas cadastradas',
	   'Cadastrar nova pessoa',
	   'Sair do Sistema'
	   ]
while True:
	resp = menuprincipal(txt)
	if resp > 3:
		print(f"{corletra('vm')}ERRO! Opção inválida.Tente outra vez.{corletra()}")
	elif resp == 3:
		texto('Saindo do sistema ... Até logo')
		break
	elif resp == 1:
		opcao('Pessoas cadastradas')
		lerarq(arq)
	else:
		opcao('Novo cadastro')
		nome = str(input('Nome: ')).capitalize()
		idade = leiaint('Idade: ')
		cadarq(arq, nome, idade)
	sleep(1.3)
