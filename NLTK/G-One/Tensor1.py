import tensorflow as tf

x1 = tf.constant([5])
x2 = tf.constant([3])

#res = tf.matmul(x1, x2)
res = x1 * x2
print(res)

s = tf.Session()
print(s.run(res))
s.close()
