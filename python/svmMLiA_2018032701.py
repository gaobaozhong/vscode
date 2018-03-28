# coding:utf

# 6-1
# load data set
def loadDataSet(filename):
    dataMat = []
    labelMat = []
    fr = open(filename)
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        dataMat.append([float(lineArr[0]),float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat, labelMat

# select a random ,which is not i, and is in range(0,m)
def selectJrand(i,m):
    j=i
    while (j==i):
        j = int(random.uniform(0,m))
    return j

# change L<=aj<=H
def clipAlpha(aj,H,L):
    if aj > H:
        aj = H
    if L > aj:
        aj = L
    return aj
# 这个函数比较大，是目前本书中最大的函数。
# 有五个参数，分别是，数据集，类别标签，常数C，容错率，和退出前最大的循环次数

def smoSimple(dataMatIn,classLabel,C,toler,maxIter):
    # 在本书中，我们构建函数是采用了通用的接口，这样就可以对算法和数据源进行组合或配对处理。 
    # 上述函数将多个列表和输入参数转换为Numpy矩阵，遮掩提供就可以简化很多数学处理操作，由于转置了类别标签，以后那次我们的得到就是一个列向量而不是一个列表。 
    # 于是类别标签相连的每行月还俗和数据矩阵中的行一一对应。
    dataMatrix = mat(dataMatIn)
    labelMat = mat(classLabel)
    b = 0
    # 我们可以通过矩阵dataMatIn的shape属性得到常数m和n。 
    m,n = shape(dataMatrix)
    # 最后我们可以构建一个alpha列矩阵，矩阵中的元素都初始化为0.
    alphas = mat(zeros(m,1))
    # 并建立一个iter变量。该变量存储的则是在么有任何alpha改变的情况下便利数据集的次数。
    iter = 0
    
    # 当该变量达到输入值maxIter时，函数结束运行并退出
    while(iter<maxIter):
        # 每次循环当中，将alpahpairschanged设为0 ，变量apphaPairschanged用于记录appha是否已经进行优化。当然，在循环结束是就会得知这一点，
        alphaPairsChanged = 0
        # 然后在对整个集合顺序遍历。
        for i in range(m):
            # 首先fxi能计算出来，这就是我们预测的类别。
            fXi = float(multiply(alphas,labelMat).T * (dataMatrix* dataMatrix[i,:].T))+b
            # 然后，基于这个实例的预测结果和真实值结果的对比，就可以计算误差Ei。
            Ei = fXi - float(labelMat[i])
            # 如果为误差很大，那么可以对该数据实例所对应的alpha进行优化。对该条件的测试处于上述清单的1处。在if语句中，不管正间隔还是副间隔都会被测试。 并且在该if语句中，也要同时检查alpah，以保证其不能等于0或者C。 后面alpah小于0或者大于C是将被调整为0或者C，所以一旦在该if语句中他们等于这两个值的话，那么他们就已经在“边界”上了。因此不能够减小或者增大，因此也就不值得对他们进行优化了。
            if (((labelMat[i]*Ei < -toler) and (alphas[i] < C))or((labelMat[i].Ei > toler) and (alphas[i] > 0):
                # 接下来，可以利用程序清单6-1中的辅助函数来随机选择第二个alpha值，alpha[j]，
                j = selectJrand(i,m)
                # 同样，可以采用第一个alpha值，alpha[i]的误差计算方法，来计算这个alpha的误差，这个过程可以通过copy（）的方法来实现，一次你稍后可以将新的alpha只和老的alpha只进行比较。python则会通过引用的方式来传递所有的列表，必须明确的告知python要alphaIold和alphaJold分配新的内存，否则的话，在对新值和旧值进行比较时，我们就看不到新旧值的变化。
                fXj = float(multiply(alphas,labelMat).T*(dataMatrix*dataMatrix[j,:].T))+b
                Ej = fXj - float(labelMat[j])
                alphaIold = alphas[i].copy()
                alphaJold = alphas[j].copy()
                #L和H，用于将alpha[j]调整到0和C之间。 如果L和H相等，就不做任何改变， 直接执行continue语句。在python中，则意味着本次循环结束直接运行下一次for的循环。
                if (labelMat[i] != labelMat[j]):
                    L = max(0,alphas[j]-alphas[i])
                    H = min(C,C+alphas[j]-alphas[i])
                else:
                    L = max(0,alphas[j] + alphas[i] -C)
                    H = min (C, alphas[j]+ alpahs[i])
                if L == H:
                    print "L == H"
                    continue
                # eta是alpha[j]的最有修改量，在那个很长的计算代码行中得到。。如果eta为0，那就是说需要退出for循环的当前迭代过程。 该过程对真实smo算法进行了简化处理。如果eta为0，那么计算机新的alpha[j]就比较麻烦了，这里我们就不对此进行详细的介绍了。有需要的可以自己查阅文献。现实中这种情况并不常发生，因此忽略这一部分通常也可以。于是我们计算出一个新的alpha[j]然后利用程序清单6-1中的辅助函数，以及L和H值进行调整
                eta = 2.0 * dataMatrix[i,:]*dataMatrix[j,:].T - dataMatrix[i,:]*dataMatrix[i,:].T - dataMatrix[j,:]*dataMatrix[j,:].T
                if eta >= 0:
                    print "eta>=0" 
                    continue
                alphas[j] -= labelMat[j]*(Ei-Ej)/eta
                alphas[j] = clipAlpha(alphas[j],H,L)
                # 然后就是检查alpha[j]是否有轻微改变，如果是的话，就退出for循环。
                if (abs(alphas[j]-alpahJold)<0.0001):
                    print "j not moving enough"
                    continue
                #然后，alpha[i]和alpha[j]同样进行改变，虽然改变的大小一样，但是改变的方向正好想法，如果一个增加，来那么另外一个减少。在对alpha[i]和alpha[j]进行改变之后，给这两值设置一个常数项b
                alphas[i] += labelMat[j] * labelMat[i]*(alphaJold-alphas[j])
                b1 = b - Ei - labelMat[i] * (alphas[i] - alphaIold) * dataMatrix[i,:] * dataMatrix[i,:].T - labelMat[j] * (alphas[j] - alphaJold) * dataMatrix[i,:] * dataMatrix[j,:].T
                b2 = b - Ej - labelMat[i] * (alphas[i] - alphaIold) * dataMatrix[i,:] * dataMatrix[j,:].T - labelMat[j] * (alphas[j] - alphaJold) * dataMatrix[j,:] * dataMatrix[j,:].T
                if (0<alphas[i]) and (C > alpha[i]):
                    b = b1
                elif (0< alphas[j]) and(C> alphas[j]):
                    b = b2
                else:
                    b = (b1+b2)/2.0
                alphaPairsChanged +=1
                print " iter:  %d i: %d, parirs chagedc %d " % (iter,i,alphaPairsChanged)
        # 最后，在优化过程结束的同事，必须䧁在合适的实际结束训话如果程序执行到forUN互动呢在以后一行都不行coninu鳄鱼局，那么就已经成功地改版了一堆alpha，同事可以alphapaireshced的值。鞭阿紫for黄菡之外需要检查alpha值是否已经做了更新，如果有跟新iter设为0后继续运行程序，只有在所有数据集便利maxiter词，之后，并且不再发生任何alpha修改的时候，郑旭才会停止并退出while虚汗。
        if(alphaPairsChanged == 0): 
            iter += 1
        else:
            iter = 0
        print "iteration numberr: %d " % iter
    return b,alphas
    
