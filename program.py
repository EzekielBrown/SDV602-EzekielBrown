### Import ###
import sys
sys.dont_write_bytecode = True
from view.data_view import DataView

### Main ###

if __name__ == '__main__':
    app = DataView()

    app.layout_build()
    app.layout_show()
    app.accept_input()

    pass