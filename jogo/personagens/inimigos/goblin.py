from .inimigo import Inimigo
import random

class Goblin(Inimigo):
    def __init__(self):
        self.forca = random.randint(5, 15)
        self.vida = random.randint(10, 40)
        self.nome = "Goblin"
        self.xp = 1