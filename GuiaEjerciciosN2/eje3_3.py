class Empleado:
    def __init__(self, nombre:str, sueldo:int):
        self.nombre = nombre
        self.sueldo = sueldo
    
    def imprimir(self):
        print(f"Su nombre es {self.nombre} con un sueldo de ${self.sueldo}")
    
    def impuestos(self):
        if self.sueldo > 3000:
            print (f"{self.nombre} tiene que pagar impuestos")

e1 = Empleado("Matias", 2000)
e2 = Empleado("Federico", 3500)
e1.imprimir()
e2.imprimir()
e1.impuestos()
e2.impuestos()