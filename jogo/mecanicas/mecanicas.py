import random
from jogo.gui.cores import CORES
import pygame
import os
import os.path
from . import som
from ..personagens.inimigos.leviathan import Leviathan
from ..personagens.inimigos.goblin import Goblin
from ..personagens.inimigos.ogro import Ogro
import time


# Combate
def iniciar_combate(aventureiro, inimigo):
    while True:
        dano = aventureiro.atacar()
        inimigo.defender(dano)
        if not inimigo.esta_vivo():
            if inimigo.nome == "Boss":
                inimigo.morrer()
            return True

        dano = inimigo.atacar()
        aventureiro.defender(dano)
        if not aventureiro.esta_vivo():
            aventureiro.morrer()
            return False

def existe_obstaculo(posicao, npc):
    x, y = posicao
    if x < 0 or x > 9 or y < 0 or y > 9:
        return True

    if posicao == npc.posicao:
        return True

    return False

# Operação principal do jogo
def movimentar(aventureiro, direcao, npc, dificuldade):
    pos_futura = aventureiro.calcular_pos_futura(direcao)
    if existe_obstaculo(pos_futura, npc):
        return True

    aventureiro.andar(pos_futura)

    efeito = random.choices(["nada", "monstro"], [0.6, 0.4])[0]
    if efeito == "monstro":
        monstro = random.choices([Leviathan, Ogro, Goblin], [1, 3, 10])[0]()
        monstro.forca = int(monstro.forca * dificuldade.multiplicador)
        monstro.vida = int(monstro.vida * dificuldade.multiplicador)
        if iniciar_combate(aventureiro, monstro):
            aventureiro.status = f"{monstro.nome} foi derrotado!"
            aventureiro.xp += monstro.xp
            # Aventureiro sobe de nível
            if aventureiro.xp >= aventureiro.xp_por_nivel:
                aventureiro.xp = 0
                aventureiro.nivel += 1
                aventureiro.forca = aventureiro.forca + (aventureiro.forca * 0.1)
                aventureiro.defesa = aventureiro.defesa + (aventureiro.defesa * 0.1)
                aventureiro.vida += 10
                aventureiro.xp_por_nivel += 1
                levelup = pygame.mixer.Sound(os.path.join(som.DIRETORIO, "levelup.wav"))
                pygame.mixer.Sound.play(levelup)
            else:
                monstro.morrer()
            aventureiro.nv = f"nv {aventureiro.nivel} ({aventureiro.xp}/{aventureiro.xp_por_nivel})"
            return True

        aventureiro.status = f"Você foi derrotado por {monstro.nome}! Game Over..."
        return False

    aventureiro.status = "Continue explorando"
    som.passo()
    return True

def conversar(aventureiro, npc):
    x_a, y_a = aventureiro.posicao
    x_n, y_n = npc.posicao

    if (x_a + 1 == x_n or x_a - 1 == x_n) and y_a == y_n:
        aventureiro.status = npc.mensagem
        npc.falar()

    if (y_a + 1 == y_n or y_a - 1 == y_n) and x_a == x_n:
        aventureiro.status = npc.mensagem
        npc.falar()

def tomar_pocao(aventureiro, pocao):
    if pocao.efeito == 1:
        aventureiro.vida *= 2
        aventureiro.status = "Sua vida foi dobrada!"

    if pocao.efeito == 2:
        aventureiro.forca += 15
        aventureiro.status = "Sua força aumentou em 15!"

    if pocao.efeito == 3:
        aventureiro.defesa += 10
        aventureiro.status = "Sua defesa aumentou em 10!"

    pocao.posicao = [1000, 1000]
    aventureiro.tomou_pocao = "sim"
