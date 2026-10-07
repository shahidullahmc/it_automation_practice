#!/usr/bin/env python3

import os
import requests

# Directory containing feedback files
feedback_dir = "/data/feedback"

# IP address of the web server (Replace with actual IP, e.g., 35.192.10.1 or localhost)
corpweb_ip = "<corpweb-external-IP>" 
url = f"http://{corpweb_ip}/feedback"

# List all files in the feedback directory
files = os.listdir(feedback_dir)

for file in files:
    # Process only .txt files (ignoring hidden files)
    if file.endswith(".txt"):
        file_path = os.path.join(feedback_dir, file)
        
        with open(file_path, "r") as f:
            # Read all lines and strip trailing newlines
            lines = [line.strip() for line in f.readlines()]
            
            # Ensure the file has all 4 expected fields
            if len(lines) >= 4:
                feedback_dict = {
                    "title": lines[0],
                    "name": lines[1],
                    "date": lines[2],
                    "feedback": lines[3]
                }
                
                # Send the POST request to the Django API
                response = requests.post(url, json=feedback_dict)
                
                # Print status code and response text for verification
                print(f"File {file} - Status Code: {response.status_code}")
                if response.status_code != 201:
                    print(f"Error posting {file}: {response.text}")
                    