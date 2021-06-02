import random

class Dado:
    valor:int
    def tirar(self):
        self.valor = random.randint(1,6)
    def imprimir(self):
        print(f"El valor del dado es: {self.valor}")
    def retornar_valor(self):
        return self.valor

class JuegoDeDados:
    dado1:Dado()
    dado2:Dado()
    dado3:Dado()
    def __init__(self, dado1:Dado(), dado2:Dado(), dado3:Dado()):
        self.dado1 = dado1
        self.dado2 = dado2
        self.dado3 = dado3
    
    def jugar(self):
        self.dado1.tirar()
        self.dado2.tirar()
        self.dado3.tirar()
        self.dado1.imprimir()
        self.dado2.imprimir()
        self.dado3.imprimir()
        if(self.dado1.retornar_valor() == self.dado2.retornar_valor() == self.dado3.retornar_valor()):
            print("Gano")
        else:
            print("Perdio")

d1 = Dado()
d2 = Dado()
d3 = Dado()

juego1 = JuegoDeDados(d1,d2,d3)
juego1.jugar()
