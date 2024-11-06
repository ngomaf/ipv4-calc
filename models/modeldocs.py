
class ModelDocs:

	__slots__ = []

	def get_doc(self):
		doc = '\nOlá caro(a) usuário(a)!\n'
		doc += 'Com muito gosto desenvolvi esse pequeno software, para facilitar os cálculos de sub-redes IPv4 (Internet Protocol version 4), para melhor uso do mesmo cosulte o instrutivo a baixo:\n\n'
		doc += 'Entrada de dados\n'
		doc += '(1) Endereço é um campo onde se colaca IP no formato decimal, ex.: 192.168.1.1. (2) Mascara/prefixo é o campo onde se coloca o valor do prefixo de rede, ex.: 24. Um detalhe, caso se deixe este vázio o programa vai considerar 24.\n\n'
		doc += 'Resultado\n'
		doc += 'Nos campos a baixo de resultado são retornados, um conjunto de dados resultantes do processamento dos dados digitados (IP e Mascara). Cada parâmetro apresentado e sucedido pelo respectivo valor em binário.\n\n'
		
		return doc

	def get_about(self):
		about = '\n= Sobre o software =\n'
		about += 'nome: Calculadora IPv4\n'
		about += 'versão: 2.2\n'
		about += '---\n'
		about += 'linguagem: python 3.8\n'
		about += 'interface: Tkinter\n'
		about += 'data da 1ra versão: 22.05.2021\n'
		about += 'data da presente versão: 09.03.2022\n'
		about += '---\n'
		about += 'por: ngoma manuel fortuna, eng.º\n'
		about += 'design: guerrito frangueira\n'

		return about
