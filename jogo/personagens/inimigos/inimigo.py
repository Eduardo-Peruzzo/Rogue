import random

class Inimigo:
    def __init__(self):
        self.forca = random.randint(5, 25)
        self.vida = random.randint(10, 100)

    def atacar(self):
        return self.forca

    def defender(self, dano):
        self.vida -= dano

    def esta_vivo(self):
        return self.vida > 0