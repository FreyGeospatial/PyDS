#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 16:36:52 2022

@author: jfrey
"""

# type annotations are also known as type signatures. They are used to identify the data type of input/output of functions and methods
# in many language (e.g., java), data types must be declared. Not so in Python


from typing import Union, TypeVar
T = TypeVar('T')

help(TypeVar) # type variables exist primarily for the benefit of static type checkers
                # they serve as the params for generic types as well as for generic function definitions.

def f(x: T) -> Union[str, None]:
    if x:
        return "x"
    
f("blah") # returns 'x'
f(1) # returns 'x'
f() # errors out
f(None) # does not return anything

# it
