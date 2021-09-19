import requests
from settings import *

respuesta = requests.get(URL_HABITANTES)
my_data = respuesta.json()
poblacion = my_data["data"]
datos_poblacion = {}

print("================= Datos de poblacion =================")

for i in range(len(poblacion)):
    for j in range(len(paises_america_poblacion)):
        if poblacion[i]["country"].find(paises_america_poblacion[j]) != -1:
            datos_poblacion[poblacion[i]["country"]] = poblacion[i]["populationCounts"][-1]["value"]


print(len(datos_poblacion))

if poblacion[i]["country"].find("Zimb") != -1:
    print( poblacion[i]["country"] )


if paises_america_poblacion[1].find("Ar") != -1:
    print(paises_america_poblacion[1])


print("==========================================")
# print(poblacion[53]["country"])

if poblacion[53]["country"].find(paises_america_poblacion[1]) != -1:
    print( poblacion[53]["country"] )
