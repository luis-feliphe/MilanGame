from Inimigo import Inimigo
from Nave import Nave
import random
class NaveInimigaComum(Nave):

       def moverAleatorio(self):
                movimentoX = [1, 2, 3,  -1 , -2, -3]
                movimentoY = [1, 2, -2]
                self.moverNave(random.choice(movimentoX),random.choice( movimentoY))

