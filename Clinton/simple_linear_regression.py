# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 13:36:38 2016

@author: ttw
"""

import pandas as pd
import numpy as np

def training_error(w_hat):
    tr_error =[0.00]
    for i in range(x.shape[0])  :
        tr_error += np.power((y[i] - np.dot(w_hat.T,x[i])), 2)
    return tr_error
    
df = pd.read_csv(r'Book2.csv', header=None)
df_num = df.values

# x feature matrix and its transpose, y training outputs
x_t = np.ones(df_num.shape[0])

for p in range(df_num.shape[1]-1):
    x_t = np.vstack((x_t,df_num[:,p]))
    
x = x_t.T
y = df_num[:,[df_num.shape[1]-1]]

# w_hat=(xx^T)^-1.x^T.y
w_hat = np.dot(np.dot(np.linalg.inv(np.dot(x_t,x)),x_t),y)

tr_error = training_error(w_hat)
