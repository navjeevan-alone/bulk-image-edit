from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QLineEdit, QComboBox, QSpinBox, QFileDialog,QSpacerItem, QSizePolicy
)
from PyQt5.QtGui import QIcon,QFontDatabase,QPixmap,QFont
from PyQt5.QtCore import Qt
import logging
import sys
from utils import load_stylesheet, resource_path, update_aspect_ratio, update_size_units
from image_processing import ImageProcessing

class AppUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Set main window properties
        self.setWindowTitle("Magic Edits")
        self.setGeometry(200, 100, 800, 500)
        self.setMaximumWidth(600)  # Max width for central alignment
        self.setWindowIcon(QIcon(resource_path("./assets/icon.ico")))
        self.setStyleSheet(load_stylesheet(resource_path("./styles.css")))

        # Load custom fonts
        QFontDatabase.addApplicationFont(resource_path("assets/Norican-Regular.ttf"))
        QFontDatabase.addApplicationFont(resource_path("assets/Poppins-Regular.ttf"))

        # self.setFont(QFont("Poppins", 14))
        # Central widget for layout
        central_widget = QWidget(self)
        central_layout = QVBoxLayout(central_widget)
        central_layout.setAlignment(Qt.AlignCenter)

        # App image and title
        brand_layout = QHBoxLayout()
        # brand_layout.insertSpacing(3,100)
        # Add spacer
        self.right_spacer = QSpacerItem(40, 40, QSizePolicy.Expanding, QSizePolicy.Maximum)

        self.app_image_label = QLabel(self)
        self.app_image_label.setPixmap(QPixmap(resource_path("assets/logo-transparent.png")).scaled(120, 120, Qt.KeepAspectRatio))
        self.app_image_label.setAlignment(Qt.AlignRight)
        
        # App title with 'Norican' font
        self.app_title_label = QLabel("Magic Edits")
        self.app_title_label.setObjectName("app_title_label")
        self.app_title_label.setAlignment(Qt.AlignCenter)

        # Add widgets to brand layout 
        brand_layout.addWidget(self.app_image_label)
        brand_layout.addWidget(self.app_title_label)
        brand_layout.addItem(self.right_spacer)

        
        # Input Folder Selection
        input_layout = QHBoxLayout()
        input_label = QLabel("Select Input Folder:")
        self.input_folder_path = QLineEdit()
        self.input_folder_path.setPlaceholderText("Input folder path...")
        input_button = QPushButton("Select Folder") 
        input_button.clicked.connect(self.select_input_folder)

        input_layout.addWidget(input_label)
        input_layout.addWidget(self.input_folder_path)
        input_layout.addWidget(input_button)

        # Output Folder Selection
        output_layout = QHBoxLayout()
        output_label = QLabel("Select Output Folder:")
        self.output_folder_path = QLineEdit()
        self.output_folder_path.setPlaceholderText("Output folder path...")
        output_button = QPushButton("Select Folder")
        output_button.clicked.connect(self.select_output_folder)

        output_layout.addWidget(output_label)
        output_layout.addWidget(self.output_folder_path)
        output_layout.addWidget(output_button)

        # Image Size
        size_layout = QHBoxLayout()
        size_label = QLabel("Image Size (Width x Height):")
        self.width_input = QSpinBox()
        self.width_input.setValue(1080)
        self.width_input.setMaximum(10000)
        self.height_input = QSpinBox()
        self.height_input.setValue(1080)
        self.height_input.setMaximum(10000)

        self.size_unit_combo = QComboBox()
        self.size_unit_combo.addItems(["px", "mm", "cm", "inch"])
        self.size_unit_combo.currentIndexChanged.connect(self.sync_size_units)

        size_layout.addWidget(size_label)
        size_layout.addWidget(self.width_input)
        size_layout.addWidget(self.height_input)
        size_layout.addWidget(self.size_unit_combo)

        # Background Color
        bg_layout = QHBoxLayout()
        bg_label = QLabel("Background Color:")
        self.bg_color_input = QLineEdit()
        self.bg_color_input.setPlaceholderText("Enter color (e.g., #FFFFFF for white)")
        
        bg_layout.addWidget(bg_label)
        bg_layout.addWidget(self.bg_color_input)
        
        # Background Color
        padding_layout = QHBoxLayout()
        padding_label = QLabel("Padding :")
        
        self.padding_input = QSpinBox()
        # self.padding_input.setPlaceholderText("Input folder path...") 
        self.padding_input.setValue(0)
        self.padding_input.setMaximum(1000) 

        padding_layout.addWidget(padding_label)
        padding_layout.addWidget(self.padding_input)

        # File Format Selection
        format_layout = QHBoxLayout()
        format_label = QLabel("Output File Format:")
        self.file_format_combo = QComboBox()
        self.file_format_combo.setObjectName("file_format_combo")
        self.file_format_combo.addItems(["Original", "JPG", "PNG", "JPEG", "WEBP"])

        format_layout.addWidget(format_label)
        format_layout.addWidget(self.file_format_combo)

        # Run Button
        self.run_button = QPushButton("Run")
        self.run_button.setObjectName("runButton")
        self.run_button.clicked.connect(self.run_processing)

        # Adding layouts to the central layout
        central_layout.addLayout(brand_layout)
        central_layout.addLayout(input_layout)
        central_layout.addLayout(output_layout)
        central_layout.addLayout(size_layout) 
        central_layout.addLayout(bg_layout)
        central_layout.addLayout(padding_layout)
        central_layout.addLayout(format_layout) 
        central_layout.addWidget(self.run_button, alignment=Qt.AlignRight)

        # Set central widget layout
        self.setLayout(central_layout)

    def select_input_folder(self):
        """Open a dialog to select the input folder."""
        folder_path = QFileDialog.getExistingDirectory(self, "Select Input Folder")
        if folder_path:
            self.input_folder_path.setText(folder_path)

    def select_output_folder(self):
        """Open a dialog to select the output folder."""
        folder_path = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        if folder_path:
            self.output_folder_path.setText(folder_path)

    def run_processing(self): 
        """Initiate the image processing."""
        input_folder = self.input_folder_path.text()
        output_folder = self.output_folder_path.text()
        width = self.width_input.value()
        height = self.height_input.value() 
        background_color=self.bg_color_input.text()
        padding=self.padding_input.value()
        output_format=self.file_format_combo.currentText() 
        
        
        image_processor = ImageProcessing(
        input_folder=input_folder,
        output_folder=output_folder,
        width=width,
        height=height,
        background_color=background_color,  # Optional, e.g., "#FFFFFF"
        padding=padding,                    # Optional, default 0
        output_format=output_format,        # Optional, "original" as default
        output_size_range=None # Optional, e.g., (min_kb, max_kb)
    )

        # Run processing
        image_processor.run()

    def sync_size_units(self):
        """Synchronize size units between width, height, and the selected unit."""
        print("sync size units triggered",self.size_unit_combo.currentText())
        update_size_units(self.width_input, self.height_input, self.size_unit_combo.currentText())

    def sync_aspect_ratio(self):
        """Synchronize aspect ratio width and height inputs."""
        update_aspect_ratio(self.ratio_width_input, self.ratio_height_input, self.ratio_combo.currentText())
        