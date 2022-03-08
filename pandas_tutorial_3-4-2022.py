# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 12:52:17 2022

@author: jfrey
"""
# tutorial:
# https://www.youtube.com/watch?v=zmdjNSmRXF4&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=2

# data:
# https://insights.stackoverflow.com/survey

import pandas as pd
import os
os.getcwd()

df = pd.read_csv('pyds/stack-overflow-developer-survey-2020/survey_results_public.csv')
df.head()

# data schema, data dictionary
schema_df = pd.read_csv('pyds/stack-overflow-developer-survey-2020/survey_results_schema.csv')
schema_df

######################
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
######################

df.head()
df.shape # ~64,000 rows, 61 columns
df.columns

# Who programs as a hobby? Multiple ways to get this data
df['Hobbyist'].value_counts() # for counting categorical data
                                # ~50,000 said yes

df.loc[0, 'Hobbyist'] # first row, hobbyist column
df.loc[range(0,3), 'Hobbyist'] # first 3 rows, hobbyist column
df.loc[0:2, 'Hobbyist'] # first 3 rows, hobbyist column
df.loc[0:2, 'Hobbyist':'Employment'] # first 3 rows, hobbyist column through employment

################################# ^^^ finishes parts 1-2
################################################################
# PART 3: INDEXES ##############################################
################################################################
################################################################

# what is a pandas index?
people_df # index would be the row numbers (0,1,2) and are usually unique.

# can also manually set index:
people_df.set_index('email', inplace = True) # email now replaces rownumbers
                                            # inplace = True makes this change
                                            # actually occur, not just temporarily
people_df.index
people_df
people_df['email'] # no longer exists as it is now index
people_df.loc['CoreyMSchafer@gmail.com', 'last']

# to reset index...
people_df.reset_index(inplace=True)
people_df
###############################
# can also just set index within read_csv function
df = pd.read_csv('pyds/stack-overflow-developer-survey-2020/survey_results_public.csv', index_col = "Respondent")
df.head()

schema_df.set_index("Column", inplace = True)
schema_df.sort_index(inplace=True)

################################################################
# PART 4: FILTERING ############################################
################################################################
################################################################

# filter all rows that contain "doe" as last name
people_df['last'] == "Doe" # same as in R: people_df$last == "Doe"
type(people_df['last'] == "Doe")
people_df[(people_df['last'] == "Doe")] # parenthesis not necessary, but does help
                                        # readability...
                                        
# reset index
people_df.reset_index(inplace=True)
# just email column                       
people_df.loc[(people_df['last'] == "Doe"), 'email']


people_df.loc[(people_df['last'] == "Doe") & (people_df['first'] == "John")] # AND
people_df.loc[(people_df['last'] == "Schafer") | (people_df['first'] == "John")] # OR

# NEGATE FILTER: '~' instead of '!'
people_df.loc[~((people_df['last'] == "Schafer") | (people_df['first'] == "John"))] # OR

# same as R's %in% operator
df['Country'].isin(['United Stares', 'India', 'United Kingdom', 'Germany', 'Canada'])


# find high salaries in select countries
schema_df.loc['ConvertedComp', 'QuestionText'] # describe convertedcomp column
df.loc[(df['ConvertedComp'] > 70000) & (df['Country'].isin(['United Stares', 'India', 'United Kingdom', 'Germany', 'Canada'])& (df['LanguageWorkedWith'].str.contains('Python', na=False))), ['Country', 'LanguageWorkedWith', 'ConvertedComp']] # do not include NaN's

###################################################
# vectorized concatenation
people_df['first'] + ' ' + people_df['last']
# create new column, 'full_name'
people_df['full_name'] = people_df['first'] + ' ' + people_df['last']
people_df['full_name']
# drop columns
people_df.drop(columns=['first', 'last'], inplace=True)
people_df['full_name'].str.split(' ')








