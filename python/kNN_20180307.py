#coding:utf
#这是一个实验，关于使用排山倒海数据的，这个数据线文件是第17页，世纪学习实战的身体是企业的一个例子，这里怎么打也打不变，我希望自己能从这个例子中好好学习一下，把我给你吃药不能长时间的事，我想今晚上，他们早上起来一定会做这个事情，这是音标练习的骄傲，最近邻算法大概的意思就是说我通过一些数据有没有出处？两个数的距离，然后得看看自己是不是极品，然后去前几个，然后就前几个的几个基本上就是，你说你可以随时监听，那你就是那种离别了多种方式来得到那边，第一个函数的话呢，这是，来源显示，几个。点，还有它们的类别，创建一个函数，就还是我都没想到，原来通过这个方式跟小孩说，

from numpy import *
import operator#这个运算符，这个算法在执行排序操作时，将使用这个模块提供的函数，后面将进一步介绍，
#为了方便使用这个函数，我们创建了数据集合，标签，然后那一次执行以下步骤，保存文件，改变当前路径到存储文件的位置，打开这个开发环境，无论什么时候系统做，打开终端，用命令提示符，完了你上手操作，只要我们默认安装好的东西，然后输出输入相应的命令的时候，就可以进入开发环境，然后呢我们按照下列命令导入上面程序的，模块，看来这个文件要背别的引用，
def createDataSet():
    group = array(#只要注意这个地方列表是小写，
        [
            [
                1.0,
                1.1
            ],
            [
                1.0,
                1.0
            ],
            [0,0],
            [0,0.1]
        ]
    )#注意这个地方可能出错了，少了一个中国号，也就是说里面做的数据,不是一个数组，
    labels = ['A','A','B','B']
    return group, labels

def classify0(inX,dataSet,labels,k):#这个函数有四个输入参数，用于分类的树下两只，第一个，我去年样本集，第三个是标签向量，最后的参数表是用于选择最近邻居的数目，其中标签向量的元素，数目和取证的行数相同，程序使用的是否是距离公式，计算两个向量点之间的距离，就是所谓的，平方和，在，平方根，计算完所有点之间的距离之后呢，可以对数据按照从小到大的次序排序，然后呢确定前，开个距离，最小元素所在的主要分类，输入看总是正整数，最后将，我们得到的，立即数字点分解为援助列表，然后使用程序第二行导入的运算符模块的，按照第二个元素的次序对元素进行排序，财富的排序应该为女婿就按照由大到小的次序排序，最后返回发生频率最高的元素标签，你的预测数据所在的分类，我们可以在提示符中输入下面的命令，就直接掉这个函数，就可以了，输入的，原宿的话呢，它就是一个，因为我们现在的数据即是二维的，也就是每一句正中的美好是两个元素，这两个元素，那我们输入的这个，数字也是两个元素就可以了，我们可以尝试的，来输入一些值，还需练一下大概效果如何？
    dataSetSize = dataSet.shape[0]#这个地方得到数据集的大小，世界的大小是什么呢？这个是个矩阵和矩阵，是一个4×2的矩阵，也就是说她有，四行两列，它的形状的应该是4号两列，这里，他取了第一个参数是零，就表示这里应该是得到，第一个数就是四，就是依据大小这样，就是说这个有多少个条目了？
    diffMat = tile(inX,(dataSetSize,1)) -dataSet#这个地方比较复杂，哦，首先他用了一个太好了太好的话难受来做矩阵的，怎么做决定呢？他说他可以把那个，我们的，就是一行数据啊重复多少次，将生成一个矩阵，到了第一个，就是你的银行是什么？这里他用的第一个参数，就是那一行，第二个参数的话，那就是表示他要重复多少次？他说多少次了？在这里，那个有两个参数，第一个参数呢这里太有意思了，这个就是好的意思了吧？d2366212，这个什么意思不太懂，这里可能是只得，嗯各位参考为嘛，还说是这样子吗？也可能是这样子，他家来的话他创业好，这个这个重复四次的一个矩阵之后，然后他又剪了一下之前的那个数据集，这之前的矩阵加一减的话，那就表示是什么呢？就是那个数据差了，数据的差异，哦，我明白了，原来这个地方是这样子啊，你有没有街上所有的就是这个，所有的每一个数据条目，和我们对应点的，我们新的那个新的让利点的差，因此的话我们就把那个新的压力点，然后变成一个大姐姐，这几天就是重复多少次，你多少个条目，然后就有多少行，初步得出多少次？是每个矩阵，然后接下来的话就可以实现，然后，求插在出品方，在触屏方便，掉就可以了，然后再排序就行了，
    sqDiffMat = diffMat**2#这个就是，矩阵求，平方矩阵的平方，这里的应该是矩阵的平方，因为我们的这个编程语言支持这个矩阵的平方运算，虽然他这种人把所有的矩阵的元素多平方，我们这个已经是绝症的，差的，这里是绝对的，差的平方，
    sqDistances = sqDiffMat.sum(axis=1)#这个地方也很容易解释了，那就是，那个，主动一点是周敦颐的话，这里应该是，行，你美好，然后呢这里用了一个单排数，就是求和，每行求和，这里因为刚才已经得到那个差的平方了，然后在，求和，这里这个参数，周，等于。这个表是按号，来求和，然后呢如果他对您的话呢要是暗恋求和，在这里的就没有意义了，
    distances = sqDistances**0.5#这个就是那个距离了，有了那个方根就得到距离了，转到任何一个点，他们距离是多少？这样我就得到那个，一个，新的，集镇，
    sortedDistIndicies = distances.argsort()#它的距离是多少了？我们继续，然后呢？听培训，招牌，去得到一个新的一个，就是列表，类型，这礼拜内行的话呢，它掉了这个函数就是，按照那个，就是这个，它的大小，然后去一个序号，
    classCount = {}#这里就是进行类别技术了，
    for i in range(k):#这里能是循环多少次？这里注意是从零开始的，领导k减一，
        voteIlabel = labels[sortedDistIndicies[i]]#这个就是，得到一下我们那个对应的类别的值，
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1#这个地方是，根据我们，类别的值，然后呢，来，忠诚相应的，技术，是每种类别，这里加一，
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)#根据上面的雪花已经得到那个类别有多少个？这么一个。列表了，我们在通过这个，烧退了，还说，然后，把这个整个，列表，进行一个排序，恩爱到逆水进行排序，他使用的是，对函数中又能，三个参数，这三个参数的第一个，是使用的，就是我们要排序的数据，这里面这个数据返回一个，循环的一个数据集，在这里呢，它掉了内部的一个叫一点一tm这个函数，注意好这个函数，所以，刘家小哥号，
    return sortedClassCount[0][0]#好最后了，然后我们打牌，我去的第一个数，他的支取出来，就可以了，它的类别是。什么？就是什么了？

def file2matrix(filename):#首先我们要知道我们本文件包含哪些额多少号得到文件的行数然后创建以零填充的矩阵，实际上这个是一个二维数组，但不可以弄出，为了简化处理，我们将去另一个维度的设置为固定值，然后按照自己的实际需要，增加相应的代码，以适应变化的输入值，循环处理文件中的每行数据，首先得根据函数，也许到所有的回车制服，然后使用碳粉，这不出来，加上不得到整行数据分成四类表，然后我们先去前三元素，将不清楚到特殊九点钟去，然后呢这个圆可以用索引值来表示最后一行元素，利用这种富有，所以我们可以方便的将列表中最后一列存储到项链中，就是我们必须明确通知解释器告诉他，600路车的颜色为整型，否则颜色会把原色的姿态处理完毕，把自己处理的元素与哲学比较简单的数据库来处理处理，
    fr = open(filename)
    arrayOLines=fr.readlines()#先得到每一行，
    numberOfLines = len(arrayOLines)#然后呢？看了一下，好的树木，
    returnMat=zeros((numberOfLines,3))
    classLabelVector=[]
    index=0
    for line in arrayOLines:#曲美一行
        line = line.strip()#网行的空格去掉
        listFromLine = line.split('\t')#按照那个淘宝店，然后把所有的行，然后转换成一个列表,我没想到这个地方会出错，就是说这个，谁敢替这个斜杠，它有两种，一种是写了一本反斜杠，其实我现在也分不清楚什么叫刺激，什么叫反斜杠，谁能告诉我什么叫什么叫反斜杠，谁能告诉我，对，是的，如果他是学长的话呢，他表示就是这是一个符号，如果是的话，那可是一个，好像什么都不表示啊，这个在我们这里还没什么意义，还有意义吗？
        returnMat[index,:]=listFromLine[0:3]#得到一个矩阵，这个矩阵，
        classLabelVector.append(int(listFromLine[-1]))
        index+=1
    return returnMat,classLabelVector

def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals -minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals,(m,1))
    normDataSet = normDataSet/tile(ranges,(m,1))
    return normDataSet,ranges,minVals

def datingClassTest():#这是一个测试数据的，
    hoRatio = 0.10#首先定义了一个范围，10%了，
    datingDataMat,datingLabels = file2matrix("C:\Users\gao\Documents\code\python\datingTestSet2_20180308.txt")#这是设置数据，
    normMat,ranges,minVals = autoNorm(datingDataMat) #这个是得到规划之后的数据，
    m = normMat.shape[0]#这个是取样本个数，
    numTestVecs = int(m*hoRatio)#这个是得到那个测试样本个数，
    errorCount = 0.0#这是技术不错的技术
    for i in range(numTestVecs):#开始循环，每个样本都要测一遍，
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)#这个开始做费力气了，然后把每个样本，和这是把这个测试卷中的每个样本，我记得好像是几个参数的，第一个参数肯定是那个是x表示那个我们测试样对，是的我们的属性，然后第三个是类别，第四个就是我们最后我们取得钱多少个的数，本，第二个就是我们的
        print "the classifier cam eback with : %d, the readl anssdf ix : %d " % (classifierResult, datingLabels[i])#日打印，
        if(classifierResult!=datingLabels[i]):#这个是我们之前的结果，如果不是的话呢，就出错率加一，
            errorCount += 1.0
    print "the total error rae is : %f"%(errorCount/float(numTestVecs))

def classifyPerson():
    resultList = ['not at all','in small doese','in large doses']
    percentTats = float(raw_input("percentage of time spendt playing videogames?"))
    ffMiles = float(raw_input("frequent flier miles earned per year?"))
    iceCreame = float(raw_input("liters of ice cream consumed per year?"))
    datingDataMat, datingLabels = file2matrix('C:\Users\gao\Documents\code\python\datingTestSet2_20180308.txt')
    normMat,ranges,minVals=autoNorm(datingDataMat)
    inArr = array([ffMiles,percentTats,iceCream])
    classifierResult = classify0((inArr-minVals)/ranges,normMat,datingLabels,3)
    print "you  will probably like this person:",resultList[classifierResult-1]