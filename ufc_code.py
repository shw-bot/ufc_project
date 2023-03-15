# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 22:52:13 2023

@author: cinshalewolfe
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup

#soupy time
url = 'http://ufcstats.com/statistics/events/completed?page=all'

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

#create a dataframe with info from events page

main_event = []
urls = []
dates = []
locations = []
    
date = soup.find_all('span', class_= 'b-statistics__date')
location = soup.find_all('td', class_='b-statistics__table-col b-statistics__table-col_style_big-top-padding')
match = soup.find_all('a', class_ = "b-link b-link_style_black")
    
for item in match:
        main_event.append(item.text.strip())
        urls.append(item['href'])
        
for item in date:
        dates.append(item.text.strip())
        
for item in location:
        locations.append(item.text.strip())
        
dates = date[1:]
locations = locations[1:]
    
events_df = pd.DataFrame({'Main Event': main_event, 'Date': dates, 'Location': locations, 'URL': urls})
  
#print df  
events_df

#create a df from the individual fights

fight_urls = []
fighters = []


for item in soup.find_all('tr', class_='b-fight-details__table-row b-fight-details__table-row__hover js-fight-details-click'):
    fight_urls.append(item['data-link'])
    
for item in match:
    fighters.append(item.text.strip())
    
print(fighters)
