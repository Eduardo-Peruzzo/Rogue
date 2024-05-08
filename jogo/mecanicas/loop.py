import random
from ..personagens.aventureiro import Aventureiro
from ..personagens.tesouro import Tesouro
from ..gui.mapa import desenhar
from . import mecanicas

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

    desenhar(aventureiro, tesouro)

    while True:
        op = input("Insira o seu comando: ").upper()
        if op == "Q":
            print("Já correndo?")
            break
        elif op == "T":
            aventureiro.ver_atributos()
        elif op in ["W", "A", "S", "D"]:
            if mecanicas.movimentar(aventureiro, op):
                desenhar(aventureiro, tesouro)
            else:
                print("Game Over...")
                break
        else:
            print(f"{aventureiro.nome}, não conheço essa opção! Tente novamente!")

        if aventureiro.posicao == tesouro.posicao:
            print(f"Parabéns, {aventureiro.nome}! Você encontrou o tesouro!")
            break