#coding:utf
#这是一个测试例子，就是命好的地方，我现在写的代码了，
import kNN_2018030703 as kNN
from numpy import *
import operator
group,labels = kNN.createDataSet() 

print group
print labels
print group.shape
print group.shape[0]
inX=[1,1]
dataSet = group
dataSetSize=group.shape[0]
print inX
print dataSet
print dataSetSize
print tile(inX,(dataSetSize,1))
diffMat = tile(inX,(dataSetSize,1))-dataSet
print diffMat
print diffMat**2
print (diffMat**2).sum(axis=1)
print (diffMat**2).sum(axis=0)
distances = ((diffMat**2).sum(axis=1))**0.5
print distances
sortedDistIndicies = distances.argsort()
print sortedDistIndicies 
print operator.itemgetter(1)

classCount={}
for i in range(3):
    print i
    voteIlabel = labels[sortedDistIndicies[i]] 
    print voteIlabel
    classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
    print classCount[voteIlabel]
sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
print classCount
print classCount.iteritems()
print sortedClassCount
print sortedClassCount[0][0]

print kNN.classify0([0,0],group,labels,3)