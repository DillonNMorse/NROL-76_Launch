# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 20:18:13 2020

@author: Dillon Morse
"""
import numpy as np
import pandas as pd
from Read_Frame_Digits import Read_Digit
from keras.models import load_model
import time
import tensorflow as tf


# =============================================================================
# Create list of strings with appropriate frame-numbers for accessing image files
# =============================================================================
frame_start = 193
frame_end = 13993
Frames = [str(i) for i in np.arange(frame_start, frame_end, 6) ]
for j, frame in enumerate(Frames):
    if len(frame) == 3:
        Frames[j] = '00'+frame
    elif len(frame) == 4:
        Frames[j] = '0'+frame


# =============================================================================
# Create pandas dataframe to hold scraped data
# =============================================================================
df = ( pd.DataFrame(Frames)
      .rename( columns = {0:'Frame'}))
df['Alt'] = np.zeros(len(Frames))
df['Speed'] = np.zeros(len(Frames))


# =============================================================================
# Loop over all 2,301 frames
# =============================================================================
kk = 0
start = time.time()

config = tf.ConfigProto(intra_op_parallelism_threads = 8,
                        inter_op_parallelism_threads = 8)
with tf.Session(config = config) as sess:
    tf.compat.v1.keras.backend.set_session(sess)
    model = load_model("test_model.h5")
    for frame in Frames:
    
        # =========================================================================
        # Call Read_Digit to extract each of the 7 digits available on the frame
        # =========================================================================
        (speed_ones_digit,  speed_tens_digit, 
         speed_hunds_digit, speed_thous_digit,
          dist_ones_digit,   dist_tens_digit, 
          dist_hunds_digit )                   = Read_Digit(frame, model)
        
        
        # =========================================================================
        # Compute the rocket speed based on the scraped digits
        # ========================================================================= 
        speed = (  speed_ones_digit
                 + speed_tens_digit*10
                 + speed_hunds_digit*100
                 + speed_thous_digit*1000)
        
        # =========================================================================
        # Compute rocket altitude based on scraped digits. Need to account for the
        # change in formatting of on-screen numbers as altitude exceeds 100 km (
        # which is true between frames 4687 and 10555)
        # =========================================================================
        if (int(frame) < 4687 ) | (int(frame) > 10555 ):
            altitude = (  dist_ones_digit*0.1 
                        + dist_tens_digit 
                        + dist_hunds_digit*10)
        else:
            altitude = (  dist_ones_digit
                        + dist_tens_digit*10
                        + dist_hunds_digit*100)        
            
        # =========================================================================
        # Assign values to dataframe, print encouraging numbers for runtime
        # =========================================================================
        df.loc[kk, 'Speed'] = speed
        df.loc[kk, 'Alt'] = altitude
        kk += 1
        end = time.time()
        print('You are {:.2f}% done after {:.1f} seconds'
              .format(kk/len(Frames)*100, end-start))
        print('Speed is: ', speed, 'm/s')
        print('Altitude is: ', altitude, 'km')
    
# =============================================================================
# Save to csv file
# =============================================================================
df.to_csv('Telemtry_Data.csv')