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

    # fr = open(filename)
    # arrayOLines = fr.readlines()
    # numberOfLines = len(arrayOLines)
    # returnMat = zeros((numberOfLines,3))
    # labels = []

    # index=0
    # for line in arrayOLines:
    #     line = line.strip()
    #     listFromLine = line.split('/t')
    #     returnMat[index,:]=listFromLine[0:3]
    #     labels.append(int(listFromLine[-1]))
    #     index+=1
    # return returnMat,labels