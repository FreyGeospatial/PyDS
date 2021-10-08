# -*- coding: utf-8 -*-
"""
Created on Tue May 21 18:57:44 2019

@author: FreyGeospatial
"""

#RUN THE UDEMY MATRIX DATA FIRST!

import numpy as np
import matplotlib.pyplot as plt


throwsPerGame = FieldGoalAttempts / Games
overall_accuracy = FieldGoals/FieldGoalAttempts


#plot free throw attempts per game


def throws(player):
    plt.plot(throwsPerGame[Pdict[player]], label = player, ls = "--", marker = 's')
    
def accuracy(player):
    plt.plot(overall_accuracy[Pdict[player]], label = player, ls = "--", marker = 's')