from main import Habilidades
from personagem import Personagem
from dados import Dado

class Mago(Personagem):
    def __init__(self, nome, arma, armadura, vida, moedas, magia):
        super().__init__(nome, arma, armadura, vida, moedas)
        self.magia = magia
        
    def sofrer_dano(self, dano):
        return super().sofrer_dano(dano)

    def defesa(self, dano):
        return super().defesa(dano)
    
    def cura(self):
        valor = Dado.d6()
        if self.magia:
            self.vida += valor

class Guerreiro(Personagem):
    def __init__(self, nome, arma, armadura, vida, moedas, forca):
        super().__init__(nome, arma, armadura, vida, moedas)
        self.forca = forca
        
    def sofrer_dano(self, dano):
        return super().sofrer_dano(dano)

    def defesa(self, dano):
        return super().defesa(dano)
    
    def porrada(self):
        valor = Dado.d6()
        if self.forca:
            self.arma += valor