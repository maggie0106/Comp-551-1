# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 12:33:57 2016

@author: Home
"""
from __future__ import division
import csv
import numpy as np
from operator import itemgetter
from math import log
import matplotlib.pyplot as plt

with open('classification_features.csv', 'rb') as f:
    file = csv.reader(f)
    data = list(file)
    
data.pop(0)
getter1 = itemgetter(3,6,7,8)    
xData=map(list, map(getter1, data))
getter2 = itemgetter(9) 
yData=map(list, map(getter2, data))

xData=np.array(xData)
yData=np.array(yData)
xData = [map(int, i) for i in xData]
yData = [map(int, i) for i in yData]
xData=np.array(xData)
yData=np.array(yData)

for i in range(len(xData)):
    if xData[i][0] == -1:
        xData[i][0] = 0
        
# Parameter Estimation
theta = sum(yData)/float(len(yData))
t = float(sum(yData))
tp = len(yData) - float(sum(yData))

theta1 = np.zeros(shape = (len(xData[1]),1))
theta0 = np.zeros(shape = (len(xData[1]),1))
for i in range(len(xData[1])):
    cnt1 = 0
    cnt2 = 0
    for j in range(len(xData)):
        if xData[j][i] == 1 and yData[j] == 1:
            cnt1 += 1
        elif xData[j][i] == 1 and yData[j] == 0:
            cnt2 += 1
    theta1[i] = (cnt1 / t)
    theta0[i] = (cnt2 / tp)


def naivebayes(theta, theta1, theta0, x, y):

    b = 0
    a = y * log(theta) + (1-y) * log(1-theta)
    for i in range(len(theta1)):
        b += y * (x[i] * log(theta1[i]) + (1-x[i]) * log(1 - theta1[i])) \
        + (1-y) * (x[i] * log(theta0[i]) + (1-x[i]) * log(1 - theta0[i]))
    c = a + b
    return c

p0 = 0
p1 = 0
prediction = []


for i in range(len(data)):
    p1 = (naivebayes(theta, theta1, theta0, xData[i], 1)) 
    p0 = (naivebayes(theta, theta1, theta0, xData[i], 0))
    if p1/p0 > 1:
        prediction.append(1)
    else:
        prediction.append(0)
prediction = np.array(prediction)
Prediction = np.ones(len(data))-prediction

def comparematrix(a,b):
    cnt = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            cnt += 1
    accuracy = cnt/len(a)
    return accuracy

accuracy = comparematrix(yData, prediction)
            
    
plt.plot(range(4),theta0)
plt.plot(range(4),theta1)
plt.title('Estmated Parameters')
plt.ylabel('Parameters')
plt.xlabel('Features index')



