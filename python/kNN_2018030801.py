#coding:utf

from numpy import *
import operator
from os import listdir

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

def img2vector(filename):#这是一个图像转成向量哦，
    returnVect = zeros((1,1024))#时间处理一下销量的销量，现在是一行124，
    fr = open(filename)#接下来的话是打开文件，
    for i in range(32):#他接下来的话能开始使用那个h9，先是九一到21到32，32×32是多少？900？
        lineStr = fr.readline()#这是读取一行数据，一行数据就是那个图吧，又多了一行，
        for j in range(32):#的哦，接下来就是那个什么嗯嗯，下一行是
            returnVect[0,32*i+j] = int(lineStr[j])#
    return returnVect

def handwritingClassTest():
    hwLabels = []#好让接下来就是那个数学题的，首先是谁提的类别？
    trainingFileList = listdir(r'C:\Users\gao\Documents\code\python\digits\trainingDigits')#接下来这个是得到文件的列表，这个是取文件目录，
    m = len(trainingFileList)#然后得到这个文件目录中有多少个文件
    trainingMat = zeros((m,1024))#然后那个创建一下我们的训练矩阵，
    for i in range(m):
        fileNameStr = trainingFileList[i]#得到每个文件的名字得不转，
        fileStr = fileNameStr.split('.')[0]#然后开始把文件名，然后切割一下，然后取出名字部分去掉后缀，
        classNumStr = int(fileStr.split('_')[0])#然后再把那个，而且您继续切割，然后因为文件名中的第一部分就是这个类名，类别名，
        hwLabels.append(classNumStr)#然后把这个数学题的类别，然后加入到，然后这个加入到我们目标结果中去，结果这个类别的列表中去，
        trainingMat[i,:]=img2vector('C:\Users\gao\Documents\code\python\digits\trainingDigits\%s'%fileNameStr)#然后把文件名和我们的目录名结合到一起，然后转换成矩阵，
    testFileList = listdir(r'C:\Users\gao\Documents\code\python\digits\trainingDigits')#同样的方法在得到一下我们的目录，
    errorCount = 0.0#然后出错率，
    mTest = len(testFileList)#将来是得到我们那个目录中包含多少个文件？
    for i in range(mTest):
        fileNameStr = testFileList[i]#同样的方法，然后得到目录中文件的每个名字，然后再得到文件的名字的那个去掉后缀，然后再取出，
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits\%s'%fileNameStr)#然后得到我们的，文件，名字然后就可以转换成销量了，
        classifierResult = classify0(vectorUnderTest,trainingMat,hwLabels,3)#然后可以把这个我们的类别，然后进行一个处理了，因为我们现在所有数据都得到了，
        print "the classifier came back with: %d, the real answer is : %d"% (classifierResult, classNumStr)#
        if(classifierResult!=classNumStr):errorCount += 1.0#
    print "\nthe total number of errors is : %d "%errorCount
    print "\n the total error rate is : %f" % (errorCount /float (mTest)) 