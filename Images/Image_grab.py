# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:06:15 2020

@author: Dillon Morse
"""

from skimage import io
from skimage.color import  rgb2gray
#from skimage.transform import resize
import cv2 as cv
import matplotlib.pyplot as plt
from matplotlib import patches



Frame_num = '00493'
image = io.imread( 'vid{}.jpg'.format(Frame_num) )
#image = rgb2gray(image)
#image = cv.threshold(image , 130/255, 255, cv.THRESH_BINARY)[1]

fig_liftoff, ax = plt.subplots(1,1)
ax.imshow(image)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
plt.setp(ax,
         xticks = [],
         xticklabels = [],
         yticks = [],
         yticklabels = [])

rect_vel = patches.Rectangle((1550,200),
                             115,
                             50, 
                             edgecolor='r', 
                             facecolor="None")
rect_alt = patches.Rectangle((1750,195),
                             100,
                             50, 
                             edgecolor='g', 
                             facecolor="None")

ax.add_patch(rect_vel)
ax.add_patch(rect_alt)

plt.savefig('NROL-76_Frame.jpeg',
            dpi = 200,
            bbox_inches = 'tight',
            transparent = True)


fig_velocity, ax = plt.subplots(1,1)
image_cropped = image[200:250, 1550:1675, :]
ax.imshow(image_cropped)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
plt.setp(ax,
         xticks = [],
         xticklabels = [],
         yticks = [],
         yticklabels = [])
rect_vel = patches.Rectangle((0,0),
                             124,
                             49, 
                             edgecolor='r', 
                             facecolor="None")
ax.add_patch(rect_vel)
plt.savefig('NROL-76_Velocity.jpeg',
            dpi = 200,
            bbox_inches = 'tight',
            transparent = True)


plt.show()


