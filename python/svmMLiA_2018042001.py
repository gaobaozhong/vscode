# 6 svm
# smo
# kernel
# 6-1
def loadDataSet(fileName):
    dataMat = []
    labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        dataMat.append([
            float(lineArr[0]),
            float(lineArr[1])
        ])
        labelMat.append(
            float(lineArr[2])
        )
    return dataMat, labelMat
def selectJrand(i,m):
    j = i
    while(j==i):
        j = int(random.uniform(0,m))
    return j

def clipAlpha(aj,H,L):
    if aj > H:
        aj = H
    if L > aj:
        aj = L
    return aj
    
# 6-2
def smoSimple(
    dataMatIn,
    classLabels,
    C,
    toler,
    maxIter
    ):

    dataMatrix = 
    labelMat =
    b =
    m,n = 
    alphas =
    iter =

    while(iter < maxIter):
        alphaPairsChanged = 0
        for i in range(m):
            fXi = float() + b
            Ei = fXi - float()
            if ():
                j = 
                fXj = 
                Ej =
                alphaIold =
                alphaJold =
                if (labelMat[i] != labelMat[j]):
                    L = 
                    H =
                else:
                    L = 
                    H =
                if L == H:
                    print "L==H"
                    continue
                eta = 
                if eta >= 0:
                    print "eta >= 0"
                    continue
                alphas[j] -=
                alphas[j] =
                if(abs()):
                    print "j not moving enough"
                    continue
                alphas[i] +=
                b1 = b - E
