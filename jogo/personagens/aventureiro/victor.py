from .aventureiro import Aventureiro

import random

class Victor(Aventureiro): # Sub-classe secreta do Victor, o aventureiro mais poderoso!
    def __init__(self, nome):
        super().__init__(nome)
        self.forca = random.randint(50, 100)
        self.defesa = random.randint (40, 80)
        self.vida = random.randint(500, 1000)

        self.char = "V"
        self.chars.append("V")