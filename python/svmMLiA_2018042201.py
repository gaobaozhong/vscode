from numpy import *
# 6-1


def loadDataSet(fileName):
    dataMat = []
    labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        dataMat.append(
            [
                float(
                    lineArr[0]
                ),
                float(
                    lineArr[1]
                )
            ]
        )
        labelMat.append(
            float(
                lineArr[2]
            )
        )
    return dataMat, labelMat


def selectJrand(i, m):
    j = i
    while(j == i):
        j = int(random.uniform(0, m))
    return j


def clipAlpha(aj, H, L):
    if aj > H:
        aj = H
    if L > aj:
        aj = L
    return aj


6-2
# b, alphas = svmMLiA.somSimple(dataArr,labelArr,0.6,0.001,40)
# print labelArr[:5] # [-1.0, -1.0, 1.0, -1.0, 1.0]
# print dataArr[:5] #[[3.542485, 1.977398], [3.018896, 2.556416], [7.55151, -1.58003], [2.114999, -0.004466], [8.127113, 1.274372]]


def somSimple(
    # [[3.542485, 1.977398], [3.018896, 2.556416], [7.55151, -1.58003], [2.114999, -0.004466], [8.127113, 1.274372]]
    dataMatIn,

    classLabels,  # [-1.0, -1.0, 1.0, -1.0, 1.0]

    C,
    toler,
    maxIter
):
    dataMatrix = mat(dataMatIn)
    labelMat = mat(classLabels).transpose()
    b = 0
    m, n = shape(dataMatrix)
    alphas = mat(zeros((m, 1)))
    iter = 0
    while(iter < maxIter):
        alphaPairsChanged = 0
        for i in range(m):
            fXi = float(
                multiply(
                    alphas, labelMat
                ).T *
                (
                    dataMatrix*dataMatrix[i, :].T
                )
            ) + b
            Ei = fXi - float(
                labelMat[i]
            )
            if(
                (
                    (
                        labelMat[i]*Ei < -toler
                    )
                    and
                    (
                        alphas[i] < C
                    )
                )
                or
                (
                    (
                        labelMat[i]*Ei > toler
                    )
                    and
                    (
                        alphas[i] > 0
                    )
                )
            ):
                j = selectJrand(i, m)
                fXj = float(
                    multiply(
                        alphas,
                        labelMat
                    ).T
                    *
                    (
                        dataMatrix
                        *
                        dataMatrix[j, :].T
                    )
                ) + b
                Ej = fXj - float(labelMat[j])
                alphaIold = alphas[i].copy()
                alphaJold = alphas[j].copy()
                if(
                    labelMat[i] != labelMat[j]
                ):
                    L = max(0, alphas[j]-alphas[i])
                    H = min(C, C+alphas[j]-alphas[i])
                else:
                    L = max(0, alphas[j]+alphas[i]-C)
                    H = min(C, alphas[j]+alphas[i])
                if L == H:
                    print "L == H"
                    continue
                eta = (
                    2.0
                    *
                    dataMatrix[i, :]
                    *
                    dataMatrix[j, :].T
                    -
                    dataMatrix[i, :]
                    *
                    dataMatrix[i, :].T
                    -
                    dataMatrix[j, :]
                    *
                    dataMatrix[j, :].T
                )
                if eta >= 0:
                    print "eta>=0"
                    continue
                alphas[j] -= (
                    labelMat[j]
                    *
                    (
                        Ei - Ej
                    )
                    /
                    eta
                )
                alphas[j] = clipAlpha(alphas[j], H, L)
                if(
                    abs(
                        alphas[j] - alphaJold
                    ) < 0.001
                ):
                    print "j not moving enough"
                    continue
                alphas[i] += (
                    labelMat[j]
                    *
                    labelMat[i]
                    *
                    (
                        alphaJold
                        -
                        alphas[j]
                    )
                )
                b1 = (
                    b
                    -
                    Ei
                    -
                    labelMat[i]
                    *
                    (
                        alphas[i]
                        -
                        alphaIold
                    )
                    *
                    dataMatrix[i, :]
                    *
                    dataMatrix[i, :].T
                    -
                    labelMat[j]
                    *
                    (
                        alphas[j]
                        -
                        alphaJold
                    )
                    *
                    dataMatrix[i, :]
                    *
                    dataMatrix[j, :].T
                )
                b2 = (
                    b
                    -
                    Ej
                    -
                    labelMat[i]
                    *
                    (
                        alphas[i]
                        -
                        alphaIold
                    )
                    *
                    dataMatrix[i, :]
                    *
                    dataMatrix[j, :].T
                    -
                    labelMat[j]
                    *
                    (
                        alphas[j]
                        -
                        alphaJold
                    )
                    *
                    dataMatrix[j, :]
                    *
                    dataMatrix[j, :].T
                )

                if(
                    (
                        0 < alphas[i]
                    )
                    and
                    (
                        C > alphas[i]
                    )
                ):
                    b = b1
                elif(
                    (
                        0 < alphas[j]
                    )
                    and
                    (
                        C > alphas[j]
                    )
                ):
                    b = b2
                else:
                    b = (b1 + b2) / 2.0
                alphaPairsChanged += 1
                print "iter: %d i: %d, pairs changed %d " % (
                    iter, i, alphaPairsChanged)
        if (
            alphaPairsChanged == 0
        ):
            iter += 1
        else:
            iter = 0
        print "iteration number: %d" % iter
    return b, alphas


class optStruct:
    def __init__(
        self,
        dataMatIn,
        classLabels,
        C,
        toler
    ):
        self.X = dataMatIn
        self.labelMat = classLabels
        self.C = C
        self.tol = toler
        self.m = shape(dataMatIn)[0]
        self.alphas = mat(zeros((self.m, 1)))
        self.b = 0
        self.eCache = mat(zeros((self.m, 2)))


def calcEk(oS, k):
    fXk = (
        float(
            multiply(
                oS.alphas,
                oS.labelMat
            ).T
            *
            (
                oS.X
                *
                oS.X[k, :].T
            )
        )
        +
        oS.b
    )
    Ek = fXk - float(oS.labelMat[k])
    return Ek


def selectJ(i, OS, Ei):
    maxK = -1
    maxDeltaE = 0
    Ej = 0
    oS.eCahce[i] = [1, Ei]
    validEcacheList = nonzero(
        oS.eCache[:, 0], A
    )[0]
    if(
        len(validEcacheList) > 1

    ):
        for k in validEcacheList:
            if k == i:
                continue
            Ek = calcEk(oS, k)
            deltaE = abs(Ei-Ek)
            if(
                deltaE > maxDeltaE
            ):
                maxK = k
                maxDeltaE = deltaE
                Ej = Ek
        return maxK, Ej
    else:
        j = selectJrand(i, oS.m)
        Ej = calcEk(oS, j)
    return j, Ej


def updateEk(oS, k):
    Ek = calcEk(oS,k)
    oS.eCache[k] = [1,Ek]


def innerL(i, oS):
    Ei = calcEk(oS, i)
    if (
        (
            (
                oS.labelMat[i].Ei < -oS.tol
            )
            and
            (
                oS.alphas[i] < oS.C
            )
        )
        or
        (
            (oS.labelMat[i].Ei > os.tol)
            and
            (
                os.alphas[i] > 0
            )
        )
    ):
        j,Ej =
        alphaIold =
        alphaJold=
        if():
            L =
            H =
        else:
            L =
            H =
        if L==H:
            print "L==H"
            return 0
        eta =
        if eta >=0:
            print "eta>=0"
            return 0
        oS.alphas[j] -=
        oS.alphas[j] = 
        updateEk(oS,j)
        if():
            print "j not moving enought"
            return 0
        oS.alphas[i] +=
        updateEk(oS,i)
        b1 =
        b2 =
        if():

        elif():
        
        else:
        
        return 1
    else:
        return 0

def smoP():
    oS = 
    iter =
    entireSet =
    alphaPairsChanged =
    while():
        alphaPairsChanged = 0
        if entireSet:
            for i in range(oS.m):
                alphaPairsChanged += 
            print ""
            iter +=1
        else:
            nonBoundIs= 
            for i in nonBoundIs:
                alphaPairsChanged +=
                print ""
            iter += 1
        if entireSet: 
            entireSet =
        elif():
            entireSet =     
        print ""
    return oS.b,oS.alphas

def calcWs(alphas,dataArr,classLabels):
    X =
    m,n =
    w =
    for i in range(m):
        w +=
    return w
