#!/usr/bin/env python3

import os
from PIL import Image

src_dir = "./images"
target_dir = "/opt/icons/"

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

for filename in os.listdir(src_dir):
    src_file_path = os.path.join(src_dir, filename)

    if os.path.isfile(src_file_path) and not filename.startswith('.'):
        try:
            with Image.open(src_file_path) as img:
                processed_img = img.rotate(-90).resize((128, 128)).convert("RGB")

                # Append .jpeg extension to the filename
                save_path = os.path.join(target_dir, filename + ".jpeg")
                processed_img.save(save_path, "JPEG")
        except Exception as e:
            print(f"Skipping {filename}: {e}")
            