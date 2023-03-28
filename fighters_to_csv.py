# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 15:44:35 2023

@author: cinshalewolfe
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

#soupy time
url = 'http://ufcstats.com/statistics/fighters'
r = requests.get(url)

soup = bs(r.content, 'html.parser')

#find all the letters:

letters = soup.find_all('a', {"class":"b-statistics__nav-link"})

links = []
fighters_df = pd.DataFrame()

for letter in letters:
    url = 'http://ufcstats.com' + letter["href"]
    links.append(url)
    
for link in links:
    r = requests.get(link)
    soup = bs(r.content, 'html.parser')
    table = soup.find('table', {'class':'b-statistics__table'})
    df = pd.read_html(str(table))[0]
    
    fighters_df = pd.concat([fighters_df, df], ignore_index=True)
    
fighters_df.to_csv(r'C:\Users\cinshalewolfe\Desktop\ufc project\Data\fighters.csv', index=False)
