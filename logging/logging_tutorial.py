#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 12:24:28 2022

@author: jfrey
"""

# https://www.youtube.com/watch?v=-ARI4Cz-awo

import logging

# five levels of severity:
    # - debug (value of 10)
    # - info (val of 20)
    # - warning (30)
    # - error (40)
    # - critical (50)
    
# logging prints to either a file or to a shell/terminal console, NOT to the iPython console
logging.debug("this is a debug message") # nothing prints to terminal.
logging.info("this is an info message") # nothing prints to terminal
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

logging.basicConfig(level = logging.DEBUG) # debug and any level over that will now print to terminal
logging.debug("this is a debug message") 