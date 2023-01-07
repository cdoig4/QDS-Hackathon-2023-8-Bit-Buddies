import pandas as pd
import plotly.express as px
import statsmodels.api as sm
import csv


test_file = pd.read_csv('2015.csv')
fig = px.scatter(test_file, x='Economy (GDP per Capita)', y = 'Happiness Score', trendline='ols')
fig.show()

results = px.get_trendline_results(fig)
print(results)

