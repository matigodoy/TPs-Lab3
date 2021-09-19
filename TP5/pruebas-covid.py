import requests #para traer los datos de la api
import operator #para poder ordenar un dict
from settings import (URL_COVID, URL_HABITANTES) #traemos las urls de las APIs

paises_america = ["Antigua and Barbuda","Argentina","Bahamas","Barbados","Belize","Bolivia","Brazil","Canada","Chile","Colombia","Costa Rica","Cuba","Dominica","Dominican Republic","Ecuador","El Salvador","Grenada","Guatemala","Guyana","Haiti","Honduras","Jamaica","Mexico","Nicaragua","Panama","Paraguay","Peru","Saint Kitts and Nevis","Saint Lucia","Saint Vincent and Grenadines","Suriname","Trinidad and Tobago","United States of America","Uruguay","Venezuela (Bolivarian Republic)"]
url = "https://api.covid19api.com/summary"

respuesta = requests.get(url)
my_data = respuesta.json()
countries = my_data["Countries"]
datos = {}
for i in range(len(countries)):
    if countries[i]["Country"] in paises_america:
        datos[countries[i]["Country"]] = [countries[i]["TotalDeaths"],"Habitantes"]

print("-------------------------DATOS------------------------")
datos_ordenados = sorted(datos.items(), key=operator.itemgetter(1), reverse=True)
for x in datos_ordenados:
    print(f"{x[0]} : {x[1]}")

print(datos_ordenados[4][1][1])
'''Info:
datos_ordenados[i] = Todos los datos de un pais en la posicion "i"
datos_ordenados[i][0] = Nombre del pais en la posicion "i"
datos_ordenados[i][1] = Info del pais en la posicion "i"
datos_ordenados[i][1][0] = Cantidad de muertos del pais en la posicion "i"
datos_ordenados[i][1][1] = Cantidad de habitantes del pais en la posicion "i"
'''
