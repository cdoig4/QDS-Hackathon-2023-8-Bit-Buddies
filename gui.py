import PySimpleGUI as sg

layout = [
    [sg.Text("Hello from PySimpleGUI")],
    [sg.In(size=(25, 1), enable_events=True, key='location')],
    [sg.Button("OK")],
    [sg.Listbox(values=[], enable_events=True, size=(40, 20), key='file_list')]
]

window = sg.Window(title="Happiness Report", layout=layout)

while True:
    event, values = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()
