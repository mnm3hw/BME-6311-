# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 09:52:18 2021

@author: mmalett
"""

# Melissa Malette
# BME 6311
# Practice Set #3 Stats 2 

# Question 1: Statistical Power 
from numpy.random import seed
import numpy as np
from scipy import stats 
from numpy import mean

# Part 1: Use sampling from two different distributions and calculate the means 
N=10
seed(1)
x=stats.norm.rvs(loc=8, scale=10, size=N)
m1=mean(x)
seed (2)
y=stats.norm.rvs(loc=5, scale=10, size=N)
m2=mean(y)
meandiff=m1-m2
print("The difference in means is: {} " .format(meandiff))
# Part 2: Calculate the standard deviations 
#var_x=x.var(ddof=1)
#var_y=y.var(ddof=1)
#stdev=np.sqrt((var_x+var_y)/2)
#stdev

# Part 3: T test 
#ttest=(x.mean()-y.mean())/(stdev*np.sqrt(2/N))
#df=2*N-2
#p=1-stats.t.cdf(ttest,df=df)
#print("t= " +str(ttest))
#print("p= " + str(2*p))


t2,p2=stats.ttest_ind(x,y)
print("t = " + str(t2))
print("p = " + str(p2))