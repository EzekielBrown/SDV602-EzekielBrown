import sys
from time import sleep
sys.dont_write_bytecode = True
import PySimpleGUI as sg

def send( event, values,state):
    
    keep_going = True
    if event == "Send":   
        print("Message Recieved")

        from model.user_manager import UserManager
        a_user_manager = UserManager()
        user = UserManager().get_user()
        
        message = values['-CHAT-']
        print(f"{user}: {message}")

        message_result = a_user_manager.chat(message)
        print(f"Got login result: {message_result}")


    else:
        keep_going = True

    return keep_going 