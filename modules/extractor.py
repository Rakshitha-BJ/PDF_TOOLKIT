import pdfplumber, fitz, os
from pypdf import PdfReader
import pandas as pd
from PIL import Image

def extract_text(pdf_path):
    reader = PdfReader(pdf_path)
    return "\n\n".join(page.extract_text() or "" for page in reader.pages)

def extract_tables(pdf_path):
    tables = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            for table in page.extract_tables():
                tables.append(pd.DataFrame(table))
    return tables

def extract_images(pdf_path, output_dir="output/images"):
    os.makedirs(output_dir, exist_ok=True)
    pdf = fitz.open(pdf_path)
    for page_index in range(len(pdf)):
        images = pdf[page_index].get_images(full=True)
        for img_index, img in enumerate(images):
            xref = img[0]
            pix = fitz.Pixmap(pdf, xref)
            if pix.n > 4:
                pix = fitz.Pixmap(fitz.csRGB, pix)
            img_path = f"{output_dir}/page{page_index+1}_img{img_index+1}.png"
            pix.save(img_path)
    return output_dir

from pdf2image import convert_from_path

def convert_pdf_to_images(pdf_path, output_folder="output/previews"):
    import os
    os.makedirs(output_folder, exist_ok=True)
    images = convert_from_path(pdf_path)
    image_paths = []
    for i, img in enumerate(images):
        img_path = f"{output_folder}/page_{i+1}.png"
        img.save(img_path, "PNG")
        image_paths.append(img_path)
    return image_paths
