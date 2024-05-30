from jogo.personagens.inimigos.inimigo import Inimigo
import random

class Wither(Inimigo):
    def __init__(self):
        self.forca = random.randint(45, 65)
        self.vida = random.randint(100, 140)
        self.nome = "Wither"
        self.xp = 12