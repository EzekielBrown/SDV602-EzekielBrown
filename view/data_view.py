### Import ###
import sys
sys.dont_write_bytecode = True
from typing import Dict
import PySimpleGUI as sg
import inspect
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt

### Custom ###
import view.view_layout as vl

### Main ###

class DataView(object):
    datawindow = []
    currentdatawindow = 0
    def __init__(self):
        
        self.window = None
        self.layout = []
        self.components = {"has_components":False}
        self.controls = []
        DataView.currentdatawindow +=1 
        DataView.datawindow += [self]


    def layout_build(self,**kwargs):

        sg.theme('DarkGrey1')      
        ### Layout ###

        self.components['canvas'] = sg.Canvas(size=(400, 400))
        self.components['test'] = sg.Text('Test')
        self.components['test2'] = sg.Text('Test2')
        self.components['row_input'] = sg.Frame('Input Data', vl.row_input_data(self))
        self.components['row_settings'] = sg.Frame('Graph Settings', vl.row_graph_settings(self))
        self.components['row_chat'] = sg.Frame('Chat', vl.row_chat_box(self))

        col1 = [
            [self.components['test']],
            [self.components['row_input']],
            [self.components['row_settings']],
            [self.components['row_chat']]
        ]

        col2 = [
            [self.components['canvas']]
        ]

        self.components['col_1'] = sg.Col(col1)
        self.components['col_2'] = sg.Col(col2)

        self.layout = [[
                [vl.row_header(self)],
                [self.components['col_1'], self.components['col_2']]
                ]]

    def layout_show(self):
        self.window = sg.Window('Data View', self.layout, finalize=True)

    def accept_input(self):

            if self.window != None :
                keep_going = True
                
                while keep_going == True:
                    event, values = self.window.read()
                    for accept_control in self.controls:
                        keep_going = accept_control(event,values,{'view':self})
                self.window.close()        



### 