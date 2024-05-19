import random
from jogo.gui.cores import CORES

class Nether:
    def __init__(self, tesouro, npc, pocao) -> None:
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if [x, y] not in [tesouro.posicao, [0, 0], npc.posicao, pocao.posicao]:
                break

        self.posicao = [x, y]
        self.char = "{}"
        self.cor = CORES.roxo
        self.background = CORES.preto