import PySimpleGUI as sg
import os.path

sg.theme('DarkGrey1')
col1 =[
        [sg.Button(button_text="Change Chart Settings") ],
        [sg.Button(button_text="Pan") ],
        [sg.Button(button_text="Update") ]
        ]

layout = [
    [sg.Text('EXAMPLE WINDOW')],
    [sg.Button('New Window')],
    [sg.InputText(), sg.FolderBrowse()],
    [sg.Graph(canvas_size=(400, 400), graph_bottom_left=(0, 0), graph_top_right=(400, 400)), sg.VSeperator(), sg.Frame(layout=col1, title='Graph')],
    [sg.Text('Table Infomation')],
    [sg.Table(values=[['1', '2', '3', '4'], ['a', 'b', 'c', 'd'], ['1', '2', '3', '4'], ['a', 'b', 'c', 'd']], headings=['col1', 'col2', 'col3', 'col4'], max_col_width=25, auto_size_columns=False, justification='right', num_rows=4, alternating_row_color='lightblue', key='-TABLE-', row_height=15, hide_vertical_scroll=False, enable_events=True, bind_return_key=True, col_widths=[10, 10, 10, 10], tooltip='This is a table')],
    [sg.Output(size=(80, 10), font=('Helvetica 10'))],
          [sg.Multiline(size=(80, 3), enter_submits=False, key='-QUERY-', do_not_clear=False),
           sg.Button('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True),]
    ]


window =sg.Window("Data Explorer",layout)


while True:
    event, value = window.read()
    if event in (sg.WIN_CLOSED, 'EXIT'):
        break
    if event == 'SEND':
        query = value['-QUERY-'].rstrip()
        print('User: {}'.format(query), flush=True)


window.close()  

