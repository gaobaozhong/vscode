import tensorflow as tf
# a = tf.zeros((2,2))
# print(a.shape)

# a = tf.constant(5.0)
# b = tf.constant(6.0)
# c = a*b
# sess = tf.Session()
# print(sess.run(c))

# with tf.Session() as sess:
#     result = sess.run(c)
#     print(result)

# with tf.InteractiveSession() as sess:
#     x = tf.Variable([1.0,2.0])
#     a = tf.constant([3.0,3.0])
#     x.initializer.run()
#     sub = tf.sub(x,a)
#     print(sub.eval())

# sess = tf.InteractiveSession()
# x = tf.Variable([1.0, 2.0])
# a = tf.constant([3.0, 3.0])
# # Initialize 'x' using the run() method of its initializer op.
# x.initializer.run()
# # Add an op to subtract 'a' from 'x'.  Run it and print the result
# sub = tf.sub(x, a)
# print(sub.eval())

W = tf.Variable(tf.zeros((2, 2)), name="weights")
R = tf.Variable(tf.random_normal((2, 2)), name="random_weights")
with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())
    print(sess.run(W))
    print(sess.run(R))

def loadMNIST():
    from tensorflow.examples.tutorials.mnist import input_data
    mnist = input_data.read_data_sets('MNIST_data',one_hot=True)
    return mnist

def KNN(mnist):
    train_x,train_y = mnist.train.next_batch(5000)
    test_x,test_y = mnist.train.next_batch(200)
 
    xtr = tf.placeholder(tf.float32,[None,784])
    xte = tf.placeholder(tf.float32,[784])
    distance = tf.sqrt(tf.reduce_sum(tf.pow(tf.add(xtr,tf.negative(xte)),2),reduction_indices=1))
 
    pred = tf.argmin(distance,0)
 
    init = tf.initialize_all_variables()
 
    sess = tf.Session()
    sess.run(init)
 
    right = 0
    for i in range(200):
        ansIndex = sess.run(pred,{xtr:train_x,xte:test_x[i,:]})
        print ('prediction is ',np.argmax(train_y[ansIndex]))
        print ('true value is ',np.argmax(test_y[i]))
        if np.argmax(test_y[i]) == np.argmax(train_y[ansIndex]):
            right += 1.0
    accracy = right/200.0
    print (accracy)
 
if __name__ == "__main__":
    mnist = loadMNIST()
    KNN(mnist)