# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 16:25:37 2020

@author: Dillon Morse
"""


from skimage import io, util, exposure
from skimage.color import  rgb2gray
from matplotlib import pyplot as plt

image = io.imread('SpaceX/Frames/vid07711.jpg')
image = rgb2gray(image)
image = util.invert(image)
image = exposure.adjust_sigmoid(image, 0.2, 5, False)
#image = exposure.adjust_log(image, 0.1, False)

print(image.shape)

time_top = 32
time_bot = 64

seconds_1_left = 1715
seconds_1_right = 1735

seconds_10_left = 1695
seconds_10_right = 1715

minutes_1_left = 1670
minutes_1_right = 1690


speed_top = 215
speed_bot = 245

speed_1_left = 1645
speed_1_right = 1666

speed_10_left = 1624
speed_10_right = 1645

speed_100_left = 1605
speed_100_right = 1626

speed_1000_left = 1585
speed_1000_right = 1606



dist_top = 213
dist_bot = 242

dist_1_left = 1812
dist_1_right = 1835

dist_10_left = 1792
dist_10_right = 1815

dist_100_left = 1773
dist_100_right = 1796


seconds_ones_digit = image[time_top:time_bot, seconds_1_left:seconds_1_right]
seconds_tens_digit = image[time_top:time_bot, seconds_10_left:seconds_10_right]
minutes_ones_digit = image[time_top:time_bot, minutes_1_left:minutes_1_right]


speed_ones_digit  = image[speed_top:speed_bot,    speed_1_left:speed_1_right]
speed_tens_digit  = image[speed_top:speed_bot,   speed_10_left:speed_10_right]
speed_hunds_digit = image[speed_top:speed_bot,  speed_100_left:speed_100_right]
speed_thous_digit = image[speed_top:speed_bot, speed_1000_left:speed_1000_right]


dist_ones_digit  = image[dist_top:dist_bot,    dist_1_left:dist_1_right]
dist_tens_digit  = image[dist_top:dist_bot,   dist_10_left:dist_10_right]
dist_hunds_digit = image[dist_top:dist_bot,  dist_100_left:dist_100_right]




fig, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8), (ax9, ax10, ax11, ax12)) = plt.subplots(3,4)

ax1.imshow( minutes_ones_digit, cmap=plt.cm.gray )
ax2.imshow( seconds_tens_digit, cmap=plt.cm.gray )
ax3.imshow( seconds_ones_digit, cmap=plt.cm.gray )

ax5.imshow( speed_thous_digit, cmap=plt.cm.gray )
ax6.imshow( speed_hunds_digit, cmap=plt.cm.gray )
ax7.imshow( speed_tens_digit, cmap=plt.cm.gray )
ax8.imshow( speed_ones_digit, cmap=plt.cm.gray )

ax9.imshow( dist_hunds_digit, cmap=plt.cm.gray )
ax10.imshow( dist_tens_digit, cmap=plt.cm.gray )
ax11.imshow( dist_ones_digit, cmap=plt.cm.gray )




plt.show()