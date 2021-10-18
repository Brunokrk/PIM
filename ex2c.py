from PIL import Image
import numpy
    
img = Image.open("mandril.jpg")
img=img.convert('L')
img.show()
a = numpy.array(img)

#Emoldurando a imagem
# frame superior
a[ :50, : ] = 0 
# frame inferior
a[-50: , : ] = 0 
# frame esquerdo
a[ : , :50] = 0 
# frame direito
a[ : ,-50: ] = 0 

img1= Image.fromarray(a)
img1.show() # com frame de 10 pixels de espessura
