#!/usr/bin/env python3

from datetime import date
import os
import emails
import reports

DESC_DIR = os.path.expanduser("~/supplier-data/descriptions")


def process_fruit_data():
  """Parses description files and formats name and weight with line breaks."""
  summary_lines = []

  for file_name in sorted(os.listdir(DESC_DIR)):
    if file_name.endswith(".txt"):
      file_path = os.path.join(DESC_DIR, file_name)

      with open(file_path, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file.readlines()]

      if len(lines) >= 2:
        name = lines[0]
        weight = lines[1]
        summary_lines.append(f"name: {name}<br/>weight: {weight}<br/><br/>")

  return "".join(summary_lines)


def main():
  # Current date string
  today = date.today().strftime("%B %d, %Y")
  title = f"Processed Update on {today}"

  # Formatted paragraph content
  paragraph = process_fruit_data()

  # Output path for generated PDF
  attachment = "/tmp/processed.pdf"

  # Generate PDF report
  reports.generate_report(attachment, title, paragraph)

  # Email parameters required by the lab
  sender = "automation@example.com"
  receiver = "student@example.com"
  subject = "Upload Completed - Online Fruit Store"
  body = (
      "All fruits are uploaded to our website successfully. A detailed list is"
      " attached to this email."
  )

  # Generate email with PDF attachment and send it
  message = emails.generate_email(sender, receiver, subject, body, attachment)
  emails.send_email(message)


if __name__ == "__main__":
  main()
  