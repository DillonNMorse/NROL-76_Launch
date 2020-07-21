# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 16:25:37 2020

@author: Dillon Morse
"""

def Retrieve_Digit(Frame_num):
    
    from skimage import io
    from skimage.color import  rgb2gray
    #from skimage.transform import resize
    import cv2 as cv
    
    image = io.imread( 'Frames/vid{}.jpg'.format(Frame_num) )
    image = rgb2gray(image)
    image = cv.threshold(image , 130/255, 255, cv.THRESH_BINARY)[1]

    
    # =========================================================================
    # Extract time data - currently broken (digit sizes changes digit position)
    # =========================================================================
    time_top = 32
    time_bot = 64
    
    seconds_1_left = 1715
    seconds_1_right = 1735
    
    seconds_10_left = 1695
    seconds_10_right = 1715
    
    minutes_1_left = 1670
    minutes_1_right = 1690
    
    # =========================================================================
    # Extract speed data. All boxes give 28x22 arrays.
    # =========================================================================
    speed_top = 215
    speed_bot = speed_top + 28
    
    speed_1_left = 1644
    speed_1_right = speed_1_left + 22
    
    speed_10_left = 1624
    speed_10_right = speed_10_left + 22
    
    speed_100_left = 1604
    speed_100_right = speed_100_left + 22
    
    speed_1000_left = 1584
    speed_1000_right = speed_1000_left + 22

    
    # =========================================================================
    # Extract altitude distance - need to account for altitudes above/below 
    # 100 km where number changes format. All boxes give 28x22 arrays.
    # =========================================================================
    dist_top = 213
    dist_bot = dist_top + 28
    
    if (int(Frame_num) < 4687 ) | (int(Frame_num) > 10555 ):
        dist_1_left = 1820
        dist_1_right = dist_1_left + 22
        
        dist_10_left = 1788
        dist_10_right = dist_10_left + 22
        
        dist_100_left = 1768
        dist_100_right = dist_100_left + 22
    else:
        dist_1_left = 1812
        dist_1_right = dist_1_left + 22
        
        dist_10_left = 1792
        dist_10_right = dist_10_left + 22
        
        dist_100_left = 1772
        dist_100_right = dist_100_left + 22     
    
    # =========================================================================
    # Assign time data - currently broken (digit sizes changes digit position)
    # =========================================================================
    seconds_ones_digit = image[time_top:time_bot, seconds_1_left:seconds_1_right]
    seconds_tens_digit = image[time_top:time_bot, seconds_10_left:seconds_10_right]
    minutes_ones_digit = image[time_top:time_bot, minutes_1_left:minutes_1_right]
    
    # =========================================================================
    # Assign speed data
    # =========================================================================  
    speed_ones_digit  = image[speed_top:speed_bot,    speed_1_left:speed_1_right]
    speed_tens_digit  = image[speed_top:speed_bot,   speed_10_left:speed_10_right]
    speed_hunds_digit = image[speed_top:speed_bot,  speed_100_left:speed_100_right]
    speed_thous_digit = image[speed_top:speed_bot, speed_1000_left:speed_1000_right]
    
    # =========================================================================
    # Assign altitude data
    # =========================================================================
    dist_ones_digit  = image[dist_top:dist_bot,    dist_1_left:dist_1_right]
    dist_tens_digit  = image[dist_top:dist_bot,   dist_10_left:dist_10_right]
    dist_hunds_digit = image[dist_top:dist_bot,  dist_100_left:dist_100_right]
    

    return (speed_ones_digit, speed_tens_digit, speed_hunds_digit, speed_thous_digit,
            dist_ones_digit, dist_tens_digit, dist_hunds_digit )



# =============================================================================
# Test functionality
# =============================================================================
# frame = '00493'
# (speed_ones_digit, speed_tens_digit, speed_hunds_digit, speed_thous_digit,
#             dist_ones_digit, dist_tens_digit, dist_hunds_digit ) = Retrieve_Digit( frame )
# 
# from matplotlib import pyplot as plt
# fig, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8)) = plt.subplots(2,4)
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
# 
# 
# 
# # =============================================================================
# # fig, ax = plt.subplots(1,4)
# # ((ax1, ax2, ax3, ax4)) = ax
# # ax1.imshow( speed_thous_digit)
# # ax2.imshow( speed_hunds_digit)
# # ax3.imshow( speed_tens_digit)
# # ax4.imshow( speed_ones_digit)
# # 
# # for axes in ax:
# #     axes.spines['top'].set_visible(False)
# #     axes.spines['right'].set_visible(False)
# #     axes.spines['left'].set_visible(False)
# #     axes.spines['bottom'].set_visible(False)
# #     plt.setp(axes,
# #              xticks = [],
# #              xticklabels = [],
# #              yticks = [],
# #              yticklabels = [])
# #     
# # plt.savefig('Images/NROL-76_Velocity_Processed.jpeg',
# #             dpi = 200,
# #             bbox_inches = 'tight',
# #             transparent = True)   
# # plt.show()
# # =============================================================================
# =============================================================================




