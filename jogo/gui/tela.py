from .cores import CORES

import pygame

GRID = 40
MARGEM = 10
LARGURA = GRID * 10 + 350
ALTURA = GRID * 10 + 100
FONTE = "Courier New"

def centralizar_texto(texto, posicao_original):
    x = GRID * posicao_original[0] + (LARGURA - 10 * GRID) // 2 + (GRID - texto.get_width()) // 2
    y = GRID * posicao_original[1] + (ALTURA - 10 * GRID) // 2 + (GRID - texto.get_height()) // 2
    return [x, y]

class Tela:
    def __init__(self):
        self.display = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Rogue")

        self.fonte_gde = pygame.font.SysFont(FONTE, GRID)
        self.fonte_peq = pygame.font.SysFont(FONTE, GRID // 2)

    def renderizar(self, aventureiro, tesouro, npc, pocao, dificuldade, portal):
        self.display.fill(CORES.preto)
        self.informacoes(aventureiro, dificuldade)
        self.personagem(tesouro)
        self.personagem(aventureiro)
        self.personagem(npc)
        self.personagem(pocao)
        self.personagem(portal)
        if aventureiro.dimensao == "nether":
            self.mapa_nether(aventureiro, tesouro, npc, pocao)
        else:
            self.mapa(aventureiro, tesouro, npc, pocao, portal)
        pygame.display.update()

    def mapa(self, aventureiro, tesouro, npc, pocao, portal):
        texto = self.fonte_gde.render(".", True, CORES.branco)
        for linha in range(10):
            for coluna in range(10):
                if [linha, coluna] not in [aventureiro.posicao, tesouro.posicao, npc.posicao, pocao.posicao, portal.posicao]:
                    self.display.blit(texto, centralizar_texto(texto, [linha, coluna]))

    def personagem(self, personagem):
        texto = self.fonte_gde.render(personagem.char, True, personagem.cor, personagem.background)
        self.display.blit(
            texto,
            centralizar_texto(texto, [personagem.posicao[0], personagem.posicao[1]])
        )

    def informacoes(self, aventureiro, dificuldade):
        atributos = f"{aventureiro.nome} {aventureiro.nv} / " \
            f"Vida: {aventureiro.vida:.0f} / Força: {aventureiro.forca:.0f} / Defesa: {aventureiro.defesa:.0f}"
        texto = self.fonte_peq.render(atributos, True, CORES.branco)
        self.display.blit(texto, [LARGURA // 2 - texto.get_width() // 2, ALTURA - MARGEM - texto.get_height()])

        texto = self.fonte_peq.render(aventureiro.status, True, CORES.branco)
        self.display.blit(texto, [MARGEM, MARGEM])

        texto = self.fonte_peq.render(f"Dificuldade: {dificuldade.multiplicador:.4f}", True, CORES.branco)
        self.display.blit(texto, [LARGURA - texto.get_width() - MARGEM, MARGEM])

    def mapa_nether(self, aventureiro, tesouro, npc, pocao):
        texto = self.fonte_gde.render(".", True, CORES.preto, CORES.roxo)
        for linha in range(10):
            for coluna in range(10):
                if [linha, coluna] not in [aventureiro.posicao, tesouro.posicao, npc.posicao, pocao.posicao]:
                    self.display.blit(texto, centralizar_texto(texto, [linha, coluna]))

    def renderizar_nether(self, aventureiro, tesouro, npc, pocao, dificuldade, portal):
        self.display.fill(CORES.roxo)
        self.informacoes(aventureiro, dificuldade)
        self.personagem(tesouro)
        self.personagem(aventureiro)
        self.personagem(npc)
        self.personagem(pocao)
        self.personagem(portal)

        self.mapa_nether(aventureiro, tesouro, npc, pocao)
        pygame.display.update()
