import random
from jogo.gui.cores import CORES

class Pocao:
    def __init__(self, tesouro, npc) -> None:
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if [x, y] not in [tesouro.posicao, [0, 0], npc.posicao]:
                break

        self.posicao = [x, y]
        self.char = "%"
        self.cor = CORES.verde
        self.efeito = random.randint(1, 3)