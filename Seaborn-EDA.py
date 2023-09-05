# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 14:53:44 2022

@author: NCBC
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

c=sns.load_dataset('iris')
#Box Plot
sns.boxplot( y=c["sepal_width"] )
#Density Plot
sns.displot(x=c["sepal_width"])


a=sns.load_dataset('flights')

#Visualizing Statical Relationship
sns.relplot(x='passengers',y='month',data=a)
sns.relplot(x='passengers',y='month',hue='year',data=a)
sns.relplot(x='month',y='passengers',kind='line',data=a)

sns.relplot(data=a, x="month", y="passengers", col="year",hue="year", style="year", kind="line",)

#Visualizing Categorical Data
a=sns.load_dataset('tips')
# Neither the `x` nor `y` variable appears to be numeric.
sns.catplot(x='day',y='total_bill',data=a,kind="bar")

# Categorical scatterplots:
# stripplot() (with kind="strip"; the default)
# swarmplot() (with kind="swarm")

# Categorical distribution plots:
# boxplot() (with kind="box")
# violinplot() (with kind="violin")
# boxenplot() (with kind="boxen")

# Categorical estimate plots:
# pointplot() (with kind="point")
# barplot() (with kind="bar")
# countplot() (with kind="count")

#Visualizing Distribution Data joinplot
# distplot
#Displot It is used basically for univariant set of observations and visualizes it through a histogram
sns.distplot(a['passengers'], kde = False, color ='red', bins = 50)

#Joinplot kind ='kde'
#It is used to draw a plot of two variables with bivariate and univariate graphs. It basically combines two different plot
sns.jointplot(x ='total_bill', y ='tip', data = a)

from scipy import stats
c=np.random.normal(loc=5,size=100,scale=2)
sns.distplot(c)


#Grid Plot
c=sns.load_dataset('iris')
d=sns.FacetGrid(c,col='species')
d.map(plt.hist,'sepal_length')

d=sns.PairGrid(c)
d.map(plt.scatter)

