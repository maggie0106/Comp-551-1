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

new_dict = {}
montreal = re.compile('montr.al', re.IGNORECASE)
for runner in your_list:
    runner_id = int(runner[0])
    new_dict[runner_id] = [runner[i:i+5] for i in xrange(1, len(runner), 5)]
    for everyevent in new_dict[runner_id]:
        Date, Events, Type, Finish_time, gender_age = everyevent
        #whether it is in Montreal or not
        #whether it is a full Morothon
        Montreal_event = montreal.search(Events) != None
        marathon = (type == 'Marathon')
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
 