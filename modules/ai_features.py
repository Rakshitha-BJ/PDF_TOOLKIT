import pytesseract, pyttsx3, os
from transformers import pipeline
from PIL import Image
from langdetect import detect
from deep_translator import GoogleTranslator
from PyPDF2 import PdfReader

def ocr_pdf(pdf_path):
    from pdf2image import convert_from_path
    pages = convert_from_path(pdf_path)
    text = ""
    for page in pages:
        text += pytesseract.image_to_string(page)
    return text

def summarize_text(text):
    summarizer = pipeline("summarization")
    return summarizer(text[:1000])[0]['summary_text']

def text_to_speech(text, filename="output/audio.mp3"):
    from gtts import gTTS
    tts = gTTS(text=text)
    tts.save(filename)
    return filename

def detect_and_translate(text, target='en'):
    lang = detect(text)
    if lang != target:
        return GoogleTranslator(source='auto', target=target).translate(text)
    return text
import matplotlib.pyplot as plt

def keyword_heatmap(pdf_path, keyword):
    reader = PdfReader(pdf_path)
    freqs = []
    for page in reader.pages:
        text = page.extract_text() or ""
        freqs.append(text.lower().count(keyword.lower()))
    
    # Generate bar chart
    fig, ax = plt.subplots()
    ax.bar(range(1, len(freqs)+1), freqs)
    ax.set_xlabel("Page")
    ax.set_ylabel("Frequency")
    ax.set_title(f"Keyword Frequency: '{keyword}'")
    heatmap_path = "output/keyword_heatmap.png"
    fig.savefig(heatmap_path)
    return heatmap_path
import json

def export_annotation_json(text, comment, page_num, output_path="output/annotations.json"):
    annotation = {
        "page": page_num,
        "highlight": text,
        "comment": comment
    }
    annotations = []
    if os.path.exists(output_path):
        with open(output_path, "r") as f:
            annotations = json.load(f)
    annotations.append(annotation)
    with open(output_path, "w") as f:
        json.dump(annotations, f, indent=4)
    return output_path
