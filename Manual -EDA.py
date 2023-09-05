# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 10:28:41 2022

@author: NCBC
"""
# EDA on IPL Dataset
# Importing libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# **Importing IPL dataset**
data=pd.read_csv("matches.csv")
data.head(5)


# How big is the dataset? (Rows and columns)
data.shape
data.info()
data.columns

# Statistical Description of dataset
data.describe()

# Finding Unique
data.nunique()
# How many IPL seasons are we using to analyse?**
data['Season'].unique()

# Finding out NaN values
data.isna().any()
data.isna().sum()

# Indexing Dataframe
data['city'].isna().sum()

# Dataframe.[ ] ; This function also known as indexing operator
# Dataframe.loc[ ] : This function is used for labels.
# Dataframe.iloc[ ] : This function is used for positions or integer based
# loc is label-based, which means that you have to specify rows and columns based on their row and column labels.
# iloc is integer position-based, so you have to specify rows and columns by their integer position values (0-based integer position).

# retrieving all rows and some columns by loc method
first = data.loc[:, ["id", "city"]]
# retrieving rows by iloc method 
row2 = data.iloc [:, [1, 2]]
# retrieving multiple rows by iloc method 
row2 = data.iloc [[3, 5, 7]]
# retrieving all rows and some columns by iloc method 
# ?










row3=data.iloc[:, :]

# How many matches (in total) were played according to the dataset?
data['id'].count()

# Which IPL team won by scoring the maximum runs?
data['win_by_runs'].idxmax()

# Which IPL team won by consuming maximum wickets?
# Which IPL team won by taking minimum wickets?
data.iloc[data['win_by_wickets'].idxmax()]
data.iloc[data['win_by_wickets'].idxmin()]


b=data.groupby('Season')
b=data.groupby(['Season','city'])

# Highest wins by teams per season
data.groupby('Season')['winner'].value_counts()
data['toss_decision'].value_counts()

# Man of the match - Highest to lowest (in won matches)
data['player_of_match'].value_counts()

# In which city were the number of matches played?
data['city'].value_counts()

# Histograms represent the data distribution by forming bins 
# along the range of the data and then drawing bars to show the 
#number of observations that fall in each bin.
sns.distplot(x=data['win_by_wickets'], kde = True)
plt.show()

a=((data['win_by_wickets'] == 2).sum())

# Which season consisted of the highest number of matches ever played?
fig_dims = (20, 4)
fig, ax = plt.subplots(figsize=fig_dims)
sns.countplot(x='Season', ax=ax,data=data)
plt.show()

# Which city consisted of the highest number of matches ever played?
fig_dims = (50, 30)
fig, ax = plt.subplots(figsize=fig_dims)
sns.countplot(x='city', ax=ax,data=data)
plt.show()

aa=data['player_of_match'].value_counts()

# Which player_of_match won number of matches ever played?
fig_dims = (50, 30)
fig, ax = plt.subplots(figsize=fig_dims)
sns.countplot(x='player_of_match', ax=ax,data=data)
plt.show()

# Which is the most successful IPL team with all the data at hand?
data1 = data.winner.value_counts()
sns.barplot(y = data1.index, x = data1)

# What is the probability of winning a match if the toss was won?
probability_of_win = data['toss_winner'] == data['winner']
# probability_of_win.groupby(probability_of_win).size()
sns.countplot(probability_of_win)


# Swarmplot
ax = sns.swarmplot(x=data1, y=data1.index, data=data)
plt.title('Graph')
plt.show()

fig_dims = (30, 10)
fig, ax = plt.subplots(figsize=fig_dims)
ax = sns.swarmplot(y=data['win_by_runs'], x=data['Season'], data=data)
plt.title('Graph')
plt.show()

data=pd.read_csv("iris.csv")
data.head(5)
#Relation Plot
sns.pairplot(data)
#ScatterPLot relation between two continous variable
sns.relplot(x='sepal.length',y='sepal.width',data=data)
#distribution of data
#! distplot
sns.distplot(data['sepal.length'])
#2catplot
#x=data['sepal.length']
sns.catplot(x=data['sepal.length'],kind='box',data=data)

