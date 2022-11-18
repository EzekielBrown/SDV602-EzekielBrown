### Imports ##
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg


### Login Button Function For Login screen###
def login_button(event, values, state):
    from view.view_des import DataView
    
    keep_going = True
    if event == 'Log In':
        print("Got login - just testing")

        from model.user_manager import UserManager
        a_user_manager = UserManager()

        user_name = values['User']
        password = values['Password']
        print(f"Got User = {user_name} , Password = {password} - just testing")

        login_result = a_user_manager.login(user_name,password)
        print(f"Got login result: {login_result}")

        if login_result == "Login Success":
            UserManager.current_screen ="A TEST"
            app = DataView()

            app.layout_build()
            app.layout_show()
            app.layout_input()

    else:
        keep_going = True

    return keep_going

### Exit Button Function For Login screen###
def exit_button(event, values, state):
    keep_going = True
    if event in (sg.WIN_CLOSED, 'Exit'):
        keep_going = False
    else:
        keep_going = True
    
    return keep_going

### Register Button Function For Login screen###

def register_button(event, values, state):
    from view.view_register import RegisterView

    
    keep_going = True
    if event == "Register":   
        print("Got Register - just testing")
        
        from model.user_manager import UserManager
        a_user_manager = UserManager()

        user_name = values['User']
        password = values['Password']
        print(f"Got User = {user_name} , Password = {password} - just testing")
        
        register_result = a_user_manager.register(user_name,password)
        print(f"REGISTER RESULT {register_result}")

    else:
        keep_going = True

    return keep_going 