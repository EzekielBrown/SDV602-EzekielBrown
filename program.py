### Imports ###
import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import csv
from matplotlib.ticker import FormatStrFormatter
import fastf1
import fastf1.plotting


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
BPAD_TOP = ((20,20), (20, 10))
BPAD_LEFT = ((20,10), (0, 0))
BPAD_LEFT_INSIDE = (0, (10, 0))
BPAD_RIGHT = ((10,20), (10, 0))

x = []
y = []

### F1 Data ###
fastf1.plotting.setup_mpl()
session = fastf1.get_session(2022, 'singapore', 'Race')
fastf1.Cache.enable_cache('cache/')

### Main ###
def draw_figure_w_toolbar(canvas, fig, canvas_toolbar):
    if canvas.children:
        for child in canvas.winfo_children():
            child.destroy()
    if canvas_toolbar.children:
        for child in canvas_toolbar.winfo_children():
            child.destroy()
    figure_canvas_agg = FigureCanvasTkAgg(fig, master=canvas)
    figure_canvas_agg.draw()
    toolbar = Toolbar(figure_canvas_agg, canvas_toolbar)
    toolbar.update()
    figure_canvas_agg.get_tk_widget().pack(side='right', fill='both', expand=1)


class Toolbar(NavigationToolbar2Tk):
    def __init__(self, *args, **kwargs):
        super(Toolbar, self).__init__(*args, **kwargs)


### Layouts ###


### Layout 1 ###
def make_window1():
    top_banner1 = [
        [sg.Text('Data Set 1', font='Any 20', background_color=DARK_HEADER_COLOR, enable_events=True, grab=False), sg.Push(background_color=DARK_HEADER_COLOR)],
]
    col11 = [
        [sg.Text('Driver                                               ', font='Any 12', background_color=DARK_HEADER_COLOR, enable_events=True, grab=False)],
        [sg.Combo(values=['Hamilton','Russell', 'Vertstappen', 'Perez', 'Leclerc', 'Sainz', 'Norris', 'Ricciardo', 'Alonso', 'Ocon', 'Gasly', 'Tsunoda', 'Bottas', 'Guanyu', 'Vettel', 'Stroll', 'Magnussen', 'Schumacher', 'Albon', 'Latifi'], key='-RACER-', default_value='Hamilton', enable_events=True)],
        [sg.B('Plot', pad=(5,5,100,100))],
        [sg.Text('')],
        [sg.Text('Chat                                                 ', font='Any 12', background_color=DARK_HEADER_COLOR, enable_events=True, grab=False)],
        [sg.Output(size=(30, 10))],
        [sg.Multiline('Input Chat', size=(23, 1),  enter_submits=False, key='-QUERY-', do_not_clear=False), sg.Button('Send')],
    ]

    col12 = [
        [sg.Canvas(key='fig_cv', size=(600, 500))],
        [sg.Canvas(key='controls_cv')],
    ]

    layout1 = [ 
            [sg.Frame('', top_banner1,   pad=(0,0), background_color=DARK_HEADER_COLOR,  expand_x=True, border_width=0, grab=True)],
            [sg.B('Next'), sg.B('Exit')],
            [sg.Column(col11), sg.Column(col12)]]
    return sg.Window('Window 1', layout1, finalize=True, margins=(0,0), background_color=BORDER_COLOR, no_titlebar=True, resizable=True, right_click_menu=sg.MENU_RIGHT_CLICK_EXIT)

### Layout 2 ###

def make_window2():
    top_banner2 = [
    [sg.Text('Data Set 2', font='Any 20', background_color=DARK_HEADER_COLOR, enable_events=True, grab=False), sg.Push(background_color=DARK_HEADER_COLOR)],
]
    col21 = [
    [sg.Text('Driver                                               ', font='Any 12', background_color=DARK_HEADER_COLOR, enable_events=True, grab=False)],
    [sg.Combo(values=['Hamilton','Russell', 'Vertstappen', 'Perez', 'Leclerc', 'Sainz', 'Norris', 'Ricciardo', 'Alonso', 'Ocon', 'Gasly', 'Tsunoda', 'Bottas', 'Guanyu', 'Vettel', 'Stroll', 'Magnussen', 'Schumacher', 'Albon', 'Latifi'], key='-RACER-', default_value='Hamilton', enable_events=True)],
    [sg.B('Plot')],
    [sg.Text('')],
    [sg.Text('Chat                                                 ', font='Any 12', background_color=DARK_HEADER_COLOR, enable_events=True, grab=False)],
    [sg.Output(size=(30, 10))],
    [sg.Multiline('Input Chat', size=(23, 1),  enter_submits=False, key='-QUERY-', do_not_clear=False), sg.Button('Send')],
    ]

    col22 = [
        [sg.Canvas(key='fig_cv', size=(600, 500))],
        [sg.Canvas(key='controls_cv')],
    ]   
    layout2 = [
            [sg.Frame('', top_banner2,   pad=(0,0), background_color=DARK_HEADER_COLOR,  expand_x=True, border_width=0, grab=True)],
            [sg.B('Next'), sg.B('Exit')],
            [sg.Column(col21), sg.Column(col22)]]
    return sg.Window('Window 2', layout2, finalize=True, margins=(0,0), background_color=BORDER_COLOR, no_titlebar=True, resizable=True, right_click_menu=sg.MENU_RIGHT_CLICK_EXIT)

### Layout 3 ###

def make_window3():
    top_banner3 = [
    [sg.Text('Data Set 3', font='Any 20', background_color=DARK_HEADER_COLOR, enable_events=True, grab=False), sg.Push(background_color=DARK_HEADER_COLOR)],
]
    col31 = [
    [sg.Text('Driver                                               ', font='Any 12', background_color=DARK_HEADER_COLOR, enable_events=True, grab=False)],
    [sg.Combo(values=['Hamilton','Russell', 'Vertstappen', 'Perez', 'Leclerc', 'Sainz', 'Norris', 'Ricciardo', 'Alonso', 'Ocon', 'Gasly', 'Tsunoda', 'Bottas', 'Guanyu', 'Vettel', 'Stroll', 'Magnussen', 'Schumacher', 'Albon', 'Latifi'], key='-RACER-', default_value='Hamilton', enable_events=True)],
    [sg.B('Plot')],        
    [sg.Text('')],
    [sg.Text('Chat                                                 ', font='Any 12', background_color=DARK_HEADER_COLOR, enable_events=True, grab=False)],
    [sg.Output(size=(30, 10))],
    [sg.Multiline('Input Chat', size=(23, 1),  enter_submits=False, key='-QUERY-', do_not_clear=False), sg.Button('Send')],
    ]

    col32 = [
        [sg.Canvas(key='fig_cv', size=(600, 500))],
        [sg.Canvas(key='controls_cv')],
    ]
    layout3 = [
            [sg.Frame('', top_banner3,   pad=(0,0), background_color=DARK_HEADER_COLOR,  expand_x=True, border_width=0, grab=True)],
            [sg.B('Next'), sg.B('Exit')],
            [sg.Column(col31), sg.Column(col32)]]
    return sg.Window('Window 3', layout3, finalize=True, margins=(0,0), background_color=BORDER_COLOR, no_titlebar=True, resizable=True, right_click_menu=sg.MENU_RIGHT_CLICK_EXIT)



### Window ###

window1, window2, window3 = make_window1(), None, None

while True:
    window, event, values = sg.read_all_windows()
    if window == window1 and event in (sg.WIN_CLOSED, 'Exit'):
        break
    if window == window1:
        

        if event == 'Plot':
            session.load()
            fast_hamilton = session.laps.pick_driver('HAM').pick_fastest()
            ham_car_data = fast_hamilton.get_car_data()
            t = ham_car_data['Time']
            vCar = ham_car_data['Speed']

            fig, ax = plt.subplots()
            ax.plot(t, vCar, label='Fast')
            ax.set_xlabel('Time')
            ax.set_ylabel('Speed [Km/h]')
            ax.set_title('Hamilton Max Speed Analysis')
            ax.legend()

            draw_figure_w_toolbar(window['fig_cv'].TKCanvas, fig, window['controls_cv'].TKCanvas)

        elif event == 'Next':
            window1.hide()
            window2 = make_window2()
    
    if window == window2:
        if event == 'Plot':
            session.load()
            fast_hamilton = session.laps.pick_driver('HAM').pick_fastest()
            ham_car_data = fast_hamilton.get_car_data()
            t = ham_car_data['Time']
            vCar = ham_car_data['Speed']

            fig, ax = plt.subplots()
            ax.plot(t, vCar, label='Fast')
            ax.set_xlabel('Time')
            ax.set_ylabel('Speed [Km/h]')
            ax.set_title('Hamilton Max Speed Analysis')
            ax.legend()

            draw_figure_w_toolbar(window['fig_cv'].TKCanvas, fig, window['controls_cv'].TKCanvas)

        elif event == 'Next':
            window2.hide()
            window3 = make_window3()

        elif event == 'Exit':
            break
    
    if window == window3:
        if event == 'Plot':
            session.load()
            fast_hamilton = session.laps.pick_driver('HAM').pick_fastest()
            ham_car_data = fast_hamilton.get_car_data()
            t = ham_car_data['Time']
            vCar = ham_car_data['Speed']

            fig, ax = plt.subplots()
            ax.plot(t, vCar, label='Fast')
            ax.set_xlabel('Time')
            ax.set_ylabel('Speed [Km/h]')
            ax.set_title('Hamilton Max Speed Analysis')
            ax.legend()

            draw_figure_w_toolbar(window['fig_cv'].TKCanvas, fig, window['controls_cv'].TKCanvas)
        elif event == 'Next':
            window1 = make_window1()
            window3.hide()
        
        elif event == 'Exit':
            break

window.close()
