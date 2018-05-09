import svmMLiA_2018050902 as svmMLiA
from numpy import *
dataArr, labelArr = svmMLiA.loadDataSet(
    r'D:\Users\gao\Documents\Code\machinelearninginaction\Ch06\testSet.txt')
# print labelArr[:5] # [-1.0, -1.0, 1.0, -1.0, 1.0]
# print dataArr[:5] #[[3.542485, 1.977398], [3.018896, 2.556416], [7.55151, -1.58003], [2.114999, -0.004466], [8.127113, 1.274372]]
# b, alphas = svmMLiA.somSimple(dataArr,labelArr,0.6,0.001,40)
# C = 0.6
# toler = 0.001
# maxIter = 40
# dataMatIn = dataArr[:5]
# classLabels = labelArr[:5]
# dataMatrix = mat(dataMatIn)
# # [[ 3.542485e+00  1.977398e+00]
# #  [ 3.018896e+00  2.556416e+00]
# #  [ 7.551510e+00 -1.580030e+00]
# #  [ 2.114999e+00 -4.466000e-03]
# #  [ 8.127113e+00  1.274372e+00]]
# labelMat = mat(classLabels).transpose()
# # [[-1.]
# #  [-1.]
# #  [ 1.]
# #  [-1.]
# #  [ 1.]]
# b = 0
# m,n = shape(dataMatrix)
# #5 2
# alphas = mat(zeros((m,1)))
# # [[0.]
# #  [0.]
# #  [0.]
# #  [0.]
# #  [0.]]
# iter = 0
# print dataMatrix
# print labelMat
# print m,n
# print alphas
# print multiply(
#                     alphas,labelMat
#                 ).T
# #                 [[-0.]
# #  [-0.]
# #  [0.]
# #  [-0.]
# #  [0.]]
# # [[-0. -0.  0. -0.  0.]]
# print dataMatrix[0,:]
# print dataMatrix[0,:].T
# print dataMatrix*dataMatrix[0,:].T
# # [[3.542485 1.977398]]
# # [[3.542485]
# #  [1.977398]]
# # [[16.45930283]
# #  [15.74944568]
# #  [23.62676274]
# #  [ 7.48352117]
# #  [31.31011654]]
# print multiply(alphas,labelMat).T *(dataMatrix*dataMatrix[0,:].T)
# # [[0.]]
# fXi = float(
#                 multiply(
#                     alphas,labelMat
#                 ).T
#                 *
#                 (
#                     dataMatrix*dataMatrix[0,:].T
#                 )
#             ) + b
# print fXi
# # 0.0
# Ei = fXi - float(
#                 labelMat[0]
#             )
# print float(
#                 labelMat[0]
#             )
# print Ei
# # -1.0
# # 1.0

# i =0
# Ei = fXi - float(
#                 labelMat[i]
#             )
# print( (
#         (
#             labelMat[i]*Ei < -toler
#         )
#         and
#         (
#             alphas[i] < C
#         )
#     )
#     or
#     (
#         (
#             labelMat[i]*Ei > toler
#         )
#         and
#         (
#             alphas[i] > 0
#         )
#     )
# )

# print (
#         (
#             labelMat[i]*Ei < -toler
#         )
#         and
#         (
#             alphas[i] < C
#         )
#     )
# print labelMat[i]*Ei

# b, alphas = svmMLiA.smoP(dataArr, labelArr, 0.6, 0.001, 40)
# ws = svmMLiA.calcWs(alphas,dataArr,labelArr)
# print ws

# dataMat = mat(dataArr)
# for i in range(50):
#     # print i
#     fXi =  (dataMat[i]*mat(ws)+b)
#     # print fXi
#     Yi= labelArr[i]
#     if (fXi * Yi < 0):
#         print i
#         print  fXi
#         print Yi

svmMLiA.testRbf()
