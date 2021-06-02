class Triangulo:
    def inicializar(self, lado1: int, lado2: int, lado3: int):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def mayor(self):
        lados = [self.lado1, self.lado2, self.lado3]
        print(f"El lado mayor es: {max(lados)}")
    
    def equilatero(self):
        if(self.lado1 == self.lado2 == self.lado3):
            print("Es un triangulo equilatero")
        else:
            print("NO es un triangulo equilatero")

    def imprimir(self):
        print(f"Lados: {self.lado1} - {self.lado2} - {self.lado3}")

t1 = Triangulo()
t2 = Triangulo()
t1.inicializar(20,20,20)
t2.inicializar(4,20,69)
t1.imprimir()
t2.imprimir()
t1.mayor()
t2.mayor()
t1.equilatero()
t2.equilatero()