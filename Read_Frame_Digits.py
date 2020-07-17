# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 13:32:33 2020

@author: Dillon Morse
"""

from Digit_Retrieve import Retrieve_Digit
from keras.models import load_model

#frame = '01891'


def Read_Digit(Frame_num, model):
    
    Image = Retrieve_Digit( Frame_num )
    Images = []
    img_rows = 28
    img_cols = 22
    for image in Image:
        x = image.reshape(1, img_rows, img_cols, 1)
        Images.append(x)
    
    
# =============================================================================
#     model = load_model("test_model.h5")
# =============================================================================

    speed_ones_digit  =  model.predict( Images[0] ).argmax()
    speed_tens_digit  =  model.predict( Images[1] ).argmax()
    speed_hunds_digit =  model.predict( Images[2] ).argmax()
    speed_thous_digit =  model.predict( Images[3] ).argmax()
    dist_ones_digit   =  model.predict( Images[4] ).argmax()
    dist_tens_digit   =  model.predict( Images[5] ).argmax()
    dist_hunds_digit  =  model.predict( Images[6] ).argmax()        
        
    

    return (speed_ones_digit, speed_tens_digit, speed_hunds_digit, speed_thous_digit,
            dist_ones_digit, dist_tens_digit, dist_hunds_digit )

  
 
#print( Read_Digit( '01891' ) )


# =============================================================================
# import matplotlib.pyplot as plt
# 
# plt.imshow( Image[6] )
# =============================================================================
