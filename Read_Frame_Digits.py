# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 13:32:33 2020

@author: Dillon Morse
"""

from Digit_Retrieve import Retrieve_Digit
import keras


# =============================================================================
# Wrapper function which is called to scrape data from a frame.
# Input: The frame number (a string, five digits long) and the prediction model
# Output: The 7 digits necessary to read altitude and speed of the rocket
# =============================================================================
def Read_Digit(Frame_num, model):
    
    # =========================================================================
    # Call Retrieve_Digit to get the image data for the 7 digits on the frame
    # =========================================================================
    Image = Retrieve_Digit( Frame_num )
    
    # =========================================================================
    # Reshape image arrays to work with the trained classifier
    # =========================================================================
    Images = []
    img_rows = 28
    img_cols = 22
    for i, image in enumerate(Image):
        x = image.reshape(1, img_rows, img_cols, 1)
        Images.append(x)
    
    # =========================================================================
    # Pass each image to the classifier
    # =========================================================================
    speed_ones_digit  =  model.predict( Images[0] ).argmax()
    speed_tens_digit  =  model.predict( Images[1] ).argmax()
    speed_hunds_digit =  model.predict( Images[2] ).argmax()
    speed_thous_digit =  model.predict( Images[3] ).argmax()
    dist_ones_digit   =  model.predict( Images[4] ).argmax()
    dist_tens_digit   =  model.predict( Images[5] ).argmax()
    dist_hunds_digit  =  model.predict( Images[6] ).argmax()        
        
    # =========================================================================
    # Clear memory - improves runtime
    # =========================================================================  
    keras.backend.clear_session()
    
    return (speed_ones_digit, speed_tens_digit, speed_hunds_digit, speed_thous_digit,
            dist_ones_digit, dist_tens_digit, dist_hunds_digit )

  
 
# =============================================================================
# To test the functionality of this function.
# =============================================================================
# from keras.models import load_model
# model = load_model("test_model.h5")
# 
# frame = '01891'
# 
# import time
# begin = time.time()
# 
# print( Read_Digit(frame, model) )
# 
# end = time.time()
# 
# print('This operation took {:.3f} seconds'.format(end-begin))
# =============================================================================
