import requests
from settings import *

respuesta = requests.get(URL_HABITANTES)
my_data = respuesta.json()
poblacion = my_data["data"]
datos_poblacion = {}

#print("================= Datos de poblacion =================")

for i in range(len(poblacion)):
    if poblacion[i]["country"] in paises_america_poblacion:
        datos_poblacion[poblacion[i]["country"]] = poblacion[i]["populationCounts"][-1]["value"]

# for x in datos_poblacion:
#     print(f"{x} : {datos_poblacion[x]}")