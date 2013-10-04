# -*- coding: utf-8 -*-
from ExcecaoJogo import ExcecaoJogo
from Nave import Nave
from Persistencia import Persistencia
from Tiro import Tiro
from NaveInimigaComum import NaveInimigaComum
import random

class Gerenciador(object):
	def __init__(self):
		self.jogoIniciado = False
		self.partidaIniciada = False
		self.salvouNoRanking = False
		self.tamX =800 
		self.tamY = 600 
		self.persistencia = Persistencia()
		self.ranking = self.persistencia.lerArquivo()
		
	def iniciarJogo (self):
		if (self.jogoIniciado == True):
			raise ExcecaoJogo("Um jogo ja foi iniciado")
		self.jogoIniciado = True

		self.nave = None
		self.listaTiros = []
		self.listaNaves = []
#		self.ranking = self.persistencia.lerArquivo()
		self.salvouNoRanking = False

	def moverNavesInimigas(self):
		for naveInimiga in self.listaNaves:
			naveInimiga.moverAleatorio()

		
	def moverTiros (self):
		for tiro in self.listaTiros:
			tiro.mover()
			if tiro.posY < 0: #neste caso o tamnho da nave
				self.listaTiros.remove(tiro)

	def iniciarPartida(self):
		if (self.partidaIniciada == True):
			raise ExcecaoJogo("Uma partida ja foi iniciada")
		if (self.jogoIniciado == False):
			raise ExcecaoJogo("Jogo não iniciado")
		self.partidaIniciada = True
		self.nave = Nave(self.tamX, self.tamY)

	
	def jogoComecou(self):
		return self.jogoIniciado
	
	def getTamanhoTela(self):
		return (self.tamX, self.tamY)
	
	def getPosNave (self):
		return self.nave.getPos()
	
	def moverNave(self, deslocamentoX, deslocamentoY):
		if (self.jogoIniciado == False):
			raise ExcecaoJogo("Jogo não iniciado")
		if (self.partidaIniciada == False):
			raise ExcecaoJogo("Partida não iniciada")
		self.nave.moverNave(deslocamentoX, deslocamentoY)
	
	def atacarInimigo(self):
		if (self.jogoIniciado == False):
			raise ExcecaoJogo("Jogo não iniciado")
		if (self.partidaIniciada == False):
			raise ExcecaoJogo("Partida não iniciada")
		posNave = self.getPosNave()
		self.listaTiros.append(Tiro(posNave[0],posNave[1]))
		
	def adicionarNomeNoRanking(self, Nome):
		pontuacaoEnome = (Nome, self.getPontuacao())
		self.adicionarNoRanking(pontuacaoEnome)
		self.ranking.sort(self.funcaoOrdenacaoRanking)
		self.ranking.reverse()

	def funcaoOrdenacaoRanking(self,a,b):
		if (a[1] == b[1]):
			return (-1) * cmp(a[0], b[0])
		return cmp(a[1], b[1])
		
	def getRanking(self):
		return self.ranking

		
	def adicionarNoRanking(self, pontuacaoENome):
		if (self.jogoIniciado == False):
			raise ExcecaoJogo("Jogo não iniciado")
		if (self.partidaIniciada == True):
			raise ExcecaoJogo("Partida em andamento")
		if(pontuacaoENome[1] == 0):
			raise ExcecaoJogo("Você precisa ter pontuação maior que zero")
		if (not(pontuacaoENome in self.ranking)):
			self.ranking.append(pontuacaoENome)			
			self.ranking.sort()
			self.ranking.reverse()
			if (len(self.ranking )> 10):
				self.ranking.remove(self.ranking[10])
			#salvar em arquivo
			self.persistencia.gravarArquivo( self.ranking )
		
				
	def sairDaPartida(self):
		if (self.jogoIniciado == False):
			raise ExcecaoJogo("Jogo não iniciado")
		if (self.partidaIniciada == False):
			raise ExcecaoJogo("Partida não iniciada")
		self.partidaIniciada = False
		tamanhoRanking = len(self.ranking)
		#retorna true se for para adicionar no ranking
		if ((tamanhoRanking == 0)):
			return True
		elif (self.nave.pontuacao >= (self.ranking[tamanhoRanking-1])[1]):
			return True
		elif (tamanhoRanking < 10):
			return True

		return False
				
	def sairDoJogo(self):
		if (self.jogoIniciado == False):
			raise ExcecaoJogo("Jogo não iniciado")
		if (self.partidaIniciada == True):
			raise ExcecaoJogo("Voce precisa terminar a partida antes de sair")
		self.jogoIniciado = False

	def getNivel(self):
		if (self.jogoIniciado == False):
			raise ExcecaoJogo("Jogo não iniciado")
		if (self.partidaIniciada == False):
			raise ExcecaoJogo("Partida não iniciada")

		return self.nave.getNivel()
		
		
	def ganharVida(self):
		if (self.jogoIniciado == False):
			raise ExcecaoJogo("Jogo não iniciado")
		if (self.partidaIniciada == False):
			raise ExcecaoJogo("Partida não iniciada")	
		
		self.nave.ganharVida()
		nivel = self.nave.getNivel()
		if (nivel >= 6):
			tamanhoRanking = len(self.ranking)
			#retorna true se for para adicionar no ranking
			if (tamanhoRanking == 0):
				self.partidaIniciada = False
				return True
			elif (self.nave.pontuacao >= (self.ranking[tamanhoRanking-1])[1]):
				self.partidaIniciada = False
				return True
			elif (tamanhoRanking < 10):
				self.partidaIniciada = False
				return True
			else:
				return False
		
		return False

	def perderVida(self):
		if (self.jogoIniciado == False):
			raise ExcecaoJogo("Jogo não iniciado")
		if (self.partidaIniciada == False):
			raise ExcecaoJogo("Partida não iniciada")
		vidasAcabaram = self.nave.perderVida()
		if (vidasAcabaram == True):
			return self.sairDaPartida()
		return False
	
	def partidaFoiIniciada(self):
		return self.partidaIniciada
	
	def criarNaveInimiga(self):
		if (self.jogoIniciado == False):
			raise ExcecaoJogo("Jogo não iniciado")
		if (self.partidaIniciada == False):
			raise ExcecaoJogo("Partida não iniciada")
		escolhaPosX = random.choice
		listaPosicoes = range(0, self.tamX)
		naveInimiga = NaveInimigaComum(escolhaPosX(listaPosicoes), 50 , self.tamX, self.tamY)
		self.listaNaves.append(naveInimiga)
		
	def destruirNaveInimiga(self, nave):
		if (self.jogoIniciado == False):
			raise ExcecaoJogo("Jogo não iniciado")
		if (self.partidaIniciada == False):
			raise ExcecaoJogo("Partida não iniciada")
		if (nave in self.listaNaves):
			self.listaNaves.remove(nave)
			self.nave.pontuar()
		
	def getListaNaves(self):
		return self.listaNaves
		
	def getPontuacao(self):
		if (self.jogoIniciado == False):
			raise ExcecaoJogo("Jogo não iniciado")
		return self.nave.getPontuacao()
	
	def getListaTiros(self):
		return self.listaTiros
	
	def getVida(self):
		return self.nave.getVida()
