# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 14:52:57 2023

@author: cinshalewolfe
"""

import pandas as pd
import plotly.express as px

fighters_df = pd.read_csv(r'C:\Users\cinshalewolfe\Desktop\ufc project\clean_data\fighters_cleaned.csv')

# delete useless index column
fighters_df = fighters_df.iloc[: , 1:]

# create a scatter matric 
fig = px.scatter_matrix(fighters_df, dimensions =["Reach", "Stance", "W", "L"])
fig.show()
