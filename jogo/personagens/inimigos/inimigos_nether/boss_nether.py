import os.path
import random

from ....mecanicas import som
from ..inimigo import Inimigo

import pygame

class Hades(Inimigo):
    def __init__(self):
        super().__init__()
        self.forca = random.randint(150, 250)
        self.vida = random.randint(300, 350)
        self.defesa = random.randint(30, 50)
        self.nome = "Hades"
        self.xp = 0

    @staticmethod
    def morrer():
        barulho = pygame.mixer.Sound(os.path.join(som.DIRETORIO, "vitoria.wav"))
        pygame.mixer.Sound.play(barulho)

    def defender(self, dano):
        dano -= self.defesa
        if dano > 0:
            self.vida -= dano