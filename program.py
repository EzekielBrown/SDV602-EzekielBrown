import sys
sys.dont_write_bytecode = True
from view.view_login import LoginView

if __name__ == "__main__" :
    app = LoginView()

    app.layout_build()
    app.layout_show()
    app.layout_input()

    pass