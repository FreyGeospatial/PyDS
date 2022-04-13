#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 12:17:31 2022

@author: jfrey
"""

import config

config.a # you can see here that these variables are accessible from our config.py file located in this repository
config.b # just call config.<variable_name> and you will return its contents

# to update it, we will simply use normal assignment operators
config.a = 10
config.b = "alphabet"

# then we need to create a main.py file to test changes in value

