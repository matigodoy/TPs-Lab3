def cargar(dic: dict):
    dic.update({input("Ingrese palabra en ingles: "):input("Ingrese la traduccion al español: ")})

def mostrar(dic: dict):
    print("Diccionario:")
    for key in dic:
        print(f"Ingles: {key} -> Español: {dic[key]}")

def buscar(dic: dict):
    palabra = input("Ingrese la palabra en ingles a buscar: ")
    valores = dic.items()
    for x in valores:
        if(x[0] == palabra):
            return x[1]
    return "No se encontro la palabra"

dic = {"hello":"hola","for":"para","get":"obtener","bye":"chau"}
cargar(dic)
print("La palabra buscada es:",buscar(dic))