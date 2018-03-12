#coding:utf
#一个机器学习有8个步骤
#第一个是收集数据：提供文本文件
#第二个是准备数据：使用Python解析文本文件
#第三个是分析数据：使用Matplotlib画二维扩散图
#第四个是训练算法：次步骤不适用于K-近邻算法，因为一般是调整参数
#第五个测试算法：使用很轮提供的部分数据作为测试样本
#第六个使用算法：产生简单的命令行程序，然后海伦可以输入一些特征数据一判断对方是否为自己喜欢的类型。

import matplotlib
import matplotlib.pyplot as plt
from numpy import *
import operator

##一个机器学习有8个步骤
#第一个是收集数据：提供文本文件
#文件datingTestSet2.txt得到了
#第二个是准备数据：
# 1.使用Python解析文本文件;
# 目的：把待处理数据改为适合numpy处理的格式，就是一个属性矩阵，一个目标分类列表类型
# 2.归一化数据
# 目的：让特征有同样的计算量度

def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector

def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals-minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet-tile(minVals,(m,1))
    normDataSet = normDataSet/tile(ranges,(m,1))
    return normDataSet,ranges, minVals

    #第三个是分析数据：使用Matplotlib画二维扩散图
def createScatter(dataSetMat, classLabelVector):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(dataSetMat[:, 1], dataSetMat[:, 2],
               15 * array(classLabelVector), 15 * array(classLabelVector))
    plt.show()


#第四个是训练算法：次步骤不适用于K-近邻算法，因为一般是调整参数
def classify0(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX,(dataSetSize,1))-dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndices[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
    sortedClassCount =sorted(classCount.iteritems,key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

#第五个测试算法：使用很轮提供的部分数据作为测试样本
def datingClassTest(filename):
    hoRatio = 0.10
    dataMat,labels = file2matrix(filename)
    normMat, ranges,minVals = autoNorm(dataMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],labels[numTestVecs:m],3)
        print "the classifier came back wieth : %d, the real answer is : %d  " & (classifierResult, datingLabels[i])
        if (classifierResult!=datingLabels[i]):
            errorCount+=1.0
    print "the total error rate is : &f" % (errorCount/float(numTestVecs))


    


#第六个使用算法：产生简单的命令行程序，然后海伦可以输入一些特征数据一判断对方是否为自己喜欢的类型。

def classifyPerson(filename):
    resultList=['not at all','in small doses','in large doses']
    percentTats =float(raw_input("percentage of time spent playing video games?"))
    ffMiles = float(raw_input("frequentt flier miles eraned pers yesr?"))
    iceCream = float(raw_input("liters of ice cream consumed per year?"))
    datingDataMat,datingLabels = file2matrix(filename)
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles,percentTats,iceCream])
    classifierResult = classify0((inArr-minVals)/ranges,normMat,datingLabels,3)
    print "you will probablyh like this person: ",resultList[classifierResult-1]