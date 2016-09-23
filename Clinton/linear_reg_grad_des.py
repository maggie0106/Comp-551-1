# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 19:37:21 2016

@author: ttw
"""

import pandas as pd
import numpy as np

# cost function
def cost_function(q):
    cost = np.multiply(2,(np.dot(np.dot(x_t,x),w_hat[:,[q]])-np.dot(x_t,y)))
    return cost

# read the file    
df = pd.read_csv(r'Book2.csv', header=None)
df_num = df.values

# x feature matrix and its transpose, y training outputs
x_t = np.ones(df_num.shape[0])

for p in range(df_num.shape[1]-1):
    x_t = np.vstack((x_t,df_num[:,p]))

# find mean and std dev for every column

x = x_t.T
"""
for r in range(df_num.shape[1]):
    x_mean = np.mean(x[:,[r]], dtype=np.float64)
    x_max = np.amax(x[:,[r]])
    # replace each row in given column with normalized data
    for l in range(df_num.shape[0]):
        temp12 = x[l][r]-x_mean
        x[l][r] = np.divide(temp12,x_max)
    
        
x_t=x.T"""
y = df_num[:,[df_num.shape[1]-1]]

# w_hat
w_hat = np.zeros((((x.shape[1]),2000)))
#w_hat= np.random.uniform(-2, 2, size=((x.shape[1]),20000))
alpha = 0.001

for q in range(1,1999):
    alpha=alpha*0.9
    w_hat[:,[q+1]] = w_hat[:,[q]] - np.multiply(alpha,cost_function(q))
    
    




