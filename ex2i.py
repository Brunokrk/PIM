from PIL import Image 
import numpy as np
import time as tm
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter



pil1=Image.open('mantis.jpg')#('mandril.jpg')#('arara.jpg')#('qrcode.jpg')#
pil1.show()


(l,h)=pil1.size 
print(l,h) 

tmp= np.zeros((l,h))

for j in range(0, h): 
    for i in range(0, l): 
		pix=pil1.getpixel((i,j))
		r=pix[0]
		g=pix[1]
		b=pix[2]
		gray= 0.2989 * r + 0.5870 * g + 0.1140 * b
		#print('coord: '+repr((i,j))+' --- pixel = '+repr(np.uint8(gray)))
		tmp[j,i]=gray


imgTmp=Image.fromarray(np.uint8(tmp))
imgTmp.show()

fig = plt.figure()
ax = fig.gca(projection='3d')

step= 10
x = np.arange(0.0, l, step)
y = np.arange(0.0, h, step)
X, Y = np.meshgrid(x, y)

# atenuando picos
tmp = gaussian_filter(tmp, sigma=7)

Z = tmp[::step,::step]
ax.plot_surface(X, Y, Z)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()
