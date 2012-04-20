# -*- coding: utf-8 -*-
from ExcecaoJogo import ExcecaoJogo
from Nave import Nave
from Tiro import Tiro
from NaveInimigaComum import NaveInimigaComum
import random

class Gerenciador(object):
	def __init__(self):
		self.jogoIniciado = False
		self.partidaIniciada = False
		self.tamX = 500
		self.tamY = 500
		self.nave = None
		self.listaTiros = []
		self.listaNaves = []
		self.ranking = []
		
	def iniciarJogo (self):
		if (self.jogoIniciado == True):
			raise ExcecaoJogo("Um jogo ja foi iniciado")
		self.jogoIniciado = True

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
	
	def adicionarNoRanking(self, pontuacaoENome):
		if (self.jogoIniciado == False):
			raise ExcecaoJogo("Jogo não iniciado")
		if (self.partidaIniciada == True):
			raise ExcecaoJogo("Partida em andamento")
		if(pontuacaoENome[0] == 0):
			raise ExcecaoJogo("Você precisa ter pontuação maior que zero")
		if (not(pontuacaoENome in self.ranking)):
			self.ranking.append(pontuacaoENome)
			self.ranking.sort()
			self.ranking.reverse()
			if (len(self.ranking )> 10):
				self.ranking.remove(self.ranking[10])
				
	def sairDaPartida(self):
		if (self.jogoIniciado == False):
			raise ExcecaoJogo("Jogo não iniciado")
		if (self.partidaIniciada == False):
			raise ExcecaoJogo("Partida não iniciada")
		self.partidaIniciada = False
		self.listaTiros = []
		self.listaNaves = []
		self.ranking = []
		self.nave = None
		
	def sairDoJogo(self):
		if (self.jogoIniciado == False):
			raise ExcecaoJogo("Jogo não iniciado")
		if (self.partidaIniciada == True):
			raise ExcecaoJogo("Voce precisa terminar a partida antes de sair")
		self.jogoIniciado = False

	def ganharVida(self):
		if (self.jogoIniciado == False):
			raise ExcecaoJogo("Jogo não iniciado")
		if (self.partidaIniciada == False):
			raise ExcecaoJogo("Partida não iniciada")	
		self.nave.ganharVida()
	
	def perderVida(self):
		if (self.jogoIniciado == False):
			raise ExcecaoJogo("Jogo não iniciado")
		if (self.partidaIniciada == False):
			raise ExcecaoJogo("Partida não iniciada")
		vidasAcabaram = self.nave.perderVida()
		if (vidasAcabaram == True):
			self.sairDaPartida()
	
	def partidaFoiIniciada(self):
		return self.partidaIniciada
	
	def criarNaveInimiga(self):
		if (self.jogoIniciado == False):
			raise ExcecaoJogo("Jogo não iniciado")
		if (self.partidaIniciada == False):
			raise ExcecaoJogo("Partida não iniciada")
		escolhaPosX = random.choice
		listaPosicoes = range(0, self.tamX)
		naveInimiga = NaveInimigaComum(escolhaPosX(listaPosicoes), 0)
		self.listaNaves.append(naveInimiga)
		
	def destruirNaveInimiga(self, nave):
		if (self.jogoIniciado == False):
			raise ExcecaoJogo("Jogo não iniciado")
		if (self.partidaIniciada == False):
			raise ExcecaoJogo("Partida não iniciada")
		if (nave in self.listaNaves):
			self.listaNaves.remove(nave)
			self.nave.pontuar()
			
	def calcularPontuacao(self):
		tamanhoRanking = len(self.ranking)
		if (tamanhoRanking == 0):
			return True
		elif (self.nave.pontuacao > self.ranking[tamanhoRaking-1]):
			return True
		return False
		
	def getListaNaves(self):
		return self.listaNaves
		
	def getPontuacao(self):
		return self.nave.getPontuacao()
	
	def getListaTiros(self):
		return self.listaTiros
	
	def getVida(self):
		return self.nave.getVida()
