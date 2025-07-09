import os

def save_uploaded_file(uploaded_file):
    os.makedirs("uploaded", exist_ok=True)
    path = f"uploaded/{uploaded_file.name}"
    with open(path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return path

def get_pdf_metadata(pdf_path):
    from pypdf import PdfReader
    reader = PdfReader(pdf_path)
    return reader.metadata

from pypdf import PdfReader, PdfWriter

def encrypt_pdf(input_path, user_pwd, owner_pwd="admin", output_path="output/encrypted.pdf"):
    reader = PdfReader(input_path)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.encrypt(user_pwd, owner_pwd, use_128bit=True)
    with open(output_path, "wb") as f:
        writer.write(f)
    return output_path

def auto_generate_bookmarks(pdf_path):
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    for i, page in enumerate(reader.pages):
        writer.add_page(page)
        writer.add_outline_item(title=f"Page {i+1}", page_number=i)
    output_path = "output/bookmarked.pdf"
    with open(output_path, "wb") as f:
        writer.write(f)
    return output_path
