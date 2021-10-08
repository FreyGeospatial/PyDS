# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# check this resource: https://jakevdp.github.io/PythonDataScienceHandbook/03.10-working-with-strings.html

import numpy as np

# simple vector
x = np.array([2, 3, 5, 7, 11, 13])

# simple scalar function on vector
x*2 

# vectorized operations on strings is a little different in Python
data = ['peter', 'Paul', 'MARY', 'gUIDO']

# essentially an anonymous function (remember lapply() in R)
[s.capitalize() for s in data]

# in R, anonymous functions are written as:
#    lapply(data, function(s){
#        toTitleCase(s)
#    })

# this breaks with None values
data = ['peter', 'Paul', None, 'MARY', 'gUIDO']
[s.capitalize() for s in data]


import pandas as pd
names = pd.Series(data)
names

# vectorized function now works in pandas series
names.str.capitalize()





