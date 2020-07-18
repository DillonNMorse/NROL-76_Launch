# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 13:20:58 2020

@author: Dillon Morse
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

import numpy as np
import findiff as fd
from scipy.signal import savgol_filter

# =============================================================================
# Read data, convert speed to km/s
# =============================================================================
telemetry = pd.read_csv('Telemetry_Data.csv').drop(columns = 'Unnamed: 0')
telemetry['Speed'] = telemetry['Speed']/1000                            # In km/s

# =============================================================================
# Define conversion between frames and seconds, useful for computing
# derivatives as well as for defining the time coordinate
# =============================================================================
k = 2301/(9*60 + 3) 
                  
# =============================================================================
#   Define operators for first and second derivatives
# =============================================================================
d_df   = fd.FinDiff(0, 1, acc = 8) # axis zero, first derivative, accuracy = 8
d2_df2 = fd.FinDiff(0, 1, 2, acc = 8)                   
  
# =============================================================================
# Smooth the scraped data, replace every point with the polynomial fit to all
# data in a window centered at that point
# =============================================================================
window_size = 101
poly_order = 1
                    
Alt   = savgol_filter(telemetry['Alt'],   window_size, poly_order)      # In km
Speed = savgol_filter(telemetry['Speed'], window_size, poly_order)      # In km/s

# =============================================================================
# Compute both components of speed vector, then smooth.
# =============================================================================
dAlt_dt = d_df( Alt )*k                                                 # In km/s
dX_dt   = np.sqrt( abs(Speed**2 - (dAlt_dt)**2) )                       # In km/s

dAlt_dt   = savgol_filter(dAlt_dt,   window_size, poly_order) 
dX_dt     = savgol_filter(dX_dt,     window_size, poly_order)

# =============================================================================
# Compute second derivatives, then smooth
# =============================================================================
d2Alt_dt2 = d2_df2( Alt )*(k **2)*1000                                  # In m/s/s
dX2_dt2 = d_df( dX_dt )*1000                                            # In m/s/s
       
d2Alt_dt2 = savgol_filter(d2Alt_dt2, window_size*2+1, poly_order) 
dX2_dt2   = savgol_filter(dX2_dt2,   window_size*2+1, poly_order)

# =============================================================================
# Define time coordinate
# =============================================================================
Time_coord = np.arange(0, len(telemetry.index)*(1/k), (1/k))


# =============================================================================
# Make plot for Speed and Altitude
# =============================================================================
fig, axes_1 = plt.subplots(2,1)

( ax1, ax2 ) = axes_1

ax1.plot(Time_coord, Speed )
ax1.set_ylabel('Total Speed (km/s)')
ax2.plot(Time_coord, Alt )
ax2.set_ylabel('Altitude (km)')



ax_list = fig.axes
ml = MultipleLocator(60)
for ax in ax_list:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.xaxis.set_minor_locator(ml)
plt.tight_layout()

fig.text(0.5, -0.02, 'Time Since Launch (minutes)', ha='center')

plt.setp(axes_1,
         xticks = np.arange(0,Time_coord[-1], 180),
         xticklabels = [0, 3, 6, 9])

plt.savefig('NROL-76_Telemetry_Information.jpeg',
            dpi = 100,
            bbox_inches = 'tight',
            transparent = True)
plt.show()




# =============================================================================
# Make plot for Speed and Acceleration
# =============================================================================
fig, axes_2 = plt.subplots(2,2)

( (ax1, ax2), (ax3, ax4) ) = axes_2

ax1.plot(Time_coord, dAlt_dt)
ax1.set_ylabel('Speed (km/s)')
ax1.set_title('Vertical Motion')
ax2.plot(Time_coord, dX_dt )
ax2.set_title('Horizontal Motion')

ax3.plot(Time_coord, d2Alt_dt2)
ax3.plot(Time_coord, [-9.8/1]*len(Time_coord), 'r--')
ax3.set_ylabel('Acccel. (m/s/s)')
ax4.plot(Time_coord, dX2_dt2)

ax_list = fig.axes
for ax in ax_list:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.xaxis.set_minor_locator(ml)
plt.tight_layout()

fig.text(0.5, -0.02, 'Time Since Launch (minutes)', ha='center')

plt.setp(axes_2,
         xticks = np.arange(0, Time_coord[-1], 180),
         xticklabels = [0, 3, 6, 9] )

plt.savefig('NROL-76_Speed_and_Accel.jpeg',
            dpi = 100,
            bbox_inches = 'tight',
            transparent = True)
plt.show()