import matplotlib
import matplotlib.pyplot as plt
import kNN_20180307 as kNN
from numpy import *

datingDataMat,datingLabels = kNN.file2matrix("C:\Users\gao\Documents\code\python\datingTestSet2_20180308.txt")
flg = plt.figure()
ax= flg.add_subplot(111)
ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*array(datingLabels),15.0*array(datingLabels))
plt.show()