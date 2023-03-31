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
fighters_df.head()

# create a scatter matrix 
fig = px.scatter_matrix(fighters_df, dimensions =["Ht.", "Reach", "W", "L", "D"])
fig.show()

# first we'll group the dataframe by stance and count the number of wins, losses, and draws for each stance
stance_grouped_df = fighters_df.groupby('Stance').agg({'W': 'sum', 'L': 'sum', 'D': 'sum'}).reset_index()
melted_df = pd.melt(stance_grouped_df, id_vars='Stance', var_name='Result', value_name='Count')

# next we will create a bar graph for the data and separate each bar by win, loss, or draw
fig2 = px.bar(melted_df, x='Stance', y='Count', color='Result', barmode='stack')
fig2.show()
print(stance_grouped_df)

data = []

for stance in stance_grouped_df['Stance'].unique():
    total_wins = stance_grouped_df[stance_grouped_df['Stance'] == stance]['W'].sum()
    total_losses = stance_grouped_df[stance_grouped_df['Stance'] == stance]['L'].sum()
    total_draws = stance_grouped_df[stance_grouped_df['Stance'] == stance]['D'].sum()
    total_fights = total_wins + total_losses + total_draws
    win_percentage = round((total_wins / total_fights) * 100, 2)
    loss_percentage = round((total_losses / total_fights) * 100, 2)
    draw_percentage = round((total_draws / total_fights) * 100, 2)
    
    data.append({'Stance': stance, 'Win Percentage': win_percentage, 'Loss Percentage': loss_percentage, 'Draw Percentage': draw_percentage})
    
stance_data = pd.DataFrame(data)
stance_data

weight_grouped_df = fighters_df.groupby(['weight_class', 'Stance']).agg({'W': 'sum', 'L': 'sum', 'D': 'sum'}).reset_index()

# Calculate total fights and percentages
weight_grouped_df['Total Fights'] = weight_grouped_df['W'] + weight_grouped_df['L'] + weight_grouped_df['D']
weight_grouped_df['Win Percentage'] = round(weight_grouped_df['W'] / weight_grouped_df['Total Fights'] * 100, 2)

# Select relevant columns and sort by weight class and stance
result_cols = ['Win Percentage']
result_df = weight_grouped_df[['weight_class', 'Stance'] + result_cols].sort_values(['weight_class', 'Stance'])

import plotly.graph_objs as go

pivoted_df = weight_grouped_df.pivot(index='weight_class', columns='Stance', values='Win Percentage')

heat = go.Figure(data=go.Heatmap(z=pivoted_df.values, x=pivoted_df.columns, y=pivoted_df.index, colorscale='Viridis'))
heat.update_layout(title='Win Percentage by Stance and Weight Class', xaxis_title='Stance', yaxis_title='Weight Class')

heat.show()
