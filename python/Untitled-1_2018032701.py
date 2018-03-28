import logRegres_2018032701 as logRegres
from numpy import *

data_Arr, label_Mat = logRegres.loadDataSet()
weights =  logRegres.stocGradAscent1(array(data_Arr),label_Mat)
# print 'weights.getA():',weights.getA()
logRegres.plotBestFit(weights)
