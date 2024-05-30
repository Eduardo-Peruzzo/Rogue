from jogo.personagens.inimigos.inimigo import Inimigo
import random

class Ender_dragon(Inimigo):
    def __init__(self):
        self.forca = random.randint(60, 80)
        self.vida = random.randint(140, 180)
        self.nome = "Ender Dragon"
        self.xp = 16