# -*- coding: utf-8 -*-
"""
@author: Jan Walach
"""

# Analysis of transcripts of my favorite TV show Stargate: SG-1. 
# The script will web scrape transcrips of all episodes and count the number of words said by each main character by season. 

import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import inflect

# Load names of seasons  (1,'one',...)
season_number=range(1,11)

p = inflect.engine()
season_name = list(map(p.number_to_words,season_number))


# Main characters
# Could be better to be found automatically
    
s = ['O\'NEILL',
     'DANIEL',
     'CARTER',
     'HAMMOND',
     'TEAL\'C',
     'JONAS',
     'MITCHELL',
     'LANDRY',
     'BRA\'TAC',
     'Season',
     'Episode']

# Result dataframe alocation
data = pd.DataFrame(np.nan, index=range(0,22*len(season_number)), columns=s)
data_per_apper  = pd.DataFrame(np.nan, index=range(0,22*len(season_number)), columns=s)
# Pozition in df
poz=0

# Loop over all seasions -------------
for season in range(10):
    # 1.Nacist jmena episod ------------------
    URL = 'http://www.stargate-sg1-solutions.com/wiki/Season_' + season_name[season].capitalize() + '_Transcripts'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    jmena = soup.prettify().splitlines()
    
    
    # Looking for rows containing sub a sub2
    sub = '<a href="/wiki/' + str(season_number[season])
    sub2 = 'Transcript'
    
    index_list = []
    episody=[]
    i = 0
    for e in jmena:
        if ((sub in e) & (sub2 in e)):
            index_list.append(i)
            episody.append(e)
        i +=1
    print(episody)
    
    # Remove duplicities
    episody=list( dict.fromkeys(episody) )
    
    
    # Create proper url
    for x in episody:
        print(x.split('"')[1].split('/')[2])
        
        
    url = []
    for x in episody:
        url.append('http://www.stargate-sg1-solutions.com' +
              x.split('"')[1])
        
    
    
    # For loop over episodes   
    episode_number=1
    for l in url:
        URL = l
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        result = soup.prettify().splitlines()
        
        # Begenning of transcript
        #result.index('        Transcript',)
        #result2.index('        Transcript',)
        
        
        # End of transcript
        #result.index('       <span class="mw-headline" id="Related_Articles">')
        #result2.index('       <span class="mw-headline" id="Related_Articles">')
          
        for sub in s[:-2]:
            index_list = []
            i = 0
            for e in result:
                if sub in e.replace("’","'"):
                    index_list.append(i)
                i +=1
            
            
            # Indexes of rows with anyone's names - find capital words
            velke = []
            i = 0
            for e in result:
                if e.isupper():
                    velke.append(i)
                i +=1
    
            
            # Total number of words
            k=0
            #Number of apperances
            apper = 0
            for j in index_list:
                # Rows between names
                lines = result[(j+1):[i for i in velke if i > j][0]]
                # What she/he reallz said
                sais = [i for i in lines if ('<' not in i) & ('[' not in i) & ('(' not in i)]
            
                # Sum
                for i in range(len(sais)):
                    sais2 = sais[i].split(' ')                
                    
                    for kkk in sais2:
                        if len(kkk)>0:
                            k+=1
                    apper += 1 
            print(k)
            data.loc[poz,sub] = k
            data.loc[poz,s[-2]] = season_number[season]
            data.loc[poz,s[-1]] = episode_number
        
            if apper !=0:
                num=k/apper
            else: num=0
            
            data_per_apper.loc[poz,sub] = num
            data_per_apper.loc[poz,s[-2]] = season_number[season]
            data_per_apper.loc[poz,s[-1]] = episode_number
           
        
        episode_number += 1
        poz += 1

# Remove nan rows if any
data=data.loc[data.isnull().sum(axis=1) != len(s),:]
data_per_apper=data_per_apper.loc[data_per_apper.isnull().sum(axis=1) != len(s),:]

# Save results as csv
data.to_csv('Stargate.csv')
data_per_apper.to_csv('Stargate_per_apper.csv')

