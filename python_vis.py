# -*- coding: utf-8 -*-
"""
Created on Tue May 21 17:09:59 2019

@author: FreyGeospatial
"""

#RUN THE UDEMY MATRIX DATA FIRST!

import numpy as np
import matplotlib.pyplot as plt

Salary[0]
#defaults to line plot
plt.plot(Salary[0])

plt.rcParams['figure.figsize'] = 8,4 #change plot dimensions

plt.plot(Salary[0], 
         c = 'Black', #color
         ls = '--', #line style
         marker = 's', #marker type
         ms = 10) #marker size


#run both together, notebook style
plt.plot(Salary[0], 
         c = 'Black', #color
         ls = '--', #line style
         marker = 's', #marker type
         ms = 10) #marker size
plt.xticks(list(range(0,10)), Seasons) #changes x axis labels to years


#run all together notebooks style
plt.plot(Salary[0], 
         c = 'Black', #color
         ls = '--', #line style
         marker = 's', #marker type
         ms = 10, #marker size
         label = Players[0]) 
plt.plot(Salary[1], 
         c = 'Red', #color
         ls = '--', #line style
         marker = 'o', #marker type
         ms = 10, #marker size
         label = Players[1]) 
plt.xticks(list(range(0,10)), Seasons, rotation = 'vertical') #changes x axis labels to years, and change text direction



#run all together notebooks style
plt.plot(Salary[0], 
         c = 'Black', #color
         ls = '--', #line style
         marker = 's', #marker type
         ms = 10, #marker size
         label = Players[0]) 
plt.plot(Salary[1], 
         c = 'Red', #color
         ls = '--', #line style
         marker = 'o', #marker type
         ms = 10, #marker size
         label = Players[1]) 
plt.xticks(list(range(0,10)), Seasons, rotation = 'vertical') #changes x axis labels to years, and change text direction
plt.legend()