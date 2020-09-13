# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 20:46:49 2020

@author: walach
"""

# Libraries
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import inflect
import matplotlib.pyplot as plt


# Load data
season_number=range(1,11)

data = pd.read_csv('Stargate.csv')
data_per_apper = pd.read_csv('Stargate_per_apper.csv')


# Graph - median number of rows per season
df_grouped = data.groupby('Season',as_index=False).mean().drop('Episode',axis=1)
 
plt.plot( season_number, 'O\'NEILL', data=df_grouped,marker ='o')
plt.plot( season_number, 'DANIEL', data=df_grouped,marker ='o')
plt.plot( season_number, 'CARTER', data=df_grouped,marker ='o')
plt.plot( season_number, 'TEAL\'C', data=df_grouped,marker ='o')
#plt.plot( season_number, 'HAMMOND', data=df_grouped)
#plt.plot( season_number, 'JONAS', data=df_grouped)
#plt.plot( season_number, 'MITCHELL', data=df_grouped)
#plt.plot( season_number, 'LANDRY', data=df_grouped)
#plt.plot( season_number, 'BRA\'TAC', data=df_grouped)

lgd=plt.legend(loc='upper right', bbox_to_anchor=(1.27,1))

plt.title('Stargate: Average number of words by main characters')
plt.ylabel('Average number of words')
plt.xlabel('Season')

plt.xticks(season_number)

plt.savefig('Number_of_words.png', bbox_extra_artists=(lgd,), bbox_inches='tight', dpi=150)
plt.clf()

# Graph - median number per apperance

df_grouped = data_per_apper.groupby('Season',as_index=False).mean().drop('Episode',axis=1)
 
plt.plot( season_number, 'O\'NEILL', data=df_grouped,marker ='o')
plt.plot( season_number, 'DANIEL', data=df_grouped,marker ='o')
plt.plot( season_number, 'CARTER', data=df_grouped,marker ='o')
plt.plot( season_number, 'TEAL\'C', data=df_grouped,marker ='o')
#plt.plot( season_number, 'HAMMOND', data=df_grouped)
#plt.plot( season_number, 'JONAS', data=df_grouped)
#plt.plot( season_number, 'MITCHELL', data=df_grouped)
#plt.plot( season_number, 'LANDRY', data=df_grouped)
#plt.plot( season_number, 'BRA\'TAC', data=df_grouped)

lgd=plt.legend(loc='upper right', bbox_to_anchor=(1.27,1))

plt.title('Stargate: Average number of words per apperance')
plt.ylabel('Average number of words per apperance')
plt.xlabel('Season')

plt.xticks(season_number)

plt.savefig('Number_of_words_per_apperance.png', bbox_extra_artists=(lgd,), bbox_inches='tight', dpi=150)

plt.clf()

# Number of times they did not appear on episode

df1 = data.iloc[:,:-2]==0
season = data.iloc[:,-2:]

df = pd.concat([df1,season],axis=1)

df_grouped = df.groupby('Season',as_index=False).sum().drop('Episode',axis=1)
 
plt.plot( season_number, 'O\'NEILL', data=df_grouped,marker ='o')
plt.plot( season_number, 'DANIEL', data=df_grouped,marker ='o')
plt.plot( season_number, 'CARTER', data=df_grouped,marker ='o')
plt.plot( season_number, 'TEAL\'C', data=df_grouped,marker ='o')
#plt.plot( season_number, 'HAMMOND', data=df_grouped)
#plt.plot( season_number, 'JONAS', data=df_grouped)
#plt.plot( season_number, 'MITCHELL', data=df_grouped)
#plt.plot( season_number, 'LANDRY', data=df_grouped)
#plt.plot( season_number, 'BRA\'TAC', data=df_grouped)

lgd=plt.legend(loc='upper right', bbox_to_anchor=(1.27,1))

plt.title('Stargate: Number of missed episodes')
plt.ylabel('Number of missed episodes')
plt.xlabel('Season')

plt.xticks(season_number)
plt.yticks(range(22))


plt.savefig('Number_of_missing.png', bbox_extra_artists=(lgd,), bbox_inches='tight', dpi=150)

