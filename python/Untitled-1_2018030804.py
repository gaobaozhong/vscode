from numpy import *
import matplotlib.pyplot as plt
import kNN_2018030801 as kNN

datingDataMat,labels = kNN.file2matrix("C:\Users\gao\Documents\code\python\datingTestSet2_20180308.txt")


dataSet = datingDataMat
print dataSet

minVals = dataSet.min(0)
print minVals
maxVals = dataSet.max(0)
print maxVals
ranges = maxVals - minVals
print ranges
normDataSet = zeros(shape(dataSet))
print shape(dataSet)
print dataSet.shape
print normDataSet
m = dataSet.shape[0]
normDataSet = dataSet - tile(minVals,(m,1))
print tile(minVals,(m,1))
print normDataSet
normDataSet = normDataSet/tile(ranges,(m,1))
print tile(ranges,(m,1))
print normDataSet
kNN.datingClassTest()
