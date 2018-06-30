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
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    sortedDistances = argsort(distances)
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

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
        returnMat[index,:]=listFromLine[0:-1]
        labels.append(listFromLine[-1])
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
    # print(datingDataMat[0])
    # print(datingLabels[0])
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m,n = normMat.shape
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],90)
        # print(classifierResult)
        
        if(classifierResult!=datingLabels[i]):
            errorCount += 1.0
            print (" the classifer came bakc with:%s, the real answer is : %s" % (classifierResult, datingLabels[i]))
    print ("the total error rate is : %f" % (errorCount/float(numTestVecs)))
