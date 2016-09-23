# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 14:17:13 2016

@author: ttw
"""

import pandas as pd
import numpy as np

def error(w_hat, xe, ye):
    tr_error =  np.empty([1,1])
    for i in range(xe.shape[0])  :
        tr_error += np.power((ye[i] - np.dot(w_hat.T,xe[i])), 2) 
    return tr_error/xe.shape[0]
    
df = pd.read_csv(r'Book3.csv', header=None)

df_rest = df.loc[df.index.isin(df.index)]
df_master=[]

for o in range (10):
    df_master.append(df_rest.sample(n=8, axis =0))
    df_rest = df_rest.loc[~df_rest.index.isin(df_master[o].index)]

tr_error= []
tst_error=[]

  
for p in range(len(df_master)):
    temp2 = pd.concat(df_master[:p] + df_master[p+1:])
    df_num = temp2.values
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
  
    tr_error.append(error(w_hat_ridge, x, y))
    
    #validation
    df_numv = df_master[p].values
    xv = np.empty([df_numv.shape[0],df_numv.shape[1]-1])
    yv = np.empty([df_numv.shape[0],1])


    for qv in range(df_numv.shape[1]-1):
        x_meanv = np.mean(df_numv[:,[qv]], dtype=np.float64)
        x_stdv = np.std(df_numv[:,[qv]])
        # replace each row in given column with normalized data
        for rv in range(df_numv.shape[0]):
            xv[rv][qv] = (df_numv[rv][qv]-x_meanv)/x_stdv
        
        
    x_tv = xv.T
        
    for sv in range (df_numv.shape[0]):
        y_meanv = np.mean(df_numv[:,[df_numv.shape[1]-1]], dtype=np.float64)
        y_stdv = np.std(df_numv[:,[df_numv.shape[1]-1]])
        yv[sv][0] = (df_numv[sv,[df_numv.shape[1]-1]]-y_meanv)/y_stdv

    lamv =[0.0]

    tst_error.append(error(w_hat_ridge, xv, yv))
    
