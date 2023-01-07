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
family = data['Happiness Score']
economy = data['Economy (GDP per Capita)']
plt.scatter(family, economy, edgecolor='black', linewidths=1)
plt.title('Happiness Score vs Economy (GDP per Capita)')
plt.xlabel('Happiness Score')
plt.ylabel('Economy')
plt.tight_layout()
trendline = np.polyfit(family, economy, 1)
calculate_trend = np.poly1d(trendline)
plt.plot(family, calculate_trend(family))
plt.show()



