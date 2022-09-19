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

        ### Header Components
        self.components['header'] = sg.Text('Data View', font=('Helvetica', 20))
        self.components['data1button'] = sg.Button('Data 1')
        self.components['data2button'] = sg.Button('Data 2')
        self.components['data3button'] = sg.Button('Data 3')
        self.components['hseperator'] = sg.Text('_'*90)

        ### Input Data Components ###
        self.components['inputinputtext'] = sg.InputText('Input Data', key='inputdata', size=(20,1))
        self.components['inputbrowse'] = sg.FolderBrowse('Browse')
        self.components['inputload'] = sg.Button('Load Data')

        row_input =[
            [self.components['inputinputtext']],
            [self.components['inputbrowse'], self.components['inputload']]
        ]
        
        self.components['row_input'] = sg.Frame('Input Data', row_input)

        ### Graph Components ###
        self.components['canvas'] = sg.Canvas(size=(400, 400))
        self.components['vseperator'] = sg.VSeperator()
        self.components['graphbutton1'] = sg.Button("Change Chart Settings")
        self.components['graphbutton2'] = sg.Button("Pan")
        self.components['graphbutton3'] = sg.Button("+", size=(4,2))
        self.components['graphbutton4'] = sg.Button('-', size=(4,2))

        col2_graph = [
            [self.components['graphbutton1']],
            [self.components['graphbutton2']],
            [self.components['graphbutton3'], self.components['graphbutton4']]
        ]

        self.components['col2_graph'] = sg.Column(col2_graph)

        row_graph =[
            [self.components['canvas'], self.components['vseperator'], self.components['col2_graph']]
        ]

        self.components['row_graph'] = sg.Frame('Graph', row_graph)

        ### Data Components ###
        self.components['datatable'] = sg.Table(values=[['1', '2', '3', '4'], ['a', 'b', 'c', 'd'], ['1', '2', '3', '4'], ['a', 'b', 'c', 'd']], headings=['col1', 'col2', 'col3', 'col4'], max_col_width=25, auto_size_columns=False, justification='right', num_rows=4, alternating_row_color='lightblue', key='-TABLE-', row_height=15, hide_vertical_scroll=False, enable_events=True, bind_return_key=True, col_widths=[10, 10, 10, 10], tooltip='This is a table')

        row_data =[
            [self.components['datatable']]
        ]

        self.components['row_data'] = sg.Frame('Data', row_data)

        ### Chat Components ###
        self.components['outputchat'] = sg.Output(size=(30, 10))
        self.components['sendbutton'] = sg.Button('Send')
        self.components['inputchat'] = sg.Multiline('Input Chat',  enter_submits=False, key='-QUERY-', do_not_clear=False)

        row_chat =[
            [self.components['outputchat']],
            [self.components['inputchat'], self.components['sendbutton']]
        ]

        self.components['row_chat'] = sg.Frame('Chat', row_chat)
        
        ### Layout ###
        self.layout = [
                [self.components['header']],
                [self.components['data1button'],self.components['data2button'],self.components['data3button']],
                [self.components['hseperator']],
                [self.components['row_input']],
                [self.components['row_graph']],
                [self.components['row_data']],
                [self.components['row_chat']]
                ]

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
