#Currently testing and working to create a GUI for the Yu-Gi-OH! API

import PySimpleGUI as sg

layout = [[sg.Text('Hello from PySimpleGUI')], [sg.Button('OK')]]

window = sg.Window('Demo', layout)

while True:
    event, values = window.read()
    # end program if user closes window or
    # presses the ok button
    if event == 'OK' or event == sg.WIN_CLOSED:
        break

window.close()