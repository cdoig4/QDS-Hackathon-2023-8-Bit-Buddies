import PySimpleGUI as sg
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')


def plot_bar_chart(plot_title, values_to_plot, x_value_labels, y_axis_label):
    ind = np.arange(len(values_to_plot))
    width = 0.4

    p1 = plt.bar(ind, values_to_plot, width)

    plt.ylabel(y_axis_label)
    plt.title(plot_title)
    plt.xticks(ind, x_value_labels)
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0],), ('Data Group 1',))


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


fig = plt.gcf()
figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds

layout = [
    [sg.Text("Location")],
    [sg.In(size=(25, 1), enable_events=True, key='-LOCATION-')],
    [sg.Button("PLOT")],
    [sg.Canvas(size=(figure_w, figure_h), key='-CANVAS-')],
    [sg.Button("CLOSE")]
]

window = sg.Window(title="Happiness Report", layout=layout, force_toplevel=True, finalize=True)

while True:
    event, values = window.read()
    if event == "PLOT" or event == sg.WIN_CLOSED:
        plot_bar_chart('Plot Title', (20, 35, 30, 35, 27), ('Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5')
             , 'Y-Axis Values')
        fig_photo = draw_figure(window['-CANVAS-'].TKCanvas, fig)
    if event == "CLOSE" or event == sg.WIN_CLOSED:
        break

window.close()
