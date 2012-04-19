# -*- coding: utf-8 -*-
from ObjetoPintavel import ObjetoPintavel
class Nave(ObjetoPintavel):
# já pinta a nave no meio da tela na parte inferior da tela
	def __init__(self,tamTelaX, tamTelaY):
	# calculos para deixar nave no ponto inicial
		self.posX = tamTelaX/2
		self.posY =  tamTelaY - 30
		self.tamTelaX = tamTelaX
		self.tamTelaY = tamTelaY
		self.vida = 3
		self.pontuacao = 0
	
	def moverNave (self, deslocamentoX, deslocamentoY):
		if ((self.posX + deslocamentoX)> self.tamTelaX):
			self.posX = self.tamTelaX
		elif((self.posX + deslocamentoX)< 0):
			self.posX = 0
		else:
			self.posX = self.posX + deslocamentoX
		if ((self.posY + deslocamentoY)> self.tamTelaY):
			self.posY = self.tamTelaY
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
	
	def perderVida(self):
		self.vida -= 1
		if (self.vida == 0):
			return True
		return False
	def pontuar(self):
		self.pontuacao += 10