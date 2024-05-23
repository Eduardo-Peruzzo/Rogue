import os.path
import random

from ...mecanicas import som
from .inimigo import Inimigo

import pygame

class Boss(Inimigo):
    def __init__(self):
        super().__init__()
        self.forca = random.randint(15, 30)
        self.vida = random.randint(50, 130)
        self.defesa = random.randint(1, 6)
        self.nome = "Boss"
        self.xp = 0

    @staticmethod
    def morrer():
        barulho = pygame.mixer.Sound(os.path.join(som.DIRETORIO, "vitoria.wav"))
        pygame.mixer.Sound.play(barulho)

    def defender(self, dano):
        dano -= self.defesa
        if dano > 0:
            self.vida -= dano