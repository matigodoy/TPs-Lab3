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

for x in datos:
    aux = (datos[x][0] / datos[x][1] * 100)
    datos[x].insert(0,aux)

datos_ordenados = sorted(datos.items(), key=operator.itemgetter(1), reverse=True)

print("-------------------------DATOS-------------------------")
for x in datos_ordenados:
    print(f"{x[0]} : {x[1]}")
