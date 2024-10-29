import os
from PIL import Image

def process_images(input_folder, output_folder):
    """
    Process all images in the input folder, resize them to fit within 1080x1080,
    and save them to the output folder with a white background and at least
    20 pixels of padding from all sides.
    
    Args:
        input_folder (str): Path to the input folder containing images.
        output_folder (str): Path to the output folder for saving processed images.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            image_path = os.path.join(input_folder, filename)
            try:
                with Image.open(image_path) as img:
                    # Convert image to RGB if necessary
                    img = img.convert('RGB') if img.mode in ('RGBA', 'LA') else img.convert('RGB')
                    
                    # Resize image while maintaining aspect ratio
                    img.thumbnail((1080 - 40, 1080 - 40), Image.LANCZOS)  # Subtract padding
                    
                    # Create a new white background image with padding
                    new_image = Image.new('RGB', (1080, 1080), (255, 255, 255))
                    
                    # Calculate position to center the image with 20px padding
                    x = (new_image.width - img.width) // 2
                    y = (new_image.height - img.height) // 2
                    
                    # Paste image onto the new background
                    new_image.paste(img, (x, y))

                    # Save the new image in the same format as the original
                    output_path = os.path.join(output_folder, filename)
                    new_image.save(output_path, format='JPEG' if img.format == 'JPEG' else img.format)
                    print(f"Processed and saved: {output_path}")

            except Exception as e:
                print(f"Error processing {image_path}: {e}")

def change_file_format(input_file_path, output_format):
    """
    Change the file format of an image to the specified format.
    
    Args:
        input_file_path (str): Path to the input image file.
        output_format (str): Desired output format (jpg, png, jpeg, webp).
    
    Returns:
        str: Path to the saved file in the new format.
    """
    output_file_path = f"{os.path.splitext(input_file_path)[0]}.{output_format.lower()}"
    
    try:
        with Image.open(input_file_path) as img:
            img.save(output_file_path, format=output_format.upper())
            print(f"Converted {input_file_path} to {output_file_path}")
            return output_file_path
    except Exception as e:
        print(f"Error converting {input_file_path}: {e}")
        return None

def adjust_file_size(file_path, min_size_kb, max_size_kb, min_quality):
    """
    Adjust the file size of an image to be within the specified range.
    
    Args:
        file_path (str): Path to the input image file.
        min_size_kb (int): Minimum file size in KB.
        max_size_kb (int): Maximum file size in KB.
        min_quality (int): Minimum quality percentage (1-100) for JPEG.
    
    Returns:
        str: Path to the adjusted file.
    """
    try:
        quality = 100
        while True:
            with Image.open(file_path) as img:
                if img.format == 'JPEG':
                    img.save(file_path, 'JPEG', quality=quality)
                else:
                    img.save(file_path)  # No need to compress non-JPEG formats

            current_size_kb = os.path.getsize(file_path) / 1024  # Size in KB
            
            if current_size_kb <= max_size_kb and current_size_kb >= min_size_kb:
                print(f"Adjusted {file_path} to size {current_size_kb:.2f} KB.")
                return file_path
            
            if img.format == 'JPEG' and quality > min_quality:
                quality -= 5  # Reduce quality to decrease file size
            else:
                break  # Stop if not a JPEG or quality is at minimum
            
    except Exception as e:
        print(f"Error adjusting file size for {file_path}: {e}")
        return None
