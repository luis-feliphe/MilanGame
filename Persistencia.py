# -*- coding: utf-8 -*-

import pickle
import os
class Persistencia(object):

	def funcaoOrdenacaoRanking(self,a,b):
		if (a[1] == b[1]):
			return (-1) * cmp(a[0], b[0])
		return cmp(a[1], b[1])


	def gravarArquivo(self, ranking):
		arquivo = open("Ranking.dat", "wb")
		pickle.dump(ranking, arquivo)
		#arquivo.write(ranking)
		arquivo.close()
		
	def lerArquivo(self):
		if (os.path.isfile("Ranking.dat")):
			arquivo = open("Ranking.dat")
			lista =  pickle.load(arquivo)
			arquivo.close()
			#ordena lista (por pontuacao depois por nome)
			lista.sort(self.funcaoOrdenacaoRanking)
			lista.reverse()
			return lista
		return []