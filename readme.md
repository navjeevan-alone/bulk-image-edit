# 🌟 Magic Edits - Bulk Image Editor

Magic Edits is a versatile bulk image processing tool designed to simplify the process of resizing, formatting, and applying uniform edits to a folder of images. Built with PyQt5 for a sleek and user-friendly GUI, Magic Edits is ideal for photographers, designers, and anyone working with bulk image editing tasks.

## Motivation 
As a freelancer, I often lost hours resizing and editing product images for clients—adjusting dimensions, backgrounds, and formats for consistency. Frustrated by the repetitive, time-consuming process, I developed *Magic Edits* 🎨✨—a free, easy-to-use tool that does all the heavy lifting for me. Now, what once took hours is done in seconds ⏱️: over 200 images processed in just 15 seconds! *Magic Edits* has truly transformed my workflow, saving me valuable time for more creative work ❤️💼.

## 🎯 Use Case

Magic Edits helps automate repetitive image editing tasks, like resizing, adding padding, changing background colors, and adjusting file formats in bulk. With intuitive controls and a clear layout, users can efficiently apply uniform edits across an entire folder of images and save significant time on batch processing.

## 🗂️ File Structure

Here's a quick look at the project’s file organization:

```
Magic-Edits/
├── ui.py                # Main GUI window and user interactions
├── image_processing.py  # Core image processing logic and operations
├── logger.py            # Logger class for handling logs and console updates
├── utils.py             # Utility functions for loading styles, fonts, etc.
├── assets/              # Icons, fonts, and QSS stylesheets
│   ├── icon.ico         # Application icon
│   ├── dark_theme.qss   # Dark theme stylesheet
│   ├── Norican.ttf      # Norican font for app title
│   ├── Poppins.ttf      # Poppins font for other text
└── README.md            # Documentation and information about the project
```

## 🚀 Features

- **Batch Processing**: Process all images within a selected folder.
- **Size Adjustments**: Set width, height, padding, and background color.
- **Format Conversion**: Export to JPG, PNG, WebP, or maintain the original format.
- **Real-time Logs**: Monitor progress through console output and a built-in log viewer.
- **Output Management**: Choose output folder or have one created automatically within the input folder.
- **Clear Entries**: Easily reset entries for new tasks.
- **Open Output Folder**: Quick access to the output folder upon task completion.

## 🔍 Classes and Main Files

- **`AppUI`** (`ui.py`): Manages the main GUI and user interactions, including buttons, dropdowns, and text fields.
- **`ImageProcessing`** (`image_processing.py`): Handles all image processing tasks, including resizing, adding background color, applying padding, and exporting images. Runs in a loop for each image in the selected input folder.
- **`Logger`** (`logger.py`): Records log messages for each processing step, visible in both the console and the GUI's log view. (TODO :under implementation, currently saves to log file)
- **`utils.py`**: Provides helper functions, like loading the custom dark theme stylesheet and setting up fonts, to enhance the user experience.

## 🛠️ Setup and Installation
- TODO : Under development

## 🚧 Future Improvements

- **Additional Export Formats**: Support for more image formats like GIF, BMP, etc.
- **Custom Ratio Presets**: Add more customizable aspect ratio presets.
- **Image Quality Adjustment**: Fine-grained control over quality settings based on file size.
- **Preset Saving**: Allow users to save frequently used settings as presets.
- **Localization Support**: Add multi-language support for a global audience.

## 🤝 Contributing

We welcome contributions from the community! If you’d like to improve Magic Edits, please feel free to:

- 📥 **Fork the repository** and create a pull request with your changes.
- 🐛 **Report Issues**: Found a bug? Open an issue and help us improve.
- 🌟 **Request Features**: Have an idea? Let us know by opening a feature request!

Contributions are what make open-source projects great, so thank you for helping us make Magic Edits better! ✨