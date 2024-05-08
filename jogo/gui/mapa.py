def desenhar(aventureiro, tesouro):
    """
    Desenha um mapa 10 x 10, posicionando o tesouro e o aventureiro.
    Representa o aventureiro por um @, o tesouro por um X, e por um ponto (.)
    os demais locais.
    """
    for y in range(10):
        for x in range(10):
            if [x, y] == aventureiro.posicao:
                print("@", end=" ")
            elif [x, y] == tesouro.posicao:
                print("X", end=" ")
            else:
                print(".", end=" ")
        print()