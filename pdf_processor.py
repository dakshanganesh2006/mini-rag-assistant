from pypdf import PdfReader

def extract_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
            
    # Clean up invalid surrogate characters that break text-database formatting
    cleaned_text = "".join(c for c in text if not (0xD800 <= ord(c) <= 0xDFFF))
    return cleaned_text
