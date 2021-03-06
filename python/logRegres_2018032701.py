# coding:utf
from numpy import *


# 5-1
def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open(
        r'D:\Users\gao\Documents\Code\machinelearninginaction\Ch05\testSet.txt'
    )
    # print 'fr:', fr
    for line in fr.readlines():
        lineArr = line.strip().split()
        # print 'lineArr', lineArr
        dataMat.append([1.0, float(lineArr[0]),
                        float(lineArr[1])])  # 这里为什么要加一个第一列全1呢？
        labelMat.append(int(lineArr[2]))  # 这个属性没有问题
    return dataMat, labelMat


def sigmoid(inX):  # 这里inX就是一个整形，不是的，这里这inX是input X的意思，是一个向量。也就是一个列表类型
    return 1.0 / (1 + exp(-inX))


def gradAscent(
        dataMatIn, classLabels
):  # 这里dataMatIn是一个输入的二位列表，第一维是100行，第二维是3列，分别是x0，x1，x2，这里代表的就是一个直线？这个直线有什么用，和我们的最后结果，以及和权值有什么关系？
    # print 'dataMatIn:', dataMatIn
    # print 'classLabels:', classLabels
    dataMatrix = mat(dataMatIn)  # 这里dataMatrix是一个矩阵
    labelMat = mat(classLabels).transpose(
    )  # 这里进行转置矩阵的原因就是，因为mat直接把一个列表转为矩阵之后，就是一个1行100列的矩阵，但是我们这里每一个类别对应的是100行3列的矩阵，所以，没一行是一个类别，所以，这里用了转置函数transpose，把列表转为了100行1列的矩阵
    # print 'mat(classLabels):', mat(classLabels)
    # print 'mat(classLabels).transpose():', mat(classLabels).transpose()
    m, n = shape(dataMatrix)  # 这里得到了矩阵的m,n,100,3
    # print 'm,n:', m, n
    alpha = 0.001  #是步长，这个值是默认值，是经验值，很重要，决定了我们的执行速度和精度
    maxCycles = 500
    weights = ones(
        (n, 1))  #这是一个3*1的矩阵，就是一个n维，在这里就是100行，一列的1的矩阵，这是初始权值，也就是那个最基础的初始值
    for k in range(maxCycles):
        # print 'k:',k
        # print 'dataMatrix:',dataMatrix
        # print 'weights:',weights
        # print 'dataMatrix* weights:', dataMatrix * weights
        h = sigmoid(dataMatrix * weights)
        # print 'h:', h
        error = (labelMat - h)
        # print 'error:', error
        weights = weights + alpha * dataMatrix.transpose() * error
        # print 'weights:', weights
        # plotBestFit(weights.getA())
    return weights


def plotBestFit(weights):
    import matplotlib.pyplot as plt
    dataMat,labelMat = loadDataSet()
    dataArr = array(dataMat)
    print 'dataMat',dataMat
    print 'dataArr',dataArr
    n = shape(dataArr)[0]
    print 'n = shape(dataArr)[0]:',n
    xcord1 = []
    ycord1 = []
    xcord2 = []
    ycord2 = []
    for i in range(n):
        # print 'i:',i
        # print 'labelMat[i]:',labelMat[i]
        # print 'dataArr[i]:',dataArr[i]
        if int(labelMat[i])== 1:
            xcord1.append(dataArr[i,1])
            ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1])
            ycord2.append(dataArr[i,2])
    fig  = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1,ycord1,s=30,c='red',marker='s')
    ax.scatter(xcord2,ycord2,s=30,c='green')
    x = arange(-3.0,3.0,0.1)
    y = (-weights[0]-weights[1]*x)/weights[2]
    ax.plot(x,y)
    y = (-1-x)
    ax.plot(x,y)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()

# 5-3
def stocGradAscent0(dataMatrix,classLabels):
    m,n = shape(dataMatrix)
    alpha = 0.01
    weights = ones(n)
    for i in range(m):
        h = sigmoid(sum(dataMatrix[i]*weights))
        error = classLabels[i] - h
        weights = weights + alpha * error * dataMatrix[i]
    return weights

# 5-4
def stocGradAscent1(dataMatrix,classLabels,numIter=150):
    m,n = shape(dataMatrix)
    weights = ones(n)
    for j in range(numIter):
        dataIndex = range(m)
        for i in range(m):
            alpha = 4/(1.0+j+i)+0.01
            randIndex = int(random.uniform(0,len(dataIndex)))
            h = sigmoid(sum(dataMatrix[randIndex]*weights))
            error = classLabels[randIndex] - h
            weights = weights + alpha * error * dataMatrix[randIndex]
            del(dataIndex[randIndex])
    return weights

#  5.3.2 用逻辑回归预测病症

def classifyVector(inX,weights):
    prob = sigmoid(sum(inX*weights))
    if prob > 0.5:
        return 1
    else:
        return 0

def colicTest():
    frTrain = open(r'D:\Users\gao\Documents\Code\machinelearninginaction\Ch05\horseColicTraining.txt')
    frTest = open(r'D:\Users\gao\Documents\Code\machinelearninginaction\Ch05\horseColicTest.txt')
    trainingSet = []
    trainingLabel = []
    for line in frTrain.readlines():
        currLine = line.strip().split('\t')
        lineArr = []
        for i in range(21):
            lineArr.append(float(currLine[i]))
        trainingSet.append(lineArr)
        trainingLabel.append(float(currLine[21]))
    trainingWeights = stocGradAscent1(array(trainingSet),trainingLabel,500)
    errorCount = 0
    numTestVec = 0
    for line in frTest.readlines():
        numTestVec += 1.0
        currLine = line.strip().split('\t')
        lineArr = []
        for i in range(21):
            lineArr.append(float(currLine[i]))
        if int(classifyVector(lineArr,trainingWeights))!=int(currLine[21]):
            errorCount +=1
    errorRate = (float(errorCount)/numTestVec)
    print "the erro rate of his test is : %f " % errorRate  
    return errorRate

def multiTest():
    numTests = 10
    errorSum = 0.0
    for k in range(numTests):
        errorSum += colicTest()
    print " after %d iterations the average error rate is : %f" % (numTests,errorSum/float(numTests))