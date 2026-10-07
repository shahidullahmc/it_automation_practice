#!/usr/bin/env python3

import os
import requests

# URL of the upload endpoint
URL = "http://localhost/upload/"

# Path to processed images directory
IMAGE_DIR = os.path.expanduser("~/supplier-data/images")


def upload_images():
  for file_name in os.listdir(IMAGE_DIR):
    # Only upload .jpeg files
    if file_name.lower().endswith(".jpeg"):
      file_path = os.path.join(IMAGE_DIR, file_name)

      with open(file_path, "rb") as opened:
        response = requests.post(URL, files={"file": opened})

      # Check upload status
      if response.status_code == 201:
        print(f"Successfully uploaded: {file_name}")
      else:
        print(f"Failed to upload {file_name}: Status {response.status_code}")


if __name__ == "__main__":
  upload_images()
  