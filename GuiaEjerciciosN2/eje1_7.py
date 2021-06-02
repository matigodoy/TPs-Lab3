def carga():
    lista = []
    for x in range(5):
        lista.append(int(input(f"Ingrese el valor n° {x+1}: ")))
    return lista

def mostrar(lista: list):
    print("La lista es: \n[ ",end="")
    for x in lista:
        if(x > 10):
            print(x,end=" ")
    print("]")

lista = carga()
mostrar(lista)
#mostrar(cargar())