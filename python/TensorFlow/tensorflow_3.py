#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import tensorflow as tf

# 日志级别
tf.logging.set_verbosity(tf.logging.ERROR)

# 训练数据
train_x = np.floor(10 * np.random.random([5]), dtype=np.float32)
train_y = train_x * 3.0 + 8.0

# 输入
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

# 变量
a = tf.Variable(0.0)
b = tf.Variable(0.0)

# 损失函数
loss = tf.reduce_sum(tf.square(x * a + b - y))
# 定义模型
train = tf.train.GradientDescentOptimizer(0.001).minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
for i in range(10000):
    sess.run(train, {x: train_x, y: train_y})
    a_value, b_value, _ = sess.run([a, b, loss], {x: train_x, y: train_y})
    print("a = {}, b = {}".format(a_value, b_value))
