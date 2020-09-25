Tuplas:

Definição de TUPLA

Tupla é uma Lista imutável,  já que após definida, não permite a adição ou remoção de elementos, é uma lista que restringe a adição, alteração, remoção e o ordenamento do elementos.
Tuplas são estruturas de dados heterogêneas. Em outras palavras, numa Tupla, os elementos podem ser de tipos distintos, por exemplo, uma Tupla pode conter o dia, o dia da semana, o mês e o ano.
Exemplo:
t = ("10", "segunda-feira", "Fevereiro", 2022)

Manipulando e Controlando as Tuplas

O que estudamos até o momento a respeito de manipulação de strings, pode ser utilizado para manipular e controlar Tuplas, salvo a alteração da lista ou de seus elementos.

>>> t = ("x", "y", 10, 20, "c")
>>> t
("x", "y", 10, 20, "c")
>>> t[0]
"x"
>>> t[-1]
"c"
>>> t[1:3]
('y', 10, 20)

       Uma Tupla tem seus elementos delimitados por parêntesis.

Conforme a documentação oficial do Python, uma Tupla é declarada pela utilização do operador vírgula, que é utilizado para separar os elementos.
A única exceção é na declaração de tuplas vazias, quando é necessário o uso do parêntesis.

Exemplo:
#tupla declarada sem o uso de parentesis
t1 = 1, 2, 3
#tupla declarada com o uso de parentesis
t2 = (1, 2, 3)
#tupla com um único elemento
t3 = 1, (Observe que a declaração é finalizada com uma vírgula! É dessa forma que declaramos Tuplas com um único elemento)
#tupla vazia
t4 = () (Essa é a única situação onde é obrigatório a utilização dos parêntesis na declaração da Tupla)
Conforme a documentação do Python, entende-se que é a vírgula quem realmente define uma Tupla, não os parênteses. Os parênteses são opcionais, exceto no caso da Tupla vazia, ou quando são necessários para evitar a ambiguidade sintática. 

       A ordem dos elementos numa Tupla será a ordem na qual estes foram definidos, ou seja, não é possível reordenar, alterar ou excluir seus elementos em tempo de execução.
       
A Tupla é IMUTÁVEL

       O primeiro elemento de uma Tupla também possui índice igual a 0 e o último índice igual a -1. 
       Assim o acesso a elementos, bem como o fatiamentos funciona da mesma forma como já estudado no fatiamento de strings.

Exemplo:

>>> lanche = ('hambúrguer', 'suco', 'pizza', 'pudim')
>>> type (lanche)
<class 'tuple'>
>>> print(lanche)
('hambúrguer', 'suco', 'pizza', 'pudim')
>>> print(lanche[2])
pizza
>>> print(lanche[0:2])
('hambúrguer', 'suco')
>>> print(lanche[1:])
('suco', 'pizza', 'pudim')
>>> print(lanche[-1])
pudim
>>> len(lanche)
4

>>> for c in lanche:
	     print(c)        
hambúrguer
suco
pizza
pudim
>>>