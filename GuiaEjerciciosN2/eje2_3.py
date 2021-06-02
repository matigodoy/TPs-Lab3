def mostrar(dic: dict):
    print("Todos los articulos:")
    for key in dic:
        print(f"Nombre: {key} - Precio: ${dic[key]}")

def superior(dic: dict):
    print("Articulos mayores a 100:")
    for key in dic:
        if(dic[key] > 100):
            print(f"Nombre: {key} - Precio: ${dic[key]}")

dic = {"Fideos":120, "Manzana":67, "Lechuga":150, "Tomates":101, "Chocolate":32}
mostrar(dic)
superior(dic)