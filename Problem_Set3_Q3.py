# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 10:19:20 2021

@author: mmalett
"""

# Melissa Malette 
# BME 6311 Practice Set 3 

# Question 3 
import numpy as np
import matplotlib.pyplot as plt 
from scipy import stats 

# Part 1: Create two random normal distributions 
rvs1=stats.norm.rvs(loc=5, scale=10, size=1000, random_state=0)
rvs2=stats.norm.rvs(loc=6.5, scale=8, size=1000, random_state=0)

# Part 2: T-test Analysis Function 
def t_test_function(rvs,alpha, no_test):
    counter=0
    for i in range(no_test):
        rvs_random=stats.norm.rvs(loc=5, scale=10, size=1000, random_state=i+1)
        statistic, pvalue = stats.ttest_ind(rvs, rvs_random, equal_var=False)
        if pvalue <= alpha: 
            counter=counter + 1 
            
    print(counter)
  
# Part 3: Run T-Test 
# result printed is the number of tests that were found statistically significant  
t_test_function(rvs1, alpha=0.05, no_test=100)
t_test_function(rvs2, alpha=0.05, no_test=100)       

# Part 4: Bonferroni Correction Function 
def bonferroni_correction_function(rvs, alpha, no_test):
    alpha_bonferroni = alpha/no_test
    
    counter = 0
    for i in range(no_test):
        rvs_random = stats.norm.rvs(loc=5, scale=10, size=1000, random_state=i+1)

        statistic, pvalue = stats.ttest_ind(rvs, rvs_random, equal_var=False)

        if pvalue <= alpha_bonferroni:
            counter = counter + 1

    print(counter)
    
# Part 5: Run Bonferroni Correction 
bonferroni_correction_function(rvs1, alpha=0.05, no_test=100)
bonferroni_correction_function(rvs2, alpha=0.05, no_test=100)

import numpy as np 
from statsmodels.stats._knockoff import RegressionFDR

def multipletests(pvals, alpha=0.05, method='fdr_bh', is_sorted=False, returnsorted=False):
    method.lower() in ['fdr_bh']:
        reject, pvals_corrected=fdrcorrection(pvals,alpha=alpha,method='indep', is_sorted=True)
    
multipletests(pvalue, alpha=0.05, method='fdr_bh', is_sorted=False, returnsorted=False)


def fdrcorrection(pvals, alpha=0.05, method='indep', is_sorted=False):
fdrcorrection(pvalue, alpha=0.05, method='indep', is_sorted=False)

