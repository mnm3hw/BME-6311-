# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 09:52:18 2021

@author: mmalett
"""

# Melissa Malette
# BME 6311
# Practice Set #3 Stats 2 

# Question 1
import numpy as np 
from numpy import mean 
from numpy.random import seed
from scipy import stats 

# when n=5
seed(1)
N=10
mu, sigma=6,2
mu2, sigma2=3, 2
distribution1=np.random.normal(6, 2, N) 
distribution2=np.random.normal(3, 2, N) 
print('The known difference between means is : {}' .format(mu-mu2))

m1=mean(distribution1)
m2=mean(distribution2)
diff=m1-m2
print('The actual difference between means is: {} '. format(diff))

t2,p2=stats.ttest_ind(distribution1,distribution2)
print("t = " + str(t2))
print("p = " + str(p2))

# when n=10
seed(1)
N=25
mu, sigma=6,2
mu2, sigma2=3, 2
distribution1=np.random.normal(6, 2, N) 
distribution2=np.random.normal(3, 2, N) 
print('The known difference between means is : {}' .format(mu-mu2))

m1=mean(distribution1)
m2=mean(distribution2)
diff=m1-m2
print('The actual difference between means is: {} '. format(diff))

t2,p2=stats.ttest_ind(distribution1,distribution2)
print("t = " + str(t2))
print("p = " + str(p2))

# when n=25
seed(1)
N=50
mu, sigma=6,2
mu2, sigma2=3, 2
distribution1=np.random.normal(6, 2, N) 
distribution2=np.random.normal(3, 2, N) 
print('The known difference between means is : {}' .format(mu-mu2))

m1=mean(distribution1)
m2=mean(distribution2)
diff=m1-m2
print('The actual difference between means is: {} '. format(diff))

t2,p2=stats.ttest_ind(distribution1,distribution2)
print("t = " + str(t2))
print("p = " + str(p2))




