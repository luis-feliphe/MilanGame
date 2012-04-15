# -*- coding: utf-8 -*-
from Gerenciador import *

class Facade(object):
	#construtor
	def __init__ (self):
		self.gerenciador = Gerenciador()
	
	#retorna tela com instrucoes 
	def verInstrucoes(self):
		return "Use as setas para mover a nave e ctrl para atirar"

	#retorna tela com ranking 
	def verRanking(self):
		return  

	#retorna tela com creditos
	def verCreditos(self):
		return 

	#inicia jogo 
	def iniciarJogo(self):
		self.gerenciador.iniciarJogo()
		return
	
	def jogoComecou(self):
		return self.gerenciador.jogoComecou()

	#iniciar partida
	def iniciarPartida(self):
		return self.gerenciador.iniciarPartida()

	#move nave do jogador 
	def moverNave(self,deslocamentoX, deslocamentoY):
		self.gerenciador.moverNave(deslocamentoX, deslocamentoY)

	#mudaArmaSePassarPorCimaDaArma
	def mudarArma(self, tipoDeArma):
		return


	#jogador atira no inimigo
	def atacarInimigo(self):
		self.gerenciador.atacarInimigo()
	
	#pegarPosição usuario
	def getPosNave(self):
		return self.gerenciador.getPosNave()
	
	def getTamanhoTela(self):
		return self.gerenciador.getTamanhoTela()
		
	#se tiver Vidas volta ao jogo com uma vida a menos senão , tela game over
	def serDestruido(self):
		return
		
	#encerra partida
	def terminaPartida(self):
		return

	#adiciona nome no ranking
	def adicionarNomeNoRanking(self, pontuacaoENome):
		self.gerenciador.adicionarNoRanking(pontuacaoENome)
		
	#encerra jogo
	def sairDoJogo(self):
		return


