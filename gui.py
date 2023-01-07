import PySimpleGUI as sg
import pandas as pd
import math
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
from country_history import country_history

matplotlib.use('TkAgg')


def plot_bar_chart(plot_title, values_to_plot, y_axis_label):
    ind = np.arange(len(values_to_plot))
    width = 0.4

    p1 = plt.bar(ind, values_to_plot, width)

    maximum_value = max(values_to_plot)
    y_tick = math.ceil(maximum_value * 1.1)

    plt.ylabel(y_axis_label)
    plt.title(plot_title)
    plt.xticks(ind, (2015, 2016, 2017, 2018, 2019))
    plt.yticks(np.arange(0, y_tick, y_tick * 0.1))
    plt.legend((p1[0],), ('Data Group 1',))


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
               "Perceptions of corruption"],
              enable_events=True, key='-PARAMETER-')],
    [sg.Button("PLOT 2"), sg.Button("PLOT 3")],
    [sg.Canvas(size=(500, 350), key='-CANVAS-')],
    [sg.Button("CLOSE")]
]

window = sg.Window(title="Happiness Report", layout=layout, force_toplevel=True, finalize=True,
                   size=(1000, 1000))

while True:
    event, values = window.read()
    if event == "PLOT 1" or event == sg.WIN_CLOSED:
        parameter = values['-PARAMETER-']
        plot_values = country_history(values['-LOCATION-'], parameter)
        plot_bar_chart('Plot Title', plot_values, f'{parameter}')
        draw_figure(window['-CANVAS-'].TKCanvas, fig)
    if event == "CLOSE" or event == sg.WIN_CLOSED:
        break

window.close()
