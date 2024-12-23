import fitz  # PyMuPDF

def find_pages_with_string(pdf_path, search_string, count):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    pages_with_string = []

    # Iterate through each page
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text = page.get_text()
        # Count the occurrences of the search string in the text of the page
        count += text.count(search_string)
        # Check if the search string is in the text of the page
        if search_string in text:
            pages_with_string.append(page_num + 1)  # Page numbers are 1-based

    return pages_with_string, count

def get_tables(pdf_path,pages):
   document = fitz.open(pdf_path)
   page_num = 0

   for page_num in pages:
      page = document.load_page(page_num)
      tabs = page.find_tables()
      print(f"{len(tabs.tables)} found on {page}")
   return tabs

if __name__ == "__main__":
    pdf_path = 'C:/Users/admin/Desktop/Github/ebill-automation/BWP-January.pdf'
    search_string = 'Electric  (kWh)'
    count = 0
    pages, count = find_pages_with_string(pdf_path, search_string,count)
    print(f"Pages containing '{search_string}': {pages}")
    print(f"Count: '{count}' Total Pages: {len(pages)}")
    tables = get_tables(pdf_path,pages)