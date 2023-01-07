import pandas as pd


def country_history(country_name, parameter):
    mapped_values = []
    year_start = 2015
    while year_start <= 2019:
        year_read = str(year_start) + ".csv"
        df = pd.read_csv(year_read)
        data = df[df['Country'] == country_name]
        parameter_score = data[parameter].values[0]
        mapped_values.append(parameter_score)
        year_start += 1
    return mapped_values

