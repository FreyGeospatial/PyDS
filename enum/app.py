#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 13:51:22 2022

@author: jfrey
"""
# from youtube video "Learn Enum in object-oriented python" by Programmable Finance

from enum import Enum, auto

# auto class instances generated are replaced with an appropriate value in Enum class suites
class Suite(Enum):
    DIAMOND = auto()
    CLUB = auto()
    HEART = auto()
    SPADE = auto()
    
# this will return a value of 2 automatically!
Suite.CLUB.value

class Value(Enum):
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    TEN = auto()
    JACK = auto()
    QUEEN = auto()
    KING = auto()
    ACE = auto()
    
class Card:
    def __init__(self, suite: Suite, value: Value):
        self.suite = suite
        self.value = value
    
    @property
    def suite(self):
        return self._suite # convention for private, internal variables is to use underscore
    
    @property
    def value(self):
        return self._value
    
    @suite.setter
    def suite(self, suite: Suite): # paramater name suite is expecting Suite object type
        if suite not in Suite:
            raise Exception
        self._suite = suite
    
    
    @value.setter
    def value(self, value: Value): # paramater name value is expecting Value object type
        if value not in Value:
            raise Exception
        self._value = value
        
    
    def __repr__(self):
        return f"<Card {self.value} of {self.suite}>"
    

class Deck:
    def __init__(self):
        self.cards = [Card(s, v) for s in Suite for v in Value]
        
    def __repr__(self):
        output = [f"{c}\n" for c in self.cards]
        return "".join(output)
    
        
        
        
    
    
    
    
    
    
    
    