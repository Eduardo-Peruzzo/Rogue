from .inimigo import Inimigo

class Monstro(Inimigo):
    def __init__(self):
        super().__init__()
        self.nome = "Monstro"