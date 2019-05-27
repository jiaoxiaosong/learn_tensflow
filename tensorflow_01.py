# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 上午11:34
# @Author  : baby松
# @FileName: tensorflow_01.py
# @Software: PyCharm

import tensorflow as tf
# constant 常量
a = tf.constant(10)
b = tf.constant(5)

with tf.Session() as sess:
    c = a+b
    r = sess.run(c)
    print(r)