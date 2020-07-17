# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 16:25:37 2020

@author: Dillon Morse
"""

def Retrieve_Digit(Frame_num):
    
    from skimage import io, util, exposure
    from skimage.color import  rgb2gray
    from skimage.transform import resize
    import cv2 as cv
    
    image = io.imread( 'Frames/vid{}.jpg'.format(Frame_num) )
    image = rgb2gray(image)
 #   image = util.invert(image)
 #   image = exposure.adjust_sigmoid(image, 0.9, 5, False)
    image = cv.threshold(image , 130/255, 255, cv.THRESH_BINARY)[1]

    
    # Extract time data - currently broken (digit sizes changes digit position)
    time_top = 32
    time_bot = 64
    
    seconds_1_left = 1715
    seconds_1_right = 1735
    
    seconds_10_left = 1695
    seconds_10_right = 1715
    
    minutes_1_left = 1670
    minutes_1_right = 1690
    
    # Extract speed data
    speed_top = 215
    speed_bot = speed_top + 28 # 244
    
    speed_1_left = 1644
    speed_1_right = speed_1_left + 22 #1666
    
    speed_10_left = 1624
    speed_10_right = speed_10_left + 22 # 1645
    
    speed_100_left = 1604
    speed_100_right = speed_100_left + 22 # 1626
    
    speed_1000_left = 1584
    speed_1000_right = speed_1000_left + 22 #1606

    
   #Extract altitude distance - need to account for altitudes above/below 100 km 
    dist_top = 213
    dist_bot = dist_top + 28 #241
    
    if (int(Frame_num) < 4687 ) | (int(Frame_num) > 10555 ):
        dist_1_left = 1820
        dist_1_right = dist_1_left + 22 #1843
        
        dist_10_left = 1788
        dist_10_right = dist_10_left + 22 #1812
        
        dist_100_left = 1768
        dist_100_right = dist_100_left + 22 #1790
    else:
        dist_1_left = 1812
        dist_1_right = dist_1_left + 22 #1837
        
        dist_10_left = 1792
        dist_10_right = dist_10_left + 22 #1815
        
        dist_100_left = 1772
        dist_100_right = dist_100_left + 22 #1795        
    
    
    seconds_ones_digit = image[time_top:time_bot, seconds_1_left:seconds_1_right]
    seconds_tens_digit = image[time_top:time_bot, seconds_10_left:seconds_10_right]
    minutes_ones_digit = image[time_top:time_bot, minutes_1_left:minutes_1_right]
    
    
    speed_ones_digit  = image[speed_top:speed_bot,    speed_1_left:speed_1_right]
    speed_tens_digit  = image[speed_top:speed_bot,   speed_10_left:speed_10_right]
    speed_hunds_digit = image[speed_top:speed_bot,  speed_100_left:speed_100_right]
    speed_thous_digit = image[speed_top:speed_bot, speed_1000_left:speed_1000_right]
    
#    speed_ones_digit = resize(speed_ones_digit, (28,28) )
#    speed_tens_digit = resize(speed_tens_digit, (28,28) )
#    speed_hunds_digit = resize(speed_hunds_digit, (28,28) )
#    speed_thous_digit = resize(speed_thous_digit, (28,28) )
    
    
    dist_ones_digit  = image[dist_top:dist_bot,    dist_1_left:dist_1_right]
    dist_tens_digit  = image[dist_top:dist_bot,   dist_10_left:dist_10_right]
    dist_hunds_digit = image[dist_top:dist_bot,  dist_100_left:dist_100_right]
    
#    dist_tens_digit = resize(dist_tens_digit, (28,28) )  
    

    return (speed_ones_digit, speed_tens_digit, speed_hunds_digit, speed_thous_digit,
            dist_ones_digit, dist_tens_digit, dist_hunds_digit )


# =============================================================================
# Image = Retrieve_Digit('00511')
# import matplotlib.pyplot as plt
# plt.imshow( Image[2] )
# =============================================================================


# =============================================================================
# frame = '04693'
# 
# (speed_ones_digit, speed_tens_digit, speed_hunds_digit, speed_thous_digit,
#             dist_ones_digit, dist_tens_digit, dist_hunds_digit ) = Retrieve_Digit( frame )
# 
# from matplotlib import pyplot as plt
# 
# # =============================================================================
# # fig, (ax1, ax2, ax3, ax4) = plt.subplots(1,4)
# # ax1.imshow(speed_thous_digit)
# # ax2.imshow(speed_hunds_digit)
# # ax3.imshow(speed_tens_digit)
# # ax4.imshow(speed_ones_digit)
# # =============================================================================
# 
# 
# 
# fig, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8)) = plt.subplots(2,4)
# 
# #ax1.imshow( minutes_ones_digit, cmap=plt.cm.gray )
# #ax2.imshow( seconds_tens_digit, cmap=plt.cm.gray )
# #ax3.imshow( seconds_ones_digit, cmap=plt.cm.gray )
# 
# ax1.imshow( speed_thous_digit)
# ax2.imshow( speed_hunds_digit)
# ax3.imshow( speed_tens_digit)
# ax4.imshow( speed_ones_digit)
# 
# ax5.imshow( dist_hunds_digit)
# ax6.imshow( dist_tens_digit )
# ax7.imshow( dist_ones_digit )
# 
# plt.show()
# =============================================================================
