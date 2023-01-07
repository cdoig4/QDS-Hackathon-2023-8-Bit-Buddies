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
def global_data(parameter):
    data = pd.read_csv('2019.csv')
    happiness_score = data['Happiness score']
    comparison_data = data[parameter]
    plt.scatter(happiness_score, comparison_data, edgecolor='black', linewidths=1)
    plt.title(f"Correlation between {parameter} and Happiness")
    plt.xlabel('Happiness Score')
    plt.ylabel(parameter)
    plt.tight_layout()
    trendline = np.polyfit(happiness_score, comparison_data, 1)
    calculate_trend = np.poly1d(trendline)
    plt.plot(happiness_score, calculate_trend(happiness_score))
    plt.show()



