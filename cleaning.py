# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 17:34:25 2023

@author: cinshalewolfe
"""
import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\cinshalewolfe\Desktop\ufc project\raw_data\fights.csv')

# create dataframe that separates fighter data
fights = pd.DataFrame()
fights[['fighter1', 'fighter2']] = df['Fighter'].str.split('  ', expand=True)
fights[['fighter1_kd', 'fighter2_kd']] = df['Kd'].str.split('  ', expand=True)
fights[['fighter1_str', 'fighter2_str']] = df['Str'].str.split('  ', expand=True)
fights[['fighter1_td', 'fighter2_td']] = df['Td'].str.split('  ', expand=True)
fights[['fighter1_sub', 'fighter2_sub']] = df['Sub'].str.split('  ', expand=True)
fights['weight_class'] = df['Weight class']
fights['method'] = df['Method']
fights['round'] = df['Round']
fights['time'] = df['Time']
fights['event'] = df['event']
fights['w/l'] = df['W/L']

# create a new column that shows the result of the fight  
fights['winner'] = np.where(fights['w/l'] == 'win', fights['fighter1'], 'draw')
fights = fights.drop('w/l', axis=1)

# show the fights df
fights.to_csv(r'C:\Users\cinshalewolfe\Desktop\ufc project\clean_data\fights_cleaned.csv')

###

#create a dataframe from the fighters csv file we scraped earlier

fighters = pd.read_csv(r'C:\Users\cinshalewolfe\Desktop\ufc project\raw_data\fighters.csv')

#drop empty first row and irrelevant column
fighters = fighters.drop(fighters.index[0])
fighters = fighters.drop('Belt', axis=1)

#fill NaN values in different columns
fighters['Stance'] = fighters['Stance'].fillna('Unknown')
fighters['Nickname'] = fighters['Nickname'].fillna('')

# create a function that changes the height column from strings in feet, inches format to total inches
# first, ensure all values in the column are strings
fighters['Ht.'] = fighters['Ht.'].astype(str)

# next, create the function
def convert_height(height):
    if height == "--":
        return None
    else:
        feet_inches = height.split("' ")
        if len(feet_inches) == 2:
            feet, inches = feet_inches
            total_inches = int(feet) * 12 + int(inches.strip('"'))
            return total_inches
        else:
            return None

# apply the function to the 'Ht.' column
fighters['Ht.'] = fighters['Ht.'].apply(convert_height)

# fill NaN values with the mean of the column and change type to integers
fighters['Ht.'] = fighters['Ht.'].fillna(fighters['Ht.'].mean())
fighters['Ht.'] = fighters['Ht.'].astype(int)

# reformat Reach column + fill NaN values with column avg
fighters['Reach'] = fighters['Reach'].replace('--', np.nan)
fighters['Reach'] = fighters['Reach'].str.replace('"', '').astype(float)
fighters['Reach'] = fighters['Reach'].fillna(fighters['Reach'].mean())
fighters['Reach'] = fighters['Reach'].astype(int)

# reformat Weight column
fighters['Wt.'] = fighters['Wt.'].replace('--', np.nan)
fighters['Wt.'] = fighters['Wt.'].str.replace(' lbs.', '').astype(float)
##here, we need to figure out how to replace the NaN, but it would affect their weightclass so...

# drop other empty rows
fighters = fighters.dropna()


# print the fighters df
fighters.to_csv(r'C:\Users\cinshalewolfe\Desktop\ufc project\clean_data\fighters_cleaned.csv')

