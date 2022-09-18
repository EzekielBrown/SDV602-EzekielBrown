### Imports ###
import PySimpleGUI as sg
import os.path
import pandas as pd
import matplotlib.pyplot as plt

### Theme ###
sg.theme('DarkGrey1')

### Row Layout ###
row_chart =[
    [sg.Button("Change Chart Settings") ],
    [sg.Button("Pan") ],
    [sg.Button("+", size=(4,2)), sg.Button('-', size=(4,2))]
]

row_header =[
    [sg.Text('EXAMPLE WINDOW')], 
    [sg.Button('New Window')]
]

row_inputdata =[
    [sg.InputText('Input Data', key='inputdata', size=(20,1))],
    [sg.FolderBrowse('Browse'), sg.Button('Load Data')],
    [sg.Text('Data Loaded:'), sg.Text('No', key='dataloaded', size=(5,1))]
]

row_graph =[
    [sg.Graph(canvas_size=(400, 400), graph_bottom_left=(0, 0), graph_top_right=(400, 400)), sg.VSeperator(), sg.Frame(layout=row_chart, title='Graph Settings')]
]

row_data =[
    [sg.Table(values=[['1', '2', '3', '4'], ['a', 'b', 'c', 'd'], ['1', '2', '3', '4'], ['a', 'b', 'c', 'd']], headings=['col1', 'col2', 'col3', 'col4'], max_col_width=25, auto_size_columns=False, justification='right', num_rows=4, alternating_row_color='lightblue', key='-TABLE-', row_height=15, hide_vertical_scroll=False, enable_events=True, bind_return_key=True, col_widths=[10, 10, 10, 10], tooltip='This is a table')]
]

row_chat =[
    [sg.Output(size=(80, 10), font=('Helvetica 10'))],
    [sg.Multiline(size=(80, 3), enter_submits=False, key='-QUERY-', do_not_clear=False), sg.Button('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True)]
]

### Layout ###
layout = [
    [sg.Frame(layout=row_header, title='Header')],
    [sg.Frame(layout=row_inputdata, title='Input Data')],
    [sg.Frame(layout=row_graph, title='Graph')],
    [sg.Frame(layout=row_data, title='Data')],
    [sg.Frame(layout=row_chat, title='Chat')]
    ]

### Window ###

window = sg.Window("Data Explorer",layout)


### Event Loop ###
while True:
    event, value = window.read()
    if event in (sg.WIN_CLOSED, 'EXIT'):
        break
    if event == 'SEND':
        query = value['-QUERY-'].rstrip()
        print('User: {}'.format(query), flush=True)


### Close Window ###
window.close()  