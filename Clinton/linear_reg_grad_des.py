# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 19:37:21 2016

@author: ttw
"""

import pandas as pd
import numpy as np

"""
def training_error(w_hat):
    tr_error =[0.00]
    for i in range(x.shape[0])  :
        tr_error += np.power((y[i] - np.dot(w_hat.T,x[i])), 2)
    return tr_error
    """
    
def cost_function(q):
    temp2 =np.dot(np.dot(x_t,x),w_hat[:,q])
    cost = 2*(temp2-np.dot(x_t,y))
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
w_hat = np.zeros((((x.shape[1]),200)))
alpha = [1.00]################
diff=[0.00]

for q in range(200):
    w_hat[q+1] = w_hat[q] - alpha[q] * cost_function(q)
    
    """diff[1] = abs(w_hat[q+1]-w_hat[q])
    if diff[1]>diff[0]:
        break;
    diff[0] = diff[1]
    """
        



