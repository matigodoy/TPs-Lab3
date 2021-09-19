import requests #para traer los datos de la api
import operator #para poder ordenar un dict
from settings import *
from datosPoblacion import datos_poblacion

respuesta = requests.get(URL_COVID)
my_data = respuesta.json()
countries = my_data["Countries"]
datos = {}
poblacion = []
for x in datos_poblacion:
    poblacion.append(datos_poblacion[x])
contador = 0
for i in range(len(countries)):
    if countries[i]["Country"] in paises_america:
        datos[countries[i]["Country"]] = [countries[i]["TotalDeaths"], int(poblacion[contador])]
        contador = contador +1
porcentaje = {}
for x in datos:
    aux = (datos[x][0] / datos[x][1] * 100)
    porcentaje[x] = aux

datos_ordenados = sorted(porcentaje.items(), key=operator.itemgetter(1), reverse=True)

print("-------------------------DATOS-------------------------")
for x in datos_ordenados:
     print(f"{x[0]} : {x[1]}")

print("--------------INTERVALOS--------------")
maximo = datos_ordenados[0][1]
print(f"primer intervalo: [0;{maximo/3}]")
print(f"segundo intervalo: [{maximo/3};{maximo/3*2}]")
print(f"tercer intervalo: [{maximo/3*2};{maximo}]")
