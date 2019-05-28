# -*- coding: utf-8 -*-
# @Time    : 2019/5/28 上午11:24
# @Author  : baby松
# @FileName: tensorflow_04.py
# @Software: PyCharm
import tensorflow as tf

# # 需求一
# # 1.定义一个变量
# x = tf.Variable(0, dtype=tf.int32, name='v_x')
#
# # 2. 变量的更新
# assign_op = tf.assign(ref=x, value=x+1)
#
# # 3.变量初始化
# x_init_op = tf.global_variables_initializer()
#
# # 4.运行
# with tf.Session() as sess:
#     sess.run(x_init_op)
#     # 模拟迭代更新累积器
#     for i in range(5):
#         result = sess.run(assign_op)
#         print(result)


# 需求二
# 1. 定义一个不定形状的变量
# x = tf.Variable(
#     initial_value=[],  # 给定一个空值
#     dtype=tf.float32,
#     trainable=False,
#     validate_shape=False  # 设置为True，表示在变量更新的时候，进行shape的检查，默认为True
# )
#
# # 2. 变量更改
# concat = tf.concat([x, [0.0, 0.0]], axis=0)
# assign_op = tf.assign(x, concat, validate_shape=False)
#
# # 3. 变量初始化操作
# x_init_op = tf.global_variables_initializer()
#
# # 3. 运行
# with tf.Session(config=tf.ConfigProto(log_device_placement=True, allow_soft_placement=True)) as sess:
#     # 变量初始化
#     sess.run(x_init_op)
#
#     # 模拟迭代更新累加器
#     for i in range(5):
#         # 执行更新操作
#         sess.run(assign_op)
#         r_x = sess.run(x)
#         print(r_x)

# 需求三
# 1 定义一个变量
sum = tf.Variable(1, dtype=tf.int32)
i = tf.placeholder(dtype=tf.int32)
tmp_sum = sum * i
assign_op = tf.assign(sum, tmp_sum)
# with tf.control_dependencies([assign_op]):
#     sum = tf.Print(sum, data=[sum, sum.read_value()], message='sum:')

x_init_op = tf.global_variables_initializer()

with tf.Session(config=tf.ConfigProto(log_device_placement=True, allow_soft_placement=True)) as sess:
    sess.run(x_init_op)
    for j in range(1, 6):
        # r = sess.run(assign_op)
        r = sess.run(assign_op, feed_dict={i: j})
        print(r)
    print('5!={}'.format(sess.run(sum)))