import pandas as pd
import plotly.express as px
import csv


test_file = pd.read_csv('2015.csv')
fig = px.scatter(test_file, x = 'Economy (GDP per Capita)', y = 'Happiness Score', title='Economy with Happiness Rank (2015)')
fig.show()

