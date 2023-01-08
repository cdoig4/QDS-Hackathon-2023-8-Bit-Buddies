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


# data_2019 = pd.read_csv('2019.csv')
# happiness_score = data_2019['Happiness score']
# gdp_per_capita = data_2019['GDP per capita']
# social_support = data_2019['Social support']
# life_expectancy = data_2019['Healthy life expectancy']
# freedom = data_2019['Freedom to make life choices']
# generosity = data_2019['Generosity']
# corruption = data_2019['Perceptions of corruption']
# gdp_correlation, _ = pearsonr(happiness_score, gdp_per_capita)
# social_support_correlation, _ = pearsonr(happiness_score, social_support)
# life_expectancy_correlation, _ = pearsonr(happiness_score, life_expectancy)
# freedom_correlation, _ = pearsonr(happiness_score, freedom)
# generosity_correlation, _ = pearsonr(happiness_score, generosity)
# corruption_correlation, _ = pearsonr(happiness_score, corruption)
#
# correlation_list = [gdp_correlation, social_support_correlation, life_expectancy_correlation, freedom_correlation,
#                     generosity_correlation, corruption_correlation]
#
# print(correlation_list)

correlation_list_2019 = [[0.7938828678781273, 0.777057788063864, 0.7798831492425831, 0.56674182571999,
                          0.07582369490389648, 0.38561307086647867]]