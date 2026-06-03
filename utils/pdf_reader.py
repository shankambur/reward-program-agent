from pypdf import PdfReader


def extract_pdf_pages(pdf_file):
    print("**reading pdf:", pdf_file.name)
    reader = PdfReader(pdf_file)

    pages = []
    for page_number, page in enumerate(reader.pages, start=1):
        print("reading pageNumber=",page_number)
        page_text = page.extract_text()
        
        if page_text:
            print("reading text from page")
            pages.append(
                {
                    "page_number": page_number,
                    "text": page_text
                }
            )
        
    return pages, len(reader.pages)