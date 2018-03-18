import treePlotter_2018031701 as treePlotter

myTree = treePlotter.retrieveTree(1)
print treePlotter.getNumLeafs(myTree)
print treePlotter.getTreeDepth(myTree)
print myTree
treePlotter.createPlot1(myTree)
myTree['no surfacing'][3]='maybe'
treePlotter.createPlot1(myTree)