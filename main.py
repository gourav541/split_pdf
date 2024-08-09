import fitz
from datetime import datetime
import os

def split_pdf_pages(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            file_path = os.path.join(input_folder, filename)
            fileName = os.path.splitext(filename)[0]
            print(fileName)
            pdf_document = fitz.open(file_path)
            for page_num in range(pdf_document.page_count):
                page = pdf_document[page_num]
                new_pdf_document = fitz.open()
                new_pdf_document.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)
               
                output_pdf_path = f"{output_folder}/{fileName}_{page_num + 1}.pdf"
                new_pdf_document.save(output_pdf_path)
                new_pdf_document.close()
            pdf_document.close()

if __name__ == "__main__":
    input_pdf_path =r"input"# Replace with your input PDF path
    output_folder =r"output"  # Replace with the folder where you want to save the output PDFs
    
    try:
        split_pdf_pages(input_pdf_path, output_folder)
        print("PDF split successfully.")
    except Exception as e:
        print(f"Error: {e}")