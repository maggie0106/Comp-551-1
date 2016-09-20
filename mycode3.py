# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 13:07:14 2016

@author: Home
"""

import csv
with open('Project1_data.csv', 'rb') as f:
    file = csv.reader(f)
    data = list(file)
# Extracting gender feature   
gender = []
for i in range(len(data)-1):
    if not data[i+1][5]:
        gender.append(-1) #Unknown gender
    elif data[i+1][5][0] == 'M' or data[i+1][5][0] == 'm':
        gender.append(1) # 1 shows the participant is male.
    elif data[i+1][5][0] == 'F' or data[i+1][5][0] == 'f':
        gender.append(0) # 0 shows the participant is female.
    else :
        gender.append(-1) #Unknown gender
# Extracting age feature
age = []
for j in range((len(data[1])-1)/5):
    for i in range(len(data)-1):
         if not bool(data[i+1][5*(j+1)]) or len(data[i+1][5*(j+1)]) != 6:
             age.append('-1') #Unknown age
    ############################################
         elif data[i+1][5*(j+1)][1] == '1' and data[i+1][5*(j+1)][4] == '1':
             age.append('1')
    ##############################################
         elif data[i+1][5*(j+1)][1] == '2' and data[i+1][5*(j+1)][4] == '2':
             if (data[i+1][5*(j+1)][2] <= '4' and data[i+1][5*(j+1)][2] >= '0')\
                and data[i+1][5*(j+1)][5] <= '4' and data[i+1][5*(j+1)][5] >= '0':
                 age.append('2A')
             elif (data[i+1][5*(j+1)][2] <= '9' and data[i+1][5*(j+1)][2] >= '5')\
                  and (data[i+1][5*(j+1)][5] <= '9' and data[i+1][5*(j+1)][5] >= '5'):
                 age.append('2B')
             else:
                 age.append('2')
      #################################
         elif data[i+1][5*(j+1)][1] == '3' and data[i+1][5*(j+1)][4] == '3':
             if (data[i+1][5*(j+1)][2] <= '4' and data[i+1][5*(j+1)][2] >= '0')\
                and data[i+1][5*(j+1)][5] <= '4' and data[i+1][5*(j+1)][5] >= '0':
                 age.append('3A')
             elif (data[i+1][5*(j+1)][2] <= '9' and data[i+1][5*(j+1)][2] >= '5')\
                  and (data[i+1][5*(j+1)][5] <= '9' and data[i+1][5*(j+1)][5] >= '5'):
                 age.append('3B')
             else:
                 age.append('3')
      ###############################
         elif data[i+1][5*(j+1)][1] == '4' and data[i+1][5*(j+1)][4] == '4':
             if (data[i+1][5*(j+1)][2] <= '4' and data[i+1][5*(j+1)][2] >= '0')\
                and data[i+1][5*(j+1)][5] <= '4' and data[i+1][5*(j+1)][5] >= '0':
                 age.append('4A')
             elif (data[i+1][5*(j+1)][2] <= '9' and data[i+1][5*(j+1)][2] >= '5')\
                  and (data[i+1][5*(j+1)][5] <= '9' and data[i+1][5*(j+1)][5] >= '5'):
                 age.append('4B')
             else:
                 age.append('4')
            
     ########################################     
         elif data[i+1][5*(j+1)][1] == '5' and data[i+1][5*(j+1)][4] == '5':
             if (data[i+1][5*(j+1)][2] <= '4' and data[i+1][5*(j+1)][2] >= '0')\
                and data[i+1][5*(j+1)][5] <= '4' and data[i+1][5*(j+1)][5] >= '0':
                 age.append('5A')
             elif (data[i+1][5*(j+1)][2] <= '9' and data[i+1][5*(j+1)][2] >= '5')\
                  and (data[i+1][5*(j+1)][5] <= '9' and data[i+1][5*(j+1)][5] >= '5'):
                 age.append('5B')
             else:
                 age.append('5')
     ###########################################
         elif data[i+1][5*(j+1)][1] == '6' and data[i+1][5*(j+1)][4] == '6':
             age.append('6')
     ########################################
         else: 
             age.append('-1')
    
age_feature = []
for k in range((len(data[1])-1)/5):
    age_feature.append(age[(len(data)-1)*k:(len(data)-1)*(k+1)])

with open('Sanitized Data.csv', 'wb') as g:
    file_s = csv.writer(g, delimiter=' ')
    file_s.writerows(data)
        
        
        