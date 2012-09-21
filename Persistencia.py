# -*- coding: utf-8 -*-

import pickle

class Persistencia(object):

	def gravarArquivo(self, ranking):
		arquivo = open("Ranking.dat", "wb")
		pickle.dump(ranking, arquivo)
		#arquivo.write(ranking)
		arquivo.close()
		
	def lerArquivo(self):
		arquivo = open("Ranking.dat")
		lista =  pickle.load(arquivo)
		arquivo.close()
		return lista
