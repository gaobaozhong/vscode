#coding:utf

from math import log

#决策树

#3.1决策树的构造
#优点：计算复杂度不高，输出结果易于理解，对中介安置的确实不敏感，可以处理不相关的调整数据。
#缺点，可能会产生过度匹配问题。
#使用数据累心给，数值型和飙车行in习惯

#本节将通过算法一步步构造决策树，并会设计许多有趣的细节。
# 首先我们讨论数学上如何使用信息论划分数据集，
# 然后编码代码讲理论应用到具体的数据集上，
# 最后编写代码构建决策树。

#3-1 计算给定数据集的香农熵
def calcShannonEnt(dataSet):
    num = len(dataSet)#這是得到總數
    labelCounts = {}#得到類的總數
    for data in dataSet:
        currentLabel = data[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=0
        labelCounts[currentLabel]+=1
    shannonEnt = 0.0
    for key in labelCounts:
        p = float(labelCounts[key])/num
        shannonEnt -= p*log(p,2)

    return shannonEnt

def calcShannonEnt1(dataSet):  
    num = len(dataSet)
    labelCounts = {}
    for  data in dataSet:
        currentLabel = data[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=0
        labelCounts[currentLabel]+=1
    shannonEnt = 0.0
    for key in labelCounts:
        p = float(labelCounts[key])/num
        shannonEnt -= p*log(p,2)
    return shannonEnt

def calcShannonEnt2(dataSet):
    num = len(dataSet)
    labelCounts = {}
    for data in dataSet:
        currentLabel = data[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        p = float(labelCounts[key])/num
        shannonEnt -= p*log(p,2)
    return shannonEnt

def calcShannonEnt3(dataSet):
    num = len(dataSet)
    labelCounts = {}
    for data in dataSet:
        currentLabel = data[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key  in labelCounts:
        p = float(labelCounts[key])/num
        shannonEnt -= p*log(p,2)
    return shannonEnt

def calcShannonEnt4(dataSet):
    num = len(dataSet)
    labelCounts = {}
    for data in dataSet:
        if currentLabel  not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        p = float(labelCounts[key])/num
        shannonEnt -= p*log(p,2)
    return shannonEnt

def calcShannonEnt5(dataSet):
    num = len(dataSet)
    labelCounts = {}
    for data in dataSet:
        currentLabel = data[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        p = float(labelCounts[key])/num
        shannonEnt -= p*log(p,2)
    return shannonEnt

#为了测试，接下来就是创建临时数据集了
def createDataSet():
    dataSet = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
    labels = ['no surfacing','flippers']
    return dataSet, labels

def createDataSet1():
    dataSet = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
    labels = ['no surfacing','flippers']
    return dataSet,labels
def creatDataSet2():
    dataSet = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
    labels = ['no surfacing','flippers']
    return dataSet,labels
    