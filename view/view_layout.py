import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg

import controller.input_controller as input_controller
import controller.header_controller as header_controller

### Input View ###
def row_input_data(self):
        self.components['data_loaded'] = sg.Text('Data Loaded:')
        self.components['data_file_name'] = sg.Text('No data')
        self.components['input_browse'] = sg.FolderBrowse('Browse')
        self.components['input_load'] = sg.Button('Load Data', key='-LOADDATA')
        self.components['input_data'] = sg.Combo(['Australia','Austria', 'Azerbaijan'], key='-INPUTDATA-', enable_events=True)

        ### Return ###
        return [
                [self.components['input_data']],
                [self.components['input_browse'], self.components['input_load']],
                [self.components['data_loaded'], self.components['data_file_name']]
                ]

### Header View ###

def row_header(self):
        self.components['header'] = sg.Text('Data View', font=('Helvetica', 20))
        self.components['data1button'] = sg.Button('Data 1')
        self.controls += [header_controller.dataset1]
        self.components['data2button'] = sg.Button('Data 2')
        self.controls += [header_controller.dataset2]
        self.components['data3button'] = sg.Button('Data 3')
        self.controls += [header_controller.dataset3]
        self.components['hseperator'] = sg.Text('_'*90)


        ### Return ###
        return [
            [self.components['header']],
            [self.components['data1button'], self.components['data2button'], self.components['data3button']],
            [self.components['hseperator']]
        ]

### Graph Settings View ###


def row_graph_settings(self):
        self.components['graphbutton1'] = sg.Button("Change Chart Settings")
        self.components['graphbutton2'] = sg.Button("Pan")
        self.components['graphbutton3'] = sg.Button("+", size=(4,2))
        self.components['graphbutton4'] = sg.Button('-', size=(4,2))

        ### Return ###
        return [
            [self.components['graphbutton1']],
            [self.components['graphbutton2']],
            [self.components['graphbutton3'], self.components['graphbutton4']]     
        ]

### Chat View ###

def row_chat_box(self):
        self.components['outputchat'] = sg.Output(size=(30, 10))
        self.components['sendbutton'] = sg.Button('Send')
        self.components['inputchat'] = sg.Multiline('Input Chat',  enter_submits=False, key='-QUERY-', do_not_clear=False)

        ### Return ###
        return [
            [self.components['outputchat']],
            [self.components['inputchat'], self.components['sendbutton']]     
        ]
    