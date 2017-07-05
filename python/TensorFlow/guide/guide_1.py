#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tensorflow as tf

sess = tf.Session()

# Tensor
constant_1 = tf.constant([4, 5, 6], shape=[1, 3], dtype=tf.float32)
constant_2 = tf.constant([1, 2, 3], shape=[1, 3], dtype=tf.float32)
print(sess.run(constant_2))
print(sess.run(tf.add(constant_1, constant_2)))
print(sess.run(tf.zeros([2, 3], dtype=tf.int32)))
print(sess.run(tf.random_uniform([2, 3], -1, 1, dtype=tf.float32)))

placeholder_1 = tf.placeholder(tf.float32)

# Variable
variable_1 = tf.Variable([1, 2], dtype=tf.float32)
