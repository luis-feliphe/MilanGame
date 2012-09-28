from Gerenciador import *

class Facade(object):
	#construtor
	def __init__ (self):
		self.gerenciador = Gerenciador()
	
	#retorna tela com instrucoes 
	def verInstrucoes(self):
		return "Use as setas para mover a nave e ctrl para atirar"

	#retorna lista com ranking 
	def getRanking(self):
		return  self.gerenciador.getRanking()

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
		
	def partidaFoiIniciada(self):
		return self.gerenciador.partidaFoiIniciada()

	#move nave do jogador 
	def moverNave(self,deslocamentoX, deslocamentoY):
		self.gerenciador.moverNave(deslocamentoX, deslocamentoY)

	#mudaArmaSePassarPorCimaDaArma
	def mudarArma(self, tipoDeArma):
		return


	#jogador atira no inimigo
	def atacarInimigo(self):
		self.gerenciador.atacarInimigo()
	

	#pegarPosicao da nave
	def getPosNave(self):
		return self.gerenciador.getPosNave()
	
	def getTamanhoTela(self):
		return self.gerenciador.getTamanhoTela()
		
	# se tiver vidas volta ao jogo
	def serDestruido(self):
		return
			
	#encerra jogo
	def sairDoJogo(self):
		self.gerenciador.sairDoJogo()
	
	def sairDaPartida(self):
		return self.gerenciador.sairDaPartida()
	
	def ganharVida(self):
		return self.gerenciador.ganharVida()
	
	def perderVida(self):
		return self.gerenciador.perderVida()
	
	# nave inimiga
	def criarNaveInimiga(self):
		self.gerenciador.criarNaveInimiga()
		
	def destruirNaveInimiga(self, nave):
		self.gerenciador.destruirNaveInimiga(nave)
		
#	def calcularPontuacao(self):
#		return self.gerenciador.calcularPontuacao()
		
	def getListaNaves(self):
		return self.gerenciador.getListaNaves()
	
	def getPontuacao (self):
		return self.gerenciador.getPontuacao()
	
	def getListaTiros(self):
		return self.gerenciador.getListaTiros()
	
	def getVida(self):
		return self.gerenciador.getVida()
	
	def getNivel(self):
		return self.gerenciador.getNivel()
	
	def adicionarNomeNoRanking(self, nome):
		return self.gerenciador.adicionarNomeNoRanking(nome)
	def getNivel(self):
		return self.gerenciador.getNivel()