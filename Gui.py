#Currently testing and working to create a GUI for the Yu-Gi-OH! API

import PySimpleGUI as sg
from API import YuGiOhAPI as yugs

layout = [
    [sg.Text('Yugioh Card'),
    sg.In(size=(25, 1), enable_events = True, key = '-CARD_NAME-')
    ],
    [sg.Listbox(
        values=[], enable_events= True, size = (40,20), key='List_box'
    )
    ]
]

window = sg.Window('Demo', layout)

while True:
    event, values = window.read()
    # end program if user closes window or
    # presses the ok button
    if event == 'OK' or event == sg.WIN_CLOSED:
        break

    if event == '-CARD_NAME-':
        card = yugs('-CARD_NAME-')
        details = [card.get_name(),
                    card.get_type,
                    ]
        try:
            
        except:

        


window.close()