# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 下午1:38
# @Author  : baby松
# @FileName: tensorflow_03.py
# @Software: PyCharm
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

a = tf.constant([[1, 2], [3, 4]], dtype=tf.int32, name='a')
b = tf.constant([5, 6, 7, 8], dtype=tf.int32, shape=[2, 2], name='b')
c = tf.matmul(a, b, name='matmul')
g = tf.add(a, c, name='add')
h = tf.subtract(b, a, name='b-a')
l = tf.matmul(h, c, name='hc')

# 启动默认图
# sess = tf.Session()

# c_result = sess.run(c)
# g_result = sess.run(g)
# print(c_result)

# 关闭会话
# sess.close()

with tf.Session() as sess:
    # l = sess.run(l)
    l = l.eval()
    print(l)
    # print(c_result)
    # print(g_result)