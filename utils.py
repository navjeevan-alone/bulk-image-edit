import sys
import os 
import re

def load_stylesheet(stylesheet_path):
    """Loads a stylesheet from the given path and converts relative asset URLs to absolute paths."""
    with open(stylesheet_path, "r") as stylesheet_file:
        stylesheet = stylesheet_file.read()
        # Replace all occurrences of 'url(./assets/...' with absolute paths
        stylesheet = re.sub(
            r'url\((\./assets/.*?)\)', 
            lambda match: f'url({resource_path(match.group(1))})',
            stylesheet
        )
    return stylesheet

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# utils.py

def update_size_units(width_input, height_input, unit):
    """Synchronize size units between width and height.
    
    Args:
        width_input (QSpinBox): The width input widget.
        height_input (QSpinBox): The height input widget.
        unit (str): The selected unit (e.g., 'px', 'mm', 'cm', 'inch').
    """
    # Logic to convert units based on the current unit
    if unit == "px":
        # Do nothing if already in pixels
        return
    elif unit == "inch":
        # Assuming 96 DPI for pixel conversion
        width_input.setValue(int(width_input.value() * 96))
        height_input.setValue(int(height_input.value() * 96))
    elif unit == "mm":
        # Convert mm to pixels (1 mm = 3.779527559 pixels)
        width_input.setValue(int(width_input.value() * 3.779527559))
        height_input.setValue(int(height_input.value() * 3.779527559))
    elif unit == "cm":
        # Convert cm to pixels (1 cm = 37.795275591 pixels)
        width_input.setValue(int(width_input.value() * 37.795275591))
        height_input.setValue(int(height_input.value() * 37.795275591))

def update_aspect_ratio(ratio_width_input, ratio_height_input, ratio_type):
    """Synchronize aspect ratio width and height inputs based on the selected ratio type.
    
    Args:
        ratio_width_input (QSpinBox): The width aspect ratio input widget.
        ratio_height_input (QSpinBox): The height aspect ratio input widget.
        ratio_type (str): The selected aspect ratio type.
    """
    if ratio_type == "Original":
        pass
    elif ratio_type == "1:1":
        ratio_width_input.setValue(1)
        ratio_height_input.setValue(1)
    elif ratio_type == "16:9":
        ratio_width_input.setValue(16)
        ratio_height_input.setValue(9)
    elif ratio_type == "4:3":
        ratio_width_input.setValue(4)
        ratio_height_input.setValue(3)

    # Automatically adjust width if height is changed
    height = ratio_height_input.value()
    width = ratio_width_input.value()
    if height != 0:
        # Calculate width based on the height
        ratio = width / height
        new_width = int(height * ratio)
        ratio_width_input.setValue(new_width)
    elif width != 0:
        # Calculate height based on the width
        ratio = height / width
        new_height = int(width * ratio)
        ratio_height_input.setValue(new_height)
