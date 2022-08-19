import PySimpleGUI as sg
import os.path


# -- Layouts that will be displayed --
login_layout = [
    [sg.Text("Username"), sg.InputText(key='-USERNAME-')],
    [sg.Text("Password"), sg.InputText(password_char="*", key='-PASSWORD-')],
    [sg.Button("Login"), sg.Button("Close")],
]

home_layout = [
    [sg.Text("Welcome to the home screen\nThis Application will...")]
]
           

data_layout = [
    [sg.Text('Current Data Loaded:')],
    [sg.Text('\nLoad Data')],
    [sg.InputText(), sg.FolderBrowse()],
]

graph_layout = [
    [sg.Listbox(values=[], size=(40,20)), sg.VSeperator(), sg.Graph(canvas_size=(400, 400), graph_bottom_left=(0, 0), graph_top_right=(400, 400))]
]

# -- Create the Layout that will be display --
layout = [
    [sg.Text('Login', key='-TITLE-' )],
    [sg.Button('Home', key='-HOMEBUTTON-', visible=False), sg.Button('Data', key='-DATABUTTON-', visible=False), sg.Button('Graph', key='-GRAPHBUTTON-', visible=False)],
    [sg.Column(login_layout, key='-COL1-'), sg.Column(home_layout, visible=False, key='-COL2-'), sg.Column(data_layout, visible=False, key='-COL3-'), sg.Column(graph_layout, visible=False, key='-COL4-')],
]


window = sg.Window('Data + Graph Viewer', layout,)

layout = 1  # The current visible layout
while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Close'):
        print("Close")
        break

    if event == '-HOMEBUTTON-' or 'login':
        window[f'-COL{layout}-'].update(visible=False)
        layout = 2
        window[f'-COL{layout}-'].update(visible=True)
        window['-TITLE-'].update('Home')
        window['-HOMEBUTTON-'].update(visible=True)
        window['-DATABUTTON-'].update(visible=True)
        window['-GRAPHBUTTON-'].update(visible=True)
        print("This is the Home Page")

    if event == '-DATABUTTON-': 
        window[f'-COL{layout}-'].update(visible=False)
        layout = 3
        window[f'-COL{layout}-'].update(visible=True)
        window['-TITLE-'].update('Data')
        print("This is the Data Page")

    if event == '-GRAPHBUTTON-': 
        window[f'-COL{layout}-'].update(visible=False)
        layout = 4
        window[f'-COL{layout}-'].update(visible=True)
        window['-TITLE-'].update('Graph')
        print("This is the Graph Page")

window.close()
