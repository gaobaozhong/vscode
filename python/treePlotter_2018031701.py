# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 11:19:43 2018

@author: gao
"""

#coding:utf

import matplotlib.pyplot as plt

decisionNode = dict(boxstyle="sawtooth",fc="0.8")
leafNode= dict(boxstyle="round4",fc="0.8")
arrow_args= dict(arrowstyle="<-")

def plotNode(
    nodeTxt,
    centerPt,
    parentPt,
    nodeType
    ):
    createPlot.ax1.annotate(
        nodeTxt,
        xy=parentPt,
        xycoords='axes fraction',
        xytext=centerPt,
        textcoords='axes fraction',
        va="center",
        ha="center",
        bbox=nodeType,
        arrowprops=arrow_args
    )

def createPlot():
    fig = plt.figure(1,facecolor='white')
    fig.clf()
    createPlot.ax1=plt.subplot((111))
    plotNode('decision node',(0.5,0.1),(0.1,0.5),decisionNode)
    plotNode('leaf node',(0.8,0.1),(0.3,0.8),leafNode)
    plt.show()

def getNumLeafs(myTree):
    numLeafs = 0
    firstStr = myTree.keys()[0]
    secondDict=myTree[firstStr]
    for key in secondDict.keys():
        if(type(secondDict[key]).__name__=='dict'):
            numLeafs += getNumLeafs(secondDict[key])
        else: numLeafs+=1
    return numLeafs  

def getNumLeafs1(myTree):
    numLeafs = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if(type(secondDict[key]).__name__=='dict'):
            numLeafs += getNumLeafs1(secondDict[key])
        else: numLeafs+=1
    return numLeafs

def getNumLeafs2(myTree):
    numLeafs = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if(type(secondDict[key]).__name__=='dict'):
            numLeafs += getNumLeafs2(secondDict[key])
        else:numLeafs+=1
    return numLeafs

def getNumLeafs3(myTree):
    numLeafs = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if(type(secondDict[key]).__name__=='dict'):
            numLeafs += getNumLeafs3(secondDict[key])
        else: numLeafs +=1
    return numLeafs

def getNumLeafs4(myTree):
    numLeafs = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if(type(secondDict[key]).__name__=='dict'):
            numLeafs += getNumLeafs4(secondDict[key])
        else:numLeafs+=1
    return numLeafs


def getTreeDepth(myTree):
    maxDepth =0
    firstStr = myTree.keys()[0]
    secondDict  = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':
            thisDepth =1 + getTreeDepth(secondDict[key])
        else: thisDepth = 1
        if thisDepth > maxDepth:
            maxDepth = thisDepth
    return maxDepth

def getTreeDepth1(myTree):
    maxDepth = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            thisDepth = 1+ getTreeDepth1(secondDict[key])
        else: thisDepth = 1
        if thisDepth > maxDepth:
            maxDepth = thisDepth
    return maxDepth

def getTreeDepth2(myTree):
    maxDepth = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            thisDepth = 1+getTreeDepth2(secondDict[key])
        else: thisDepth = 1
        if thisDepth > maxDepth:
            maxDepth = thisDepth
    return maxDepth


def retrieveTree(i):
    listOfTrees = [
        {
            'no surfacing':{
                0:'no',
                1:{
                    'flippers':{
                        0:'no',
                        1:'yes'
                    }
                }
            }
        },
        {
            'no surfacing':{
                0:'no',
                1:{
                    'flippers':{
                        0:{
                            'head':{
                                0:'no',
                                1:'yes'
                            }
                        },
                        1:'no'
                    }
                }
            }   
        }

    ]
    return listOfTrees[i]

#3-7
def plotMidText(
    cntrPt,
    parentPt,
    txtString
    ):
    xMid = (parentPt[0]-cntrPt[0])/2.0 + cntrPt[0]
    yMid =(parentPt[1]-cntrPt[1])/2.0+cntrPt[1]
    createPlot.ax1.text(xMid,yMid,txtString)

def plotMidText1( cntrPt,parentPt,txtString):
    xMid = (parentPt[0]-cntrPt[0])/2.0+cntrPt[0]
    yMid = (parentPt[1]-cntrPt[1])/2.0+cntrPt[1]
    createPlot.ax1.text(xMid,yMid,txtString)

def plotMidText2(cntrPt,parentPt,txtString):
    xMid = (parentPt[0]-cntrPt[0])/2.0+cntrPt[0]
    yMid = (parentPt[1]-cntrPt[1])/2.0+cntrPt[1]
    createPlot.ax1.text(xMid,yMid,txtString)

def plotTree1(
    myTree,
    parentPt,
    nodeTxt
    ):
    numLeafs = getNumLeafs(myTree)
    depth = getTreeDepth(myTree)
    firstStr = myTree.keys()[0]
    cntrPt = (plotTree1.xOff + (1.0 + float(numLeafs))/2.0/plotTree1.totalW,plotTree1.yOff)
    plotMidText(cntrPt,parentPt,nodeTxt)
    plotNode(firstStr,cntrPt,parentPt,decisionNode)
    secondDict = myTree[firstStr]
    plotTree1.yOff = plotTree1.yOff - 1.0/plotTree1.totalD
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':
            plotTree1(secondDict[key],cntrPt,str(key))
        else:
            plotTree1.xOff = plotTree1.xOff + 1.0/plotTree1.totalW
            plotNode(secondDict[key],(plotTree1.xOff,plotTree1.yOff),cntrPt,leafNode)
            plotMidText((plotTree1.xOff,plotTree1.yOff),cntrPt,str(key))
    plotTree1.yOff =  plotTree1.yOff +1.0/plotTree1.totalD

def plotTree2(myTree,parentPt,nodeTxt):
    numLeafs = getNumLeafs(myTree)
    depth = getTreeDepth(myTree)
    firstStr = myTree.keys()[0]
    cntrPt = (plotTree2.xOff+(1.0+float(numLeafs))/2.0/plotTree2.totalW,plotTree2.yOff)
    plotMidText(cntrPt,parentPt,nodeTxt)
    plotNode(firstStr, cntrPt,parentPt,decisionNode)
    secondDict = myTree[firstStr]
    plottree2.yOff = plotTree2.yOff -1.0/plotTree2.totalD
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':
            plotTree2(secondDict[key],cntrPt,str(key))
        else:
            plotTree2.xOff = plotTree2.xOff + 1.0/plotTree2.totalW
            plotNode(secondDict[key],(plotTree2.xOff,plotTree2.yOff),cntrPt,leafNode)
            plotMidText((plotTree2.xOff,plotTree2.yOff),cntrPt,str(key))
    plotTree2.yOff = plotTree2.yOff +1.0/plotTree2.totalD
            

def createPlot1(inTree):
    fig = plt.figure(1,facecolor='white')
    fig.clf()
    axprops = dict(xticks = [],yticks = [])
    createPlot.ax1 = plt.subplot(111,**axprops)
    plotTree1.totalW = float(getNumLeafs(inTree))
    plotTree1.totalD = float(getTreeDepth(inTree))
    plotTree1.xOff = -0.5/plotTree1.totalW
    plotTree1.yOff = 1.0
    plotTree1(inTree,(0.5,1.0),'')
    plt.show()

def createPlot2(inTree):
    fig = plt.figure(1,facecolor = 'white' )
    fig.clf()
    axprops = dict(xticks = [],yticks=[])
    createPlot.ax1 = plt.subplot(111,**axprops)
    plotTree2.totalW = float(getNumLeafs(inTree))
    plotTree2.totalD = float(getTreeDepth(inTree))
    plotTree2.xOff = -0.5/plotTree2.totalW
    plotMidText2.yOff = 1.0
    plotTree2(inTree,(0.5,1.0),'')
    plt.show()