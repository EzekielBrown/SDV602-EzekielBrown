### Imports ###
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg

### Custom Imports ###
import controller.ctrl_login as ctrl

'''
The View for the login screen.
'''

### Main Class ###
class LoginView(object):  
    def __init__(self):       
        self.window = None
        self.layout = []
        self.components = {'components': False}
        self.controls = []
        
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


        ### Login Components ###
        header = [
            [sg.Text('Welcome', font='Any 20', background_color=DARK_HEADER_COLOR, enable_events=True, grab=False), sg.Push(background_color=DARK_HEADER_COLOR)],
        ]

        self.components['header'] = sg.Frame('', header,   pad=(0,0), background_color=DARK_HEADER_COLOR,  expand_x=True, border_width=0, grab=True)
        self.components['usr_label'] = sg.T('Username')
        self.components['usr_entry'] = sg.In("", key="User", size=(40, 2))
        self.components['pw_label'] = sg.T('Password')
        self.components['pw_entry'] = sg.In('', key="Password", password_char='*', size=(40, 2))
        self.components['blank'] = sg.T('', background_color=BORDER_COLOR)
        self.components['login_button'] = sg.B('Log In')
        self.controls += [ctrl.login_button]
        self.components['register_button'] = sg.B('Register')
        self.controls += [ctrl.register_button]
        self.components['exit_button'] = sg.B('Exit')
        self.controls += [ctrl.exit_button]
        
        ### Login Layout ###
        self.layout = [
            [self.components['header']],
            [self.components['blank']],
            [self.components['usr_label'], self.components['usr_entry']],
            [self.components['pw_label'], self.components['pw_entry']],
            [self.components['login_button'], self.components['register_button'], self.components['exit_button']],
        ]
        
    def layout_show(self):
        if self.layout != []:
            print("Login Screen")
            self.window = sg.Window('Login', self.layout, finalize=True, margins=(0,0), background_color="#C7D5E0", no_titlebar=False, resizable=True, right_click_menu=sg.MENU_RIGHT_CLICK_EXIT)
            
    def layout_input(self):
        if self.window != None:
            keep_going = True

            while keep_going == True:
                event, values = self.window.read()
                for accept_control in self.controls:
                    keep_going = accept_control(event, values, {'view':self})
                else:
                    continue
            self.window.close()