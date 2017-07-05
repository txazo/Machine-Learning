#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tensorflow as tf

hello_op = tf.constant('Hello, TensorFlow!')
a = tf.constant(10)
b = tf.constant(32)
compute_op = tf.add(a, b)

with tf.Session() as session:
    print(session.run(hello_op))
    print(session.run(compute_op))
