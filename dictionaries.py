# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:39:40 2019

@author: FreyGeospatial
"""
import numpy as np
#create dict
dict1 = {'key1':'val1', 'key2':'val2', 'key3':'val3'}

#access dict:
dict1["key1"]

mydata = np.arange(0,20)
mydata2 = mydata.reshape(4,5)

#required to prevent errors when dividing by 0.
import warnings
warnings.filterwarnings('ignore')

1 / mydata2

np.matrix.round(1/mydata2, 1) #round to 1 decimal place


##########################

# update: May 10, 2022:
    
cities = {"San Diego": "CA",
          "New York": "NY",
          "Detroit": "MI"}

print(cities)

# returns state abbr
def find_city(map, city): # map is a builtins function... help(map)
    # does something, returns some value
    if city in map:
        return map[city]
    else:
        return "Not Found"
    
find_city(cities, "New York")

# BUT! We can add this to dict:

cities['_found'] = find_city # add function as key-value pair in dict

cities["_found"](cities, "New York") # calls function and passes arguments to it

