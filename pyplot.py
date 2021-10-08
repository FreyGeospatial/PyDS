#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 21:41:55 2018

@author: jordanfrey
"""
import os
os.chdir("/Users/jordanfrey/Documents/OneDrive/Documents/School Work/Udemy/LearnPy")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline #for jupyter notebooks to show plot inline instead of new window

myTable = pd.read_csv("hw1_test_data.csv", index_col=0)
plt.plot(myTable)

help(pd.read_csv)