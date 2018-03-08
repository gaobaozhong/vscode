#coding:utf
# 这是一个实验，例子,在这个例子中嗯解释一下如何创建一个数据，就是第一步，出去的，所有的数据，科学的算法一般都有这么六步，第一步就是收集数据，准备数据分析数据，训练数据，测试数据的使用书籍，在2400不中都是，而且差不多都是对数据进行处理，请问这个数据数据也就是找数据，准备出去的话，就是一键清洗，分数低的话，那就对数据进行一些统计，也简单的处理了，
from numpy import *
import operator

def createDataSet():
    group = array([
        [1.0,1.1],[1.0,1.0],[0,0],[0,0.1]
    ])
    labels = ['A','A','B','B'
    ]
    return group,labels

def classify0(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX,(dataSetSize,1))
    distances = ((diffMat**2).sum(axis=1))**0.5
    sortedDistIndicies = distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]] 
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines,3))
    classLabelVector=[]
    index=0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:]=listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index+=1
    return returnMat,classLabelVector