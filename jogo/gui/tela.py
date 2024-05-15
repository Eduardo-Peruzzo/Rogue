import pygame
from .cores import CORES

GRID = 40
MARGEM = 10
LARGURA = GRID * 10 + 200
ALTURA = GRID * 10 + 100
FONTE = "Courier New"

def centralizar_texto(texto, posicao_original):
    x = GRID * posicao_original[0] + (LARGURA - GRID*10) // 2 + (GRID - texto.get_width()) // 2
    y = GRID * posicao_original[1] + (ALTURA - GRID*10) // 2 + (GRID - texto.get_height()) // 2
    return [x, y]

class Tela:
    def __init__(self) -> None:
        self.display = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Rogue")

        self.fonte_grd = pygame.font.SysFont(FONTE, GRID)
        self.fonte_peq = pygame.font.SysFont(FONTE, GRID // 2)

    def renderizar(self, aventureiro, tesouro, npc):
        self.display.fill(CORES.preto)
        self.personagem(aventureiro)
        self.personagem(tesouro)
        self.personagem(npc)
        self.informacoes(aventureiro)
        self.mapa(aventureiro, tesouro, npc)
        pygame.display.update()

    def personagem(self, personagem):
        texto = self.fonte_grd.render(personagem.char, True, CORES.branco)

        self.display.blit(texto, centralizar_texto(texto, [personagem.posicao[0], personagem.posicao[1]]))

    def informacoes(self, aventureiro):
        # renderização do texto
        # texto = self.fonte_grd.render("@", True, CORES.branco)

        # inserção do render na tela
        # self.display.blit(texto, centralizar_texto(texto, [aventureiro.posicao[0], aventureiro.posicao[1]]))

        atributos = """{} / Vida: {} / Força: {} / Defesa: {}""".format(aventureiro.nome, aventureiro.vida, aventureiro.forca, aventureiro.defesa)

        texto = self.fonte_peq.render(atributos, True, CORES.branco)
        self.display.blit(texto, [MARGEM, ALTURA - MARGEM - texto.get_height()])

        texto = self.fonte_peq.render(aventureiro.status, True, CORES.branco)
        self.display.blit(texto, [MARGEM, MARGEM])

    def mapa(self, aventureiro, tesouro, npc):
        texto = self.fonte_grd.render(".", True, CORES.branco)
        for linha in range(10):
            for coluna in range(10):
                if [linha, coluna] not in [aventureiro.posicao, tesouro.posicao, npc.posicao]:
                    self.display.blit(texto, centralizar_texto(texto, [linha, coluna]))