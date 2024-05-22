from .inimigo import Inimigo
import random

class Ogro(Inimigo):
    def __init__(self):
        self.forca = random.randint(10, 25)
        self.vida = random.randint(50, 100)
        self.nome = "Ogro"
        self.xp = 3