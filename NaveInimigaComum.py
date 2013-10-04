from Inimigo import Inimigo
from Nave import Nave
import random
class NaveInimigaComum():
	def __init__(self, x , y, tamTelaX, tamTelaY):
		self.telaX = tamTelaX
		self.telaY = tamTelaY
		self.posX = x
		self.posY = y
		self.movimentacao = random.choice(["direita", "esquerda"])
		self.contadorMovimentos = random.choice([5, 8])
		#super(NaveInimigaComum, self).__init__(x, y)
	def moverAleatorio(self):
		if self.contadorMovimentos == 0:
			self.movimentacao = random.choice(["direita", "esquerda", "frente"])
			self.contadorMovimentos = random.choice([40 , 120, 80])
	
		if self.movimentacao =="direita":
			self.posX -= 2#random.choice([1, 2,3])
		if self.movimentacao =="esquerda":
			self.posX += 2#random.choice([-1, -2,-3])

		self.contadorMovimentos -= 1
		self.posY += 2# += random.choice ([1, 2, 3])	
		if self.posY < -10: 
			self.posY = 0
		if self.posX < 0: 
			self.posX = 0
		if self.posY > (self.telaY + 100):
			self.posY = 0
		if self.posX > (self.telaX + 100):
			self.posY = -10
			self.posX = random.choice ([self.telaX/2 , self.telaX/3, self.telaX/5])
	
	def getPos(self):
		return self.posX, self.posY
