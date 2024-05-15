import random

class NPC:
    def __init__(self, tesouro) -> None:
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if [x, y] not in [tesouro.posicao, [0, 0]]:
                break

        self.posicao = [x, y]
        self.char = "!"