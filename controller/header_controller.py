import sys
sys.dont_write_bytecode = True

import PySimpleGUI as sg

def dataset1 (event, values, state):
    from view.data_view import DataView

    keep_going = True
    if event == 'Data 1':
        app = DataView()
        app.layout_build()
        app.layout_show()
        app.accept_input()
    return keep_going

def dataset2 (event, values, state):
    from view.data_view import DataView

    keep_going = True
    if event == 'Data 2':
        app = DataView()
        app.layout_build()
        app.layout_show()
        app.accept_input()
    return keep_going

def dataset3 (event, values, state):
    from view.data_view import DataView

    keep_going = True
    if event == 'Data 3':
        app = DataView()
        app.layout_build()
        app.layout_show()
        app.accept_input()
    return keep_going