
from PIL import Image 
import numpy as np 
import time as tm 

arqName = 'mandril.jpg'
pil1=Image.open(arqName) 
(l,h)=pil1.size 
print(l,h) 
out=Image.new(pil1.mode, (l,h)) 
angDeg=10 #30 
angRad=(angDeg*np.pi)/180 
a=np.cos(angRad) 
b=np.sin(angRad) 

# Matriz de rotacao obtida no Gonzalez e Woods, 2010, 3ra ed. p. 57 
rot=np.matrix([[a,b, 0],[-b, a, 0], [0,0,1]]) 
print(rot) 
tm.sleep(2) 
for j in range(0, h): 
    for i in range(0, l): 
        #print(j,i) 
        tmp=np.trunc(rot*np.matrix([i,j,1]).T) 
       # print(tmp) 
        try:    out.putpixel((tmp[0],tmp[1]),pil1.getpixel((i,j))) 
        except: print('mapeado para fora da imagem: '+repr(tmp)) 
out.show() 
out.save(arqName.split('.')[0]+'_rot.jpg',"JPEG")

