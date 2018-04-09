from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
figure = plt.figure()
ax = Axes3D(figure)
X = np.arange(0, 10, 1)
Y = np.arange(0, 10, 1)
Z = np.arange(-1000,0,1)
#网格化数据
X, Y = np.meshgrid(X, Y)

# R = np.sqrt(X**2 + Y**2)
# Z = np.cos(R)
Z = 4*X*X+(13/2)*Y*Y+10*X*Y-2*X-2*Y



ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
plt.show()