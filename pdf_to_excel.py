import fitz  # PyMuPDF
import matplotlib
import pandas as pd
import numpy as np
from pprint import pprint

def save_text_to_file(text, filename):
  """
  Saves the given text to a file.

  Args:
    text: The text to be saved.
    filename: The name of the file to save the text to.
  """

  try:
    with open(filename, 'w') as file:
      file.write(text)
    print(f"Text saved successfully to '{filename}'")

  except IOError as e:
    print(f"An error occurred while saving the file: {e}")

def pdf_to_text(pdf_path):
    # Open the PDF file
    document = fitz.open(pdf_path)
    text = ""

    # Iterate through each page
    for page_num in range(len(document)):
        # Get the page
        page = document.load_page(page_num)
        # Extract text from the page
        text += page.get_text()

    # Close the document
    document.close()

    return text

def get_tables(pdf_path):
   document = fitz.open(pdf_path)
   page = document[6]
   tabs = page.find_tables()  # detect the tables
   print(f"{len(tabs.tables)} found on {page}")

   if tabs.tables:  # at least one table found?
      pprint(tabs[0].extract())  # print content of first table
   return tabs
#    for i,tab in enumerate(tabs):  # iterate over all tables
#         for cell in tab.header.cells:
#             page.draw_rect(cell,color=fitz.pdfcolor["red"],width=0.3)
#         page.draw_rect(tab.bbox,color=fitz.pdfcolor["green"])
#         print(f"Table {i} column names: {tab.header.names}, external: {tab.header.external}")


# Example usage
pdf_path = 'C:/Users/admin/Desktop/Github/ebill-automation/BWP-January.pdf'  # Replace with your PDF file path
text_content = pdf_to_text(pdf_path)
save_text_to_file(text_content, "plaintext.txt")
print(get_tables(pdf_path))
