#!/usr/bin/env python3

import os
from PIL import Image

# Path to the images directory
IMAGE_DIR = os.path.expanduser("~/supplier-data/images")


def process_images():
  for file_name in os.listdir(IMAGE_DIR):
    # Target only .tiff or .tif files
    if file_name.lower().endswith((".tiff", ".tif")):
      file_path = os.path.join(IMAGE_DIR, file_name)

      try:
        with Image.open(file_path) as img:
          # Convert RGBA 4-channel format to RGB 3-channel format
          img_rgb = img.convert("RGB")

          # Resize resolution from 3000x2000 to 600x400
          resized_img = img_rgb.resize((600, 400))

          # Build output filename with .jpeg extension
          base_name = os.path.splitext(file_name)[0]
          output_path = os.path.join(IMAGE_DIR, f"{base_name}.jpeg")

          # Save in JPEG format
          resized_img.save(output_path, "JPEG")
      except Exception as e:
        print(f"Error processing {file_name}: {e}")


if __name__ == "__main__":
  process_images()
  