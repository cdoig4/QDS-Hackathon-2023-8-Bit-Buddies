import pandas as pd
import plotly.express as px
import statsmodels.api as sm
import csv
import matplotlib.pyplot as plt
import numpy as np

# test_file = pd.read_csv('2015.csv')
# fig = px.scatter(test_file, x='Economy (GDP per Capita)', y = 'Happiness Score', trendline='ols')
# fig.show()
#
# results = px.get_trendline_results(fig)
# print(results)

data = pd.read_csv('2015.csv')
family = data['Family'].strip()
freedom = data['Freedom']
plt.scatter(family, freedom)
plt.title('family vs freedom 2015')
plt.xlabel('family')
plt.ylabel('freedom')
plt.tight_layout()
plt.show()



