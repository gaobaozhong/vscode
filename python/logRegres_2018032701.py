# coding:utf
from numpy import *

# 5-1
def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open(r'D:\Users\gao\Documents\Code\machinelearninginaction\Ch05\testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0,float(lineArr[0]),float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat, labelMat

def sigmod(inX):
    return 1.0/(1+exp(-inX))

def gradAscent(dataMatIn, classLabels):
    dataMatrix = mat(dataMatIn)
    labelMat = mat(classLabels).transpose()
    m,n = shape(dataMatrix)
    alpha = 0.001 #是步长
    maxCycles = 500 
    weights = ones((n,1)) 
    for k in range(maxCycles):
        h = sigmod(dataMatrix * weights)
        error = (labelMat - h)
        weights = weights + alpha * dataMatrix.transpose() * error
    return weights

# def plotBestFit(weights):
#     import matplotlib.pyplot as plt
#     dataMat,labelMat =
#     dataArr = 
#     n =
#     xcord1 =
#     ycord1 =
#     xcord2 =
#     ycord2 =
#     for i in range(n):
#         if int(labelMat[i])== 1:
#             xcord1.append()
#         else:
#             xcord2.append()
#     fig  = plt.figure()
#     ax = fig.add_subplot()
#     ax.scatter()
#     ax.scatter()
#     x = arrange()
#     y = (-weights[0]-weights[1]*x)/weights[2]
#     ax.plot()
#     plt.xlabel()
#     plt.ylabel()
#     plt.show()

# # 5-3
# def stocGradAscent0(dataMatrix,classLabels):
#     m,n =
#     alpha =
#     weights =
#     for i in range(m):
#         h = 
#         error =
#         weights =
#     return weights
# # 5-4
# def stocGradAscent1(dataMatrix,classLabels,numIter=150):
#     m,n =
#     weights = ones(n)
#     for j in range(numIter):
#         for i in range(m):
#             alpha = 4/(1.0+j+i)+0.01
#             randIndex = 
#             h = sigmod()
#             error =
#             weights =
#             del()
#     return weights    