# coding:utf

# # 第六章 支持向量机

# * 简单介绍支持向量机
# * 利用SMO进行优化
# * 利用核函数进行优化
# * 将SVM和其他分类器进行对比

#  ### SVM是最好的分类器。

# ## 6.1 基于间隔分隔数据

# * 线性可分: linearly separable
# * 分隔超平面：separating hyperplane. 可以写为：WTX+b的形式
# * 分隔: margin。到分隔超平面的距离。可以些微：WTX+b/w
# * 支持向量：support vector。就是到分隔超平面的最近点。

# ## 6.2 寻找最大间隔

# ### 6.2.1 分类器分解的优化问题

# * label是+1或者-1，label*(wTx+b)就永远是正的，而且>=1。
# * 松弛变量: slack variable。
# * 朗格朗日乘子:如果有约束条件，可有将约束条件作为一个参数合为一个公式，

# ### 6.2.2 SVM的一般框架

# ## 6.3 SMO高校优化算法

# * 二次规划求解工具: quadratic solver。在一种线性约束下的多个变量的二次目标函数。一旦得到alpha的值，就可以求得wtx+b。

# ### 6.3.1 Plattde SMO算法

# * 1996年John Platt提出了SMO:Sequential Minimal Optimization. 将大优化问题，分解为个小优化问题，与他们作为整体求解的结果是一样的。时间短很多。求出一系列的alpha和b。
# * SMO的工作原理：每次循环中选择两个aplha进行优化处理。 一旦找到一堆适合的alpha，那么就增大一个，减少另一个。这里所谓的“合适”，就是两个alpha必须在分割边界之外，并且没有进行过区间处理或者不在边界上。

# ### 6.3.2 应用简化版SMO算法处理小规模数据集

# * Plant SMO要找最佳的alpha对，简化版，是遍历一个alpha，在剩下的alpha集合中，随机找另一个alpha。

from numpy import *


# 6-1
# load data set
def loadDataSet(filename):
    dataMat = []
    labelMat = []
    fr = open(filename)
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        dataMat.append([float(lineArr[0]), float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat, labelMat


# select a random ,which is not i, and is in range(0,m)
def selectJrand(i, m):
    j = i
    while (j == i):
        j = int(random.uniform(0, m))
    return j


# change L<=aj<=H
def clipAlpha(aj, H, L):
    if aj > H:
        aj = H
    if L > aj:
        aj = L
    return aj


# 这个函数比较大，是目前本书中最大的函数。
# 有五个参数，分别是，数据集，类别标签，常数C，容错率，和退出前最大的循环次数


def smoSimple(dataMatIn, classLabel, C, toler, maxIter):
    # 在本书中，我们构建函数是采用了通用的接口，这样就可以对算法和数据源进行组合或配对处理。
    # 上述函数将多个列表和输入参数转换为Numpy矩阵，遮掩提供就可以简化很多数学处理操作，由于转置了类别标签，以后那次我们的得到就是一个列向量而不是一个列表。
    # 于是类别标签相连的每行月还俗和数据矩阵中的行一一对应。
    dataMatrix = mat(dataMatIn)
    # !!!
    # bug:
    # labelMat = mat(classLabel).transpose()。同样的错误我犯了两次。transpose（）。我忘记了。。。这就是让labelMat变成了一个1*m的向量。而我需要的是m*1向量。调bug好痛苦啊！
    # !!!
    labelMat = mat(classLabel).transpose()
    b = 0
    # 我们可以通过矩阵dataMatIn的shape属性得到常数m和n。
    m, n = shape(dataMatrix)
    # 最后我们可以构建一个alpha列矩阵，矩阵中的元素都初始化为0.
    print m
    alphas = mat(zeros((m, 1)))
    # 并建立一个iter变量。该变量存储的则是在么有任何alpha改变的情况下便利数据集的次数。
    iter = 0

    # 当该变量达到输入值maxIter时，函数结束运行并退出
    while (iter < maxIter):
        # 每次循环当中，将alpahpairschanged设为0 ，变量apphaPairschanged用于记录appha是否已经进行优化。当然，在循环结束是就会得知这一点，
        alphaPairsChanged = 0
        # 然后在对整个集合顺序遍历。
        for i in range(m):
            # 首先fxi能计算出来，这就是我们预测的类别。
            # print 'i: ', i
            # print 'alphas:', alphas
            # print 'multiply(alphas,labelMat)', multiply(alphas, labelMat)
            # print 'multiply(alphas,labelMat).T', multiply(alphas, labelMat).T
            # print 'dataMatrix[i,:]', dataMatrix[i, :]
            # print 'dataMatrix[i,:].T', dataMatrix[i, :].T
            # print 'multiply(alphas, labelMat).T', multiply(alphas, labelMat).T
            # print 'dataMatrix* dataMatrix[i,:].T', dataMatrix * dataMatrix[
            #     i, :].T
            # print 'multiply(alphas, labelMat).T * (dataMatrix * dataMatrix[i, :].T)', multiply(
            #     alphas, labelMat).T * (dataMatrix * dataMatrix[i, :].T)
            # print 'float(multiply(alphas, labelMat).T * (dataMatrix * dataMatrix[i, :].T)):', float(
                # multiply(alphas, labelMat).T *
                # (dataMatrix * dataMatrix[i, :].T))
            fXi = float(
                multiply(alphas, labelMat).T *
                (dataMatrix * dataMatrix[i, :].T)) + b
            # 然后，基于这个实例的预测结果和真实值结果的对比，就可以计算误差Ei。
            Ei = fXi - float(labelMat[i])
            # 如果为误差很大，那么可以对该数据实例所对应的alpha进行优化。对该条件的测试处于上述清单的1处。在if语句中，不管正间隔还是副间隔都会被测试。 并且在该if语句中，也要同时检查alpah，以保证其不能等于0或者C。 后面alpah小于0或者大于C是将被调整为0或者C，所以一旦在该if语句中他们等于这两个值的话，那么他们就已经在“边界”上了。因此不能够减小或者增大，因此也就不值得对他们进行优化了。
            if ((labelMat[i] * Ei < -toler) and
                (alphas[i] < C)) or ((labelMat[i] * Ei > toler) and
                                     (alphas[i] > 0)):
                # 接下来，可以利用程序清单6-1中的辅助函数来随机选择第二个alpha值，alpha[j]，
                j = selectJrand(i, m)
                # 同样，可以采用第一个alpha值，alpha[i]的误差计算方法，来计算这个alpha的误差，这个过程可以通过copy（）的方法来实现，一次你稍后可以将新的alpha只和老的alpha只进行比较。python则会通过引用的方式来传递所有的列表，必须明确的告知python要alphaIold和alphaJold分配新的内存，否则的话，在对新值和旧值进行比较时，我们就看不到新旧值的变化。
                fXj = float(
                    multiply(alphas, labelMat).T *
                    (dataMatrix * dataMatrix[j, :].T)) + b
                Ej = fXj - float(labelMat[j])
                alphaIold = alphas[i].copy()
                alphaJold = alphas[j].copy()
                #L和H，用于将alpha[j]调整到0和C之间。 如果L和H相等，就不做任何改变， 直接执行continue语句。在python中，则意味着本次循环结束直接运行下一次for的循环。
                if (labelMat[i] != labelMat[j]):
                    L = max(0, alphas[j] - alphas[i])
                    H = min(C, C + alphas[j] - alphas[i])
                else:
                    L = max(0, alphas[j] + alphas[i] - C)
                    H = min(C, alphas[j] + alphas[i])
                if L == H:
                    print "L == H"
                    continue
                # eta是alpha[j]的最有修改量，在那个很长的计算代码行中得到。。如果eta为0，那就是说需要退出for循环的当前迭代过程。 该过程对真实smo算法进行了简化处理。如果eta为0，那么计算机新的alpha[j]就比较麻烦了，这里我们就不对此进行详细的介绍了。有需要的可以自己查阅文献。现实中这种情况并不常发生，因此忽略这一部分通常也可以。于是我们计算出一个新的alpha[j]然后利用程序清单6-1中的辅助函数，以及L和H值进行调整
                eta = 2.0 * dataMatrix[i, :] * dataMatrix[j, :].T - dataMatrix[i, :] * dataMatrix[i, :].T - dataMatrix[j, :] * dataMatrix[j, :].T
                if eta >= 0:
                    print "eta>=0"
                    continue
                alphas[j] -= labelMat[j] * (Ei - Ej) / eta
                alphas[j] = clipAlpha(alphas[j], H, L)
                # 然后就是检查alpha[j]是否有轻微改变，如果是的话，就退出for循环。
                if (abs(alphas[j] - alphaJold) < 0.0001):
                    print "j not moving enough"
                    continue
                #然后，alpha[i]和alpha[j]同样进行改变，虽然改变的大小一样，但是改变的方向正好想法
                # ，如果一个增加，来那么另外一个减少。在对alpha[i]和alpha[j]进行改变之后，给这两值设置一个常数项b
                alphas[i] += labelMat[j] * labelMat[i] * (
                    alphaJold - alphas[j])
                b1 = b - Ei - labelMat[i] * (
                    alphas[i] - alphaIold
                ) * dataMatrix[i, :] * dataMatrix[i, :].T - labelMat[j] * (
                    alphas[j] - alphaJold
                ) * dataMatrix[i, :] * dataMatrix[j, :].T
                b2 = b - Ej - labelMat[i] * (
                    alphas[i] - alphaIold
                ) * dataMatrix[i, :] * dataMatrix[j, :].T - labelMat[j] * (
                    alphas[j] - alphaJold
                ) * dataMatrix[j, :] * dataMatrix[j, :].T
                if (0 < alphas[i]) and (C > alphas[i]):
                    b = b1
                elif (0 < alphas[j]) and (C > alphas[j]):
                    b = b2
                else:
                    b = (b1 + b2) / 2.0
                alphaPairsChanged += 1
                print " iter:  %d i: %d, parirs chagedc %d " % (
                    iter, i, alphaPairsChanged)
        # 最后，在优化过程结束的同事，必须䧁在合适的实际结束训话如果程序执行到forUN互动呢在以后一行都不行coninu鳄鱼局，那么就已经成功地改版了一堆alpha，同事可以alphapaireshced的值。鞭阿紫for黄菡之外需要检查alpha值是否已经做了更新，如果有跟新iter设为0后继续运行程序，只有在所有数据集便利maxiter词，之后，并且不再发生任何alpha修改的时候，郑旭才会停止并退出while虚汗。
        if (alphaPairsChanged == 0):
            iter += 1
        else:
            iter = 0
        print "iteration numberr: %d " % iter
    return b, alphas


class optStruct:
    def __init__(self, dataMatIn, classLabels, C, toler):
        self.X = dataMatIn
        self.labelMat = classLabels
        self.C = C
        self.tol = toler
        self.m = shape(dataMatIn)[0]
        self.alphas = mat(zeros((self.m, 1)))
        self.b = 0
        self.eCache = mat(zeros((self.m, 2)))


def calcEk(oS, k):
    fXk = float(multiply(oS.alphas, oS.labelMat).T *
                (oS.X * oS.X[k, :].T)) + oS.b
    Ek = fXk - float(oS.labelMat[k])
    return Ek


def selectJ(i, oS, Ei):
    maxK = -1
    maxDeltaE = 0
    Ej = 0
    oS.eCache[i] = [1, Ei]
    validEcacheList = nonzero(oS.eCache[:, 0].A)[0]
    if (len(validEcacheList)) > 1:
        for k in validEcacheList:
            if k == i:
                continue
            Ek = calcEk(oS, k)
            deltaE = abs(Ei - Ek)
            if (deltaE > maxDeltaE):
                maxK = k
                maxDeltaE = deltaE
                Ej = Ek
        return maxK, Ej
    else:
        j = selectJrand(i, oS.m)
        Ej = calcEk(oS, j)
    return j, Ej


def updateEk(oS, k):
    Ek = calcEk(oS, k)
    oS.eCache[k] = [1, Ek]


# 6-4


def innerL(i, oS):
    Ei = calcEk(oS, i)
    if ((oS.labelMat[i] * Ei < -oS.tol) and
        (oS.alphas[i] < oS.C)) or ((oS.labelMat[i] * Ei > oS.tol) and
                                   (oS.alphas[i] > 0)):
        j, Ej = selectJ(i, oS, Ei)
        alphaIold = oS.alphas[i].copy()
        alphaJold = oS.alphas[j].copy()
        if (oS.labelMat[i] != oS.labelMat[j]):
            L = max(0, oS.alphas[j] - oS.alphas[i])
            H = min(oS.C, oS.C + oS.alphas[j] - oS.alphas[i])
        else:
            L = max(0, oS.alphas[j] + oS.alphas[i] - oS.C)
            H = min(oS.C, oS.alphas[j] + oS.alphas[i])
        if L == H:
            print "L==H"
            return 0
        eta = 2.0 * oS.X[i, :] * oS.X[j, :].T - oS.X[i, :] * oS.X[i, :].T - oS.X[j, :] * oS.X[j, :].T
        if eta >= 0:
            print "eta>=0"
            return 0
        oS.alphas[j] -= oS.labelMat[j] * (Ei - Ej) / eta
        oS.alphas[j] = clipAlpha(oS.alphas[j], H, L)
        updateEk(oS, j)
        if (abs(oS.alphas[j] - alphaJold) < 0.00001):
            print "j note mvoing enough"
            return 0
        oS.alphas[i] += oS.labelMat[j] * oS.labelMat[i] * (
            alphaJold - oS.alphas[j])
        updateEk(oS, i)
        b1 = oS.b - Ei - oS.labelMat[i] * (
            oS.alphas[i] - alphaIold
        ) * oS.X[i, :] * oS.X[i, :].T - oS.labelMat[j] * (
            oS.alphas[j] - alphaJold) * oS.X[i, :] * oS.X[j, :].T
        b2 = oS.b - Ej - oS.labelMat[i] * (
            oS.alphas[i] - alphaIold
        ) * oS.X[i, :] * oS.X[j, :].T - oS.labelMat[j] * (
            oS.alphas[j] - alphaJold) * oS.X[j, :] * oS.X[j, :].T
        if (0 < oS.alphas[i]) and (oS.C > oS.alphas[i]):
            oS.b = b1
        elif (0 < oS.alphas[j]) and (oS.C > oS.alphas[j]):
            oS.b = b2
        else:
            oS.b = (b1 + b2) / 2.0
        return 1
    else:
        return 0


def smoP(dataMatIn, classLabels, C, toler, maxIter, kTup=('lin', 0)):
    oS = optStruct(mat(dataMatIn), mat(classLabels).transpose(), C, toler)
    iter = 0
    entireSet = True
    alphaPairsChanged = 0
    while (iter < maxIter) and ((alphaPairsChanged > 0) or (entireSet)):
        alphaPairsChanged = 0
        if entireSet:
            for i in range(oS.m):
                alphaPairsChanged += innerL(i, oS)
                print "fullSet, iter: %d i: %d, pairs changed %d" % (
                    iter, i, alphaPairsChanged)
            iter += 1
        else:
            nonBoundIs = nonzero((oS.alphas.A > 0) * (oS.alphas.A < C))[0]
            for i in nonBoundIs:
                alphaPairsChanged += innerL(i, oS)
                print "non-bound,iter: %d i: %d,pairs changed %d" % (
                    iter, i, alphaPairsChanged)
            iter += 1
        if entireSet:
            entireSet = False
        elif (alphaPairsChanged == 0):
            entireSet = True
            print "iteration number: %d" % iter
        return oS.b, oS.alphas


def calcWs(alphas, dataArr, classLabels):
    X = mat(dataArr)
    labelMat = mat(classLabels).transpose()
    m, n = shape(X)
    w = zeros((n, 1))
    for i in range(m):
        w += multiply(alphas[i] * labelMat[i], X[i, :].T)
    return w