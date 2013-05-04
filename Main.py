import pygame, pygame.mixer 
import sys
from pygame.locals import *
from Facade import *


def atualizarTela():
	#repintar tela e nave
	tela.fill ((100,24,40))
	tela.blit(nave, facade.getPosNave())
	#repintar tiros 
	for tiro in facade.getListaTiros():
		tela.blit (imgtiro, tiro.getPos())
	#mover tiros 
	facade.moverTiros()	
	#repintar Naves Inimigas 
	for naveinimiga in facade.getListaNaves():
		tela.blit (imgNaveInimiga, naveinimiga.getPos())

	pygame.display.flip()


#algumas variaveis
velocidade = 100 
deslocamento = 2	

#iniciadno facade

facade = Facade()
facade.iniciarJogo()
facade.iniciarPartida()
#iniciando servicos do pygame

tempo = pygame.time.Clock()
pygame.init()
tela = pygame.display.set_mode(facade.getTamanhoTela())
pygame.display.set_caption("Milan the Hero of Space")
tela.fill ((100,24,40))

#inciando nave
nave = pygame.image.load("nave.png")
nave = pygame.transform.scale(nave, (100,100))
tela.blit(nave, facade.getPosNave())

#ajustando imagem de tiro 
imgtiro = pygame.image.load("tiro.png")
imgtiro = pygame.transform.scale(imgtiro, (15,70))


#ajustando imagem da nave inimiga 
imgNaveInimiga = pygame.image.load("naveInimiga.png")
imgNaveInimiga = pygame.transform.scale(imgNaveInimiga, (45,60))

#iniciando som
somTiro = pygame.mixer.Sound ("laser.wav")

#get mouse position 
#x, y = pygame.mouse.get_pos()
right = 0
left= 0
up = 0 
down = 0
navesInimigas = 0

sair = 0
while (True): 
	for event in pygame.event.get():
		if event.type == pygame.QUIT: pygame.quit() ;sys.exit()
		#sair
		elif event.type == KEYDOWN and event.key == K_ESCAPE:pygame.quit(); sys.exit()
		#apertar botao
		elif event.type == KEYDOWN and event.key == K_LEFT: left = 1
		elif event.type == KEYDOWN and event.key == K_RIGHT: right = 1
		elif event.type == KEYDOWN and event.key == K_UP: up = 1
		elif event.type == KEYDOWN and event.key == K_DOWN: down = 1
		elif event.type == KEYDOWN and event.key == K_SPACE: space = 1
		#soltar botao
		elif event.type == KEYUP and event.key == K_LEFT: left = 0
		elif event.type == KEYUP and event.key == K_RIGHT: right = 0
		elif event.type == KEYUP and event.key == K_UP: up = 0
		elif event.type == KEYUP and event.key == K_DOWN: down = 0
		elif event.type == KEYUP and event.key == K_SPACE: facade.atacarInimigo();somTiro.play()
		if (navesInimigas < 3):
			facade.criarNaveInimiga()
			navesInimigas+= 1
		facade.moverNavesInimigas()
	if right: facade.moverNave(deslocamento, 0)#deslocamento x , deslocamento y
	if up: facade.moverNave(0, -deslocamento) #deslocamento x , deslocamento y
	if down:facade.moverNave(0, deslocamento) #deslocamento x , deslocamento y 
	if left: facade.moverNave(-deslocamento, 0) #deslocamento x , deslocamento y
	#elif event.type == KEYDOWN and event.key == K_SPACE:musicaFundo.stop(); pygame.image.save(tela, "screenshot")
	#mover naves inimigas 

	tempo.tick(velocidade)
	atualizarTela()
	


