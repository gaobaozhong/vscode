import svmMLiA_2018032701 as svmMLiA
from numpy import *
dataArr,labelArr = svmMLiA.loadDataSet(r'/Users/gao/code/machinelearninginaction/Ch06/testSet.txt') 

print (labelArr)
print (dataArr[:3])

b,alphas = svmMLiA.smoP(dataArr,labelArr,0.6,0.001,40)
ws = svmMLiA.calcWs(alphas,dataArr,labelArr)
print ws

datMat = mat(dataArr)
for i in range(20):
    print datMat[i]*mat(ws) + b
    print labelArr[i]