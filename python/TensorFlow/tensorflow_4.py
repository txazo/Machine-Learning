#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import tensorflow as tf

# 日志级别
tf.logging.set_verbosity(tf.logging.ERROR)

train_count = 10
feature_count = 5

train_x = np.floor(1000 * np.random.random([train_count, feature_count]), dtype=np.float32)
train_w = np.floor(1000 * np.random.random([feature_count, 1]), dtype=np.float32)
train_y = train_x.dot(train_w)

x = tf.placeholder(tf.float32, shape=[train_count, feature_count])
y = tf.placeholder(tf.float32, shape=[train_count, 1])
w = tf.Variable(np.zeros(feature_count, dtype=np.float32).reshape((feature_count, 1)), tf.float32)

loss = tf.reduce_sum(tf.square(tf.matmul(x, w) - y))
train = tf.train.GradientDescentOptimizer(0.0000001).minimize(loss)

LOSS_MIN_VALUE = tf.constant(1e-5)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
run_count = 0
last_loss = 0
while True:
    run_count = 1
    sess.run(train, {x: train_x, y: train_y})

    curr_loss, is_ok = sess.run([loss, loss < LOSS_MIN_VALUE], {x: train_x, y: train_y})
    print("运行 {} 次,loss= {} ".format(run_count, curr_loss))

    if last_loss == curr_loss:
        break

    last_loss = curr_loss
    if is_ok:
        break

curr_W, curr_loss = sess.run([w, loss], {x: train_x, y: train_y})
print("t_w: {}, nw: {}, nfix_w: {}, nloss: {}, nfix_w_loss: {}".format(
        train_w, curr_W, np.round(curr_W), curr_loss, np.sum(np.square(train_w - np.round(curr_W)))))
