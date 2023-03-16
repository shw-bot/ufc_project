# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 16:07:28 2023

@author: cinshalewolfe
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

#soupy time
url = 'http://ufcstats.com/statistics/events/completed?page=all'
r = requests.get(url)
data = r.text
soup = BeautifulSoup(r.content, 'html.parser')


###########################
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
    
events_df  
events_df['URL'][0]



####################
testing_urls = []
my_urls = []
for index, row in events_df.iterrows():
    testing_urls.append(f"{row['URL']}")
for item in testing_urls:
    page = requests.get(item)
    data = page.text
    soup = BeautifulSoup(data, 'html.parser')
    test = soup.find_all('tr',class_='b-fight-details__table-row b-fight-details__table-row__hover js-fight-details-click')

    for x in test:
        my_urls.append(item[0])
        
print(my_urls)
