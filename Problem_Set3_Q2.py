# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 12:58:47 2021

@author: mmalett
"""

# Melissa Malette 
# BME 6311
# Practice Set #3 Stats 2 

# Question 2 
import numpy as np 
from numpy import mean 
from numpy.random import seed
from scipy import stats 
# Part 1: Initial Data 
n_white=17
n_black=4
# degrees of freedom = n-1 
df_white=n_white-1
df_black=n_black-1
stdev_white=1.6
stdev_black=1.6
mean_white=0.6 
mean_black=x 


# create two random normal distributions based on this
seed(1) 
white_patients=np.random.normal(0.6, 1.6, 17) 
black_patients=np.random.normal(0.938, 1.6, 4)

# calculate the means 
m1=mean(white_patients)
m2=mean(black_patients)
diff=m1-m2
print('The effect size is: {} '. format(diff)) 

# do the t-test
t2,p2=stats.ttest_ind(white_patients,black_patients)
print("t = " + str(t2))
print("p = " + str(p2))
