import svmMLiA_2018040201 as svmMLiA
from numpy import *
#dataArr,labelArr = svmMLiA.loadDataSet(r'/Users/gao/code/machinelearninginaction/Ch06/testSet.txt') 
dataArr,labelArr = svmMLiA.loadDataSet(r'D:\Users\gao\Documents\Code\machinelearninginaction\Ch06\testSet.txt') 

# print labelArr
# print (dataArr[:3])


# b,alphas = svmMLiA.smoSimple(dataArr,labelArr,0.6,0.001,40)
# print b
# print alphas

b,alphas = svmMLiA.smoP(dataArr,labelArr,0.6,0.001,40)
print b
print alphas

print shape(alphas[alphas>0])

for i in range(100):
    if alphas[i]>0.0:
        print dataArr[i],labelArr[i]

ws = svmMLiA.calcWs(alphas,dataArr,labelArr)
print ws

datMat = mat(dataArr)
for i in range(20):
    print datMat[i]*mat(ws) + b
    print labelArr[i]
    # if(datMat[i]*mat(ws))