from numpy import *
import numpy as np
x1 = np.arange(9.0).reshape((3,3))
print x1
x2 = np.arange(3.0)
print x2
x3 =[[0,1,2],[0,1,2],[0,1,2]]
print x3
x4 = mat(x3)
print x4
a = np.multiply(x1,x2)
print a
b = np.multiply(x1,x3)
c = np.multiply(x1,x4)
print b,c