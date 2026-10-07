#!/usr/bin/env python3

import os
import requests

# Base directory for descriptions
DESC_DIR = os.path.expanduser("~/supplier-data/descriptions")

# API endpoint (use localhost or http://127.0.0.1/fruits/)
URL = "http://localhost/fruits/"


def process_descriptions():
  for file_name in sorted(os.listdir(DESC_DIR)):
    if file_name.endswith(".txt"):
      file_path = os.path.join(DESC_DIR, file_name)

      with open(file_path, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file.readlines()]

      if len(lines) >= 3:
        name = lines[0]

        # Extract weight integer (e.g., "500 lbs" -> 500)
        weight_str = lines[1].replace("lbs", "").strip()
        weight = int(weight_str)

        description = lines[2]

        # Match fruit image file name (e.g., 001.txt -> 001.jpeg)
        base_name = os.path.splitext(file_name)[0]
        image_name = f"{base_name}.jpeg"

        # Build fruit dictionary
        fruit_data = {
            "name": name,
            "weight": weight,
            "description": description,
            "image_name": image_name,
        }

        # POST data to endpoint
        response = requests.post(URL, json=fruit_data)

        if response.status_code in (200, 201):
          print(f"Successfully uploaded: {name}")
        else:
          print(f"Failed to upload {name}: Status {response.status_code}")


if __name__ == "__main__":
  process_descriptions()
  