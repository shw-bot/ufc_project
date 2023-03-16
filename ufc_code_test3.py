# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 16:40:14 2023

@author: cinshalewolfe
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://ufcstats.com/statistics/events/completed?page=all"

# Create an empty list to store the dataframes
dfs = []

# Send an HTTP request to the URL and retrieve the HTML content of the page
response = requests.get(url)
html_content = response.content

# Use BeautifulSoup to parse the HTML content and extract the URLs of each event
soup = BeautifulSoup(html_content, "html.parser")
event_links = soup.find_all("a", class_="b-link b-link_style_black")

# Loop through each event URL and extract the tables
for link in event_links:
    event_url = link.get("href")
    event_response = requests.get(event_url)
    event_html_content = event_response.content
    event_soup = BeautifulSoup(event_html_content, "html.parser")
    
    # Extract the tables from the event page using BeautifulSoup
    tables = event_soup.find_all("table")
    
    # Create a dataframe for each table and append it to the list
    for table in tables:
        df = pd.read_html(str(table))[0]
        dfs.append(df)

# Concatenate all the dataframes in the list into one
combined_df = pd.concat(dfs)

# Print the first few rows of the combined dataframe
print(combined_df.head())