# -*- coding: cp1252 -*-
from PIL import Image
pil1=Image.open('mandril.jpg')#('lena.pgm')
pil1.show()
a=pil1.split() # retorna uma tupla contendo os canais RG e B
a[0].show()
a[1].show()
a[2].show()
out=pil1.rotate(45) # retorna instância da imagem rotacionada
out.show()
