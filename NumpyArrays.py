#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 10:43:48 2017

@author: jordanfrey
"""

import numpy as np
l = [123, 55665, -21, 343]

#convery list to numpy array
np.array(l)

#why use array as opposed to list?
#1) cannot have different data types in array
#2) more methods available for arrays

#returns last element of list, but that element no longer exists in
#the original list
l.pop()
l

a = np.array(l)
a.mean()