#!/usr/bin/python3
# -*- coding: utf-8 -*-

# MNIST

import ssl
from keras.models import Sequential
from keras.layers import Dense, Activation
from tensorflow.examples.tutorials.mnist import input_data

ssl._create_default_https_context = ssl._create_unverified_context

# 下载数据集
mnist = input_data.read_data_sets('/tmp/mnist', one_hot=True)
x_train = mnist.train.images
y_train = mnist.train.labels
x_test = mnist.test.images
y_test = mnist.test.labels

model = Sequential()
model.add(Dense(units=500, input_dim=28 * 28))
model.add(Activation('sigmoid'))
model.add(Dense(units=500))
model.add(Activation('sigmoid'))
model.add(Dense(units=10))
model.add(Activation('softmax'))

# 模型编译, optimizer 优化器, loss 损失函数
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 训练模型, batch_size 每次梯度下降处理时的样本数, epochs 训练轮数
model.fit(x_train, y_train, batch_size=100, epochs=20)

score = model.evaluate(x_test, y_test, batch_size=128)
print('\n\n')
print('Loss: {}'.format(score[0]))
print('Accuracy: {}'.format(score[1]))

y_predict = model.predict(x_test, batch_size=128)
print("Report: \n{}".format(y_predict))

model.summary()
