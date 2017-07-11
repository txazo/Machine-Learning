#!/usr/bin/python3
# -*- coding: utf-8 -*-

# MNIST

import ssl
from keras.models import Sequential
from keras.layers import Dense, Activation
from tensorflow.examples.tutorials.mnist import input_data

ssl._create_default_https_context = ssl._create_unverified_context

mnist = input_data.read_data_sets('/tmp/mnist', one_hot=True)

model = Sequential()
model.add(Dense(input_dim=28 * 28, units=500))
model.add(Activation('sigmoid'))
model.add(Dense(units=500))
model.add(Activation('sigmoid'))
model.add(Dense(units=10))
model.add(Activation('softmax'))

# loss损失函数, optimizer优化器
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

x_train = mnist.train.images
y_train = mnist.train.labels
x_test = mnist.test.images
y_test = mnist.test.labels

model.fit(x_train, y_train, batch_size=100, epochs=20)

score = model.evaluate(x_test, y_test, batch_size=128)
print('\n\n')
print('Loss: {}'.format(score[0]))
print('Accuracy: {}'.format(score[1]))

y_predict = model.predict(x_test, batch_size=128)
print("Report: \n{}".format(report))
