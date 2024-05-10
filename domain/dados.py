import random

faces = [6, 8, 12, 20]

def gerarFaceAleatoria():
    indice = random.randint(1, 3)
    return faces[indice]    

class Dado:
    def init(self):
        self.faceDado = gerarFaceAleatoria()

    def jogarDado(self):
        return random.randint(1, self.faceDado)
    
    def d6():
        indice = random.randint(1, 6)
        return faces[indice]

    def d8():
        indice = random.randint(1, 8)
        return faces[indice]
        
    def d12():
        indice = random.randint(1, 12)
        return faces[indice]
        
    def d20():
        indice = random.randint(1, 20)
        return faces[indice]