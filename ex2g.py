
from PIL import Image 
import numpy as np
arqName='mandril.jpg' 
pil1=Image.open(arqName)
(l,h)=pil1.size 
print(l,h) 
out=Image.new(pil1.mode, (l,h)) 
for j in range(0, h): 
    for i in range(0, l): 
        out.putpixel((i,j),pil1.getpixel((i,j))) 
out.show() 
out.save(arqName.split('.')[0]+'_copia.jpg',"JPEG")
