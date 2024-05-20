from jogo.gui.buttonbox import Buttonbox
import pygame

def escolher_classe():
    buttonbox = Buttonbox()

    texto = ""
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return ""

            if evento.type == pygame.MOUSEBUTTONUP:
                clique = Buttonbox.mapear_clique(pygame.mouse.get_pos())
                if clique:
                    return clique



        buttonbox.renderizar()