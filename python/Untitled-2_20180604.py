# today is a nice day. curry win. i like curry. 
# chapter 1 the basick of machine llearinng 
# test

# from numpy import *
# print random.rand(4,4)

# “””
# 加载图像数据的函数,dataset_path即图像olivettifaces的路径
# 加载olivettifaces后，划分为train_data,valid_data,test_data三个数据集
# 函数返回train_data,valid_data,test_data以及对应的label
# “””
def load_data(dataset_path):
    img = Image.open(dataset_path)
    img_ndarray = numpy.asarray(img, dtype=‘float64′)/256
    faces=numpy.empty((400,2679))
    for row in range(20):
       for column in range(20):
        faces[row*20+column]=numpy.ndarray.flatten(img_ndarray [row*57:(row+1)*57,column*47:(column+1)*47])
    label=numpy.empty(400)
    for i in range(40):
    label[i*10:i*10+10]=i
    label=label.astype(numpy.int)
    #分成训练集、验证集、测试集，大小如下
    train_data=numpy.empty((320,2679))
    train_label=numpy.empty(320)
    valid_data=numpy.empty((40,2679))
    valid_label=numpy.empty(40)
    test_data=numpy.empty((40,2679))
    test_label=numpy.empty(40)
    for i in range(40):
    train_data[i*8:i*8+8]=faces[i*10:i*10+8]
    train_label[i*8:i*8+8]=label[i*10:i*10+8]
    valid_data[i]=faces[i*10+8]
    valid_label[i]=label[i*10+8]
    test_data[i]=faces[i*10+9]
    test_label[i]=label[i*10+9]
    #将数据集定义成shared类型，才能将数据复制进GPU，利用GPU加速程序。
    def shared_dataset(data_x, data_y, borrow=True):
        shared_x = theano.shared(numpy.asarray(data_x,
                                               dtype=theano.config.floatX),
                                 borrow=borrow)
        shared_y = theano.shared(numpy.asarray(data_y,
                                               dtype=theano.config.floatX),
                                 borrow=borrow)
        return shared_x, T.cast(shared_y, ‘int32′)
    train_set_x, train_set_y = shared_dataset(train_data,train_label)
    valid_set_x, valid_set_y = shared_dataset(valid_data,valid_label)
    test_set_x, test_set_y = shared_dataset(test_data,test_label)
    rval = [(train_set_x, train_set_y), (valid_set_x, valid_set_y),
            (test_set_x, test_set_y)]
    return rval
 

# 二、CNN的基本“构件”（LogisticRegression、HiddenLayer、LeNetConvPoolLayer）

# 卷积神经网络（CNN）的基本结构就是输入层、卷积层（conv）、子采样层（pooling）、全连接层、输出层（分类器）。  卷积层+子采样层一般都会有若干个，本程序实现的CNN模型参考LeNet5，有两个“卷积+子采样层”LeNetConvPoolLayer。全连接层相当于MLP（多层感知机）中的隐含层HiddenLayer。输出层即分类器，一般采用softmax回归（也有人直接叫逻辑回归，其实就是多类别的logistics regression），本程序也直接用LogisticRegression表示。
# 总结起来，要组建CNN模型，必须先定义LeNetConvPoolLayer、HiddenLayer、LogisticRegression这三种layer，这一点在我上一篇文章介绍CNN算法时讲得很详细，包括代码注解，因为太冗长，这里给出链接：《DeepLearning tutorial（4）CNN卷积神经网络原理简介+代码详解》。
# 代码太长，就不贴具体的了，只给出框架，具体可以下载我的代码看看：

# [python]
#分类器，即CNN最后一层，采用逻辑回归（softmax）
class LogisticRegression(object):
    def __init__(self, input, n_in, n_out):
        self.W = ….
        self.b = ….
        self.p_y_given_x = …
        self.y_pred = …
        self.params = …
    def negative_log_likelihood(self, y):
    def errors(self, y):
#全连接层，分类器前一层
class HiddenLayer(object):
    def __init__(self, rng, input, n_in, n_out, W=None, b=None,activation=T.tanh):
        self.input = input
        self.W = …
        self.b = …
        lin_output = …
        self.params = [self.W, self.b]
#卷积+采样层（conv+maxpooling）
class LeNetConvPoolLayer(object):
    def __init__(self, rng, input, filter_shape, image_shape, poolsize=(2, 2)):
        self.input = input
        self.W = …
        self.b = …
        # 卷积
        conv_out = …
        # 子采样
        pooled_out =…
        self.output = …
        self.params = [self.W, self.b]