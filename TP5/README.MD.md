# Laboratorio III - TP05

[![N|Solid](https://www.ubp.edu.ar/wp-content/themes/ubp-pmkt/img/logo-ubp.png)](https://www.ubp.edu.ar/)

## _Sobre el proyecto_


Este proyecto tiene como fin implementar los conceptos y familializarse con el consumo de una api restful desde un cliente python, siguiendo las buenas practicas del mismo.

## Consignas cumplidas
- Consulta a la API de COVID19 
- Consulta a la API de Población mundial
- Semaforo en PDF sobre la cantidad de muertos (según cantidad de habitantes) por países de america
- Configurable desde el archivo `settings.py`

## Instalación

Este proyecto tiene como requisitos ciertos pasos previos

Instalar las dependencias de python 

```sh
pip install reportlab
pip install request
```

*Se recomienda el uso de entornos virtuales para la instalación.*

## Clonar el repositorio

```sh
git init
git clone https://github.com/matigodoy/TPs-Lab3.git
```

## ¿Como funciona internamente?

A partir de la biblioteca ReportLab generamos un pdf en `mostrarDatos.py` con los datos que traeremos de nuestro segundo y tercer modulo `datosCOVID.py` y `datosPoblacion.py`, los cuales consultan a sus respectivas API mediante la dependencia *request*.

>NOTA: Existe la posibilidad de modificar tanto los paises a consultar datos como la URL de a que API apuntar (en caso de que cambie la misma) mediante el archivo `settings.py` 

## ¿Como ejecutarlo?
Para ejecutar el sistema abrir una consola sobre la ubicación donde clonó el repositorio y ejecutar el siguiente comando:
```sh
py mostrarDatos.py
```
Una vez ejecutado el archivo nos abrirá un PDF el cual contiene los datos consultados.


   ## Bibliografía

Este proyecto fué desarrollado gracias a la documentación encontrada en los siguientes sitios web.
_(Ordenados alfabetícamente A->Z)_

| Sitio web | URL |
| ------ | ------ |
| Documentacion COVID-19 | https://documenter.getpostman.com/view/10808728/SzS8rjbc |
| Informacion request en python | https://docs.python-requests.org/en/latest/ |
| Documentacion World-Wide Population | https://documenter.getpostman.com/view/1134062/T1LJjU52#abee09ea-aeb9-479c-b970-81d909c2a58c |
| Sitio Oficial Python | https://www.python.org/ |
| Documentacion Reportlab | https://www.reportlab.com/opensource/ |

