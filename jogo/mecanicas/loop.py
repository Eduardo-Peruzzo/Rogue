from . import mecanicas
import time
from ..gui.tela import Tela
from jogo.gui.cores import CORES
from ..personagens.aventureiro.aventureiro import Aventureiro
from ..personagens.aventureiro.guerreiro import Guerreiro
from ..personagens.aventureiro.tank import Tank
from ..personagens.aventureiro.victor import Victor
from ..personagens.tesouro import Tesouro
from ..personagens.npc import NPC
from ..personagens.pocao import Pocao
from ..personagens.inimigos.boss import Boss
from ..personagens.inimigos.inimigos_nether.boss_nether import Hades
from jogo.mecanicas.dificuldade import Dificuldade
from jogo.dimensao.nether import Nether
from .inputbox import ler_texto
from .buttonbox import escolher_classe
from . import som
import os
import os.path
import pygame
from jogo.gui.relogio import Relogio



def determinar_direcao(teclas):
    if teclas[pygame.K_a]:
        return "A"
    if teclas[pygame.K_w]:
        return "W"
    if teclas[pygame.K_s]:
        return "S"
    if teclas[pygame.K_d]:
        return "D"

    return ""


def executar():
    som.iniciar_musica()

    nome = ler_texto()
    if nome == "victor" or nome == "Victor":
        aventureiro = Victor(nome)
    else:
        classe = escolher_classe()
        match classe:
            case "Guerreiro":
                aventureiro = Guerreiro(nome)
            case "Tank":
                aventureiro = Tank(nome)
            case _:
                aventureiro = Aventureiro(nome)
    tesouro = Tesouro()
    npc = NPC(tesouro)
    pocao = Pocao(tesouro, npc)
    portal = Nether(tesouro, npc, pocao)
    tela = Tela()
    dificuldade = Dificuldade()

    jogo_rodando = True
    while jogo_rodando:
        # Análise dos eventos

        if aventureiro.tomou_pocao == "sim": # Quando o player tomar a poção ele vai ficar piscando em várias cores, para indicar que ele ficou mais forte!
            aventureiro.trocar_cor()
            time.sleep(0.05)

        if aventureiro.tomou_pocao == "sim": # O efeito da poção acaba em 10 segundos.
            if relogio.medir_tempo() >= 10:
                mecanicas.destomar_pocao(aventureiro, pocao)
                aventureiro.tomou_pocao = "nao"
                aventureiro.cor = CORES.branco

        teclas = pygame.key.get_pressed()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogo_rodando = False



            if evento.type == pygame.KEYUP:
                # Processamento do jogo
                if teclas[pygame.K_q]:
                    aventureiro.status = "Já correndo?"
                    jogo_rodando = False

                if teclas[pygame.K_c]:
                    aventureiro.trocar_char()
                elif teclas[pygame.K_v]:
                    aventureiro.trocar_cor()
                elif teclas[pygame.K_b]:
                    aventureiro.trocar_cor(aleatorio=True)

                if teclas[pygame.K_n]:
                    dificuldade.multiplicador /= 1.1

                if teclas[pygame.K_m]:
                    dificuldade.multiplicador *= 1.1

                if teclas[pygame.K_SPACE]:
                    mecanicas.conversar(aventureiro, npc)

                elif teclas[pygame.K_a] or teclas[pygame.K_d] or teclas[pygame.K_s] or teclas[pygame.K_w]:
                    if not mecanicas.movimentar(aventureiro, determinar_direcao(teclas), npc, dificuldade):
                        jogo_rodando = False

                    if aventureiro.posicao == tesouro.posicao:
                        if aventureiro.dimensao == "nether_dentro":
                            boss = Hades()
                            boss.vida *= dificuldade.multiplicador
                            boss.forca *= dificuldade.multiplicador
                            boss.defesa *= dificuldade.multiplicador
                            if mecanicas.iniciar_combate(aventureiro, boss):
                                aventureiro.status = f"Você derrotou {boss.nome} e encontrou o tesouro!"
                            else:
                                aventureiro.status = f"Você foi derrotado por {boss.nome}! Game over..."
                            jogo_rodando = False
                        else:
                            boss = Boss()
                            boss.vida *= dificuldade.multiplicador
                            boss.forca *= dificuldade.multiplicador
                            boss.defesa *= dificuldade.multiplicador
                            if mecanicas.iniciar_combate(aventureiro, boss):
                                aventureiro.status = f"Você derrotou {boss.nome} e encontrou o tesouro!"
                            else:
                                aventureiro.status = f"Você foi derrotado por {boss.nome}! Game over..."
                            jogo_rodando = False

                    if aventureiro.posicao == pocao.posicao:
                        mecanicas.tomar_pocao(aventureiro, pocao)
                        relogio = Relogio()

                    if aventureiro.posicao == portal.posicao:
                        portal.posicao = [1000, 1000]
                        aventureiro.dimensao = "nether"

        # Renderização na tela
        if aventureiro.dimensao == "nether":
            tesouro = Tesouro()
            npc = NPC(tesouro)
            pocao = Pocao(tesouro, npc)
            tela.renderizar_nether(aventureiro, tesouro, npc, pocao, dificuldade, portal)
            aventureiro.dimensao = "nether_dentro"
            aventureiro.background = CORES.roxo
            pocao.background = CORES.roxo
            npc.background = CORES.roxo
            tesouro.background = CORES.roxo
            aventureiro.posicao = [0, 0]
            aventureiro.status = "Você entrou em outra dimensão!"
            pygame.mixer.music.load(os.path.join(som.DIRETORIO, "musica_nether.mp3"))
            pygame.mixer.music.set_volume(0.4)
            pygame.mixer.music.play(-1, 98)

        elif aventureiro.dimensao == "nether_dentro":
            tela.renderizar_nether(aventureiro, tesouro, npc, pocao, dificuldade, portal)
        else:
            tela.renderizar(aventureiro, tesouro, npc, pocao, dificuldade, portal)
        pygame.time.Clock().tick(60)