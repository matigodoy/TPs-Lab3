def carga():
    lista = []
    for x in range(5):
        lista.append([input(f"Ingrese el nombre de la {x+1}° persona: "),int(input("Ingrese la edad de la persona: "))])
    return lista

def imprimir(lista: list):
    suma = 0
    print("Las personas mayores de edad:")
    for x in range(5):
        suma += lista[x][1]
        if(lista[x][1] >= 18):
            print(f"Nombre: {lista[x][0]} - Edad: {lista[x][1]}")
    print("La edad promedio es:",suma/5)

lista = carga()
imprimir(lista)