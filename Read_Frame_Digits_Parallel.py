# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 22:37:56 2020

@author: Dillon Morse
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 13:32:33 2020

@author: Dillon Morse
"""

from Digit_Retrieve import Retrieve_Digit
from keras.models import load_model

frame = '01891'


def Read_Digit_Single(Image, model):
    
    #Image = Retrieve_Digit( Frame_num )[digit_index]
# =============================================================================
#     Images = []
# =============================================================================
    img_rows = 28
    img_cols = 22
# =============================================================================
#     for image in Image:
#         x = image.reshape(1, img_rows, img_cols, 1)
#         Images.append(x)
# =============================================================================
    Image = Image.reshape(1, img_rows, img_cols, 1)
    

# =============================================================================
#     speed_ones_digit  =  model.predict( Images[digit_index] ).argmax()       
#         
#     from multiprocessing import Pool
#     pool = Pool()
#     args = [Images[0], Images[1], Images[2], Images[3], Images[4], Images[5], Images[6]]
# 
#     results = pool.map( model.predict, args)
# =============================================================================
    

    return model.predict(Image).argmax() #(speed_ones_digit, speed_tens_digit, speed_hunds_digit, speed_thous_digit,
           # dist_ones_digit, dist_tens_digit, dist_hunds_digit )

  
# =============================================================================
# model = load_model("test_model.h5") 
# print( Read_Digit_Single( '01891',1,model  ) )
# =============================================================================


def Read_Digit(Frame_num):

    model = load_model("test_model.h5")
    
    Image = Retrieve_Digit( Frame_num )    
    Images = []
    img_rows = 28
    img_cols = 22
    for image in Image:
        x = image.reshape(1, img_rows, img_cols, 1)
        Images.append(x)
    
    
    from multiprocessing import Pool
    from itertools import repeat
    pool = Pool()
    args = [Images[0], Images[1], Images[2], Images[3], Images[4], Images[5], Images[6]]
    args = zip(args, repeat(model))
    results = pool.starmap( Read_Digit_Single, args)

    return results

print( Read_Digit(frame) )

# =============================================================================
# import matplotlib.pyplot as plt
# 
# plt.imshow( Image[6] )
# =============================================================================
