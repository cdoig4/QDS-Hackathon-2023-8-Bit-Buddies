import PySimpleGUI as sg
import pandas as pd
import math
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
from country_history import country_history
from scipy.stats import pearsonr

matplotlib.use('TkAgg')


def plot_bar_chart(plot_title, values_to_plot, comparison_value, first_country, y_axis_label, second_country=None):
    ind = np.arange(len(values_to_plot))

    plt.plot(values_to_plot, label=first_country)
    maximum_value = math.ceil(max(values_to_plot))

    if second_country:
        plt.plot(comparison_value, label=second_country)
        maximum_value = math.ceil((max(values_to_plot) + max(comparison_value))/2)

    y_tick = math.ceil(maximum_value * 1.1)

    plt.ylabel(y_axis_label)
    plt.xlabel("years")
    plt.title(plot_title)
    plt.xticks(ind, (2015, 2016, 2017, 2018, 2019))
    plt.yticks(np.arange(0, y_tick, y_tick * 0.1))
    plt.legend()


def plot_correlation(values_to_plot):
    ind = np.arange(len(values_to_plot))

    plt.bar(ind, values_to_plot, 0.4, color=["blue", "red", "green", "orange", "black", "cyan"])
    y_tick = 1

    plt.ylabel("Correlation")
    plt.xlabel("Factors")
    plt.title("Correlation to Happiness")
    plt.xticks(ind, ("GDP", "Social", "Health", "Freedom", "Giving", "Corruption"))
    plt.yticks(np.arange(0, y_tick, y_tick * 0.1))
    plt.legend()


def global_data(parameter):
    data_2019 = pd.read_csv('2019.csv')
    happiness_score = data_2019['Happiness score']
    comparison_data = data_2019[parameter]
    plt.scatter(happiness_score, comparison_data, edgecolor='black', linewidths=0.5)
    plt.title(f"Happiness Score vs {parameter}")
    plt.xlabel('Happiness Score')
    plt.ylabel(parameter)
    plt.tight_layout()
    trendline = np.polyfit(happiness_score, comparison_data, 1)
    calculate_trend = np.poly1d(trendline)
    plt.plot(happiness_score, calculate_trend(happiness_score))


def min_wage_data():
    data_2018 = pd.read_csv('happiness_via_min_wage.csv')
    happiness_score = data_2018['Happiness score']
    comparison_data = data_2018['2018']
    plt.scatter(happiness_score, comparison_data, edgecolors='black', linewidths=0.5)
    plt.title(f"Happiness Score vs Minimum Wage")
    plt.xlabel('Happiness Score')
    plt.ylabel('Minimum Wage')
    plt.tight_layout()
    trendline = np.polyfit(happiness_score, comparison_data, 1)
    calculate_trend = np.poly1d(trendline)
    plt.plot(happiness_score, calculate_trend(happiness_score))


def calculate_correlation(file_name):
    correlation_list = []
    data = pd.read_csv(file_name)
    keys_to_remove = ['Happiness rank', 'Country']
    for key in keys_to_remove:
        del data[key]
    for key in data.keys():
        happiness_score = data['Happiness score']
        other_data = data[key]
        current_correlation, _ = pearsonr(happiness_score, other_data)
        correlation_list.append(current_correlation)
    correlation_list.remove(correlation_list[0])
    return correlation_list


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


fig = plt.gcf()
df = pd.read_csv("2019.csv")


layout = [
    [sg.Text("Select a country and parameter and click PLOT 1 to view the parameter score over time:")],
    [sg.Text("Country")],
    [sg.Combo(sorted(df['Country'].values[:]), enable_events=True, key='-LOCATION-')],
    [sg.Text("If you want to compare with another country, select it below.")],
    [sg.Text("Country")],
    [sg.Combo(sorted(df['Country'].values[:]), enable_events=True, key='-COMPARISON_LOCATION-')],
    [sg.Text("Parameter (by Country)")],
    [sg.Combo(["Happiness score", "Happiness rank", "GDP per capita", "Social support",
               "Healthy life expectancy", "Freedom to make life choices", "Generosity",
               "Perceptions of corruption"],
              enable_events=True, key='-PARAMETER-')],
    [sg.Button("PLOT 1")],
    [sg.Text('\nSelect a country and parameter and click PLOT 2 to view the Happiness Score vs. '
             'Parameter:')],
    [sg.Text("Parameter (Global)")],
    [sg.Combo(["Happiness score", "Happiness rank", "GDP per capita", "Social support",
               "Healthy life expectancy", "Freedom to make life choices", "Generosity",
               "Perceptions of corruption", "Minimum wage"],
              enable_events=True, key='-PARAMETER1-')],
    [sg.Button("PLOT 2")],
    [sg.Text("Calculate Correlation")],
    [sg.Button("PLOT 3")],
    [sg.Canvas(size=(500, 350), key='-CANVAS-')],
    [sg.Button("CLEAR")],
    [sg.Button("CLOSE")]
]

window = sg.Window(title="Happiness Report", layout=layout, force_toplevel=True, finalize=True,
                   size=(1000, 1000))


def delete_figure_agg(figure_agg):
    figure_agg.get_tk_widget().forget()
    plt.cla()


while True:
    event, values = window.read()
    if event == "PLOT 1":
        parameter = values['-PARAMETER-']
        comparison_country = values['-COMPARISON_LOCATION-']
        plot_values = country_history(values['-LOCATION-'], parameter)
        if comparison_country == "":
            country_a = values['-LOCATION-']
            comparison_values = 0
            plot_title = f"{parameter} of {country_a}"
            plot_bar_chart(plot_title, plot_values, comparison_values, country_a, parameter)
        else:
            country_a = values['-LOCATION-']
            country_b = values['-COMPARISON_LOCATION-']
            comparison_values = country_history(values['-COMPARISON_LOCATION-'], parameter)
            plot_title = f"Comparison of {country_a} vs {country_b} on {parameter}"
            plot_bar_chart(plot_title, plot_values, comparison_values, country_a, parameter, country_b)

        figure_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)

    if event == "PLOT 2":
        parameter = values['-PARAMETER1-']
        if parameter == 'Minimum wage':
            min_wage_data()
        else:
            global_data(parameter)
        figure_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)
    if event == "PLOT 3":
        values_to_plot = calculate_correlation("2019.csv")
        plot_correlation(values_to_plot)
        figure_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)

    if event == "CLEAR":
        if figure_agg:
            delete_figure_agg(figure_agg)

    if event == "CLOSE" or event == sg.WIN_CLOSED:
        break

window.close()
