import svmMLiA_2018033001 as svmMLiA
from numpy import *
#dataArr,labelArr = svmMLiA.loadDataSet(r'/Users/gao/code/machinelearninginaction/Ch06/testSet.txt') 
dataArr,labelArr = svmMLiA.loadDataSet(r'D:\Users\gao\Documents\Code\machinelearninginaction\Ch06\testSet.txt') 

print labelArr
print (dataArr[:3])


b,alphas = svmMLiA.smoSimple(dataArr,labelArr,0.6,0.001,4)
# ws = svmMLiA.calcWs(alphas,dataArr,labelArr)llllllllllllll
# print ws

# datMat = mat(dataArr)
# for i in range(20):
#     print datMat[i]*mat(ws) + b
#     print labelArr[i]