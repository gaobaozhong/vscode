import logRegres_2018032701 as logRegres

dataArr, labelMat = logRegres.loadDataSet()
print logRegres.gradAscent(dataArr,labelMat)
