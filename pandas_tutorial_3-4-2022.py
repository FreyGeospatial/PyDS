# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 12:52:17 2022

@author: jfrey
"""

# https://www.youtube.com/watch?v=zmdjNSmRXF4&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=2

import pandas as pd
import os
os.getcwd()

df = pd.read_csv('pyds/stack-overflow-developer-survey-2020/survey_results_public.csv')
df.head()

# data schema, data dictionary
schema_df = pd.read_csv('pyds/stack-overflow-developer-survey-2020/survey_results_schema.csv')
schema_df

######################

person = {
    "first": "Corey",
    "last": "Schafer",
    "email": "CoreyMSchafer@gmail.com"
    }


people = {
    "first": ["Corey", "Jane", "John"],
    "last": ["Schafer", "Doe", "Doe"],
    "email": ["CoreyMSchafer@gmail.com", "JaneDoe@email.com", "JohnDoe@email.com"]
    }

people
people["email"]
people["email"][0]
type(people["email"]) # list

# create df from dictionary
people_df = pd.DataFrame(people)
people_df
people_df['email']
people_df['email'][0]
type(people_df['email']) # pandas series object, 1-Dimensional
people_df.email
type(people_df.email) # pandas series object -- two different ways of 
                      # displaying same data of same type
                      
people_df[['last', 'email']] # like how R requires you to provide a vector, Python
                             # requires a 
                             
type(people_df[['last', 'email']]) # pandas dataframe

people_df[['last', 'email']].iloc[0] # iloc = integer location for ROW
people_df[['last', 'email']].iloc[[0,1]] # iloc = integer location for ROW
type(people_df[['last', 'email']].iloc[0]) # returns a series
type(people_df[['last', 'email']].iloc[[0,1]]) # returns a dataframe

# can also subset df another way:
    people_df.iloc[[0,1], 2] # 2 is the column integer location

people_df.loc[[0,1], "email"] # loc = location for ROW. Can take strings.
                              # since rownames are just integers, 
                              # it will take integers for rows too
people_df.loc[[0,1], ["last", "email"]]




######################
