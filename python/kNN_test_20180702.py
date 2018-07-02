import kNN_20180702 as kNN
from numpy import *
group,labels = kNN.createDataSet()

# print(group)
# print(labels)

dataSet = group
inX = [1,0.1]
dataSetSize=dataSet.shape[0]
diffMat = tile(
    inX,
    (
        dataSetSize,1 
    )
)-dataSet
# print("-dataSet:")
# print(diffMat)
# diffMat1 = tile(
#     inX,
#     (
#         dataSetSize,1 
#     )
# )-dataSet
# print(dataSet)
# print(dataSetSize)
# inX = [2,3]
diffMat = inX-dataSet

# print(diffMat)
# print(tile([1,2],2))
# print(tile([1,2],(2,2)))
# # print(tile([1,2],(2,2,2)))
# sqDiffMat = diffMat**2
# print(sqDiffMat)
# distanceSqDiffMat = sqDiffMat.sum(axis=None)
# print(distanceSqDiffMat)

print("test:")
# print(dataSet[:])
# print(dataSet[2:,1])
# print(dataSet[1])

# print(dataSet[1,:-1])
# kNN.datingClassTest()
kNN.classifyPerson()