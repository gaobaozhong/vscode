
from numpy import *
filename='C:\Users\gao\Documents\code\python\datingTestSet2_20180308.txt'
print filename
fr = open(filename)
print fr
arrayOLines=fr.readlines()#先得到每一行，
print arrayOLines[0]
numberOfLines = len(arrayOLines)#然后呢？看了一下，好的树木，
print numberOfLines
returnMat=zeros((numberOfLines,3))
print returnMat
classLabelVector=[]
index=0
for line in arrayOLines:#曲美一行
    line = line.strip()#网行的空格去掉
    print line
    listFromLine = line.split('\t')#按照那个淘宝店，然后把所有的行，然后转换成一个列表
    print listFromLine
    returnMat[index,:]=listFromLine[0:3]#得到一个矩阵，这个矩阵，
    print returnMat[index,:]
    print index
    classLabelVector.append(int(listFromLine[-1]))
    print listFromLine[-1]
    index+=1

