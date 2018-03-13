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
    num = len(dataSet)  #這是得到總數
    labelCounts = {}  #得到類的總數
    for data in dataSet:
        currentLabel = data[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        p = float(labelCounts[key]) / num
        shannonEnt -= p * log(p, 2)

    return shannonEnt


def calcShannonEnt1(dataSet):
    num = len(dataSet)
    labelCounts = {}
    for data in dataSet:
        currentLabel = data[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        p = float(labelCounts[key]) / num
        shannonEnt -= p * log(p, 2)
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
        p = float(labelCounts[key]) / num
        shannonEnt -= p * log(p, 2)
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
    for key in labelCounts:
        p = float(labelCounts[key]) / num
        shannonEnt -= p * log(p, 2)
    return shannonEnt


def calcShannonEnt4(dataSet):
    num = len(dataSet)
    labelCounts = {}
    for data in dataSet:
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        p = float(labelCounts[key]) / num
        shannonEnt -= p * log(p, 2)
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
        p = float(labelCounts[key]) / num
        shannonEnt -= p * log(p, 2)
    return shannonEnt


#为了测试，接下来就是创建临时数据集了
def createDataSet():
    dataSet = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels


def createDataSet1():
    dataSet = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels


def creatDataSet2():
    dataSet = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels


#3.1.2划分数据集。根据制定的属性自断的值一般是布尔型或者是标称型，就可以尝试着分类划分数据集成不同的子类，然后根据不同的子类的数据集的熵的和来看一下，这个划分是否是有意义的。
#3-2 按照制定的特征划分数据集
def splitDataSet(dataSet, axis, value):
    returnDataSet = []
    for data in dataSet:
        if data[axis] == value:
            print 'data = ', data
            print 'value = ', value
            print 'data[axis]', data[axis]
            reducedData = data[:axis]
            print 'data[:axis]', data[:axis]
            reducedData.extend(data[axis + 1:])
            print reducedData
            returnDataSet.append(reducedData)
    print returnDataSet
    return returnDataSet


def splitDataSet1(dataSet, axis, value):
    returnDataSet = []
    for data in dataSet:
        if data[axis] == value:
            reducedData = data[:axis]
            reducedData.extend(data[axis + 1:])
            returnDataSet.append(reducedData)
    return returnDataSet


def splitDataSet2(dataSet, axis, value):
    returnDataSet = []
    for data in dataSet:
        if data[axis] == value:
            reducedData = data[:axis]
            reducedData.extend(data[axis + 1:])
            returnDataSet.append(reducedData)
    return returnDataSet


def splitDataSet3(dataSet, axis, value):
    returnDataSet = []
    for data in dataSet:
        if data[axis] == value:
            reducedData = data[:axis]
            reducedData.extend(data[axis + 1:])
            returnDataSet.append(reducedData)
    return returnDataSet


def splitDataSet4(dataSet, axis, value):
    returnDataSet = []
    for data in dataSet:
        if data[axis] == value:
            reducedData = data[:axis]
            reducedData.extend(data[axis + 1:])
            returnDataSet.append(reducedData)
    return returnDataSet


def splitDataSet5(dataSet, axis, value):
    returnDataSet = []
    for data in dataSet:
        if data[axis] == value:
            reducedData = data[:axis]
            reducedData.extend(data[axis + 1:])
            returnDataSet.append(reducedData)
    return returnDataSet


#接下来要找到最要好的划分方式
def chooseBestFeatureToSplite(dataSet):
    numFeature = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeature):
        featureList = [example[i] for example in dataSet]
        uniqueVals = set(featureList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, 1, value)
            p = len(subDataSet) / float(len(dataSet))
            newEntropy += p * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

def chooseBestFeatureToSplite1(dataSet):
    numFeature= len(dataSet[0])-1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeature):
        featureList = [example[i] for example in dataSet]
        uniqueVals = set(featureList)
        newEntropy= 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet,1,value)
            p = len(subDataSet)/float(len(dataSet))
            newEntropy+=p*calcShannonEnt(subDataSet)
        infoGain = baseEntropy-newEntropy
        if(infoGain>bestInfoGain):
            bestInfoGain = infoGain
            bestFeature=i
    return bestFeature

def chooseBestFeatureToSplite2(dataSet):
    numFeature = len(dataSet[0])-1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeature):
        featureList =[example[i] for example in dataSet]
        uniqueVals = set(featureList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet,1,value)
            p = len(subDataSet)/float(len(dataSet))
            newEntropy+=p*calcShannonEnt(subDataSet)
        infoGain = baseEntropy-newEntropy
        if(infoGain>bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

def chooseBestFeatureToSplite3(dataSet):
    numFeature = len(dataSet[0])-1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain =0
    bestFeature = -1
    for i in range(numFeature):
        featureList = [example[i] for example in dataSet]
        uniqueVals = set(featureList)
        newEntropy = 0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet,1,value)
            p = len(subDataSet)/float(len(dataSet))
            newEntropy += p*calcShannonEnt(subDataSet)
        infoGain = baseEntropy-newEntropy
        if(infoGain>bestInfoGain):
            bestInfoGain= infoGain
            bestFeature = i
    return bestFeature

def chooseBestFeatureToSplite4(dataSet):
    numFeature = len(dataSet[0])-1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0
    bestFeature = -1
    for i in range(numFeature):
        featrueList = [example[i] for example in dataSet]
        uniqueVals = set(featrueList)
        newEntropy = 0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet,1,value)
            p = len(subDataSet)/float(len(dataSet))
            newEntropy += p*calcShannonEnt(subDataSet)
        infoGain = baseEntropy-newEntropy
        if(infoGain>bestInfoGain):
            bestInfoGain = infoGain
            bestFeature=i
    return bestFeature
    