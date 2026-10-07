#!/usr/bin/env python3

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


def generate_report(filename, title, paragraph):
  """Generates a PDF report with a given title and paragraph content."""
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)

  report_title = Paragraph(title, styles["Heading1"])
  report_info = Paragraph(paragraph, styles["Normal"])
  empty_line = Spacer(1, 20)

  # Build document flow
  report.build([report_title, empty_line, report_info])
  