"""
Badal Prasad Singh

same example to check how the code works:
terminal : python readpdf.py Datasets\Resume1.pdf
"""

import fitz
import sys

def extract_text_from_pdf(path):
    try:
        document = fitz.open(path)
        text = ""

        for page_num in range(len(document)):
            page = document.load_page(page_num)
            text += page.get_text()

        return text
    except Exception as e:
        return f"Error {e}"

def main():
    if len(sys.argv)!=2:
        print("Usage: python readpdf.py Datasets\Resume1.pdf")
        return

    pdf_path = sys.argv[1]
    text = extract_text_from_pdf("Datasets\Resume1.pdf")
    print(text)

if __name__ == "__main__":
    main()