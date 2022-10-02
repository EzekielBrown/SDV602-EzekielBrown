### Import ###
import sys
sys.dont_write_bytecode = True
from view import View

### Main ###

if __name__ == '__main__':
    app = View()

    app.layout_build()
    app.layout_show()
    app.accept_input()

    pass