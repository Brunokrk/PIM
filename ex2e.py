from PIL import Image 
import numpy as np
import time as tm
pil1=Image.open('mandril.jpg')

(l,h)=pil1.size 
print(l,h) 

for j in range(0, h): 
    for i in range(0, l): 
		pix=pil1.getpixel((i,j))
		r=pix[0]
		g=pix[1]
		b=pix[2]
		gray= 0.2989 * r + 0.5870 * g + 0.1140 * b
		print('coord: '+repr((i,j))+' --- pixel = '+repr(np.uint8(gray)))
		tm.sleep(0.05)
