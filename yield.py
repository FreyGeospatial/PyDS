#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 13:19:42 2022

@author: jfrey
"""

def x():
    i = 1
    while True: 
        return i * i # return immediately exits function
    
    # y() does not return scalar values like x() does when called. Must access through iteration.
def y():
    i = 1
    while True: 
        yield i * i # return immediately exits function
        i += 1

for num in y():
    if num > 100:
        break
    print(num)