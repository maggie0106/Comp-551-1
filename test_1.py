# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 15:00:25 2016

@author: YingxueZhang
"""
import csv
with open('Project1_data.csv', 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)
#your_list.pop(0)

#c=your_list[1] #the number of the player, extract all the information for this plyaer
participate_nomber=[]
finish=[]
for a in your_list:
    length=(len(a)-1)/5
    participate_nomber.append(length)
#a=your_list[2]
#b=a[9]

for a in your_list:
    length=(len(a)-1)/5
    count=0   
    for b in range(0,length):
        if a[b*5+4]!='-1':
            count=count+1
    finish.append(count)
