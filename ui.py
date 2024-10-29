# ui.py
import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel
from image_processor import process_images

class ImageEditorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Bulk Image Editor')

        layout = QVBoxLayout()

        self.input_label = QLabel('No input folder selected')
        layout.addWidget(self.input_label)

        self.output_label = QLabel('No output folder selected')
        layout.addWidget(self.output_label)

        btn_select_input = QPushButton('Select Input Folder')
        btn_select_input.clicked.connect(self.select_input_folder)
        layout.addWidget(btn_select_input)

        btn_select_output = QPushButton('Select Output Folder')
        btn_select_output.clicked.connect(self.select_output_folder)
        layout.addWidget(btn_select_output)

        btn_run = QPushButton('Run')
        btn_run.clicked.connect(self.run_processing)
        layout.addWidget(btn_run)

        self.setLayout(layout)

        self.input_folder = None
        self.output_folder = os.path.join(os.path.dirname(__file__), 'output')  # Default output folder

    def select_input_folder(self):
        self.input_folder = QFileDialog.getExistingDirectory(self, 'Select Input Folder')
        self.input_label.setText(f'Selected Input Folder: {self.input_folder}')

    def select_output_folder(self):
        self.output_folder = QFileDialog.getExistingDirectory(self, 'Select Output Folder')
        self.output_label.setText(f'Selected Output Folder: {self.output_folder}')

    def run_processing(self):
        if self.input_folder and self.output_folder:
            process_images(self.input_folder, self.output_folder)
        else:
            self.input_label.setText('Please select both input and output folders.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageEditorApp()
    ex.resize(400, 200)
    ex.show()
    sys.exit(app.exec_())
