def cargar(dic: dict):
    print("\nCARGAR UN PRODUCTO:")
    dic.update({input("Ingrese el codigo del producto: "):[input("Ingrese el nombre del producto: "),int(input("Ingrese el precio: ")),int(input("Ingrese la cantidad en stock: "))]})
    #{123456:["nombre",int,int]}

def imprimir(dic: dict):
    print("\nTODOS LOS PRODUCTOS:")
    for key in dic:
        print(f"Codigo del producto: {key} - Nombre: {dic[key][0]} | Precio: {dic[key][1]} | Cantidad stock: {dic[key][2]}")

def buscar(dic: dict):
    print("\nBUSCAR UN PRODUCTO:")
    cod = input("Ingrese el codigo del producto a buscar: ")
    valores = dic.items()
    for x in valores:
        if(cod == x[0]):
            return (f"Nombre: {x[1][0]} | Precio: {x[1][1]} | Cantidad stock: {x[1][2]}")
    return "No se encontro el producto"

def stock0(dic: dict):
    print("\nPRODUCTOS CON STOCK EN 0:")
    valores = dic.items()
    for x in valores:
        if(x[1][2] == 0):
            print(f"Codigo del producto: {x[0]} - Nombre: {x[1][0]} | Precio: {x[1][1]} | Cantidad stock: {x[1][2]}")

dic = {"123":["Producto1",123,12],"456":["Producto2",456,0]}
cargar(dic)
imprimir(dic)
print("El producto buscado es:",buscar(dic))
stock0(dic)