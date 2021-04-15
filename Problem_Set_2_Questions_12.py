# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 11:13:01 2021

@author: mmalett
"""

# Melissa Malette BME 6311 Practice Set #2
# Sampling Statistics and the Central Limit Theorem
# 2/18/2021

# Question 1 
#Part 1: Import necessry packages 
from scipy.stats import poisson 
from scipy.stats import norm
import matplotlib.pyplot as plt 
from numpy import mean
from scipy.stats import ks_2samp
from numpy.random import seed
import math
from scipy import stats
import numpy as np
from scipy.stats import kstest

# Part 2: Poisson Distribution Sampling Points
seed(2)
N=200
x=[mean(np.random.poisson(lam=1, size=1000)) for _i in range(N)]
print(x)
plt.hist(x)
plt.xlabel("Frequency")
plt.ylabel("Probability Density")
plt.title("Poisson Distribution Samples")
plt.show()

# Part 3: Take the Z-score of the distribution of means 
zp=stats.zscore(x)

# Part 4: Normal Distribution Sampling Points 
y=[mean(norm.rvs(loc=0, size=1000)) for _i in range(N)]
print(y)
plt.hist(y)
plt.xlabel('Frequency')
plt.ylabel('Probability Density')
plt.title("Normal Distribution Samples")
plt.show()
zn=stats.zscore(y)

# Part 5: Preform a KS-test to check for normality 
ks_2samp(zp,zn)

#Question 2 
seed(2)
N=100
n=80
x=[mean(np.random.poisson(lam=1, size=n)) for _i in range(N)]
xx=mean(x)
print(xx)
print(x)
plt.hist(x)
plt.xlabel("Frequency")
plt.ylabel("Probability Density")
plt.title("Poisson Distribution Samples When n={}" .format(n))
plt.show()

# Part 3: Take the Z-score of the distribution of means 
zp=stats.zscore(x)

# Part 4: Normal Distribution Sampling Points 
y=[mean(norm.rvs(loc=0, size=n)) for _i in range(N)]
yy=mean(y)
print(yy)
print(y)
plt.hist(y)
plt.xlabel('Frequency')
plt.ylabel('Probability Density')
plt.title("Normal Distribution Samples When n={}" .format(n))
plt.show()
zn=stats.zscore(y)

# Part 5: Preform a KS-test to check for normality 
ks_2samp(zp,zn)





