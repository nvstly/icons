import os
from PIL import Image

# Path to the forex_icons directory
directory = 'forex_icons/'

# Check if directory exists
if not os.path.exists(directory):
    print(f"Directory {directory} does not exist.")
else:
    # Loop through each file in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Check if the file is an image (you can add other formats like .png or .bmp as needed)
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):

            try:
                # Open the image to get its dimensions
                with Image.open(file_path) as img:
                    width, height = img.size

                    # Check if dimensions are not 500x500
                    if width != 350 or height != 350:
                        print(f"{filename} is {width}x{height} (not 350x350).")

            except Exception as e:
                print(f"Could not open {filename}: {e}")
