# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 13:20:58 2020

@author: Dillon Morse
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import findiff as fd
from scipy.signal import savgol_filter
from scipy.integrate import DOP853

telemetry = pd.read_csv('Telemetry_Data.csv').drop(columns = 'Unnamed: 0')
telemetry['Speed'] = telemetry['Speed']/1000                            # In km/s


k = 2301/(9*60 + 3) #frames/second (assuming video ran at constant speed)
                    # Multiply every d/df deriv by k to account for this
                    # (chain rule)
  
d_df   = fd.FinDiff(0, 1, acc = 8)
d2_df2 = fd.FinDiff(0, 1, 2, acc = 8)                   
  
window_size = 101
poly_order = 1
                    
Alt   = savgol_filter(telemetry['Alt'],   window_size, poly_order)      # In km
Speed = savgol_filter(telemetry['Speed'], window_size, poly_order)      # In km/s


dAlt_dt = d_df( Alt )*k                                                 # In km/s
dX_dt   = np.sqrt( abs(Speed**2 - (dAlt_dt)**2) )                       # In km/s

dAlt_dt   = savgol_filter(dAlt_dt,   window_size, poly_order) 
dX_dt     = savgol_filter(dX_dt,     window_size, poly_order)


#dSpeed_dt = d_df( Speed )*k                                             # In m/s/s
d2Alt_dt2 = d2_df2( Alt )*(k **2)*1000                                      # In km/s/s
#dX2_dt2 = np.sqrt( abs( (dSpeed_dt)**2 - (d2Alt_dt2)**2 ) )             # In m/s/s
dX2_dt2 = d_df( dX_dt )*1000
       
d2Alt_dt2 = savgol_filter(d2Alt_dt2, window_size*2+1, poly_order) 
dX2_dt2   = savgol_filter(dX2_dt2,   window_size*2+1, poly_order)



Time_coord = np.arange(0, len(telemetry.index)*(1/k), (1/k))

fig, ( (ax1, ax2, ax5), (ax3, ax4, ax6) ) = plt.subplots(2,3)
ax1.plot(Time_coord, Speed )
ax1.set_ylabel('Total Speed (km/s)')
ax3.plot(Time_coord, Alt )
ax3.set_xlabel('time (seconds)') 
ax3.set_ylabel('Altitude (km)')

ax2.plot(Time_coord, dAlt_dt)
ax2.set_ylabel('Vertical Speed (km/s)')
ax4.plot(Time_coord, dX_dt )
ax4.set_ylabel('Horizontal Speed (km/s)')

ax5.plot(Time_coord, d2Alt_dt2)
ax5.plot(Time_coord, [-9.8/1]*len(Time_coord), 'r--')
ax5.set_ylabel('Vertical Acceleration (m/s/s)')
ax6.plot(Time_coord, dX2_dt2)
ax6.set_ylabel('Horizontal Acceleration (m/s/s)')



