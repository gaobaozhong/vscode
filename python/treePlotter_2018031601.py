#coding:utf
import matplotlib.pyplot as plt
#2.2.2 分析数据

decisionNode = dict(
    boxstyle="sawtooth",
    fc="0.8"
    )
decisionNode2 = dict(
    boxstyle ="sawtooth",
    fc="0.8"
)
decisionNode3 = dict(
    boxstyle="sawtooth",
    fc="0.8"
)
leafNode = dict(
    boxstyle="round4",
    fc="0.8"
    )
leafNode2 = dict(
    boxstyle="round4",
    fc="0.8"
)
leafNode3 = dict(
    boxstyle="round4",
    fc="0.8"
)
arrow_args = dict(arrow_style="<-")
arrow_args2 = dict(arrow_style="<-")
arrow_args3 = dict(arrow_style="<-")

def plotNode(nodeTxt,centerPt,parentPt,nodeType):
    createPlot.ax1.annotate(
        nodeTxt,
        xy=parentPt,
        xycoords='axes fraction',
        xytext = centerPt,
        textcoords='axes fraction',
        va='center',
        ha='center',
        bbox=nodeType,
        arrowprops=arrow_args
        )
def plotNode2(nodeTxt,centerPt,parentPt,nodeType):
    createPlot2.ax1.annotate(
        nodeTxt,
        xy=parentPt,
        xycoords="axes fraction",
        xytext=centerPt,
        textcoords='axes fraction',
        va='center',
        ha='center',
        bbox=nodeType,
        arrowpros=arrow_args
    )
def plotNode3(nodeTxt,centerPt,parentPt,nodeType):
    createPlot3.ax1.annotate(
        nodeTxt,
        xy=parentPt,
        xycoords="axes fraction",
        va='center',
        ha='center',
        bbox=nodeType,
        arrowprops = arrow_args
    )

def createPlot():
    flg = plt.figure(1,facecolor='white')
    flg.clf()
    createPlot.ax1 = plt.subplot(111,frameon=False)
    plotNode(
        'dicision node',
        (0.5,0.1),
        (0.1,0.5),
        decisionNode
        )
    plotNode(
        'leaf node',
        (0.8,0.1),
        (0.3,0.8),
        leafNode
    )
    plt.show()
          
def createPlot2():
    flg = plt.figure(1,facecolor="white")
    flg.clf()
    createPlot.ax1 = plt.subplot(111,frameon=False)
    plotNode(
        'dicision node',
        (0.5,0.1),
        (0.1,0.5),
        decisonNode
    )
    plotNode(
        'leaf node',
        (0.8,0.1),
        (0.3,0.8),
        leafNode

    )
    plt.show()

def createPlot3():
    flg = plt.figure(1,facecolor="white")
    flg.clf()
    createPlot.ax1 = plt.subplot(111,frameon=False)
    plotNode(
        'dicision node',
        (0.5,0.1),
        (0.1,0.5),
        decisionNode
    ) 
    plotNode(
        'leaf node',
        (0.8,0.1),
        (0.3,0.8),
        leafNode
    )
decisionNode1 = dict(
    boxstyle = "sawtooth",
    fc = "0.8"
)

leafNode1 = dict(
    boxstyle = "round4",
    fc = "0.8"
)

arrow_args1 = dict(
    arrowstyle="<-"
)

def plotNode1(
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
        va='center',
        ha='center',
        bbox=nodeType,
        arrowprops=arrow_args1
    )
    
def createPlot1():
    fig = plt.figure(1,facecolor='white')
    fig.clf()
    createPlot.ax1 = plt.subplot(111,frameon=False)
    plotNode1(
        'decision node',
        (0.5,0.1),
        (0.1,0.5),
        decisionNode1
    )
    plotNode1(
        'leaf node',
        (0.8,0.1),
        (0.3,0.8),
        leafNode1
    )
    plt.show()

