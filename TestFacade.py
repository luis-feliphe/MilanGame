# -*- coding: utf-8 -*-
import unittest
from Facade import *

class TestFacade(unittest.TestCase):

	def setUp(self):
		self.fac = Facade()
	
	#testes referentes a partidas e ao jogo
	def testeIniciarJogo(self):
		self.fac.iniciarJogo()
		self.assertEqual(True,self.fac.jogoComecou())

	def testeIniciarDoisJogos(self):
		self.fac.iniciarJogo()
		try: 
			unittest.TestCase.assertRaises(ExcecaoJogo, self.fac.iniciarJogo())
		except ExcecaoJogo as e : 
			self.assertEqual(e.message, "Um jogo ja foi iniciado")

	def testeIniciarPartida(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		self.assertEqual(True,self.fac.jogoComecou())

	def testeIniciarDuasPartidas(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		try: 
			unittest.TestCase.assertRaises(ExcecaoJogo, self.fac.iniciarPartida())
		except ExcecaoJogo as e : 
			self.assertEqual(e.message, "Uma partida ja foi iniciada")

	def testeIniciarPartidaSemJogo(self):
		try: 
			unittest.TestCase.assertRaises(ExcecaoJogo, self.fac.iniciarPartida())
		except ExcecaoJogo as e : 
			self.assertEqual(e.message, "Jogo não iniciado")

	#testes referentes a Nave e sua movimentação
	def testecriarNaveAoIniciarPartida(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		tam = self.fac.getTamanhoTela()
		x = tam[0]
		y = tam[1]
		self.assertEqual((x/2, y - 30) , self.fac.getPosNave())
	
	def testemoverNave(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		posX , posY = self.fac.getPosNave()
		self.fac.moverNave(5, 5)
		self.assertEqual((posX + 5, posY + 5) , self.fac.getPosNave() )
	
	def testeMoverNaveAntesDeIniciarJogo(self):
		try: 
			unittest.TestCase.assertRaises(ExcecaoJogo, self.fac.moverNave(5,5))
		except ExcecaoJogo as e : 
			self.assertEqual(e.message, "Jogo não iniciado")
	
	def testeMoverNaveAntesDeIniciarPartida(self):
		self.fac.iniciarJogo()
		try: 
			unittest.TestCase.assertRaises(ExcecaoJogo, self.fac.moverNave(5,5))
		except ExcecaoJogo as e : 
			self.assertEqual(e.message, "Partida não iniciada")
	
	def testeMoverNaveForaDaTela(self):
		self.fac = Facade()
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		self.fac.moverNave(500,500)
		self.assertEqual((500,500),self.fac.getPosNave())

	def testeAtacarInimigo(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		self.fac.atacarInimigo()
		lista = self.fac.gerenciador.listaTiros
		self.assertEqual(self.fac.getPosNave(),lista[0].getPos() )
	
	def testeAtacarAntesDoJogoIniciar (self):
		try: 
			unittest.TestCase.assertRaises(ExcecaoJogo, self.fac.atacarInimigo())
		except ExcecaoJogo as e : 
			self.assertEqual(e.message, "Jogo não iniciado")
	
	def testeAtacarAntesDaPartidaIniciar (self):
		self.fac.iniciarJogo()
		try: 
			unittest.TestCase.assertRaises(ExcecaoJogo, self.fac.atacarInimigo())
		except ExcecaoJogo as e : 
			self.assertEqual(e.message, "Partida não iniciada")

	#testes referentes ao Ranking
	def testeAdicionarNomeAoRanking(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		x = (3000, "Luis")
		self.fac.adicionarNomeNoRanking(x)
		self.assertEqual(1,len(self.fac.gerenciador.ranking) )
	
	def testeAdicionarNomeAoRankingAntesDoJogoComecar(self):
		try: 
			unittest.TestCase.assertRaises(ExcecaoJogo, self.fac.adicionarNomeNoRanking(( 3000 ,"Luis")))
		except ExcecaoJogo as e : 
			self.assertEqual(e.message, "Jogo não iniciado")
	
	def testeAdicionarNoRankingSemPontuacaoNecessaria(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		self.fac.adicionarNomeNoRanking((200,"Luis"))
		self.fac.adicionarNomeNoRanking(( 40,"Luis"))
		self.fac.adicionarNomeNoRanking((500,"Luis"))
		self.fac.adicionarNomeNoRanking((20,"Luis"))
		self.fac.adicionarNomeNoRanking(( 30,"Luis"))
		self.fac.adicionarNomeNoRanking((330,"Luis"))
		self.fac.adicionarNomeNoRanking((550,"Luis"))
		self.fac.adicionarNomeNoRanking((220,"Luis"))
		self.fac.adicionarNomeNoRanking(( 120,"Luis"))
		self.fac.adicionarNomeNoRanking((10,"Luis"))
		self.fac.adicionarNomeNoRanking((1,"Luis"))#Não deve adicionar este ao ranking
		
		self.assertEqual(False, ((1,"Luis") in self.fac.gerenciador.ranking) )

	def testeOrdenarRanking(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		self.fac.adicionarNomeNoRanking((200,"Luis"))
		self.fac.adicionarNomeNoRanking(( 40,"Luis"))
		self.fac.adicionarNomeNoRanking((500,"Luis"))
		self.fac.adicionarNomeNoRanking((20,"Luis"))
		self.fac.adicionarNomeNoRanking(( 30,"Luis"))
		self.fac.adicionarNomeNoRanking((330,"Luis"))
		self.fac.adicionarNomeNoRanking((550,"Luis"))
		self.fac.adicionarNomeNoRanking((220,"Luis"))
		self.fac.adicionarNomeNoRanking(( 120,"Luis"))
		self.fac.adicionarNomeNoRanking((10,"Luis"))

		self.assertEqual((10,"Luis"), self.fac.gerenciador.ranking[9])
		self.assertEqual((20,"Luis"), self.fac.gerenciador.ranking[8])
		self.assertEqual((30,"Luis"), self.fac.gerenciador.ranking[7])
		self.assertEqual((40,"Luis"), self.fac.gerenciador.ranking[6])
		self.assertEqual((120,"Luis"), self.fac.gerenciador.ranking[5])
		self.assertEqual((200,"Luis"), self.fac.gerenciador.ranking[4])
		self.assertEqual((220,"Luis"), self.fac.gerenciador.ranking[3])
		self.assertEqual((330,"Luis"), self.fac.gerenciador.ranking[2])
		self.assertEqual((500,"Luis"), self.fac.gerenciador.ranking[1])
		self.assertEqual((550,"Luis"), self.fac.gerenciador.ranking[0])

	def testeTamanhoMaximoDoRankingTemQueSerDez(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		#adiciona 13 pessoas ao ranking
		self.fac.adicionarNomeNoRanking((20,"Luis"))
		self.fac.adicionarNomeNoRanking(( 30,"Luis"))
		self.fac.adicionarNomeNoRanking((500,"Luis"))
		self.fac.adicionarNomeNoRanking((200,"Luis"))
		self.fac.adicionarNomeNoRanking((330,"Luis"))
		self.fac.adicionarNomeNoRanking((550,"Luis"))
		self.fac.adicionarNomeNoRanking((220,"Luis"))
		self.fac.adicionarNomeNoRanking(( 120,"Luis"))
		self.fac.adicionarNomeNoRanking((50,"Luis"))
		self.fac.adicionarNomeNoRanking((270,"Luis"))
		self.fac.adicionarNomeNoRanking((290,"Luis"))
		self.fac.adicionarNomeNoRanking(( 450,"Luis"))
		self.fac.adicionarNomeNoRanking((10,"Luis"))
		#tem que retornar apenas 10, 3 serão descartados
		self.assertEqual(10,len(self.fac.gerenciador.ranking) )
		
			
unittest.main()
