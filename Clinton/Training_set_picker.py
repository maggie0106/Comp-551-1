# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 08:39:54 2016

@author: ttw
"""

import pandas as pd

# Read csv file
df = pd.read_csv(r'Original_data.csv', encoding='utf8', engine='python', header=None)

# Column headers dataframe
df_header = df[:1]

# Drop header and reindex to randomly pick training sets
df_rest = df.loc[df.index.isin(df.index)]
df_rest = df_rest.drop([0],axis=0)
df_rest.index = range(len(df_rest))

# First training set
df_1 = df_header.append(df_rest.sample(n=1000))
df_rest = df_rest.loc[~df_rest.index.isin(df_1.index)]
df_1.index = range(len(df_1))
# Second training set
df_2 = df_header.append(df_rest.sample(n=1000))
df_rest = df_rest.loc[~df_rest.index.isin(df_2.index)]
df_2.index = range(len(df_2))
# Third training set
df_3 = df_header.append(df_rest.sample(n=1000))
df_rest = df_rest.loc[~df_rest.index.isin(df_3.index)]
df_3.index = range(len(df_3))
# Fourth training set
df_4 = df_header.append(df_rest.sample(n=1000))
df_rest = df_rest.loc[~df_rest.index.isin(df_4.index)]
df_4.index = range(len(df_4))
# Fifth training set
df_5 = df_header.append(df_rest.sample(n=1000))
df_rest = df_rest.loc[~df_rest.index.isin(df_5.index)]
df_5.index = range(len(df_5))
# Sixth training set
df_6 = df_header.append(df_rest.sample(n=1000))
df_rest = df_rest.loc[~df_rest.index.isin(df_6.index)]
df_6.index = range(len(df_6))
# Seventh training set
df_7 = df_header.append(df_rest.sample(n=1000))
df_rest = df_rest.loc[~df_rest.index.isin(df_7.index)]
df_7.index = range(len(df_7))
# Eighth training set
df_8 = df_header.append(df_rest.sample(n=1000))
df_rest = df_rest.loc[~df_rest.index.isin(df_8.index)]
df_8.index = range(len(df_8))
# Ninth training set
df_9 = df_rest
df_9.index = range(len(df_9))

# write csv training set files
df_1.to_csv(r'Training1.csv', encoding='utf8', index=False, header=False)
df_2.to_csv(r'Training2.csv', encoding='utf8', index=False, header=False)
df_3.to_csv(r'Training3.csv', encoding='utf8', index=False, header=False)
df_4.to_csv(r'Training4.csv', encoding='utf8', index=False, header=False)
df_5.to_csv(r'Training5.csv', encoding='utf8', index=False, header=False)
df_6.to_csv(r'Training6.csv', encoding='utf8', index=False, header=False)
df_7.to_csv(r'Training7.csv', encoding='utf8', index=False, header=False)
df_8.to_csv(r'Training8.csv', encoding='utf8', index=False, header=False)
df_9.to_csv(r'Training9.csv', encoding='utf8', index=False, header=False)


