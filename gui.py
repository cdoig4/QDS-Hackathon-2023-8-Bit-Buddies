import PySimpleGUI as sg

layout = [
    [sg.Text("Location")],
    [sg.In(size=(25, 1), enable_events=True, key='location')],
    [sg.Button("OK")],
    [sg.Canvas(size=(400, 400), key='canvas')]
]

window = sg.Window(title="Happiness Report", layout=layout)

while True:
    event, values = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()
