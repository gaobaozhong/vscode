import logRegres_2018032701 as logRegres

dataArr, labelMat = logRegres.loadDataSet()
weights =  logRegres.gradAscent(dataArr,labelMat)
# print 'weights.getA():',weights.getA()
logRegres.plotBestFit(weights.getA())