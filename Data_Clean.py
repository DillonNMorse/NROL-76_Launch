# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 13:20:58 2020

@author: Dillon Morse
"""

import pandas as pd


telemetry = pd.read_csv('Telemetry_Data.csv')


print(telemetry.head(5))