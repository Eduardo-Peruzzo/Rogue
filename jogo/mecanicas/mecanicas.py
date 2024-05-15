import random
from jogo.personagens.inimigos.monstro import Monstro

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

# Operação principal do jogo
def movimentar(aventureiro, direcao):
    """
    Realiza a ação de movimento e analisa as consequências.

    Chama a função aventureiro_andar e analisa o seu resultado. Se for False,
    ou seja, se o aventureiro não tiver andado nada, retorna True.

    Em seguida, analisa o efeito do movimento. Há 60% de chance de nada
    acontecer, e 40% de chance de um monstro aparecer (pesquise sobre a função
    random.choices).

    Se um monstro aparecer, inicia um novo monstro e retorna e resultado da
    função iniciar_combate.

    Caso não seja um monstro, retorna True.
    """
    if not aventureiro.andar(direcao):
        return True

    efeito = random.choices(["nada", "monstro"], [0.6, 0.4])[0]
    if efeito == "monstro":
        monstro = Monstro()
        if iniciar_combate(aventureiro, monstro):
            aventureiro.status = f"{monstro.nome} foi derrotado"
            return True
        else:
            aventureiro.status = f"Você perdeu para {monstro.nome}! Game Over..."
            return False

    aventureiro.status = "Continue explorando"
    return True