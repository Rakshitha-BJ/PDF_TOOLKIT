from fpdf import FPDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

def create_pdf_fpdf(content, filename="output/custom.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in content.split("\n"):
        pdf.cell(200, 10, txt=line, ln=1)
    pdf.output(filename)
    return filename

def create_certificate(name, filename="output/certificate.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(300, 500, f"Certificate of Completion")
    c.setFont("Helvetica", 18)
    c.drawCentredString(300, 450, f"Presented to {name}")
    c.save()
    return filename
