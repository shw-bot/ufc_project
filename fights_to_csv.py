# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 11:41:25 2023

@author: cinshalewolfe
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

url = "http://ufcstats.com/statistics/events/completed?page=all"

r = requests.get(url)
soup = bs(r.content, "html.parser")

event_links = soup.find_all("a", {"class": "b-link b-link_style_black"})

fights_dfs = []  # create an empty list to hold data frames

for link in event_links:
    event_url = link["href"]
    
    r = requests.get(event_url)
    soup = bs(r.content, "html.parser")
    
    table = soup.find("table", {"class": "b-fight-details__table b-fight-details__table_style_margin-top b-fight-details__table_type_event-details js-fight-table"})
    df = pd.read_html(str(table))[0]
    
    event_name = soup.find("h2", {"class": "b-content__title"}).text.strip()
    df['event'] = event_name
    
    fights_dfs.append(df)  # append each data frame to the list

fights_df = pd.concat(fights_dfs, ignore_index=True)  # concatenate all data frames into one

fights_df.to_csv(r'C:\Users\cinshalewolfe\Desktop\ufc project\Data\fights.csv', index=False)