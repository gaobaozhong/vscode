import trees_2018031303 as trees

dataSet, labels = trees.createDataSet()
print dataSet
print labels

print trees.calcShannonEnt(dataSet)

dataSet[0][-1] = 'tom'
print dataSet
print trees.calcShannonEnt(dataSet)

print trees.splitDataSet(dataSet,0,1)

print trees.chooseBestFeatureToSplite(dataSet)

myTree = trees.createTree(dataSet,labels)
print myTree