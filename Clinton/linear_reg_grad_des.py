# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 19:37:21 2016

@author: ttw
"""

import pandas as pd
import numpy as np

def cost_function(q):
    cost = np.multiply(2,(np.dot(np.dot(x_t,x),w_hat[:,[q]])-np.dot(x_t,y)))
    return cost
    
df = pd.read_csv(r'Book1.csv', header=None)
df_num = df.values

# x feature matrix and its transpose, y training outputs
x_t = np.ones(df_num.shape[0])

for p in range(df_num.shape[1]-1):
    x_t = np.vstack((x_t,df_num[:,p]))
    
x = x_t.T
y = df_num[:,[df_num.shape[1]-1]]

# w_hat
w_hat = np.zeros((((x.shape[1]),20000)))
w_hat= np.random.uniform(-300, 100, size=((x.shape[1]),20000))
alpha = 0.000000001

for q in range(19999):
    w_hat[:,[q+1]] = w_hat[:,[q]] - np.multiply(alpha,cost_function(q))
    
    




