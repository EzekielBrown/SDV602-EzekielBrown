### Imports ##
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


### Custom Imports ###
import controller.ctrl_des as ctrl

### Main Class ###
class DataView(object):
    def __init__(self):
        self.window = None
        self.layout = []
        self.components = {'components': False}
        self.controls = []
        self.figure_agg = None
        self.data_frame = pd.DataFrame()
        self.data_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\data"
    
    def layout_build(self, **kwargs):
         ### Theme ###
        theme_dict = {'BACKGROUND': '#2B475D',
                    'TEXT': '#FFFFFF',
                    'INPUT': '#F2EFE8',
                    'TEXT_INPUT': '#000000',
                    'SCROLL': '#F2EFE8',
                    'BUTTON': ('#000000', '#C2D4D8'),
                    'PROGRESS': ('#FFFFFF', '#C7D5E0'),
                    'BORDER': 0,'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0}

        sg.theme_add_new('Dashboard', theme_dict)
        sg.theme('Dashboard')

        BORDER_COLOR = '#C7D5E0'
        DARK_HEADER_COLOR = '#1B2838'

        header = [
            [sg.Text('Welcome {user}', font='Any 20', background_color=DARK_HEADER_COLOR, enable_events=True, grab=False), sg.Push(background_color=DARK_HEADER_COLOR)],
        ]

        self.components['header'] = sg.Frame('', header,   pad=(0,0), background_color=DARK_HEADER_COLOR,  expand_x=True, border_width=0, grab=True)

        self.components['new_button'] = sg.B('New DES')
        self.controls += [ctrl.new_button]
        self.components['exit_button'] = sg.B('Exit')
        self.controls += [ctrl.exit_button]

        self.components['figure_select'] =  sg.B('Open CSV')
        self.components['input_label'] = sg.T('Input                                               ', font='Any 12', background_color=DARK_HEADER_COLOR, enable_events=True, grab=False)

        self.components['canvas'] = sg.Canvas(size=(650, 500), key='-CANVAS-')
        self.components['canvas_label'] = sg.T('Data Visualization                                                                                                                                ', font='Any 12', background_color=DARK_HEADER_COLOR, enable_events=True, grab=False)

        self.components['chat_label'] = sg.T('Chat                                               ', font='Any 12', background_color=DARK_HEADER_COLOR, enable_events=True, grab=False)
        self.components['chat_input'] = sg.I('Type your message...', size=(20, 1))
        self.components['send_button'] = sg.B('Send')
        self.components['chat_log'] = sg.Multiline('Input Chat', size=(30, 5),  enter_submits=False, key='-QUERY-', do_not_clear=False)

        self.components['blank'] = sg.T('', background_color=BORDER_COLOR)
        

        col1 = [
            [self.components['input_label']],
            [self.components['figure_select']],
            [self.components['blank']],
            [self.components['chat_label']],
            [self.components['chat_log']],
            [self.components['chat_input'], self.components['send_button']]
        ]

        col2 = [
            [self.components['canvas_label']],
            [self.components['canvas']],
        ]

        self.components['column1'] = sg.Column(col1, background_color=BORDER_COLOR)
        self.components['column2'] = sg.Column(col2, background_color=BORDER_COLOR)

        self.layout = [
            [self.components['header']],
            [self.components['new_button'], self.components['exit_button']],
            [self.components['column1'], self.components['column2']],
        ]
    
    def draw_figure(self, canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg

    def delete_figure_agg(self):
        if self.figure_agg:
            self.figure_agg.get_tk_widget().forget()
        plt.close('all')
    
    def layout_show(self):
        if self.layout != []:
            self.window = sg.Window('Data Explorer', self.layout, finalize=True, margins=(0,0), background_color="#C7D5E0", no_titlebar=False, resizable=True, right_click_menu=sg.MENU_RIGHT_CLICK_EXIT)
    
    def layout_input(self):
        if self.window != None:
            keep_going = True

            while keep_going == True:
                event, values = self.window.read()

                for accept_control in self.controls:
                    keep_going = accept_control(event, values, {'view':self})
                if event == 'Open CSV':
                    file_path = sg.PopupGetFile('Please select a CSV file', file_types=(("CSV Files", "*.csv"),), initial_folder=self.data_path)
                    if file_path:
                        self.delete_figure_agg()
                        self.data_frame = pd.read_csv(file_path).pivot('Race', 'Driver', 'Points')
                        data_plot = self.data_frame.plot(kind='line')
                        
                        ax = data_plot.axes
                        ax.set_title('Driver Championship Points', fontsize='12')
                        ax.set_xlabel('Race', fontsize='12')
                        ax.set_ylabel('Points', fontsize='12')
                        ax.legend(loc='center left', bbox_to_anchor=(0, 0.5))
                        ax.grid(True)

                        fig = plt.gcf()
                        self.figure_agg = self.draw_figure(self.window['-CANVAS-'].TKCanvas, fig)
            self.window.close()
            