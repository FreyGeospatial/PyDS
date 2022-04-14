#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 12:39:01 2022

@author: jfrey
"""

# single leading underscores (e.g., _foo) are syntax hints more than anything, and are not enforced by the interpreter.
# a single leading underscore typically means that these objects are used internally

# a single trailing underscore (e.g., foo_) entails a reserved keyword, such as class, def, type, etc.

# single underscores are temporary or unusued variables
for _ in range(100):
    do_some_work()
    

# double leading and trailing underscores are dunder methods, and are reserved methods, e.g. __init__ or __str__

# double leading underscores, e.g., __bar
# ----should add some use cases here-----