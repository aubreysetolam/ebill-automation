import fitz  # PyMuPDF

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

# Example usage
pdf_path = 'C:/Users/admin/Desktop/Github/ebill-automation/BWP-January.pdf'  # Replace with your PDF file path
text_content = pdf_to_text(pdf_path)
save_text_to_file(text_content, "plaintext.txt")
