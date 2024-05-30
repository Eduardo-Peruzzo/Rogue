from jogo.personagens.inimigos.inimigo import Inimigo
import random

class Diabo(Inimigo):
    def __init__(self):
        self.forca = random.randint(100, 150)
        self.vida = random.randint(200, 250)
        self.nome = "Diabo"
        self.xp = 20