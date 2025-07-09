from pypdf import PdfReader, PdfWriter

def split_pdf(path):
    reader = PdfReader(path)
    output_paths = []
    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)
        out_path = f"output/page_{i+1}.pdf"
        with open(out_path, "wb") as f:
            writer.write(f)
        output_paths.append(out_path)
    return output_paths

def merge_pdfs(pdf_list, output="output/merged.pdf"):
    writer = PdfWriter()
    for pdf in pdf_list:
        reader = PdfReader(pdf)
        for page in reader.pages:
            writer.add_page(page)
    with open(output, "wb") as f:
        writer.write(f)
    return output

def rotate_pdf(pdf_path, angle=90):
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    for page in reader.pages:
        page.rotate(angle)
        writer.add_page(page)
    output_path = "output/rotated.pdf"
    with open(output_path, "wb") as f:
        writer.write(f)
    return output_path

def reorder_pages(pdf_path, new_order):
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    for i in new_order:
        writer.add_page(reader.pages[i])
    out_path = "output/reordered.pdf"
    with open(out_path, "wb") as f:
        writer.write(f)
    return out_path

def reverse_pages(pdf_path):
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    for page in reversed(reader.pages):
        writer.add_page(page)
    out_path = "output/reversed.pdf"
    with open(out_path, "wb") as f:
        writer.write(f)
    return out_path

def delete_pages(pdf_path, delete_indices):
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    for i, page in enumerate(reader.pages):
        if i not in delete_indices:
            writer.add_page(page)
    out_path = "output/deleted_pages.pdf"
    with open(out_path, "wb") as f:
        writer.write(f)
    return out_path

def extract_selected_pages(pdf_path, selected_pages):
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    for i in selected_pages:
        writer.add_page(reader.pages[i])
    output_path = "output/extracted_pages.pdf"
    with open(output_path, "wb") as f:
        writer.write(f)
    return output_path

def crop_pdf(pdf_path, crop_box):
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    for page in reader.pages:
        page.mediabox.lower_left = (crop_box['x0'], crop_box['y0'])
        page.mediabox.upper_right = (crop_box['x1'], crop_box['y1'])
        writer.add_page(page)
    output_path = "output/cropped.pdf"
    with open(output_path, "wb") as f:
        writer.write(f)
    return output_path
