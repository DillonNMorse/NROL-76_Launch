# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 13:32:33 2020

@author: Dillon Morse
"""

from Digit_Retrieve import Retrieve_Digit
import numpy as np

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
    # Stack all image arrays in to a single array, then cut out the extra 
    # dimension (using squeeze). This allows all 7 predictions to be handed to
    # the classifier simultaneously - improves runtime
    # =========================================================================
    Images = np.array(Images)   
    im = np.squeeze(Images, axis = 1)


    
    # =========================================================================
    # Pass images to the classifier, select digit with largest probability
    # =========================================================================

    pred  =  model.predict( im ).argmax(axis=1)

    return pred 

# =============================================================================
#  Order of outputs:  ( speed_ones_digit, speed_tens_digit, speed_hunds_digit, 
#                       speed_thous_digit, dist_ones_digit,  dist_tens_digit,
#                        dist_hunds_digit )
# =============================================================================



  
 
# =============================================================================
# To test the functionality of this function.
# =============================================================================
# from keras.models import load_model
# model =load_model("test_model.h5")
# 
# frame = '01891'
# 
# import time
# begin = time.time()
# 
# print( Read_Digit(frame, model) )
# 
# end = time.time()
# keras.backend.clear_session()
# 
# print('This operation took {:.3f} seconds'.format(end-begin))
# =============================================================================
