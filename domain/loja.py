import armadura
import arma

class Loja:
  def __init__(self):
    self.arma = {}
    self.armadura = {}

  def add_armas(self, arma: arma.Arma):
    self.armas[arma.nome, arma] = arma

  def add_armaduras(self, armadura: armadura.Armadura):
    self.armaduras[armadura.nome, armadura] = armadura

  def mostrar_armas(self):
    for nome, arma in self.armas.items():
      print(f"{nome}: Dano máximo - {arma.dano_maximo}, Preço - {arma.preco}")

  def mostrar_armaduras(self):
    for nome, armadura in self.armaduras.items():
      print(f"{nome}: Dano máximo - {armadura.classe_armadura}, Preço - {armadura.preco}")