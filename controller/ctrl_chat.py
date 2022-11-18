import sys
from time import sleep
sys.dont_write_bytecode = True
import PySimpleGUI as sg

def send( event, values,state):
    
    
    keep_going = True
    if event == "Send":           
        from model.user_manager import UserManager
        a_user_manager = UserManager()
        user = UserManager().get_user()

        message = values['Message']
        print(f"{user}: {message}")
        
    else:
        keep_going = True

    return keep_going 