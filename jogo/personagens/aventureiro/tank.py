from .aventureiro import Aventureiro

import random

class Tank(Aventureiro):
    def __init__(self, nome):
        super().__init__(nome)
        self.forca = random.randint(8, 15)
        self.defesa = random.randint (15, 20)
        self.vida = random.randint(120, 150)