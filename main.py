from ui import AppUI
import sys
from PyQt5.QtWidgets import QApplication
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = AppUI()
    editor.show()
    sys.exit(app.exec_())
