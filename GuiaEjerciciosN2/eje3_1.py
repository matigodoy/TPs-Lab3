class Alumno():
    def inicializar(self, nombre: str, nota: int):
        self.nombre = nombre
        self.nota = nota
    
    def regular(self):
        if(self.nota >= 4):
            print(f"El alumno {self.nombre} esta regular con una nota de {self.nota}")
        else:
            print(f"El alumno {self.nombre} no esta regular con una nota de {self.nota}")
    
    def imprimir(self):
        print(f"Nombre: {self.nombre} - Nota: {self.nota}")

a1 = Alumno()
a2 = Alumno()
a1.inicializar("Matias",5)
a2.inicializar("Lucas",3)
a1.imprimir()
a2.imprimir()
a1.regular()
a2.regular()