#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 07:55:39 2017

@author: jordanfrey


"""
import pandas as pd

stats = pd.read_csv("D:/OneDrive/Documents/School_Work/Udemy/LearnPy/DemographicData.csv")

#change working directory
import os
os.getcwd()
os.chdir("D:/OneDrive/Documents/School_Work/Udemy/LearnPy")

#number of rows
len(stats)
stats.columns #column names
stats.head(6)
stats.tail(6)
stats.info() #like str()
stats.describe() #like summary()

#rename column
stats.columns = ['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers',
       'IncomeGroup']


# print first rows 10 - 20
stats[10:20]
stats[10:]
stats[: : -1] #reverse order (step)
stats["CountryName"]
stats[["CountryName", "BirthRate"]]
stats[3:5]["BirthRate"]
stats["BirthRate"][3:5]
stats.BirthRate

# subsetting
stats[["CountryCode", "BirthRate", "InternetUsers"]][4:8]
result = stats.BirthRate * stats.InternetUsers
stats['MyCalc'] = stats.BirthRate * stats.InternetUsers

#remove column
stats = stats.drop('MyCalc', axis=1)

#filtering
Filter = stats.InternetUsers < 2 #like which
stats[Filter] #like which

Filter2 = stats.InternetUsers < 2

#error. Why? Python is not a vectorized language; AND works with single value
stats[stats.BirthRate > 40 and stats.InternetUsers < 2]
stats[Filter and Filter2] #is the statement logically true?
stats[Filter & Filter2] #vectorized
# https://stackoverflow.com/questions/22646463/and-boolean-vs-bitwise-why-difference-in-behavior-with-lists-vs-nump

stats[stats.IncomeGroup == "High income"]

stats.IncomeGroup.unique()

#indexing!!!
stats[3,4] #error- not numpy array!
stats.iat[3,4] #by position
stats.iloc[3,4] #by position
stats.at[3,'IncomeGroup'] #by row and column names!
stats.loc[3,'IncomeGroup'] #by row and column names!


import matplotlib.pyplot as plt
import seaborn as sns #extension for matplotlib
import warnings

warnings.filterwarnings('ignore')

vis1 = sns.distplot(stats.InternetUsers, 
                    bins = 30)

vis2 = sns.boxplot(data = stats,
                   x = "IncomeGroup",
                   y = "BirthRate")

#Seaborn Gallery











#change working directory
#os.chdir("/Users/jordanfrey/Documents/OneDrive/Documents/School Work/Syracuse/Applied Data Science/LearnPy") #mac
#os.chdir("E:/OneDrive/Documents/School Work/Udemy/LearnPy") #pc
os.chdir("D:/OneDrive/Documents/School Work/Udemy/LearnPy") #remote


#confirm working directory
os.getcwd()

#store csv in variable
myData = pd.read_csv("DemographicData (1).csv")
type(myData)

#finds length of data (number of ROWS)
len(myData) #195 rows imported

#display the columns
myData.columns

#number of columns
len(myData.columns)

#top 5 rows
myData.head()

#top 6 rows
myData.head(6)

#tail
myData.tail()

#information (similar to str() function in R)
myData.info()

#summary statistics (on numeric variables)
myData.describe()

#transpose flips the data frame
myData.describe().transpose()

#rename columns
myData.columns = ['CountryName', 'CountryCode', 'BirthRate', \
                  'InternetUsers','IncomeGroup']

myData.head()

#slicing df
myData[21:26]
myData[21:]
myData[:10]

#reverse order of df (remember stepping)
myData[: :-1]

#slice by name
myData['IncomeGroup']

myData['IncomeGroup'].head()

#must pass as list, so double brackets
myData[['CountryCode', 'IncomeGroup']].head()

#for quick access to a column (similar to R's $function)
myData.IncomeGroup
myData.IncomeGroup.head()

myData[['CountryCode', 'IncomeGroup']][4:8]

