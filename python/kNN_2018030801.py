from numpy import *
import operator

def createDataSet():
    group = array([
        [1.,1.1],
        [1.,1.],
        [0,0],
        [0,0.1]
    ])
    labels = ['A','A','B','B']
    return group,labels
def classify0(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX,(dataSetSize,1))-dataSet
    sqDiffMat = diffMat**2
    sqDistance = sqDiffMat.sum(axis=1)
    distances = sqDistance**0.5
    sortedDistanceIndicies = distances.argsort()

    classCount = {}
    for i in range(k):
        classILabel = labels[sortedDistanceIndicies[i]]
        classCount[classILabel] = classCount.get(classILabel,0)+1
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def file2matrix(filename):
    fr =open(filename)
    lines = fr.readlines()
    numberOfLines = len(lines)
    returnMat = zeros((numberOfLines,3))
    labels = []

    index=0
    for line in lines:
        line = line.strip()
        listOfLine = line.split('\t')
        returnMat[index,:] = listOfLine[0:3]
        labels.append(int(listOfLine[-1]))
        index+=1
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
    datingDataMat, datingLabels = file2matrix('C:\Users\gao\Documents\code\python\datingTestSet2_20180308.txt')
    normMat,ranges,minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print "the classifier came back with: %d ,the real answer is %d"%(classifierResult,datingLabels[i])
        if(classifierResult != datingLabels[i]):
            errorCount +=1
    print "the total error rate is : %f"% (errorCount/float(numTestVecs))


def classifyPerson():
    resultList = ['not at all','in small doses','in large doses']
    percentTats = float(raw_input("percentage of time spent plahying video gaems?"))
    ffMiles = float(raw_input("frequent filer miles eraned peryea?"))
    iceCream = float(raw_input("liteso ice cream consumed peryear?"))
    datingDataMat,datingLabels = file2matrix('C:\Users\gao\Documents\code\python\datingTestSet2_20180308.txt')
    normMat, ranges , minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles,percentTats,iceCream])

    
    
    classifierResult = classify0((inArr-minVals)/ranges,normMat,datingLabels,3)
    print "you will probably like his person:", resultList[classifierResult-1]