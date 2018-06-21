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
    