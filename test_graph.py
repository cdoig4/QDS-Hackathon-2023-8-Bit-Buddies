import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import statsmodels.api as sm
import csv
from scipy.stats import pearsonr

# test_file = pd.read_csv('2015.csv')
# fig = px.scatter(test_file, x='Economy (GDP per Capita)', y = 'Happiness Score', trendline='ols')
# fig.show()
#
# results = px.get_trendline_results(fig)
# print(results)
def global_data(parameter):
    data_2019 = pd.read_csv('2019.csv')
    happiness_score = data_2019['Happiness score']
    comparison_data = data_2019[parameter]
    plt.scatter(happiness_score, comparison_data, edgecolor='black', linewidths=1)
    plt.title(f"Correlation between Happiness and {parameter}")
    plt.xlabel('Happiness Score')
    plt.ylabel(parameter)
    plt.tight_layout()
    trendline = np.polyfit(happiness_score, comparison_data, 1)
    calculate_trend = np.poly1d(trendline)
    plt.plot(happiness_score, calculate_trend(happiness_score))
    plt.show()


def min_wage_data():
    data_2018 = pd.read_csv('happiness_via_min_wage.csv')
    happiness_score = data_2018['Happiness score']
    comparison_data = data_2018['2018']
    plt.scatter(happiness_score, comparison_data, edgecolors='black', linewidths=1)
    plt.title(f"Correlation between Happiness and Minimum Wage")
    plt.xlabel('Happiness Score')
    plt.ylabel('Minimum Wage')
    plt.tight_layout()
    trendline = np.polyfit(happiness_score, comparison_data, 1)
    calculate_trend = np.poly1d(trendline)
    plt.plot(happiness_score, calculate_trend(happiness_score))
    plt.show()


def calculate_correlation():
    data_2018 = pd.read_csv('happiness_via_min_wage.csv')
    happiness_score = data_2018['Happiness score']
    comparison_data = data_2018['2018']
    correlation, _ = pearsonr(happiness_score, comparison_data)
    return correlation
