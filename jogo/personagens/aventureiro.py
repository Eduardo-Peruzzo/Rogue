import random

class Aventureiro:
    def __init__(self) -> None:

        self.forca =  random.randint(10, 18)
        self.defesa =  random.randint(10, 18)
        self.vida =  random.randint(100, 120)
        self.posicao =  [0, 0]
        self.nome = "Aventureiro"


    def andar(self, direcao):
        """
        Altera o valor da posição do aventureiro conforme a direção informada pelo
        usuário. Direções válidas:
        - W: cima
        - A: esquerda
        - S: baixo
        - D: direita

        Se o aventureiro estiver nos limites do mapa, não faz nenhum movimento.

        Considerar que o mapa é um sistema cartesiano, com o eixo x aumentando
        da esquerda para a direita, e o eixo y aumentando de cima para baixo.
        Portanto, as coordenadas (0, 0) estão no canto superior esquerdo do mapa,
        enquanto que as coordenadas (9, 9) estão no canto inferior direito.

        Retorna True caso o aventureiro tenha andado, e False caso contrário.
        """
        match direcao:
            case "W":
                if self.posicao[1] > 0:
                    self.posicao[1] -= 1
                    return True
            case "S":
                if self.posicao[1] < 9:
                    self.posicao[1] += 1
                    return True
            case "A":
                if self.posicao[0] > 0:
                    self.posicao[0] -= 1
                    return True
            case "D":
                if self.posicao[0] < 9:
                    self.posicao[0] += 1
                    return True

        return False

    def atacar(self):
        """
        Retorna um inteiro igual à Força do aventureiro, mais um valor aleatório
        entre 1 e 6.
        """
        return self.forca + random.randint(1, 6)

    def defender(self, dano):
        """
        Calcula o dano a ser absorvido pelo aventureiro, igual ao dano causado
        menos o atributo de defesa do aventureiro.

        Se o dano a ser absorvido é menor ou igual a zero, não faz nada. Se for
        maior que zero, reduz esse dano da vida do aventureiro.
        """
        dano_levado = dano - self.defesa
        if dano_levado > 0:
            self.vida -= dano_levado

    def ver_atributos(self):
        """
        Exibe na tela os atributos do aventureiro (nome, vida, força, defesa).
        """
        print("Informações de ", self.nome, ":", sep="")
        print("Vida:", self.vida)
        print("Força:", self.forca)
        print("Defesa:", self.defesa)

    def esta_vivo(self):
        """
        Retorna True se a vida do aventureiro é maior que zero.
        """
        return self.vida > 0