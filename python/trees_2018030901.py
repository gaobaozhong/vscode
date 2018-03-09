#coding:utf
from math import log

def calcShannonEnt(dataSet):#既然相同的伤，
    numEntries = len(dataSet)#首先呢，取消那个模式以及的个数
    labelCounts = {}#嗯，再记录一下，嗯，的歌曲，
    for featVec in dataSet:#然后，起初，每一个行勒，
        currentLabel = featVec[-1]#然后起行最后一个元素，当然这就是累了
        if currentLabel not in labelCounts.keys():#然后我们去，然后从我们的内中看一下，当前的这个剧集，就是专业是一条墓道的内衣，是不是在我们的类别中？
            labelCounts[currentLabel]=0#如果不在的话，我们就创建一个，你在图书馆吗？怎么才能去图书馆？昨晚出去花钱吗？可不可以带自己的书进去？
        labelCounts[currentLabel]+=1#然后接下来再给你别家一号，
    shannonEnt = 0.0#然后呢？给你一个小的，确定一下锡纸，初始化一下，
    for key in labelCounts:#哦，然后去看一下类，
        prob = float(labelCounts[key])/numEntries#然后每一个内侄，除以所有的数，一，我这周上的课更好我啊你？在你，的啊，的，我，而，的，你我，
        shannonEnt -= prob*log(prob,2)
    return shannonEnt

def createDataSet():
    dataSet = [
        [1,1,'yes'],
        [1,0,'no'],
        [0,1,'no'],
        [0,1,'no']
    ]
    labels = ['no surfacing','flippers']
    return dataSet, labels


