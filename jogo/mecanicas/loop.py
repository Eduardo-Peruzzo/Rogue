import random
import pygame
from ..personagens.aventureiro import Aventureiro
from ..personagens.tesouro import Tesouro
from ..gui.tela import Tela
from . import mecanicas

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

    print(f"Saudações, {aventureiro.nome}! Boa sorte!")

    tela = Tela()

    while True:
        # Análise dos eventos
        teclas = pygame.key.get_pressed()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return

            if evento.type == pygame.KEYUP:

        # Processamento do jogo
                if teclas[pygame.K_q]:
                    print("Já correndo?")
                    return

                if teclas[pygame.K_t]:
                    aventureiro.ver_atributos()

                if not mecanicas.movimentar(aventureiro, determinar_direcao(teclas)):
                    print("Game Over")
                    return

                if aventureiro.posicao == tesouro.posicao:
                    print(f"Parabéns, {aventureiro.nome}, você encontrou o tesouro!")
                    return

        # Renderização da tela
        tela.renderizar(aventureiro, tesouro)
        pygame.time.Clock().tick(60)