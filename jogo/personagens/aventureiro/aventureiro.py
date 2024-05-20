import random
from jogo.gui.cores import CORES

class Aventureiro:
    def __init__(self, nome):
        self.forca = random.randint(10, 18)
        self.defesa = random.randint(10, 18)
        self.vida = random.randint(100, 120)
        self.posicao = [0, 0]
        self.char = "@"
        self.nome = nome
        self.status = "Comece a explorar"
        self.cor = CORES.branco
        self.background = CORES.preto
        self.nivel = 1
        self.monstros_derrotados = 0
        self.xp_por_nivel = 1
        self.xp = f"nv {self.nivel} ({self.monstros_derrotados}/{self.xp_por_nivel})"
        self.dimensao = "normal"

    def calcular_pos_futura(self, direcao):
        x, y = self.posicao
        match direcao:
            case "W":
                y -= 1
            case "S":
                y += 1
            case "A":
                x -= 1
            case "D":
                x += 1

        return [x, y]

    def andar(self, nova_posicao):
        self.posicao = nova_posicao

    def atacar(self):
        return self.forca + random.randint(1, 6)

    def defender(self, dano):
        dano_levado = dano - self.defesa
        if dano_levado > 0:
            self.vida -= dano_levado

    def ver_atributos(self):
        print("Informações de ", self.nome, ":", sep="")
        print("Vida:", self.vida)
        print("Força:", self.forca)
        print("Defesa:", self.defesa)

    def esta_vivo(self):
        return self.vida > 0