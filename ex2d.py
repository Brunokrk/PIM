from PIL import Image
import numpy
    
img = Image.open("mandril.jpg")
img = img.convert('L')
img.show()
a = numpy.array(img)

#reticulado de linhas de espessura 10 pixels
a[ ::10, : ] = 0 
a[ : , ::10] = 0 

img= Image.fromarray(a)
img.show() 
