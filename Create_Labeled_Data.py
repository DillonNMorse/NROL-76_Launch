# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 16:23:44 2020

@author: Dillon Morse
"""

import numpy as np
import random
from Digit_Retrieve import Retrieve_Digit
import matplotlib.pyplot as plt
import pickle


# =============================================================================
# Create list of frame numbers as strings to retrieve image files
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
# Set number of frames which will be labelled. Randomly select that amount.
# =============================================================================
num_to_label = 30
sub_Frames = random.choices(Frames, k = num_to_label)

# =============================================================================
# Iterate through the randomly selected frames, prompt user for labels.
# =============================================================================
X = []
y = []
kk = 0
for frame in sub_Frames:
    pict_list = Retrieve_Digit(frame)
    for digit in np.arange(0,7,1):
        pict = pict_list[digit]
        X.append( pict )
        plt.imshow( pict  )
        plt.show()
        txt = input('Type number: ')
        y.append(txt)
    kk += 1
    print('You are {:.2f}% done!'.format(kk/num_to_label*100))
Labeled_data = X, y
        
# =============================================================================
# Print label data for use as training data in Digit_Reader
# =============================================================================
filename = 'Labeled_Digits'
outfile = open(filename, 'wb')
pickle.dump(Labeled_data, outfile)
outfile.close()