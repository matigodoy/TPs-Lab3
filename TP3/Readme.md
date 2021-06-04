# TP3
## _Laboratorio 3_

[![N|Solid](https://www.ubp.edu.ar/wp-content/themes/ubp-pmkt/img/logo-ubp.png)](https://www.ubp.edu.ar/)

ReportLab es un toolkit de código abierto para crear documentos PDF desde Python. Se trata de una librería muy extensa y con muchas funcionalidades, desde pequeños textos y figuras geométricas a grandes gráficos e ilustraciones, todo ello puede ser incluido dentro de un PDF. 


## Instalación 

Reportlab requiere [Libreria Reportlab & Pillow](https://pypi.org/project/reportlab/) para funcionar.

Instalamos en nuestro entorno de python

```sh
pip install reportlab
```

## Creando un PDF básico

Para crear un PDF básico con texto lo que hacemos es importar las librerías

```sh
from reportlab.pdfgen import canvas
```

Ahora creamos un objeto PDF vacio

```sh
c = canvas.Canvas("test.pdf")
```

Para escribir texto dentro del pdf, lo logramos con

```sh
c.drawString(50, 50, "¡Hola, mundo!")
```

Por último, vamos a guardar todos los cambios realizados.

```sh
c.save()
```

## Sobre nuestro proyecto
Ahora que ya entendemos el funcionamiento básico de la librería, podemos trabajar con nuestro proyecto.

Para ello ejecutar el archivo principal *tp3.py* el cual traerá los datos desde notas.txt.

## Bibliografía

- `ReportLab Python` https://pypi.org/project/reportlab/
- `ReportLab Docs` https://www.reportlab.com/dev/docs/
- `Recursos Python` https://recursospython.com/guias-y-manuales/crear-documentos-pdf-en-python-con-reportlab/
- `Python Library` https://www.blog.pythonlibrary.org/2010/03/08/a-simple-step-by-step-reportlab-tutorial/
- `Guía de usuario reportlab` https://www.reportlab.com/docs/reportlab-userguide.pdf



