# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 下午1:23
# @Author  : baby松
# @FileName: tensorflow_02.py
# @Software: PyCharm

import tensorflow as tf

matrix1 = tf.constant([[3., 3.]])
print(matrix1.shape)
matrix2 = tf.constant([[2.],
                       [2.]])
print(matrix2.shape)
product = tf.matmul(matrix1, matrix2)
sess = tf.Session()
result = sess.run(product)
print(result)