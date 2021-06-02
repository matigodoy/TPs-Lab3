from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

pdf = canvas.Canvas("Alumnos.pdf", pagesize=A4)

w, h = A4

def titulo():
    pdf.setFont("Times-Roman",64)
    pdf.setFillColorRGB(0.8, 0, 0)
    pdf.drawString(w/2-60, h/2+100, "TP 3")


def alumnos():
    pdf.setFont("Times-Roman",20)
    pdf.drawString(w/2-90, h/2+40, "Alumnos:")
    pdf.setFont("Times-Roman",15)
    pdf.setFillColorRGB(0, 0, 0)
    f = open("notas.txt","r")
    contador = 0
    
    for linea in f:
        pdf.drawString(w/2-70, h/2+20-contador, linea[:linea.index(",")])
        contador += 20

    f.close()

def notas():
    f = open("notas.txt","r")
    
    inicio = 300
    contador = 0
    xlist = [70,250,300,350,400,500]
    ylist = [330]

    pdf.setLineWidth(.2) #definimos el ancho de la lineas a dibujar
    
    for linea in f:
        ylist.append(inicio)
        inicio -= 30
        notas=[]
        notas.append(int(linea[linea.index(",")+1:linea.index(",")+3])) #primer nota
        notas.append(int(linea[linea.index(",")+3:linea.index(",")+5])) #segunda nota
        notas.append(int(linea[linea.index(",")+5:linea.index(",")+7])) #tercera nota
        pdf.drawString(73, 303-contador, linea[:linea.index(",")])
        pdf.drawString(253, 303-contador, str(notas[0]))
        pdf.drawString(303, 303-contador, str(notas[1]))
        pdf.drawString(353, 303-contador, str(notas[2]))

        prom = sum(notas) / 3
        if (prom >= 4):
            pdf.drawString(403, 303-contador, "Aprobado")
        else:
            pdf.drawString(403, 303-contador, "Desaprobado")

        contador += 30

    pdf.grid(xlist, ylist)
    f.close()

def imagenes():
    pdf.drawImage("encabezado.png", 0 , h-99 , width=w , height=99)
    pdf.drawImage("pie.png", 0 , 0 , width=w , height=40)


titulo()
alumnos()
imagenes()
notas()
pdf.showPage()
pdf.save()
