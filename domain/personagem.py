from main import Habilidades

class Personagem:
    def __init__(self, nome, arma, armadura, vida, moedas, habilidades: Habilidades ):
        self.nome = nome
        self.arma = arma
        self.armadura = armadura
        self.vida = vida
        self.moedas = moedas
        self.habilidades = habilidades
        self.moedas = moedas

    #Método para calculo de dano sofrido pelo personagem
    def sofrer_dano(self, dano):
        self.vida -= dano
        
    def defesa(self, dano):
        self.vida -= dano / 2
    
    