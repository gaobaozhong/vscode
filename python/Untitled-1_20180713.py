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