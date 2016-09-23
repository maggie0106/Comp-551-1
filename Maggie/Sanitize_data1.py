# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 16:45:37 2016

@author: YingxueZhang
"""
import csv
import re
with open('Project1_data.csv', 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)
#
your_list.pop(0)

new_dict = {} #sanitize data dictionary
montreal = re.compile('montr..?al', re.IGNORECASE)
for runner in your_list:
    runner_id = int(runner[0])
    new_dict[runner_id] = [runner[i:i+5] for i in xrange(1, len(runner), 5)]
    for everyevent in new_dict[runner_id]:
        Date, Events, Type, Finish_time, gender_age = everyevent
        #whether it is in Montreal or not
        #whether it is a full Morothon
        Montreal_event = montreal.search(Events) != None
        marathon = (Type == 'Marathon')
        #age and gender
        
        if len(gender_age)>2:
            gender=gender_age[0]
            age=gender_age[1] 
            gender=gender if gender in 'FM' else 'M'
            age=age if '0' < age <= '9' else '3'
        else:
            gender='M'
            age='3'
        #finishing time
        
        if Finish_time== '-1':
            Finish_time= -1
        else:
            h,m,s = Finish_time.split(':')
            h,m,s=int(h),int(m),int(s)
            Finish_time=h * 3600 + m * 60 + s
        year = int(Date[:4])
    
        everyevent[:] = [year,marathon,Montreal_event,gender,age,Finish_time]
#       everyevent[:] = [marathon,Montreal_event]

#selecting regression features
#year,marathon,Montreal_event,gender,age,Finish_time =new_dict[0]
classification_features=[]
header=['ID','Num of marathon','Unfinished_marathon','gender','Age', 'Num of mtl marathon', '2012 mtl Marathon','2013 mtl Marathon','2014 mtl Marathon','2015 mtl Marathon']
classification_features.append(header)
List_new_dict=sorted(new_dict.iteritems())
for id, runner_results in List_new_dict:
    year,marathon,Montreal_event,gender,age,Finish_time =map(list,zip(*runner_results))
    #count how many time they took Marathon
    for m in gender:
        if m=='M':
            gender_q=1
        else:
            gender_q=-1
            
    for n in age:
        age_q=int(n)
    count_marathon=0
    unfinished_marathon=0
    mtl_maraton_2012=0
    mtl_maraton_2013=0
    mtl_maraton_2014=0
    mtl_maraton_2015=0
    mtl_marathon=0 #how many time he participated in mtl marathon
    tm_mara_loc = zip(year, marathon, Montreal_event)
    for i in marathon:
        if i==True: 
            count_marathon=count_marathon+1
    #count unfinished times
    for j in Finish_time:
        if j==-1:
            unfinished_marathon=unfinished_marathon+1
    
    for k in tm_mara_loc:
        if k[0]==2012 and k[1]==True and k[2]==True:
            mtl_maraton_2012=mtl_maraton_2012+1
            mtl_marathon=mtl_marathon+1
        
            
        if k[0]==2013 and k[1]==True and k[2]==True:
            mtl_maraton_2013=mtl_maraton_2013+1
            mtl_marathon=mtl_marathon+1
 
        if k[0]==2014 and k[1]==True and k[2]==True:
            mtl_maraton_2014=mtl_maraton_2014+1
            mtl_marathon=mtl_marathon+1
            
        if k[0]==2015 and k[1]==True and k[2]==True:
            mtl_maraton_2015=mtl_maraton_2015+1
            mtl_marathon=mtl_marathon+1        
            

    if mtl_maraton_2012==0:
            mtl_maraton_2012=-1
    if mtl_maraton_2013==0:
            mtl_maraton_2013=-1  
    if mtl_maraton_2014==0:
            mtl_maraton_2014=-1           
    classification_features.append([id,count_marathon,unfinished_marathon,gender_q,age_q,mtl_marathon,mtl_maraton_2012,mtl_maraton_2013,mtl_maraton_2014,mtl_maraton_2015]) 
#data structure for classification_features is [# of marathon,unfinished_marathon,age,# of total mtl marathon,2012] 
        
# Write data to file
with open('classification_features.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(classification_features)
            
    
            
    
    
