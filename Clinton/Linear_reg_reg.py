# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 14:17:13 2016

@author: ttw
"""

import pandas as pd
import numpy as np

def error(w_hat):
    tr_error =  np.empty([1,1])
    for i in range(x.shape[0])  :
        tr_error += np.power((y[i] - np.dot(w_hat.T,x[i])), 2) 
    return tr_error/x.shape[0]
    
df = pd.read_csv(r'Book3.csv', header=None)

df_rest = df.loc[df.index.isin(df.index)]
df_master=np.empty([1,1])

for o in range (10):
    df_master.append(df_rest.sample(n=8, axis =0))
    df_rest = df_rest.loc[~df_rest.index.isin(df_master[o].index)]

tr_error= []
    
for p in range(len(df_master)-1):
    df_num = df_master[p].values
    x = np.empty([df_num.shape[0],df_num.shape[1]-1])
    y = np.empty([df_num.shape[0],1])


    for q in range(df_num.shape[1]-1):
        x_mean = np.mean(df_num[:,[q]], dtype=np.float64)
        x_std = np.std(df_num[:,[q]])
        # replace each row in given column with normalized data
        for r in range(df_num.shape[0]):
            x[r][q] = (df_num[r][q]-x_mean)/x_std
        
        
    x_t = x.T
        
    for s in range (df_num.shape[0]):
        y_mean = np.mean(df_num[:,[df_num.shape[1]-1]], dtype=np.float64)
        y_std = np.std(df_num[:,[df_num.shape[1]-1]])
        y[s][0] = (df_num[s,[df_num.shape[1]-1]]-y_mean)/y_std

    lam =[0.0]

    w_hat_ridge = np.dot(np.dot(np.linalg.inv(np.dot(x_t,x) + np.multiply(lam,np.identity(int(x.shape[1])))),x_t),y)
  
    tr_error.append(error(w_hat_ridge))

val_error.append