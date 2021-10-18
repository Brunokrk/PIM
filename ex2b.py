import numpy as np
import matplotlib.pyplot as plt
a = np.arange(10)
np.disp(a)
fig=plt.figure()
plt.plot(a,a*a)
plt.show()

#-----------------------------------------------------
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

mpl.rcParams['legend.fontsize'] = 10
fig1 = plt.figure()
ax = fig1.gca(projection='3d')
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
#print(x.type)
ax.plot(x, y, z, label='parametric curve')
ax.legend()
plt.show()
