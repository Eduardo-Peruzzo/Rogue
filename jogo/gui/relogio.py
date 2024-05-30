import time

class Relogio:
    def __init__(self):
        self.inicio = time.time()

    def medir_tempo(self):
        tempo_decorrido = time.time() - self.inicio
        minutos = int(tempo_decorrido // 60)
        segundos = int(tempo_decorrido - minutos * 60)
        return segundos

   