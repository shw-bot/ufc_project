import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://ufcstats.com/statistics/events/completed?page=all"

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
    
    # Create a dataframe for each table
    for table in tables:
        df = pd.read_html(str(table))[0]
        print(df.head())