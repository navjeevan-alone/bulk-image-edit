import sys
from PyQt5 import QtWidgets, uic

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        # Load the UI file
        uic.loadUi("initial.ui", self)  

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
