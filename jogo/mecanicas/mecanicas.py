import random

from ..personagens.inimigos.monstro import Monstro

# Combate
def iniciar_combate(aventureiro, inimigo):
    """
    Executa um loop infinito, que possui as seguintes etapas:
    - Calcula o dano causado pelo aventureiro
    - Monstro faz a sua defesa
    - Exibe na tela o dano causado pelo aventureiro e a vida atual do monstro
    - Se o monstro não está mais vivo, retorna True
    - Calcula o dano causado pelo monstro
    - Aventureiro faz sua defesa
    - Exibe na tela o dano causado pelo monstro e a vida atual do aventureiro
    - Se o aventureiro não está mais vivo, retorna False
    """
    while True:
        dano = aventureiro.atacar()
        inimigo.defender(dano)
        if not inimigo.esta_vivo():
            return True

        dano = inimigo.atacar()
        aventureiro.defender(dano)
        if not aventureiro.esta_vivo():
            return False

def existe_obstaculo(posicao, npc):
    x, y = posicao
    if x < 0 or x > 9 or y < 0 or y > 9:
        return True

    if posicao == npc.posicao:
        return True

    return False

# Operação principal do jogo
def movimentar(aventureiro, direcao, npc):
    pos_futura = aventureiro.calcular_pos_futura(direcao)
    if existe_obstaculo(pos_futura, npc):
        return True

    aventureiro.andar(pos_futura)

    efeito = random.choices(["nada", "monstro"], [0.6, 0.4])[0]
    if efeito == "monstro":
        monstro = Monstro()
        if iniciar_combate(aventureiro, monstro):
            aventureiro.status = f"{monstro.nome} foi derrotado!"
            return True

        aventureiro.status = f"Você foi derrotado por {monstro.nome}! Game Over..."
        return False

    aventureiro.status = "Continue explorando"
    return True

def conversar(aventureiro, npc):
    x_a, y_a = aventureiro.posicao
    x_n, y_n = npc.posicao

    if (x_a + 1 == x_n or x_a - 1 == x_n) and y_a == y_n:
        aventureiro.status = npc.mensagem

    if (y_a + 1 == y_n or y_a - 1 == y_n) and x_a == x_n:
        aventureiro.status = npc.mensagem