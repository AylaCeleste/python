import random

class Habilidades:

    #Este construtor assim que chamado já define o valor das habilidades aleatóriamente
    def __init__(self):
        self.forca = random.randint(1, 20)
        self.destreza = random.randint(1, 20)
        self.constituicao = random.randint(1, 20)
        self.sabedoria = random.randint(1, 20)
        self.inteligencia = random.randint(1, 20)
        self.carisma = random.randint(1, 20)

    def modificar(self, valor):
        modificadores = {
            1: -5, 2: -4, 3: -4, 4: -3, 5: -3,
            6: -2, 7: -2, 8: -1, 9: -1, 10: 0,
            11: 0, 12: 1, 13: 1, 14: 2, 15: 2,
            16: 3, 17: 3, 18: 4, 19: 4, 20: 5
        }
        return modificadores.get(valor, 0)

    #Rolagem do d20 adicionando os modificadores de habilidades
    def rolar_dado(self, habilidade):
      modificador = self.modificar(habilidade)
      resultado = random.randint(1, 20)
      resultado += modificador
      return resultado

class Item:

  def __init__(self, nome, tipo, atributo, preco):
    self.nome = nome
    self.tipo = tipo
    self.atributo = atributo
    self.preco = preco

    #Define o dano da arma de acordo com o máximo de lados do dado da arma em questão
    def dano_arma(self):
      if self.tipo == 'arma':
        return random.randint(1, self.atributo)
      else:
        print('Esse item não pode causar dano')

class Personagem:
    def __init__(self, nome, itens: Item, vida, habilidades: Habilidades, coins):
        self.nome = nome
        self.itens = []
        self.vida = vida
        self.habilidades = habilidades
        self.coins = coins

    def acessar_armas(self):
      for item in self.itens:
        if self.itens.tipo == 'arma'

    #Método para calculo de dano sofrido pelo personagem
    def sofrer_dano(self, dano):
        self.vida -= dano

    # def mostrar_informacao(self):
    #     print(f"Nome: {self.nome}\nCA: {self.armadura.classe_armadura}\nVida: {self.vida}\n")

class Loja:

  def __init__(self):
    self.itens = {}

  def mostrar_arma(self, tipo):
    for nome, item in self.itens.items():
      if item.tipo == tipo and tipo == 'arma':
        print(f'\n{nome}\nTipo: {item.tipo}\nDano: {item.atributo}\nPreço: {item.preco} po')
      elif item.tipo == tipo and tipo == 'armadura':
        print(f'\n{nome}\nTipo: {item.tipo}\nClasse de Armadura: {item.atributo}\nPreço: {item.preco} po')


#Habilidades declaradas
habilidades_personagem1 = Habilidades()
habilidades_personagem2 = Habilidades()

#Armas declaradas
adaga = Item("Adaga", "arma", 4, 10)
azaiga = Item("Azaiga", "arma", 6, 10)

#Armaduras declaradas com nome, classe de armadura, preço
armadura_couro = Item("Armadura de Couro", "armadura", 13, 10)
armadura_acolchoada = Item("Armadura Alcochoada", "armadura", 13, 10)

lista_itens1 = [adaga, armadura_couro]
lista_itens2 = [azaiga, armadura_acolchoada]

#Personagens declarados com nome, armadura, adaga, vida, habilidades, coins
personagem1 = Personagem("Maria", lista_itens1, 8, habilidades_personagem1, 0)
personagem2 = Personagem("João", lista_itens2, 8, habilidades_personagem2, 0)


#Combate
while personagem1.vida > 0 and personagem2.vida > 0:
    ataque_personagem1 = personagem1.habilidades.rolar_dado(personagem1.habilidades.destreza)
    print(f"{personagem1.nome} ataca com um resultado de {ataque_personagem1}")

    if ataque_personagem1 > personagem2.itens.:
        dano = personagem1.arma.dano_arma()
        print(f"{personagem1.nome} acerta e causa {dano} de dano!")
        personagem2.sofrer_dano(dano)
    else:
        print(f"{personagem1.nome} erra o ataque!")

    if personagem2.vida <= 0:
        coins_recompensa = random.randint(5, 20)
        personagem1.coins += coins_recompensa
        print(f"{personagem1.nome} venceu e recebeu {coins_recompensa} coins!")
        break

    ataque_personagem2 = personagem2.habilidades.rolar_dado(personagem1.habilidades.destreza)
    print(f"{personagem2.nome} ataca com um resultado de {ataque_personagem2}")

    if ataque_personagem2 > personagem1.armadura.classe_armadura:
        dano = personagem2.arma.dano_arma()
        print(f"{personagem2.nome} acerta e causa {dano} de dano!")
        personagem1.sofrer_dano(dano)
    else:
        print(f"{personagem2.nome} erra o ataque!")

    if personagem1.vida <= 0:
        coins_recompensa = random.randint(5, 20)
        personagem1.coins += coins_recompensa
        print(f"{personagem2.nome} venceu e recebeu {coins_recompensa} coins!")
        break

# Loja
# while True:
#   if personagem1.vida > 0 or personagem2.vida > 0:
#     print("")
#     print('Loja de itens')
#     print('1. Armadura')
#     print('2. Armas')
#     print('3. Sair')
#     loja = input(('Digite uma opção de (1/2/3) para escolher uma loja: '))

#     if loja == '1':
#       print('Escolha uma opção de armadura')
#       print('1. Couro')
#       print('2. Malha')
#       print('3. Metálica')
#       print('4. Sair')
#       print('Digite de (1/2/3/4)')
#       Armadura = input('Escolha uma das opções de armadura (1/2/3/4): ')
#       if Armadura == '1':
#         print('Esta armadura custa 10 moedas de ouro ')
#         if personagem1.coins >= 10:
#           print(f'Você comprou uma armadura de couro e agora possui ----- de defesa')
#         else:
#           print('Você não possui moedas o suficiente para comprar esta armadura')
#       elif Armadura == '2':
#         print('Esta armadura custa 20 moedas de ouro')
#         if personagem1.coins >= 20:
#           print(f'Você comprou uma armadura de couro e agora possui ----- de defesa')
#         else:
#           print('Você não possui moedas o suficiente para comprar esta armadura')
#       elif Armadura == '3':
#         print('Esta armadura custa 40 moedas de ouro')
#         if personagem1.coins >= 40:
#           print(f'Você comprou uma armadura de couro e agora possui ----- de defesa')
#         else:
#           print('Você não possui moedas o suficiente para comprar esta armadura')
#       elif Armadura == '4':
#         break
#       else:
#         print('Insira um comando válido')

#     elif loja == '2':
#       print('Escolha uma opção de arma')
#       print('1. Adaga')
#       print('2. Foice Pequena')
#       print('3. Porrete')
#       print('4. Sair')
#       Armas = input('Escolha uma opção de arma entre (1/2/3/4): ')
#       if Armas == '1':
#         print('Esta arma custa 10 moedas de ouro')
#         if personagem1.coins >= 10:
#           print(f'Você comprou uma adaga ela lhe dá ===== de força ')
#         else:
#           print(f'Você não possui moedas o suficiente para comprar esta arma')
#       if Armas == '2':
#         print('Esta arma custa 20 moedas de ouro')
#         if personagem1.coins >= 20:
#           print(f'Você comprou uma foice ela lhe dá ===== de força ')
#         else:
#           print(f'Você não possui moedas o suficiente para comprar esta arma')
#       if Armas == '3':
#         print('Esta arma custa 40 moedas de ouro')
#         if personagem1.coins >= 40:
#           print(f'Você comprou um porrete ela lhe dá ===== de força ')
#         else:
#           print(f'Você não possui moedas o suficiente para comprar esta arma')
#     elif loja == '3':
#       break

#   else:
#     print('Digite uma opção válida')

