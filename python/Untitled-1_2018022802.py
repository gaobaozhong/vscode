import matplotlib
import matplotlib.pyplot as plt
import kNN_20180307

datingDataMat,labels = kNN_20180307.file2matrix("C:\Users\gao\Documents\code\python\datingTestSet2_20180308.txt")
flg = plt.figure()
ax= flg.add_subplot(111)
ax.scatter(datingDataMat[:,1],datingDataMat[:,2])
plt.show()