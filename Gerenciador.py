# -*- coding: utf-8 -*-
from ExcecaoJogo import ExcecaoJogo
from Nave import Nave
from Tiro import Tiro

class Gerenciador(object):
	def __init__(self):
		self.jogoIniciado = False
		self.partidaIniciada = False
		self.tamX = 500
		self.tamY = 500
		self.nave = None
		self.listaTiros = []
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
		self.ranking.append(pontuacaoENome)
		self.ranking.sort()
		self.ranking.reverse()
		if (len(self.ranking )> 10):
			self.ranking.remove(self.ranking[10])
	