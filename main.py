# main.py
from ui import ImageEditorUI
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = ImageEditorUI()
    editor.show()
    sys.exit(app.exec_())
