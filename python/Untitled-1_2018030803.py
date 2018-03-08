from numpy import *
import matplotlib.pyplot as plt
import kNN_20180307 as kNN

datingDataMat,labels = kNN.file2matrix("C:\Users\gao\Documents\code\python\datingTestSet2_20180308.txt")
fig = plt.figure()
ax=fig.add_subplot(111)
ax.scatter(datingDataMat[:,1],datingDataMat[:,0],15*array(labels),15*array(labels))
plt.show()