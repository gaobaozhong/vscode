from numpy import *
import operator
def createDataSet():
    group = array(
            [
                [1.0,1.1],
                [1.0,1.0],
                [0,0],
                [0,0.1]
            ]
        )
    labels = [
        'A',
        'A',
        'B',
        'B'
    ]
    return group,labels

# 2.1
def classify0(inX,dataSet,labels,k):
    dataSetSize=dataSet.shape[0]
    diffMat = tile(
        inX,
        (
            dataSetSize,1 
        )
    )-dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    

def file2matrix(filename):
    fr = open(filename)
    lines = fr.readlines()
    numberOfLines = len(lines)
    returnMat = zeros((numberOfLines,3))
    labels = []

    index=0
    for line in lines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:]=listFromLine[0:3]
        labels.append(int(listFromLine[-1]))
        index += 1
    return returnMat,labels

def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals,(m,1))
    normDataSet = normDataSet/tile(ranges,(m,1))
    return normDataSet,ranges,minVals

def datingClassTest():
    hoRatio = 0.10
    datingDataMat,datingLabels = file2matrix(r'C:\Users\gao\code\machinelearninginaction\Ch02\datingTestSet.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels)
        print (" the classifer came bakc with:%d, the real answer is : %d" % (classifierResult,datingLabels[i]))
        if(classifierResult!=datingLabels[i]):
            errorCount += 1.0
        print ("the total error rate is : %f" % (errorCount/float(numTestVecs)))
