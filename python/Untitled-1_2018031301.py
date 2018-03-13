import trees_2018031301 as trees

myDat, labels = trees.createDataSet()

print trees.calcShannonEnt(myDat)

myDat[0][-1] = 'maybe'
print trees.calcShannonEnt(myDat)

