import random

class Arma:
    def init(self, nome, dano):
        self.nome = nome
        self.dano = dano

    def dano_arma(self):
        return random.randint(1, self.dano)
