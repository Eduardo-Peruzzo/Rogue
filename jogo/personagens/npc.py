import random
from jogo.gui.cores import CORES

class NPC:
    def __init__(self, tesouro):
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if [x, y] not in [tesouro.posicao, [0, 0]]:
                break

        self.posicao = [x, y]
        self.char = "&"
        self.mensagem = "Olá! Eu sou um NPC!"
        self.cor = CORES.amarelo
        self.background = CORES.preto