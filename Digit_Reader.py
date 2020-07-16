# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 09:42:00 2020

@author: Dillon Morse
"""

# Based on the tuorial at: https://www.sitepoint.com/keras-digit-recognition-tutorial/

import keras
from keras.datasets import mnist
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D

import matplotlib.pyplot as plt

keras.backend.clear_session()

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# =============================================================================
# image_index = 22
# print(y_train[image_index])
# plt.imshow(x_train[image_index], cmap = 'Greys')
# plt.show()
# =============================================================================


img_rows = 28
img_cols = 28

x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
x_test    = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)

x_train = x_train/255
x_test = x_test/255


num_classes = 10
y_train = to_categorical(y_train, num_classes)
y_test   = to_categorical(y_test, num_classes)

model = Sequential()
model.add(Conv2D(32,
                 kernel_size = (3,3),
                 activation = 'relu',
                 input_shape = (img_rows, img_cols, 1)))
model.add(Conv2D(64,
                 (3,3),
                 activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Dropout(0.25))    
model.add(Flatten())
model.add(Dense(128,
                activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes,
                activation = 'softmax'))

model.compile(loss = 'categorical_crossentropy',
             optimizer = 'adam',
             metrics = ['accuracy'])

batch_size = 128
epochs = 10

model.fit(x_train, y_train,
          batch_size = batch_size,
          epochs = epochs,
          verbose = 1,
          validation_data = (x_test, y_test))
score = model.evaluate(x_test, y_test, verbose = 0)

print('Test loss: {:.3f}'.format(score[0]))
print('Test accuracy: {:.3f}'.format(score[1]))
model.save('test_model.h5')
    