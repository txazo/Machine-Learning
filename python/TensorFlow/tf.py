# -*- coding: utf-8 -*-

import tensorflow as tf

# -------------------- tf.Tensor --------------------

# tf.constant 常量
tf.constant(1)
tf.constant([1, 2, 3, 4, 5, 6], shape=[2, 3], dtype=tf.float32)

# tf.size 大小
tf.size([1, 2, 3])  # 3
tf.size([[1, 2, 3], [4, 5, 6]])  # 6

# tf.expand_dims Tensor中插入一纬
tf.expand_dims([[[0, 0], [0, 0]], [[0, 0], [0, 0]]], axis=0)  # shape=(1, 2, 2, 2)
tf.expand_dims([[[0, 0], [0, 0]], [[0, 0], [0, 0]]], axis=1)  # shape=(2, 1, 2, 2)
tf.expand_dims([[[0, 0], [0, 0]], [[0, 0], [0, 0]]], axis=2)  # shape=(2, 2, 1, 2)
tf.expand_dims([[[0, 0], [0, 0]], [[0, 0], [0, 0]]], axis=3)  # shape=(2, 2, 2, 1)
tf.expand_dims([[[0, 0], [0, 0]], [[0, 0], [0, 0]]], axis=-1)  # shape=(2, 2, 2, 1)

# tf.range 创建数字序列, delta 步长
tf.range(1, limit=10, delta=2)  # [1, 3, 5, 7, 9]

# tf.concat 将两个Tensor在某一个纬度上合并
tf.concat([[[1, 2], [3, 4]], [[5, 6], [7, 8]]], axis=0)  # [[1, 2], [3, 4], [5, 6], [7, 8]]
tf.concat([[[1, 2], [3, 4]], [[5, 6], [7, 8]]], axis=1)  # [[1, 2, 3, 4], [5, 6, 7, 8]]

# tf.add 加
tf.add(1, 2)  # 3

# tf.assign 变量赋值
tf.assign(variable, new_value)

# tf.zeros
tf.zeros([2, 3], dtype=tf.float32)  # [[0., 0., 0.], [0., 0., 0.]]

# tf.random_uniform
tf.random_uniform([2, 3], 1, 10, dtype=tf.int32)  # [[3, 3, 4], [2, 7, 1]]

# tf.random_normal 从一个正态分布中输出随机值, mean 均数, stddev 标准差
tf.random_normal(shape=[2, 1], mean=5, stddev=1, dtype=tf.float32)  # [[5.20478249], [4.82979918]]

# tf.truncated_normal 从一个截断正态分布中输出随机值
tf.random_normal(shape=[2, 1], mean=0, stddev=0.1, dtype=tf.float32)  # [[-0.05876487], [0.08388939]]

# tf.matmul 矩阵乘积(纬数大于1)
tf.matmul([[1, 2], [3, 4]], [[1, 2], [3, 4]])  # [[7, 10], [15, 22]]

# tf.square 平方
tf.square(2)  # 4

# tf.log 求自然对数
tf.log(4.0)  # 1.3862944

# tf.reduce_mean 平均值
tf.reduce_mean([[1, 3, 5], [2, 5, 8]])  # 4
tf.reduce_mean([[1, 3, 5], [2, 5, 8]], axis=0)  # [1, 4, 6]
tf.reduce_mean([[1, 3, 5], [2, 5, 8]], axis=1)  # [3, 5]

# tf.reduce_sum 求和
tf.reduce_sum([[1, 3, 5], [2, 5, 8]])  # 24
tf.reduce_sum([[1, 3, 5], [2, 5, 8]], axis=0)  # [3,8,13]
tf.reduce_sum([[1, 3, 5], [2, 5, 8]], axis=1)  # [9,15]

# tf.argmax 最大值的下标
tf.argmax([1, 2, 3])  # 2
tf.argmax([[1, 2], [3, 4], [6, 5]], 1)  # [1, 1, 0]

# tf.equal 是否相等
tf.equal(0, 1)  # False
tf.equal([1, 0, 0], [1, 0, 1])  # [True, True, False]

# tf.cast 类型转换
tf.cast([1.0, 2.0], tf.int32)  # [1, 2]

# -------------------- tf.Variable --------------------

# tf.Variable 变量, 维护图中的状态
tf.Variable(.0)
tf.Variable([1, 2, 3, 4, 5, 6], dtype=tf.int32)

# -------------------- tf.placeholder --------------------

# tf.placeholder 占位符, 由feed_dict提供输入
tf.placeholder(tf.float32, shape=[None, 3])

# -------------------- tf.train --------------------

# tf.train.GradientDescentOptimizer 梯度下降优化器
tf.train.GradientDescentOptimizer(learning_rate=0.01)

# -------------------- tf.Operation --------------------

# tf.global_variables_initializer 初始化全局变量
tf.global_variables_initializer()

# -------------------- tf.Session --------------------

# tf.Session 启动会话
sess = tf.Session()

# tf.Session.run() 执行Operation, 计算Tensor并fetches
sess.run(feed_dict={x: 1, y: 2})

# tf.Session.close 关闭会话
sess.close()

# -------------------- tf --------------------

# tf.device 指派设备
tf.device('/gpu:0')

# -------------------- fetch --------------------
# 获取Tensor的值
result = sess.run([tensor_1, tensor_2, tensor_3])

# -------------------- feed --------------------
# 填充
sess.run(feed_dict={x: _x})
