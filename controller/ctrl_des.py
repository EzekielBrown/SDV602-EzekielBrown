import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg

def exit_button(event, values, state):
    keep_going = True
    if event in (sg.WIN_CLOSED, 'Exit'):
        keep_going = False
    else:
        keep_going = True
    return keep_going


def new_button(event, values, state):
    from view.view_des import DataView

    keep_going = True
    if event == 'New DES':
        app = DataView()

        app.layout_build()
        app.layout_show()
        app.layout_input()
    return keep_going 