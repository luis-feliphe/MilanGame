# -*- coding: utf-8 -*-

import unittest
import os
from Nave import  Nave
from Facade import *


class TestFacade(unittest.TestCase):

	def setUp(self):
		arquivoExiste= os.path.isfile("Ranking.dat")
		if(arquivoExiste):
			os.remove("Ranking.dat")
		self.fac = Facade()

	def ganharVida(self, n):
		for i in range (0,n):
			self.fac.ganharVida()

	def perderVida(self, n):
		for i in range (0,n):
			self.fac.perderVida()


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
		self.assertEqual(1, len(self.fac.getListaNaves()))
		listaDeNaves = self.fac.getListaNaves()
		self.fac.destruirNaveInimiga(listaDeNaves[0])
		self.assertEqual(100, self.fac.getPontuacao())
		self.assertEqual(0, len(self.fac.getListaNaves()))		
		#varias naves
		self.fac.criarNaveInimiga()
		self.assertEqual(1, len(self.fac.getListaNaves()))
		self.fac.criarNaveInimiga()
		self.assertEqual(2, len(self.fac.getListaNaves()))
		self.fac.criarNaveInimiga()
		self.assertEqual(3, len(self.fac.getListaNaves()))
		self.fac.criarNaveInimiga()
		self.assertEqual(4, len(self.fac.getListaNaves()))
		self.fac.destruirNaveInimiga(listaDeNaves[0])
		self.fac.destruirNaveInimiga(listaDeNaves[0])
		self.fac.destruirNaveInimiga(listaDeNaves[0])
		self.fac.destruirNaveInimiga(listaDeNaves[0])
		self.assertEqual(0, len(self.fac.getListaNaves()))
		self.assertEqual(500, self.fac.getPontuacao())

	#Testes do Ranking 	
	def testeSairDaPartida(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		self.fac.criarNaveInimiga()
		self.fac.criarNaveInimiga()
		self.assertEqual(2, len(self.fac.getListaNaves()))
		self.fac.destruirNaveInimiga(self.fac.getListaNaves()[0])
		self.fac.destruirNaveInimiga(self.fac.getListaNaves()[0])
		self.assertEqual(0, len(self.fac.getListaNaves()))
		self.ganharVida(6)
		self.assertEqual(True, self.fac.sairDaPartida())
	
	def testeCadastraNoRanking(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		#ganhar pontos com vidas
		self.ganharVida(8)
		#ganhar pontos com alvos abatidos
		self.fac.criarNaveInimiga()
		self.fac.criarNaveInimiga()
		self.fac.criarNaveInimiga()
		self.assertEqual(3, len(self.fac.getListaNaves()))
		self.fac.destruirNaveInimiga(self.fac.getListaNaves()[0])
		self.fac.destruirNaveInimiga(self.fac.getListaNaves()[0])
		self.fac.destruirNaveInimiga(self.fac.getListaNaves()[0])
		self.assertEqual(0, len(self.fac.getListaNaves()))
		self.assertTrue(self.fac.sairDaPartida())
		self.fac.adicionarNomeNoRanking("Hermanoteu")	
		self.assertEqual(1, len(self.fac.getRanking()))
		self.assertEqual(self.fac.getRanking()[0][0],"Hermanoteu")
		self.assertEqual(self.fac.getRanking()[0][1], 450)
	
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
		#criando naves e ganhando vidas para conseguir pontos
		self.fac.criarNaveInimiga()
		self.fac.criarNaveInimiga()
		self.fac.criarNaveInimiga()
		self.fac.criarNaveInimiga()
		self.assertEqual(4, len(self.fac.getListaNaves()))
		self.fac.destruirNaveInimiga(self.fac.getListaNaves()[0])
		self.fac.destruirNaveInimiga(self.fac.getListaNaves()[0])
		self.fac.destruirNaveInimiga(self.fac.getListaNaves()[0])
		self.fac.destruirNaveInimiga(self.fac.getListaNaves()[0])
		self.assertEqual(0, len(self.fac.getListaNaves()))
		self.ganharVida(3)
		self.assertEqual(0, len(self.fac.getRanking()))
		self.assertTrue(self.fac.sairDaPartida())
		self.fac.adicionarNomeNoRanking("Hermanoteu")
		self.assertEqual(1, len(self.fac.getRanking()))
		self.fac.adicionarNomeNoRanking("Hermanoteu")
		self.assertEqual(1, len(self.fac.getRanking()))
	
	def testeCadastraNoRankingEVerificarOrdem(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		#criando naves e ganhando vidas para conseguir pontos
		self.ganharVida(7)
		self.assertEqual(100, self.fac.getPontuacao())
		self.assertEqual(0, len(self.fac.getRanking()))
		self.assertTrue(self.fac.sairDaPartida())
		self.fac.adicionarNomeNoRanking("Hermanoteu")
		self.fac.sairDoJogo
		self.fac.iniciarPartida()
		self.assertEqual(0, self.fac.getPontuacao())
		self.ganharVida(6)
		self.assertEqual(50, self.fac.getPontuacao())
		self.assertEqual(1, len(self.fac.getRanking()))
		self.assertTrue(self.fac.sairDaPartida())
		self.fac.adicionarNomeNoRanking("raquel")
		self.fac.iniciarPartida()
		self.ganharVida(8)		
		self.assertEqual(150, self.fac.getPontuacao())
		self.assertEqual(2, len(self.fac.getRanking()))
		self.assertTrue(self.fac.sairDaPartida())
		self.fac.adicionarNomeNoRanking("Truta")
		self.assertEqual(3, len(self.fac.getRanking()))
		self.fac.iniciarPartida()
		self.ganharVida(8)
		self.assertEqual(150, self.fac.getPontuacao())
		self.assertEqual(3, len(self.fac.getRanking()))
		self.assertTrue(self.fac.sairDaPartida())
		self.fac.adicionarNomeNoRanking("Feliphe")
		self.assertEqual(4, len(self.fac.getRanking()))
		self.assertEqual(self.fac.getRanking()[0][0],"Feliphe")
		self.assertEqual(self.fac.getRanking()[0][1], 150)
		self.assertEqual(self.fac.getRanking()[1][0],"Truta")
		self.assertEqual(self.fac.getRanking()[1][1], 150)
		self.assertEqual(self.fac.getRanking()[2][0],"Hermanoteu")
		self.assertEqual(self.fac.getRanking()[2][1], 100)
		self.assertEqual(self.fac.getRanking()[3][0],"raquel")
		self.assertEqual(self.fac.getRanking()[3][1], 50)
	
	def testeGetNivel(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		self.assertEqual(1, self.fac.getNivel())
		self.assertTrue(self.fac.sairDaPartida())

	def testeGetNivelAntesDoJogoIniciar(self):
		try:
			unittest.TestCase.assertRaises(self.fac.getNivel())
		except ExcecaoJogo as e:
			self.assertEqual(e.message, "Jogo não iniciado")
	
	def testeGetNivelAntesDaPartidaIniciar(self):
		self.fac.iniciarJogo()
		try:
			unittest.TestCase.assertRaises(self.fac.getNivel())
		except ExcecaoJogo as e:
			self.assertEqual(e.message, "Partida não iniciada")
	
	def testeTerminarPartidaQuandoZerarVidasENaoAdicionarNoRankingPorNaoTerPontos(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		self.perderVida(2)
		self.assertTrue(self.fac.perderVida())
		try:
			unittest.TestCase.assertRaises(self.fac.adicionarNomeNoRanking("Hermanoteu"))
		except ExcecaoJogo as e:
			self.assertEqual(e.message, "Você precisa ter pontuação maior que zero")

	def testeTerminarPartidaQuandoZerarVidasEAdicionarNoRanking(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		self.ganharVida(20)
		self.perderVida(7)
		self.assertTrue(self.fac.perderVida())
		self.fac.adicionarNomeNoRanking("Hermanoteu")
		self.assertEqual(1, len(self.fac.getRanking()))
		self.assertEqual(self.fac.getRanking()[0][0],"Hermanoteu")
		self.assertEqual(self.fac.getRanking()[0][1], 750)

	def testePassarDeNivelEm700Pontos(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		self.ganharVida(8)
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
		self.assertEqual(650, self.fac.getPontuacao())
		#confere se ainda esta no nivel 1
		self.assertEqual(1, self.fac.getNivel())
		self.fac.ganharVida()
		#com a ultima vida ganha, passa para o nivel 2 com 700 pontos
		self.assertEqual(700, self.fac.getPontuacao())
		self.assertEqual(2, self.fac.getNivel())

	def testePassarDeNivelAteFimDoJogo(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		self.ganharVida(8)
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
		self.assertEqual(650, self.fac.getPontuacao())
		self.assertEqual(1, self.fac.getNivel())
		self.fac.ganharVida()
		#com a ultima vida ganha, passa para o nivel 2 com 700 pontos
		self.assertEqual(700, self.fac.getPontuacao())
		self.assertEqual(2, self.fac.getNivel())
		self.ganharVida(14)
		self.assertEqual(1400, self.fac.getPontuacao())
		self.assertEqual(3, self.fac.getNivel())
		self.ganharVida(14)
		self.assertEqual(2100, self.fac.getPontuacao())
		self.assertEqual(4, self.fac.getNivel())		
		self.ganharVida(13)
		self.assertFalse(self.fac.ganharVida())
		self.assertEqual(2800, self.fac.getPontuacao())
		self.assertEqual(5, self.fac.getNivel())
		self.ganharVida(13)
		self.assertTrue(self.fac.ganharVida())
		self.fac.adicionarNomeNoRanking("Hermanoteu")

	def testeGanharOuPerderVidaDepoisDeZerar(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		self.ganharVida(18)
		self.assertEqual(650, self.fac.getPontuacao())
		self.assertEqual(1, self.fac.getNivel())
		self.fac.ganharVida()
		self.assertEqual(700, self.fac.getPontuacao())
		self.assertEqual(2, self.fac.getNivel())
		self.ganharVida(14)
		self.assertEqual(1400, self.fac.getPontuacao())
		self.assertEqual(3, self.fac.getNivel())
		self.ganharVida(14)
		self.assertEqual(2100, self.fac.getPontuacao())
		self.assertEqual(4, self.fac.getNivel())		
		self.ganharVida(13)
		self.assertFalse(self.fac.ganharVida())
		self.assertEqual(2800, self.fac.getPontuacao())
		self.assertEqual(5, self.fac.getNivel())
		self.ganharVida(13)
		self.assertTrue(self.fac.ganharVida())
		self.fac.adicionarNomeNoRanking("Hermanoteu")
		#teste ganhar vida
		try: 
			unittest.TestCase.assertRaises(ExcecaoJogo, self.fac.ganharVida())
		except ExcecaoJogo as e : 
			self.assertEqual(e.message, "Partida não iniciada")
		#teste Perder Vida			
		try: 
			unittest.TestCase.assertRaises(ExcecaoJogo, self.fac.perderVida())
		except ExcecaoJogo as e : 
			self.assertEqual(e.message, "Partida não iniciada")

	def testeGravarRankingEmArquivoEVerificarSeDadosVoltamOrdenados(self):
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		self.ganharVida(8)
		self.assertTrue(self.fac.sairDaPartida())
		self.fac.adicionarNomeNoRanking("Hermanoteu")
		self.assertEqual(1, len(self.fac.getRanking()))
		self.assertEqual(self.fac.getRanking()[0][0],"Hermanoteu")
		self.assertEqual(self.fac.getRanking()[0][1], 150)
		#verificando se hermanoteu foi recuperado com sucesso 
		self.fac = Facade()	
		self.assertEqual(1, len(self.fac.getRanking()))
		self.assertEqual(self.fac.getRanking()[0][0],"Hermanoteu")
		self.assertEqual(self.fac.getRanking()[0][1], 150)
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		self.ganharVida(8)
		self.assertTrue(self.fac.sairDaPartida())
		self.fac.adicionarNomeNoRanking("Manolo")
		self.assertEqual(2, len(self.fac.getRanking()))
		self.assertEqual(self.fac.getRanking()[0][0],"Hermanoteu")
		self.assertEqual(self.fac.getRanking()[0][1], 150)
		self.assertEqual(self.fac.getRanking()[1][0],"Manolo")
		self.assertEqual(self.fac.getRanking()[1][1], 150)
		#Verificando se Manolo e hermanoteu foram recuperados com sucesso e ornados alfabeticamente 
		self.fac = Facade()
		self.assertEqual(2, len(self.fac.getRanking()))
		self.assertEqual(self.fac.getRanking()[0][0],"Hermanoteu")
		self.assertEqual(self.fac.getRanking()[0][1], 150)
		self.assertEqual(self.fac.getRanking()[1][0],"Manolo")
		self.assertEqual(self.fac.getRanking()[1][1], 150)
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		self.ganharVida(9)
		self.assertTrue(self.fac.sairDaPartida())
		self.fac.adicionarNomeNoRanking("Truta")
		self.assertEqual(3, len(self.fac.getRanking()))
		self.assertEqual(self.fac.getRanking()[0][0],"Truta")
		self.assertEqual(self.fac.getRanking()[0][1], 200)
		self.assertEqual(self.fac.getRanking()[1][0],"Hermanoteu")
		self.assertEqual(self.fac.getRanking()[1][1], 150)
		self.assertEqual(self.fac.getRanking()[2][0],"Manolo")
		self.assertEqual(self.fac.getRanking()[2][1], 150)
		#Verificando se Hermanoteu, Manolo e Truta foram recuperados com sucesso(primeiro em pontuacao e depois em ordem alfabetica)
		self.fac = Facade()
		self.assertEqual(3, len(self.fac.getRanking()))
		self.assertEqual(self.fac.getRanking()[0][0],"Truta")
		self.assertEqual(self.fac.getRanking()[0][1], 200)
		self.assertEqual(self.fac.getRanking()[1][0],"Hermanoteu")
		self.assertEqual(self.fac.getRanking()[1][1], 150)
		self.assertEqual(self.fac.getRanking()[2][0],"Manolo")
		self.assertEqual(self.fac.getRanking()[2][1], 150)		
		self.fac.iniciarJogo()
		self.fac.iniciarPartida()
		self.ganharVida(7)
		self.assertTrue(self.fac.sairDaPartida())
		self.fac.adicionarNomeNoRanking("Micalateia")
		self.assertEqual(4, len(self.fac.getRanking()))
		self.fac = Facade()
		self.assertEqual(self.fac.getRanking()[0][0],"Truta")
		self.assertEqual(self.fac.getRanking()[0][1], 200)
		self.assertEqual(self.fac.getRanking()[1][0],"Hermanoteu")
		self.assertEqual(self.fac.getRanking()[1][1], 150)
		self.assertEqual(self.fac.getRanking()[2][0],"Manolo")
		self.assertEqual(self.fac.getRanking()[2][1], 150)
		self.assertEqual(self.fac.getRanking()[3][0],"Micalateia")
		self.assertEqual(self.fac.getRanking()[3][1], 100)

unittest.main()
