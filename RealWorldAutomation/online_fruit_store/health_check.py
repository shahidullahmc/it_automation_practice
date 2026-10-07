#!/usr/bin/env python3

import shutil
import psutil
import socket
import emails

def check_cpu_usage():
    """Returns True if CPU usage is over 80%."""
    usage = psutil.cpu_percent(1)
    return usage > 80

def check_disk_usage(disk):
    """Returns True if available disk space is lower than 20%."""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free < 20

def check_memory():
    """Returns True if available memory is less than 100MB."""
    available_memory = psutil.virtual_memory().available / (1024 * 1024)
    return available_memory < 100

def check_localhost():
    """Returns True if localhost cannot be resolved to 127.0.0.1."""
    try:
        ip = socket.gethostbyname("localhost")
        return ip != "127.0.0.1"
    except Exception:
        return True

def main():
    sender = "automation@example.com"
    recipient = "student@example.com"
    body = "Please check your system and resolve the issue as soon as possible."
    subject = None

    if check_cpu_usage():
        subject = "Error - CPU usage is over 80%"
    elif check_disk_usage("/"):
        subject = "Error - Available disk space is less than 20%"
    elif check_memory():
        subject = "Error - Available memory is less than 100MB"
    elif check_localhost():
        subject = "Error - localhost cannot be resolved to 127.0.0.1"

    if subject:
        message = emails.generate_error_report(sender, recipient, subject, body)
        emails.send_email(message)

if __name__ == "__main__":
    main()
    