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
                
                try:
                    # Send POST request with a 5-second timeout
                    response = requests.post(url, json=feedback_dict, timeout=5)
                    
                    # Triggers HTTPError for 4xx or 5xx status codes
                    response.raise_for_status()
                    
                    # Verify target 201 Created status code
                    if response.status_code == 201:
                        print(f"Successfully posted {file} (Status Code: 201)")
                    else:
                        print(f"Warning: Got status code {response.status_code} for {file}")
                        
                except requests.exceptions.RequestException as e:
                    print(f"Failed to post {file} due to an error: {e}")
                    # Re-raise to immediately halt script execution on failure
                    raise