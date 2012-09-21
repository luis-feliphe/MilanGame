# -*- coding: utf-8 -*-

import unittest
import os
from Nave import  Nave
from Facade import *


class TestFacade(unittest.TestCase):

	def setUp(self):
		self.fac = Facade()
		os.remove("Ranking.dat")
	
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
		self.assertEqual(True ,self.fac.partidaFoiIniciada())

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

	def testeMoverNaveForaDaTelaValoresPositivos(self):
		self.fac = Facade()
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		self.fac.moverNave(500,500)
		self.assertEqual((500,500),self.fac.getPosNave())

	def testeMoverNaveForaDaTelaValoresNegativos(self):
		self.fac = Facade()
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		self.fac.moverNave(-500,-500)
		self.assertEqual((0,0),self.fac.getPosNave())

	def testeAtacarInimigo(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		self.fac.atacarInimigo()
		lista = self.fac.getListaTiros()
		self.assertEqual(self.fac.getPosNave(),lista[0].getPos() )

	def testeAtacarInimigoMaisDeUmaVezEmPosicoesDiferentes(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		self.fac.atacarInimigo()
		pos1 = self.fac.getPosNave()
		self.fac.moverNave(25,10)
		pos2 = self.fac.getPosNave()
		self.fac.atacarInimigo()
		lista = self.fac.getListaTiros()
		self.assertEqual(pos1,lista[0].getPos() )
		self.assertEqual(pos2,lista[1].getPos() )

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


	#testes referentes a sair da Partida
	def testeSairDaPartida(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		self.fac.sairDaPartida()
		self.assertEqual(False, self.fac.partidaFoiIniciada())
		
	def testeSairPartidaAntesDoJogoIniciar(self):
		try: 
			unittest.TestCase.assertRaises(ExcecaoJogo, self.fac.sairDaPartida())
		except ExcecaoJogo as e : 
			self.assertEqual(e.message, "Jogo não iniciado")
	
	def testeSairPartidaAntesDaPartidaIniciar(self):
		self.fac.iniciarJogo()
		try: 
			unittest.TestCase.assertRaises(ExcecaoJogo, self.fac.sairDaPartida())
		except ExcecaoJogo as e : 
			self.assertEqual(e.message, "Partida não iniciada")
			
	def testeSairDaPartidaMaisDeUmaVez(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		self.fac.sairDaPartida()
		try: 
			unittest.TestCase.assertRaises(ExcecaoJogo, self.fac.sairDaPartida())
		except ExcecaoJogo as e : 
			self.assertEqual(e.message, "Partida não iniciada")		
	
	#testes referentes a sair do jogo
	def testeSairDoJogo(self):
		self.fac.iniciarJogo()
		self.fac.sairDoJogo()
		self.assertEqual(False, self.fac.jogoComecou())

	def testeSairDoJogoAntesDoJogoIniciar(self):
		try: 
			unittest.TestCase.assertRaises(ExcecaoJogo, self.fac.sairDoJogo())
		except ExcecaoJogo as e : 
			self.assertEqual(e.message, "Jogo não iniciado")

	def testeSairDoJogoComUmaPartidaAcontecendo(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		try:
			unittest.TestCase.assertRaises(ExcecaoJogo, self.fac.sairDoJogo())
		except ExcecaoJogo as e:
			self.assertEqual(e.message, "Voce precisa terminar a partida antes de sair")	
			
	def testeSairDoJogoDuasVezesSeguidas(self):
		self.fac.iniciarJogo()
		self.fac.sairDoJogo()
		try: 
			unittest.TestCase.assertRaises(ExcecaoJogo, self.fac.sairDoJogo())
		except ExcecaoJogo as e : 
			self.assertEqual(e.message, "Jogo não iniciado")
			
	#----------------------------* testesSistema *-----------------------------
	#testes vidas (perder e ganhar)
	def testeGanharVida(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		self.fac.ganharVida()
		#a nave inicia com 3 vidas
		self.assertEqual(4 , self.fac.getVida())
			
	def testeGanharVidaAntesDoJogoIniciar(self):
		try: 
			unittest.TestCase.assertRaises(ExcecaoJogo, self.fac.ganharVida())
		except ExcecaoJogo as e : 
			self.assertEqual(e.message, "Jogo não iniciado")
		
	def testeGanharVidaAntesPartidaIniciar(self):
		self.fac.iniciarJogo()
		try: 
			unittest.TestCase.assertRaises(ExcecaoJogo, self.fac.ganharVida())
		except ExcecaoJogo as e : 
			self.assertEqual(e.message, "Partida não iniciada")
			
	def testePerderVida(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		self.fac.perderVida()
		self.assertEqual(2,self.fac.getVida())

	def testePerderVidaAntesDoJogoIniciar(self):
		try: 
			unittest.TestCase.assertRaises(ExcecaoJogo, self.fac.perderVida())
		except ExcecaoJogo as e : 
			self.assertEqual(e.message, "Jogo não iniciado")

	def testePerderVidaAntesPartidaIniciar(self):
		self.fac.iniciarJogo()
		try: 
			unittest.TestCase.assertRaises(ExcecaoJogo, self.fac.perderVida())
		except ExcecaoJogo as e : 
			self.assertEqual(e.message, "Partida não iniciada")
	
	def testeTerminarPartidaQuandoZerarVidas(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		self.fac.perderVida()
		self.fac.perderVida()
		self.fac.perderVida()
		self.assertEqual(False, self.fac.partidaFoiIniciada())
	
	#navesInimigas
	def testeCriarNaveInimiga(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		self.assertEqual(0, len(self.fac.getListaNaves()))
		self.fac.criarNaveInimiga()
		self.assertEqual(1, len(self.fac.getListaNaves()))
		self.fac.criarNaveInimiga()
		self.assertEqual(2, len(self.fac.getListaNaves()))
		
	def testeCriarNaveAntesDoJogoComecar(self):
		try: 
			unittest.TestCase.assertRaises(ExcecaoJogo, self.fac.criarNaveInimiga())
		except ExcecaoJogo as e : 
			self.assertEqual(e.message, "Jogo não iniciado")
			
	def testeCriarNaveAntesDaPartidaComecar(self):
		self.fac.iniciarJogo()
		try: 
			unittest.TestCase.assertRaises(ExcecaoJogo, self.fac.criarNaveInimiga())
		except ExcecaoJogo as e : 
			self.assertEqual(e.message, "Partida não iniciada")
	
	def testeDestruirNaveInimiga(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		self.fac.criarNaveInimiga()
		listaDeNaves = self.fac.getListaNaves()
		self.fac.destruirNaveInimiga(listaDeNaves[0])
		self.assertEqual(0, len(self.fac.getListaNaves()))
	
	def testeDestruirNaveInimigaAntesDeIniciarJogo(self):
		nave = Nave(2, 3)
		try: 
			unittest.TestCase.assertRaises(ExcecaoJogo, self.fac.destruirNaveInimiga(nave))
		except ExcecaoJogo as e : 
			self.assertEqual(e.message, "Jogo não iniciado")
	
	def testeDestruirNaveInimigaAntesDeIniciarPartida(self):
		nave = Nave(4,2)
		self.fac.iniciarJogo()
		try: 
			unittest.TestCase.assertRaises(ExcecaoJogo, self.fac.destruirNaveInimiga(nave))
		except ExcecaoJogo as e : 
			self.assertEqual(e.message, "Partida não iniciada")
			
	def testeDestruirNaveInimigaSemNenhumaNave(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		nave = Nave(2,2)
		self.assertEqual(0, len(self.fac.getListaNaves()))
		self.fac.destruirNaveInimiga(nave)
		self.assertEqual(0, len(self.fac.getListaNaves()))
	
	def testeDestruirNaveInimigaFazJogadorGanharPontos(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		self.fac.criarNaveInimiga()
		listaDeNaves = self.fac.getListaNaves()
		self.fac.destruirNaveInimiga(listaDeNaves[0])
		self.assertEqual(100, self.fac.getPontuacao())

	#Testes do Ranking 	
	def testeSairDoJogo(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		self.fac.ganharVida()
		self.fac.ganharVida()
		self.fac.ganharVida()
		self.fac.ganharVida()
		self.fac.ganharVida()
		self.fac.ganharVida()
		self.assertEqual(True, self.fac.sairDaPartida())
		
#========================| Testes para o 3o Estágio |========================#
	
	def testeCadastraNoRanking(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		self.fac.ganharVida()
		self.fac.ganharVida()
		self.fac.ganharVida()
		self.fac.ganharVida()
		self.fac.ganharVida()
		self.fac.ganharVida()
		self.fac.ganharVida()
		self.fac.ganharVida()
		self.assertTrue(self.fac.sairDaPartida())
		self.fac.adicionarNomeNoRanking("Hermanoteu")	
		self.assertEqual(1, len(self.fac.getRanking()))
		self.assertEqual(self.fac.getRanking()[0][0],"Hermanoteu")
		self.assertEqual(self.fac.getRanking()[0][1], 150)
	
	def testeGetPontuacaoSemJogoIniciar(self):
		try:
			unittest.TestCase.assertRaises(self.fac.getPontuacao())
		except ExcecaoJogo as e:
			self.assertEqual(e.message, "Jogo não iniciado")	

	def testeCadastrarNoRankingSemJogoInciar(self):
		try:
			unittest.TestCase.assertRaises(self.fac.adicionarNomeNoRanking("Micalateia"))
		except ExcecaoJogo as e:
			self.assertEqual(e.message, "Jogo não iniciado")
	
	def testeCadastraNoRankingDuasVezesComMesmaPontuacao(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		self.fac.criarNaveInimiga()
		self.fac.ganharVida()
		self.fac.ganharVida()
		self.fac.ganharVida()
		self.fac.ganharVida()
		self.fac.ganharVida()
		self.fac.ganharVida()
		self.fac.ganharVida()
		self.fac.ganharVida()
		self.assertTrue(self.fac.sairDaPartida())
		self.fac.adicionarNomeNoRanking("Hermanoteu")	
		
		try:
			unittest.TestCase.assertRaises(self.fac.adicionarNomeNoRanking("Hermanoteu"))
		except ExcecaoJogo as e:
			self.assertEqual(e.message, "Voce ja adcionou seu nome ao ranking")
		self.assertEqual(1, len(self.fac.getRanking()))
	

	def testePassarDeFase700Pontos(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		self.fac.ganharVida()
		self.fac.ganharVida()
		self.fac.ganharVida()
		self.fac.ganharVida()
		self.fac.ganharVida()
		self.fac.ganharVida()
		self.fac.ganharVida()
		self.fac.ganharVida()
		self.fac.criarNaveInimiga()
		self.fac.criarNaveInimiga()
		self.fac.criarNaveInimiga()
		self.fac.criarNaveInimiga()
		self.fac.criarNaveInimiga()
		listaDeNaves = self.fac.getListaNaves()
		self.fac.destruirNaveInimiga(listaDeNaves[0])
		self.fac.destruirNaveInimiga(listaDeNaves[0])
		self.fac.destruirNaveInimiga(listaDeNaves[0])
		self.fac.destruirNaveInimiga(listaDeNaves[0])
		self.fac.destruirNaveInimiga(listaDeNaves[0])
		self.fac.ganharVida()
		
		self.assertTrue(self.fac.passouDeNivel())
		self.assertEqual(700, self.fac.getPontuacao())
		self.assertEqual(0, len(self.fac.getListaNaves()))
	
	#testes relacionados a camada de persistencia  (TODO)
	def testeGravarRankingEmArquivo(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		self.fac.ganharVida()
		self.fac.ganharVida()
		self.fac.ganharVida()
		self.fac.ganharVida()
		self.fac.ganharVida()
		self.fac.ganharVida()
		self.fac.ganharVida()
		self.fac.ganharVida()
		
		self.assertTrue(self.fac.sairDaPartida())
		
		self.fac.adicionarNomeNoRanking("Hermanoteu")
		
		#self.fac = Facade()
		self.assertEqual(1, len(self.fac.getRanking()))
		self.assertEqual(self.fac.getRanking()[0][0],"Hermanoteu")
		self.assertEqual(self.fac.getRanking()[0][1], 150)
		

unittest.main()
