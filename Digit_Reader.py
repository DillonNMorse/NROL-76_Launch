# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 09:42:00 2020

@author: Dillon Morse
"""

# Based on the tuorial at: https://www.sitepoint.com/keras-digit-recognition-tutorial/

import keras
#from keras.datasets import mnist
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D

#import cv2 as cv
import numpy as np
#import matplotlib.pyplot as plt
import pickle
from sklearn.model_selection import train_test_split
import random

keras.backend.clear_session()


filename = 'Labeled_Digits'
infile = open(filename, 'rb')
X, y = pickle.load(infile)
infile.close()

y = [int(j) for j in y] 
counts = {k : y.count(k) for k in set(y) }
min_count = counts[ min(counts.keys(), key=(lambda k: counts[k])) ]

X_balanced = []
y_balanced = []

for digit in np.arange(10):
    bins = random.choices( list(np.arange(counts[ digit ])) , k = min_count )
    X_balanced = X_balanced + list( np.array( [ X[j] for j in np.arange(len(y)) if y[j] == digit] )[bins] )
    y_balanced = y_balanced + ( [digit]*min_count )

X = np.array(X)
y = np.array(y)

X_balanced = np.array(X_balanced)
y_balanced = np.array(y_balanced)


x_train, x_test, y_train, y_test = train_test_split(X_balanced, y_balanced, test_size=0.20)
#x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.20)



# If using the MNIST data - found that it didn't work well because handwritten
# 1's don't have the same shape as the 1's here.
#
# =============================================================================
# (x_train, y_train), (x_test, y_test) = mnist.load_data()
# 
# # Can apply thresholding - haven't trained yet with it.
# # =============================================================================
# # for k in np.arange( x_train.shape[0] ):
# #     x_train[k,:,:] = cv.threshold(x_train[k,:,:] , 100/255, 255, cv.THRESH_BINARY)[1]
# # for j in np.arange( x_test.shape[0] ):
# #     x_test[j,:,:] = cv.threshold(x_test[j,:,:] , 100/255, 255, cv.THRESH_BINARY)[1]
# # =============================================================================
# =============================================================================





img_rows = X[0].shape[0] # 28
img_cols = X[0].shape[1] # 28

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
             optimizer = keras.optimizers.Adadelta(), #'adam',
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
    