from . import mecanicas

from ..gui.tela import Tela

from ..personagens.aventureiro import Aventureiro
from ..personagens.tesouro import Tesouro
from ..personagens.npc import NPC
from ..personagens.pocao import Pocao
from ..personagens.inimigos.boss import Boss
from jogo.mecanicas.dificuldade import Dificuldade

import pygame




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
    """
    Fluxo principal do jogo, possui as seguintes etapas:
    - Inicia um aventureiro num dicionário com as propriedades:
        - forca: valor inteiro aleatório entre 10 e 18
        - defesa: valor inteiro aleatório entre 10 e 18
        - vida: valor inteiro aleatório entre 100 e 120
        - posicao: uma lista [0, 0]

    - Gera uma posição aleatória para o tesouro, usando a função gerar_tesouro
    - Lê um nome para o aventureiro, e armazena no dicionário
    - Desenha o mapa pela primeira vez
    - Em um loop infinito:
        - Lê o comando inserido pelo usuário
        - Se for o comando "Q", encerra o programa
        - Se for o comando "T", exibe os atributos do aventureiro
        - Se o comando for "W", "A", "S" ou "D":
            - Realiza o movimento e verifica o resultado da função movimentar
            - Se o resultado for True, desenha novamente o mapa
            - Se for False, imprime "Game over" na tela e encerra o programa
        - Se o usuário inserir algum comando diferente, diz que não reconheceu
        - Se a posição do aventureiro for igual à posição do tesouro, dispara
        uma mensagem que o aventureiro ganhou o jogo
    """
    aventureiro = Aventureiro()
    tesouro = Tesouro()
    npc = NPC(tesouro)
    pocao = Pocao(tesouro, npc)
    tela = Tela()
    dificuldade = Dificuldade()

    jogo_rodando = True
    while jogo_rodando:
        # Análise dos eventos
        teclas = pygame.key.get_pressed()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogo_rodando = False

            if evento.type == pygame.KEYUP:
                # Processamento do jogo
                if teclas[pygame.K_q]:
                    aventureiro.status = "Já correndo?"
                    jogo_rodando = False

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

        # Renderização na tela
        tela.renderizar(aventureiro, tesouro, npc, pocao, dificuldade)
        pygame.time.Clock().tick(60)