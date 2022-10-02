### Imports ###
import sys
sys.dont_write_bytecode = True
import PySimpleGUI as sg

### Main ###

### Header Functions ###
def dataset1(self):
    print("Dataset 1")
    from view import View
    app = View()
    app.layout_build()
    app.layout_show()
    app.accept_input()

def dataset2(self):
    print("Dataset 2")
    from view import View
    app = View()
    app.layout_build()
    app.layout_show()
    app.accept_input()

def dataset3(self):
    print("Dataset 3")
    from view import View
    app = View()
    app.layout_build()
    app.layout_show()
    app.accept_input()
