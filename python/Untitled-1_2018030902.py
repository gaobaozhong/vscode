#coding:utf
import trees_2018030901 as trees
reload(trees)
myDat,labels = trees.createDataSet()
print myDat
print trees.calcShannonEnt(myDat)
myDat[1][-1]='maybe'
print myDat
print trees.calcShannonEnt(myDat)