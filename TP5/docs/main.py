from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.graphics.shapes import Rect
from reportlab.lib.colors import PCMYKColor, PCMYKColorSep, Color, yellow, red, green, black
import os
from datosCOVID import datos_ordenados

# Declaramos la hoja
pdf = canvas.Canvas("Covid-19.pdf", pagesize=A4)
w, h = A4

# Seteamos tipografía y colores para escribir un titulo
def titulo():
    pdf.setFont("Helvetica",20)
    pdf.setFillColorRGB(0.8, 0, 0)
    pdf.drawString(100, h-150, "Datos de Covid-19 en los paises de America")

# Generamos la tabla con todos sus datos dinamicamente
def tabla():
    pdf.setFont("Helvetica",11)
    pdf.setFillColorRGB(0, 0, 0)
    pdf.drawString(145, 654, "PAIS")
    pdf.drawString(270, 654, "POBLACION")
    pdf.drawString(354, 654, "MUERTOS")
    pdf.drawString(416, 654, "% COVID")
    pdf.drawString(470, 654, "COLOR")
    
    xlist = [70,250,350,410,470,500]
    ylist = [650]
    inicio = 650
    maximo = datos_ordenados[0][1][0]
    minimo = 0
    pdf.setLineWidth(.2) #definimos el ancho de la lineas a dibujar
    
    for x in datos_ordenados: #recorre los datos para mostrarlos
        inicio -= 15
        ylist.append(inicio)
        pdf.drawString(72, inicio+2, x[0]) #Pais
        pdf.drawString(252, inicio+3, str(x[1][2])) #Poblacion
        pdf.drawString(352, inicio+3, str(x[1][1])) #Muertos
        pdf.drawString(417, inicio+3, str(x[1][0])[:6]+"%") #Porcentaje
        
        #Dibujamos los cuadrados
        if(float(x[1][0]) > minimo and float(x[1][0]) <= maximo / 3):
            # dibujar el cuadrado verde
            pdf.setFillColor(green)
            pdf.rect(475, inicio+2, 20,10 , fill=True, stroke=False)
        elif( float(x[1][0]) > maximo / 3 and float(x[1][0]) <= maximo / 3 * 2):
            # dibujar el cuadrado amarillovich
            pdf.setFillColor(yellow)
            pdf.rect(475, inicio+2, 20,10 , fill=True, stroke=False)
        elif( float(x[1][0]) > maximo / 3 * 2 ):
            # dibujar el cuadrado rojovich
            pdf.setFillColor(red)
            pdf.rect(475, inicio+2, 20,10 , fill=True, stroke=False)
        pdf.setFillColor(black)
    pdf.grid(xlist, ylist) # Genera la tabla a partir de las dos listas

# Mostramos las imagenes de encabezado y pie
def imagenes():
    pdf.drawImage("img/encabezado.png", 0 , h-99 , width=w , height=99)
    pdf.drawImage("img/pie.png", 0 , 0 , width=w , height=40)

# Llamamos a las funciones
titulo()
tabla()
imagenes()
# Guardamos y mostramos el pdf
pdf.showPage()
pdf.save()
os.system("Covid-19.pdf")