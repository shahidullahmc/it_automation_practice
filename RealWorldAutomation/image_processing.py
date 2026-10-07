pip3 install pillow
from PIL import Image

im = Image.open("example.jpg")
new_im = im.resize((640,480))
new_im.save("example_resized.jpg")

im = Image.open("example.jpg")
new_im = im.rotate(90)
new_im.save("example_rotated.jpg")

im = Image.open("example.jpg")
im.rotate(180).resize((640,480)).save("flipped_and_resized.jpg")


#!/usr/bin/env python3

import os
from PIL import Image

# Path to the source images and target destination
src_dir = "./images"
target_dir = "/opt/icons/"

# # Create target directory if it doesn't exist
# if not os.path.exists(target_dir):
#     os.makedirs(target_dir)

# Iterate through every file in the source folder
for filename in os.listdir(src_dir):
    src_file_path = os.path.join(src_dir, filename)

    # Process only files (skip directories or hidden files like .DS_Store)
    if os.path.isfile(src_file_path) and not filename.startswith('.'):
        try:
            with Image.open(src_file_path) as img:
                # PIL rotates counter-clockwise by default, so -90 (or 270) rotates 90° clockwise
                # Convert to RGB to safely save as JPEG
                processed_img = img.rotate(-90).resize((128, 128)).convert("RGB")

                # Define output path and save as JPEG
                save_path = os.path.join(target_dir, filename + ".jpeg")
                processed_img.save(save_path, "JPEG")
        except Exception as e:
            print(f"Skipping {filename}: {e}")

# chmod +x updated_icons.py
# ./updated_icons.py
