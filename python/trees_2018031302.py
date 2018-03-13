#coding:utf

from math import log


#机器学习的六个步骤
#1.找到数据
#这个数据是一个文件
#2.准备数据
#这是要把文件的数据转化为dataSet和labels

def createDataSet():
    dataSet = []
    labels = []
    return dataSet,labels

#3.分析数据
#这是要数据可视化
#使用文本注解绘制树节点

def plotNode():

def createPlot():

#获取叶节点的数目和树的层次
def getNumLeafs(myTree):
    return numLeafs
def getTreeDepth(myTree):
    return maxDepth
def retrieveTree(i):
    listOfTrees = []
    return listOfTrees[i]

def plotMidText(cntrPt,parentPt,txtString):

def plotTree(myTree,parentPt,nodeTxt):
    
def createPlot(inTree):
    
#4.训练算法
#这是要写出算法，并让算法的参数优化
#这里是决策树，就是要写决策树的算法了
#信息增益
#计算给定数据集的香农熵
def calcShannonEnt(dataSet):
    shannonEnt = 0.0
    return shannonEnt

#按照给定的特征划分数据集,这里有三个参数，一个是数据集，一个是axis表示特征
def splitDataSet(dataSet, axis, value):
    retDataSet=[]
    return retDataSet

#选择最好的数据集划分方法
def chooseBestFeatureToSplit(dataSet):
    bestFeature = -1
    return bestFeature

#
def majority(classList):
    
    return sortedClassCount[0][0]

#创建树的函数代码
def createTree(dataSet,labels):
    return myTree

#5.测试算法
#这是要把训练好的算法提供一个测试，并提供错误率，最好的错误率是最低的
def classify(inutTree,featLabels,testVec):
    return classLabel
#6.使用算法
#这是要把算法进行实际使用了，这就是我们要的事情
def storeTree(inputTree,filename):

def grabTree(filename):

