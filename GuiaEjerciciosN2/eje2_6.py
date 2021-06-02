def cargar(dic: dict):
    print("\nINGRESAR UNA ACTIVIDAD")
    fecha = input("Ingrese la fecha: ")
    for x in dic:
        if(x == fecha):
            dic[x].append((input("Ingrese la hora: "),input("Ingrese la actividad: ")))
            return
    dic.update({fecha:[(input("Ingrese la hora: "),input("Ingrese la actividad: "))]})

def imprimir(dic: dict):
    print("\nMOSTRAR AGENDA")
    for x in dic:
        print(f"\nActividades dia {x}:")
        for y in dic[x]:
            print(f" * Hora: {y[0]} - Actividad: {y[1]}")

def buscar(dic: dict):
    print("\nBUSCAR UNA FECHA")
    fecha = input("Ingrese la fecha a buscar: ")
    for x in dic:
        if(x == fecha):
            print(f"\nActividades del dia {x}:")
            for y in dic[x]:
                print(f" * Hora: {y[0]} - Actividad: {y[1]}")
            return
    print("No se encontro la fecha")
    

dic = {"23/08": [("14:05", "tengo que comprar el pan"), ("12:06", "visitar a mi papa")], "22/04": [("13:54", "Vender ...")]}
cargar(dic)
imprimir(dic)
buscar(dic)
