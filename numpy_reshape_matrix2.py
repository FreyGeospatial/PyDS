# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:24:40 2019

@author: FreyGeospatial
"""

import numpy as np

#create an array, 0-19
np.arange(0, 20)

mydata = np.arange(0,20)

#reshape vector into a matrix of 5 rows by 4 columns
MATR1 = np.reshape(mydata, (5,4), order = 'C') #by row
MATR2 = np.reshape(mydata, (5,4), order = 'F') #by column

#get 10
MATR1[2,2]
MATR2[0,2]
