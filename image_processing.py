# image_processing.py

import os
import logging
from PIL import Image

class ImageProcessing:
    def __init__(self, input_folder, output_folder, width, height, 
                 background_color="#FFFFFF", padding=0, 
                 output_format="original", output_size_range=None):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.width = width
        self.height = height
        self.background_color = background_color
        self.padding = padding
        self.output_format = output_format.lower()
        self.output_size_range = output_size_range  # Expecting tuple or list [min_kb, max_kb]
        self.logger = self.setup_logger()

    @staticmethod
    def setup_logger():
        """Set up a logger for tracking the image processing steps."""
        logger = logging.getLogger("ImageProcessing")
        logger.setLevel(logging.DEBUG)
        if not logger.handlers:
            handler = logging.FileHandler("image_processing.log")
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        return logger

    def run(self):
        """Process each image in the input folder according to the set parameters."""
        self.logger.info("Starting image processing.")
        for filename in os.listdir(self.input_folder):
            file_path = os.path.join(self.input_folder, filename)
            if not self.is_image_file(filename):
                self.logger.debug(f"Skipping non-image file: {filename}")
                continue
            try:
                self.process_image(file_path, filename)
            except Exception as e:
                self.logger.error(f"Failed to process image {filename}: {e}")
        
        self.logger.info("Image processing completed.")

    @staticmethod
    def is_image_file(filename):
        """Check if a file is an image based on extension."""
        valid_extensions = (".png", ".jpg", ".jpeg", ".webp")
        return filename.lower().endswith(valid_extensions)

    def process_image(self, file_path, filename):
        """Process a single image by resizing, adding padding, and exporting."""
        self.logger.debug(f"Processing image: {filename}")
        with Image.open(file_path) as img:
            # Create a new image with the specified background color and dimensions
            background = Image.new("RGB", (self.width, self.height), self.background_color)
            self.logger.debug(f"Created background image with color {self.background_color} and dimensions {self.width}x{self.height}")

            # Resize original image with padding adjustment
            resized_img = self.resize_image_with_padding(img)

            # Paste resized image onto background
            x_offset = (self.width - resized_img.width) // 2
            y_offset = (self.height - resized_img.height) // 2
            background.paste(resized_img, (x_offset, y_offset))
            self.logger.debug(f"Pasted image onto background at offset ({x_offset}, {y_offset})")

            # Save image to output folder
            output_path = os.path.join(self.output_folder, self.get_output_filename(filename))
            self.save_image(background, output_path)

    def resize_image_with_padding(self, img):
        """Resize image based on padding and original dimensions while keeping the aspect ratio."""
        aspect_ratio = img.width / img.height
        if aspect_ratio >= 1:
            target_width = self.width - 2 * self.padding
            target_height = int(target_width / aspect_ratio)
        else:
            target_height = self.height - 2 * self.padding
            target_width = int(target_height * aspect_ratio)

        resized_img = img.resize((target_width, target_height), Image.LANCZOS)
        self.logger.debug(f"Resized image with padding. New dimensions: {target_width}x{target_height}")
        return resized_img

    def get_output_filename(self, filename):
        """Generate the output filename with the appropriate format."""
        base, ext = os.path.splitext(filename)
        new_ext = f".{self.output_format}" if self.output_format != "original" else ext
        return f"{base}{new_ext}"

    def save_image(self, img, output_path):
        """Save the image in the specified output format and quality if size range is given."""
        save_params = {"format": self.output_format.upper() if self.output_format != "original" else img.format}
        if self.output_size_range:
            quality = self.find_optimal_quality(img)
            save_params["quality"] = quality

        img.save(output_path, **save_params)
        self.logger.debug(f"Image saved to {output_path} with format {save_params['format']} and quality {save_params.get('quality', 'default')}")

    def find_optimal_quality(self, img):
        """Determine the optimal quality level to match the desired file size range."""
        min_size_kb, max_size_kb = self.output_size_range
        lower_quality, upper_quality = 10, 95
        quality = upper_quality  # Start with high quality

        while lower_quality <= upper_quality:
            temp_path = "temp_image.jpg"
            img.save(temp_path, quality=quality)
            size_kb = os.path.getsize(temp_path) / 1024  # Convert to KB

            if min_size_kb <= size_kb <= max_size_kb:
                os.remove(temp_path)
                self.logger.debug(f"Optimal quality found: {quality} to achieve size {size_kb}KB within range")
                return quality
            elif size_kb > max_size_kb:
                upper_quality = quality - 1
            else:
                lower_quality = quality + 1

            quality = (lower_quality + upper_quality) // 2

        os.remove(temp_path)
        self.logger.warning(f"Could not find optimal quality within range. Using default max quality: {quality}")
        return quality  # Return best attempt