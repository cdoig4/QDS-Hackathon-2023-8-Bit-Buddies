import pandas as pd
import plotly.express as px
import csv

# with open('2015.csv') as csv_file:
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')
fig = px.line(df, x = 'AAPL_x', y = 'AAPL_y', title='Apple Share Prices over time (2014)')

fig.show()
