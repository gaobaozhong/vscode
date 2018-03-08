import matplotlib
import matplotlib.pyplot as plt
import kNN_20180307 as kNN
from numpy import *

datingDataMat,datingLabels = kNN.file2matrix("C:\Users\gao\Documents\code\python\datingTestSet2_20180308.txt")#这是就是之前的矩阵和有我们的类别，然后创建初始化，这个正好是之前写的，所以很熟悉
flg = plt.figure()#这个应该就是创建惠民一个，相当于背景图吧，也是这样子的，
ax= flg.add_subplot(111)#这个是添加竹吗？不知道什么意思，参加葡萄藤加点，
ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*array(datingLabels),15.0*array(datingLabels))#这个是绘制散点图了，这里它的参数呢，一开始是两个，两个的时候呢，就没有颜色，就是没有泪点了，后来的话呢他就加了两个，
plt.show()#这就是所谓的画图了，