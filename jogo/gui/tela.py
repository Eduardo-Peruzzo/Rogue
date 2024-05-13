import pygame
from .cores import CORES

GRID = 40
LARGURA = GRID * 10
ALTURA = GRID * 10

def centralizar_texto(texto, posicao_original):
    x = posicao_original[0] + (GRID - texto.get_width()) // 2
    y = posicao_original[1] + (GRID - texto.get_height()) // 2
    return [x, y]

class Tela:
    def __init__(self) -> None:
        self.display = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Rogue")

    def renderizar(self, aventureiro, tesouro):
        self.display.fill(CORES.preto)
        self.aventureiro(aventureiro)
        self.tesouro(tesouro)
        self.mapa(aventureiro, tesouro)
        pygame.display.update()

    def aventureiro(self, aventureiro):
        # definição da fonte
        fonte = pygame.font.SysFont(None, GRID)
        # renderização do texto
        texto = fonte.render("@", True, CORES.branco)
        # inserção do render na tela
        self.display.blit(texto, centralizar_texto(texto, [GRID * aventureiro.posicao[0], GRID * aventureiro.posicao[1]]))

    def tesouro(self, tesouro):
        fonte = pygame.font.SysFont(None, GRID)

        texto = fonte.render("X", True, CORES.branco)

        self.display.blit(texto, centralizar_texto(texto, [GRID * tesouro.posicao[0], GRID * tesouro.posicao[1]]))

    def mapa(self, aventureiro, tesouro):
        fonte = pygame.font.SysFont(None, GRID)
        texto = fonte.render(".", True, CORES.branco)
        for linha in range(10):
            for coluna in range(10):
                if [linha, coluna] not in [aventureiro.posicao, tesouro.posicao]:
                    self.display.blit(texto, centralizar_texto(texto, [linha * GRID, coluna * GRID]))