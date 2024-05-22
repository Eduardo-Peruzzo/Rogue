from .inimigo import Inimigo
import random

class Leviathan(Inimigo):
    def __init__(self):
        self.forca = random.randint(30, 40)
        self.vida = random.randint(80, 100)
        self.nome = "Leviathan"
        self.xp = 8