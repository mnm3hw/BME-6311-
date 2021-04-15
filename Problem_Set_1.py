# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 11:45:03 2021

@author: mmalett
"""
# Melissa Malette BME 6311 
# Practice Set 2 Statistics 1
# 2/18/2021 

# I want to know the average weight of women ages 35-45 years old in the US  
# Weights will range from 125 to 180 lbs 
# n=50 women 

from numpy.random import seed
from numpy.random import randint
from numpy import mean

# Part 1: create a sample of women's weights 
n=50
weight=randint(125,180,n);
print(weight)
print('The average weight is {} pounds.' .format(mean(weight)))

# Part 2: repeat the sampling 1000 times 
import matplotlib.pyplot as plt 
# calculate the mean of 50 women's weights 1000 times 
means= [mean(randint(125,180,n)) for _ in range(1000)]

# Part 3: plot the distribution of the sample means
plt.hist(means)
plt.xlabel("Women's weights [pounds]")
plt.ylabel("Probability Density")
plt.title("Distribution of Women's Weights when n={}" .format(n))
plt.show()
print('The mean is {}.' .format(mean(means)))

# Part 4: use a shapiro-wilk normality test to confirm normal distribution 
# Ho: the women's weight data follows a normal distribution
# H1: the women's weight data does NOT follow a normal distribution 
from scipy.stats import shapiro 
stat, p=shapiro(means)
print('Test Statistic={}, p={}' .format(stat,p))
alpha=0.05;
if p> alpha: 
    print('Sample follows a normal distribution, do not reject the null hypothesis')
else: 
    print('The sample does not follow normal distribution, reject the null')
    
# Part 5: repeat with a greater sample size
# change the sample size in lines 17 and 24 from 50 to 100 then 1000 and compare the results 
# the higher the sample size, the higher the p-value and confidence that the data is distributed normally 