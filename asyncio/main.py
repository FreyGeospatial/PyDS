#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 08:47:49 2022

@author: jfrey
"""

import asyncio

# # this will work in shell but not in iPython                                                    # example of SYNCHRONOUS PRGMING
# async def main():                                                                               # within an ASYNCHRONOUS environment
#     print("A")                                                                                  ####################################
#     await other_function() # wait for this function to finish, and dont do anything else        ####################################
#     print("B") # then after waiting for 1 sec, print B                                          ####################################
#                                                                                                 ####################################
# async def other_function():                                                                     ####################################
#     print("1")                                                                                  ####################################
#     await asyncio.sleep(2)                                                                      ####################################
#     print("2")                                                                                  ####################################
#                                                                                                 ####################################
# asyncio.run(main())                                                                             ####################################


