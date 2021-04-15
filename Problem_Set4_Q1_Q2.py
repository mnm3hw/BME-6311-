# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 13:40:30 2021

@author: mmalett
"""

# Melissa Malette
# BME 6311
# Practice Set 4: Visualization 

# Question 1
import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt
from scipy import stats 
from scipy.stats import median_test
from scipy.stats import ks_2samp

# Part 1: Read in the data from excel
df = pd.read_csv(r'C:\Users\Melissa\Documents\bme6311\heart.csv')

# Part 2: Make a basic scatterplot 
rbp=df["Resting Blood Pressure (mm/Hg)"]
heartdisease=df["target"]
sex=df["sex"]
g=sns.relplot(x='Heart Disease Status', y='Resting Blood Pressure (mm/Hg)', hue='Sex', data=df).set(title='Heart Disease Status vs. Resting Blood Pressure')
sns.set(font_scale=1.5)

# Part 3: Make a catplot
sns.set_theme(style="ticks", color_codes=True)
print(df.head(14))
sns.catplot(x='Heart Disease Status', y='Resting Blood Pressure (mm/Hg)', hue='Sex', data=df).set(title='Heart Disease Status vs. Resting Blood Pressure')
sns.set(font_scale=1.5)

# Part 4: Statistical correlation 
stats.pointbiserialr(heartdisease,rbp)
stats.pointbiserialr(sex,rbp)


# Question 2


# Part 2: Box plot comparing heart disease and serum cholesterol
noheartdisease=df[df["target"]==0]
heartdisease=df[df["target"]==1]
hdserum=noheartdisease["Serum Cholesterol in mg/dl"]
ndhserum=heartdisease["Serum Cholesterol in mg/dl"]
serum=df["Serum Cholesterol in mg/dl"]
x='Heart Disease Status'
y="Serum Cholesterol in mg/dl"
hue="Sex"
sns.catplot(x,y,kind='box', hue='Sex',data=df, palette='Blues', showmeans=True,
            meanprops={"marker":"*",
                       "markerfacecolor":"black", 
                       "markeredgecolor":"black",
                       "markersize":"8"}).set(title='Heart Disease Status vs. Serum Cholesterol')
sns.set(font_scale=1.7)
plt.text(2+0.2, 4.5, "* = mean ", horizontalalignment='left', size='small', color='black')

# stats 
pd.set_option('display.expand_frame_repr', False)
df.groupby([x,hue])[y].describe()
stat, p, med, tbl = median_test(hdserum,ndhserum)
med
p
stat
tbl


# Part 3: Make a violin plot of part 2
x='Heart Disease Status'
y="Serum Cholesterol in mg/dl"
sns.catplot(x,y,kind='violin', hue='Sex',data=df, palette='Blues').set(title='Heart Disease Status vs. Serum Cholesterol')
plt.text(2+0.2, 4.5, "* = mean ", horizontalalignment='left', size='small', color='black')

# stats 
df.groupby([x,hue])[y].describe()

ks_2samp(hdserum,ndhserum)

