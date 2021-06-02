'''
def perimetro(lado: int):
    return (lado*4)

def area(lado:int):
    return(lado*lado)

def cuadrado(lado: int):
    print("""Quiere calcular:)
    1. Area?
    2. Perimetro?
    3. Area y Perimetro?""")
    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        print(f"El area del cuadrado es: {area(lado)}")
    elif opcion == "2":
        print(f"El perimetro del cuadrado es: {perimetro(lado)}")
    elif opcion == "3":
        print(f"El area es: {area(lado)} y perimetro es: {perimetro(lado)}")
    else:
        print("Opcion invalida")

cuadrado(5)
'''

#----MANU----
def cuadrado():
    print("1. AREA")
    print("2. PERIMETRO")
    x = int(input("Introduce la opción que desea:  "))
    if x == 1:
        perimetro()
    elif x == 2:
        area()

def perimetro():
    lado = int (input ("Ingrese el lado del cuadrado: "))
    p = 4*lado
    print("El perimetro es: ", p)

def area():
    lado = int (input ("Ingrese el lado del cuadrado: "))
    a = lado*lado
    print("El area es: ", a)
cuadrado()