class Punto:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
    
    def cuadrante(self):
        if (self.x>0 and self.y>0):
            print(f"El punto ({self.x},{self.y}) se encuentra en el 1er cuadrante")
        elif (self.x<0 and self.y>0):
            print(f"El punto ({self.x},{self.y}) se encuentra en el 2do cuadrante")
        elif (self.x<0 and self.y<0):
            print(f"El punto ({self.x},{self.y}) se encuentra en el 3er cuadrante")
        elif (self.x>0 and self.y<0):
            print(f"El punto ({self.x},{self.y}) se encuentra en el 4to cuadrante")

p1 = Punto(12,-3)
p2 = Punto(-4,2)
p3 = Punto(-1,-3)
p1.cuadrante()
p2.cuadrante()
p3.cuadrante()
