# -*- coding: utf-8 -*-

''' *** Processador IPv4 ***
 Programa que recebe um endereco na forma: endereco/prefixo
 e retorna os seguintes parâmetros:
 - endereço de rede
 - mascara de rede
 - wildcard
 - 1ro endereço p host
 - últ. endereço p host
 - endereço de broadcast
 - qtd de enderecos
 - qtd de hosts
 - classe IP (público/privado)

Por ngoma, aos 23.02.2022 
------------------------------------------------------------'''

from components.app import App

if __name__ == '__main__':
	App().run()
