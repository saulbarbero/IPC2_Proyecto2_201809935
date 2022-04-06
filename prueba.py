from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

w, h = A4
    

c = canvas.Canvas("prueba.pdf", pagesize=A4)
        
img = ImageReader("salida.png")
        # Obtener el ancho y alto de la imagen.
img_w, img_h = img.getSize()
        
c.drawImage(img, 23,h/2 , width=550, height=400)

c.drawString((w/2)-100, (h/2)-30, "Intransitable")
c.drawString((w/2)-100, (h/2)-50, "Punto Entrada")
c.drawString((w/2)-100, (h/2)-70,"Camino")
c.drawString((w/2)-100, (h/2)-90,"Unidad Militar")
c.drawString((w/2)-100, (h/2)-110,"Unidad Civil")
c.drawString((w/2)-100, (h/2)-130,"Recurso")
c.drawString((w/2)-100, (h/2)-150,"Ruta")

c.drawString((w/2)-100, (h/2)-180," realizada por ")

    
c.setFillColorRGB(0, 0, 0)
c.rect((w/2)-120, (h/2)-30, 10, 10, fill=True)
c.setFillColorRGB(0, 128, 0)
c.rect((w/2)-120, (h/2)-50, 10, 10, fill=True)
c.setFillColorRGB(255, 255, 255)
c.rect((w/2)-120, (h/2)-70, 10, 10, fill=True)
c.setFillColorRGB(255, 0, 0)
c.rect((w/2)-120, (h/2)-90, 10, 10, fill=True)
c.setFillColorRGB(0, 0, 255)
c.rect((w/2)-120, (h/2)-110, 10, 10, fill=True)
c.setFillColorRGB(112,128,144)
c.rect((w/2)-120, (h/2)-130, 10, 10, fill=True)
c.setFillColorRGB(30,144,255)
c.rect((w/2)-120, (h/2)-150, 10, 10, fill=True)


c.showPage()
c.save()
