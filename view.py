### IMPORTS ###
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg
import csv
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


### LOCAL IMPORTS ###
import controller as ctrl

### MAIN ###

class View(object):
    def __init__(self):
        self.layout = None
        self.window = None
        self.components = {"has_components": False}
        dataset1_array = []
        dataset2_array = []
        dataset3_array = []

    def layout_build(self):
        ### HEADER COMPONENTS ###
        self.components['header'] = sg.Text('F1 Data Analysis', size=(30, 1), font=("Helvetica", 25))
        self.components['dataset1_button'] = sg.Button('Data Set 1')
        self.components['dataset2_button'] = sg.Button('Data Set 2')
        self.components['dataset3_button'] = sg.Button('Data Set 3')

        ### INPUT COMPONENTS ###
        self.components['input_data'] = sg.Combo(['Leclerc','Sainz'], key='-RACER-', enable_events=True)
        self.components['input_frame'] = sg.Frame('Input', [[self.components['input_data']]])

        ### GRAPH COMPONENTS ###
        lap = [1,2,3,4,5,6,7,8,9,10]
        time = [1.23,1.24,1.25,1.26,1.27,1.28,1.29,1.30,1.31,1.32]

        def create_plot():
            plt.plot(lap, time, color='red', marker='o')
            plt.title('Lap Time')
            plt.xlabel('Time')
            plt.ylabel('Lap')
            plt.grid(True)
            return plt.gcf()

        def draw_figure(canvas, figure):
            figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
            figure_canvas_agg.draw()
            figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
            return figure_canvas_agg
        
        def figure_draw(self, values):
            self.figure_agg = self.draw_figure(self.window['-CANVAS-'].TKCanvas, create_plot(lap, time))
            
        self.components['canvas'] = sg.Canvas(size=(640, 480), key='-CANVAS-', background_color='white')

        ### SETTINGS COMPONENTS ###
        self.components['graphbutton1'] = sg.Button("Change Chart Settings")
        self.components['graphbutton2'] = sg.Button("Pan")
        self.components['graphbutton3'] = sg.Button("+", size=(4,2))
        self.components['graphbutton4'] = sg.Button('-', size=(4,2))

        setting_col = [
            [self.components['graphbutton1']], 
            [self.components['graphbutton2']], 
            [self.components['graphbutton3'], self.components['graphbutton4']]
            ]
        
        self.components['settings_frame'] = sg.Frame('Settings', setting_col)

        ### CHAT COMPONENTS ###

        self.components['outputchat'] = sg.Output(size=(30, 10))
        self.components['sendbutton'] = sg.Button('Send')
        self.components['inputchat'] = sg.Multiline('Input Chat', size=(10, 1),  enter_submits=False, key='-QUERY-', do_not_clear=False)

        chat_col = [
            [self.components['outputchat']],
            [self.components['inputchat'], self.components['sendbutton']]
        ]

        self.components['chat_frame'] = sg.Frame('Chat', chat_col)


        ### COLUMNS LAYOUT ###
        col1 = [
            [self.components['input_frame']],
            [self.components['settings_frame']],
            [self.components['chat_frame']]
        ]

        col2 = [
            [self.components['canvas']],
        ]
        

        self.components['col_1'] = sg.Col(col1)
        self.components['col_2'] = sg.Col(col2)


        ### LAYOUT ###
        self.layout = [
            [self.components['header']],
            [self.components['dataset1_button'], self.components['dataset2_button'], self.components['dataset3_button']],
            [self.components['col_1'],self.components['col_2']]
        ]


    
    


    def layout_show(self):
        self.window = sg.Window('F1 Data Analysis', self.layout, finalize=True)



    
    def accept_input(self):

        while True:
            self.event, self.values = self.window.Read()
            if self.event is None or self.event == 'Exit':
                break
            elif self.event == 'Data Set 1':
                ctrl.dataset1(self)
            elif self.event == 'Data Set 2':
                ctrl.dataset2(self)
            elif self.event == 'Data Set 3':
                ctrl.dataset3(self)
            elif self.event == '-RACER-':
                print(self.values['-RACER-'])