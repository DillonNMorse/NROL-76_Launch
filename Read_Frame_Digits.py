# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 13:32:33 2020

@author: Dillon Morse
"""

from Digit_Retrieve import Retrieve_Digit
from keras.models import load_model
import cv2 as cv

frame = '01891'



Image = Retrieve_Digit( frame )
Images = []
img_rows = 28
img_cols = 22
for image in Image:
    x = image.reshape(1, img_rows, img_cols, 1)
    Images.append(x)


model = load_model("test_model.h5")

image_index = 6


prediction = model.predict(Images[ image_index])
print(prediction.argmax())


import matplotlib.pyplot as plt

plt.imshow( Image[image_index] )