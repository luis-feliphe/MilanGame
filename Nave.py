# -*- coding: utf-8 -*-
from ObjetoPintavel import ObjetoPintavel
import random 
class Nave(ObjetoPintavel):
# já pinta a nave no meio da tela na parte inferior da tela
	def __init__(self,tamTelaX, tamTelaY):
	# calculos para deixar nave no ponto inicial
		self.tamNavex = 100 
		self.tamNavey = 100
		self.posX = tamTelaX/2 - (self.tamNavex/2)
		self.posY =  tamTelaY - self.tamNavey 
		self.tamTelaX = tamTelaX
		self.tamTelaY = tamTelaY
		self.vida = 3
		self.pontuacao = 0

		self.nivel = 1
		self.PASSAR_DE_NIVEL = 700 #constante

	def moverAleatorio():
		movimentoX = [1, 2, 3,  -1 , -2, -3]
		movimentoY = [1, 2, -2]
		self.moverNave(random.choice(movimentoX),random.choice( movimentoY))
	
	def moverNave (self, deslocamentoX, deslocamentoY):
		if ((self.posX + deslocamentoX+self.tamNavex)> self.tamTelaX):
			self.posX = self.tamTelaX - self.tamNavex
		elif((self.posX + deslocamentoX)< 0):
			self.posX = 0
		else:
			self.posX = self.posX + deslocamentoX
		if ((self.posY + deslocamentoY+self.tamNavey)> self.tamTelaY):
			self.posY = self.tamTelaY - self.tamNavey
		elif ((self.posY + deslocamentoY)<0):		
			self.posY = 0
		else:
			self.posY = self.posY + deslocamentoY

	
#	def getPos(self):
#		return (self.posX, self.posY)
	
	def ganharVida(self):
		if (self.vida < 8):
			self.vida += 1
		else:
			self.pontuacao = self.pontuacao + 50
		self.calcularNivel()
	
	def perderVida(self):
		self.vida -= 1
		if (self.vida == 0):
			return True
		return False

	def pontuar(self):
		self.pontuacao += 100
		self.calcularNivel()

	def getPontuacao(self):
		return self.pontuacao
	
	def getVida(self):
		return self.vida
	
	def getNivel(self):
		return self.nivel
	
	def calcularNivel (self):
		self.nivel = (self.pontuacao / self.PASSAR_DE_NIVEL) + 1
