import random
from jogo.gui.cores import CORES

class Tesouro:
    def __init__(self):
        """
        Gera o tesouro em uma posição aleatória no mapa, diferente de [0, 0].

        Ou seja, deve gerar uma coordenada x entre 0 e 9, e uma coordenada y entre
        0 e 9. Porém, se a coordenada gerada for (0, 0), deve gerar uma nova
        coordenada, até atender ao requisito.
        """
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if not (x == y == 0):
                break

        self.posicao = [x, y]
        self.char = "X"
        self.cor = CORES.vermelho
        self.background = CORES.preto