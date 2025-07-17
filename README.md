download poppler
https://github.com/oschwartz10612/poppler-windows/releases/

# 📄 PDF Utility Tool – Streamlit App

A **powerful, user-friendly PDF Utility Tool** built using Python and Streamlit. Supports advanced PDF manipulation, AI-enhanced summarization, OCR, TTS, translation, and much more — all from a modern web interface.

---


## 🚀 Features

### 📄 PDF Reading & Extraction
- Extract plain text from any or all pages
- Extract tables and export to CSV/Excel
- Extract and download images
- View PDF metadata (title, author, creation date, etc.)
- Convert PDF pages to image previews (PNG thumbnails)

### ✂️ Page-Level Manipulations
- Extract selected pages into a new PDF
- Split all pages into individual PDFs
- Merge multiple PDFs
- Reorder, reverse, or delete pages
- Rotate or crop pages

### 🔐 PDF Security & Permissions
- Encrypt PDFs with user-defined passwords
- Apply view-only or restrict printing/copying
- Auto-generate clickable bookmarks from heading structure

### 📝 PDF Creation
- Create PDFs with custom text, headers, and uploaded images
- Predefined themes: Resume, Certificate, Invoice

### 🧠 AI & Advanced Tools
- Summarize PDF text using NLP (Transformers)
- Text-to-Speech: Convert text to MP3
- Keyword search + heatmap visualization
- Real-time simulated annotations
- Translate PDF content to other languages
- Auto-detect scanned pages for OCR
- Multilingual support using deep-translator

### 🌟 UI/UX Features
- Streamlit Web UI with drag & drop file support
- Dark mode toggle
- Auto-save to `/output/` folder
- Thumbnail preview of each page

---

## 🛠️ Installation

### 📦 Step 1: Clone the Repo

```bash
git clone https://github.com/your-username/pdf-utility-tool.git
cd pdf-utility-tool

 Step 2: Create Virtual Environment
python -m venv venv
venv\Scripts\activate    # On Windows
# OR
source venv/bin/activate  # On macOS/Linux


 Step 3: Install Python Dependencies
 pip install -r requirements.txt


⚠️ Additional System Dependencies
🧾 Install Poppler (for PDF to Image conversion)
Windows:

Download from: https://github.com/oschwartz10612/poppler-windows/releases

Extract and add C:\poppler\bin to your System PATH.
nstall Tesseract OCR (for scanned PDFs)
Windows:

Download from: https://github.com/UB-Mannheim/tesseract/wiki

Add the installation path (e.g., C:\Program Files\Tesseract-OCR) to your System PATH.



Running the App

streamlit run app.py
Then open http://localhost:8501 in your browser.

 AI Model Info
Summarization: Uses HuggingFace Transformers (default: t5-small)

TTS: Supports both pyttsx3 (offline) and gTTS (online)

Translation: Powered by deep-translator (Google Translate API)

OCR: Performed using pytesseract

Heatmap: Generated via matplotlib and keyword frequency


 Project Structure
 pdf_utility_tool/
│
├── app.py
├── requirements.txt
├── README.md
│
├── modules/
│   ├── extractor.py
│   ├── manipulator.py
│   ├── ai_features.py
│   ├── creator.py
│   └── utils.py
│
├── uploaded/
├── output/
│   ├── images/
│   ├── previews/
│
├── assets/
│   └── themes/
├── history/
└── .gitignore


 Future Enhancements
Full annotation editor inside the PDF

Download reports as PDF

SQLite-based operation logs

Login system with usage history

