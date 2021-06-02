def mostrar(dic: dict):
    for key in dic:
        print(f"Nombre: {key} - Habitantes: {dic[key]}")

dic = {"Argentina":45, "Alemania":32, "EEUU":120, "Peru":65, "España":73}
mostrar(dic)