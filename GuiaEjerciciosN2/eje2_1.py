def carga():
    lista = []
    for x in range(5):
        lista.append((input("Ingrese el nombre del pais: "),int(input("Ingrese la cantidad de habitantes que tiene: "))))
    return lista

def imprimir(lista: list):
    print("Los paises ingresados son:")
    for x in lista:
        print(f"Nombre: {x[0]} - Habitantes: {x[1]}")

def mayor(lista: list):
    mayor = (0,0)
    for x in lista:
        if (x[1] > mayor[1]):
            mayor = x
    print(f"El pais con mayor cantidad de habitantes es {mayor[0]} con {mayor[1]} habitantes")

lista = carga()
imprimir(lista)
mayor(lista)