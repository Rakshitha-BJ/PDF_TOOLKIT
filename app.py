import streamlit as st
import os
from modules import extractor, manipulator, ai_features, creator, utils

st.set_page_config(layout="wide", page_title="📄 PDF Utility Tool")

# Dark mode toggle
dark_mode = st.sidebar.toggle("🌙 Enable Dark Mode")

# File uploader
st.sidebar.title("📁 Upload Your PDF")
uploaded_file = st.sidebar.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file:
    pdf_path = utils.save_uploaded_file(uploaded_file)
    st.success(f"Uploaded: {uploaded_file.name}")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📄 Extract", 
        "✂️ Manipulate", 
        "🚀 AI & OCR", 
        "🔐 Security & Bookmarks", 
        "📝 Create PDF"
    ])

    # -------------------------------------------
    with tab1:
        st.header("📄 Extract Content")

        if st.button("Extract Text"):
            text = extractor.extract_text(pdf_path)
            st.text_area("Extracted Text", text, height=300)

        if st.button("Extract Tables"):
            tables = extractor.extract_tables(pdf_path)
            for i, table in enumerate(tables):
                st.write(f"Table {i+1}")
                st.dataframe(table)

        if st.button("Extract Images"):
            image_dir = extractor.extract_images(pdf_path)
            for img in os.listdir(image_dir):
                st.image(os.path.join(image_dir, img), caption=img)

        st.subheader("📊 Preview Pages as Thumbnails")
        if st.button("Show Previews"):
            previews = extractor.convert_pdf_to_images(pdf_path)
            for img in previews:
                st.image(img, width=180)

        st.subheader("📑 View PDF Metadata")
        metadata = utils.get_pdf_metadata(pdf_path)
        st.json(metadata)

    # -------------------------------------------
    with tab2:
        st.header("✂️ Manipulate PDF")

        st.subheader("Split All Pages")
        if st.button("Split"):
            files = manipulator.split_pdf(pdf_path)
            st.success("Split complete! Check output folder.")

        st.subheader("Extract Selected Pages")
        selected = st.text_input("Enter page numbers (e.g., 0,2,4)")
        if st.button("Extract Selected Pages"):
            indices = [int(i.strip()) for i in selected.split(",") if i.strip().isdigit()]
            out = manipulator.extract_selected_pages(pdf_path, indices)
            st.download_button("Download", open(out, "rb"), "extracted_pages.pdf")

        st.subheader("Merge PDFs")
        merge_files = st.file_uploader("Upload PDFs", type="pdf", accept_multiple_files=True)
        if st.button("Merge PDFs"):
            files = [utils.save_uploaded_file(f) for f in merge_files]
            merged = manipulator.merge_pdfs(files)
            st.download_button("Download Merged PDF", open(merged, "rb"), "merged.pdf")

        st.subheader("Reorder Pages")
        order = st.text_input("Enter new order (e.g., 2,0,1)")
        if st.button("Reorder"):
            new_order = [int(i.strip()) for i in order.split(",")]
            out = manipulator.reorder_pages(pdf_path, new_order)
            st.download_button("Download Reordered PDF", open(out, "rb"), "reordered.pdf")

        st.subheader("Reverse Pages")
        if st.button("Reverse"):
            out = manipulator.reverse_pages(pdf_path)
            st.download_button("Download Reversed PDF", open(out, "rb"), "reversed.pdf")

        st.subheader("Delete Pages")
        to_delete = st.text_input("Pages to delete (e.g., 1,3)")
        if st.button("Delete Pages"):
            del_list = [int(i.strip()) for i in to_delete.split(",")]
            out = manipulator.delete_pages(pdf_path, del_list)
            st.download_button("Download Modified PDF", open(out, "rb"), "deleted_pages.pdf")

        st.subheader("Crop Pages")
        x0 = st.number_input("x0", 0)
        y0 = st.number_input("y0", 0)
        x1 = st.number_input("x1", 400)
        y1 = st.number_input("y1", 600)
        if st.button("Crop"):
            crop_box = {'x0': x0, 'y0': y0, 'x1': x1, 'y1': y1}
            out = manipulator.crop_pdf(pdf_path, crop_box)
            st.download_button("Download Cropped PDF", open(out, "rb"), "cropped.pdf")

    # -------------------------------------------
    with tab3:
        st.header("🚀 AI Tools")

        st.subheader("🧠 Summarize PDF")
        if st.button("Summarize"):
            text = extractor.extract_text(pdf_path)
            summary = ai_features.summarize_text(text)
            st.info(summary)

        st.subheader("📊 Keyword Heatmap")
        keyword = st.text_input("Keyword to Search")
        if st.button("Generate Heatmap"):
            heatmap = ai_features.keyword_heatmap(pdf_path, keyword)
            st.image(heatmap, caption="Keyword Frequency Heatmap")

        st.subheader("🧾 OCR for Scanned PDFs")
        if st.button("Run OCR"):
            ocr_text = ai_features.ocr_pdf(pdf_path)
            st.text_area("OCR Text", ocr_text, height=300)

        st.subheader("🎧 Text-to-Speech (TTS)")
        if st.button("Generate Audio"):
            text = extractor.extract_text(pdf_path)
            mp3 = ai_features.text_to_speech(text)
            st.audio(mp3)

        st.subheader("🌐 Translate PDF Content")
        if st.button("Translate"):
            text = extractor.extract_text(pdf_path)
            translated = ai_features.detect_and_translate(text)
            st.text_area("Translated Text", translated, height=300)

        st.subheader("📝 Simulated Annotations")
        note = st.text_input("Text to highlight")
        comment = st.text_input("Comment")
        page = st.number_input("Page Number", 0)
        if st.button("Add Annotation"):
            path = ai_features.export_annotation_json(note, comment, int(page))
            st.success(f"Annotation saved to {path}")

    # -------------------------------------------
    with tab4:
        st.header("🔐 PDF Security & Bookmarks")

        st.subheader("Encrypt PDF")
        user_pwd = st.text_input("Set User Password")
        if st.button("Encrypt"):
            out = utils.encrypt_pdf(pdf_path, user_pwd)
            st.download_button("Download Encrypted PDF", open(out, "rb"), "encrypted.pdf")

        st.subheader("📑 Auto-Generate Bookmarks")
        if st.button("Generate Bookmarks"):
            out = utils.auto_generate_bookmarks(pdf_path)
            st.download_button("Download Bookmarked PDF", open(out, "rb"), "bookmarked.pdf")

    # -------------------------------------------
    with tab5:
        st.header("📝 Create PDF")

        st.subheader("Create PDF from Text")
        content = st.text_area("Write your content")
        if st.button("Create Text PDF"):
            path = creator.create_pdf_fpdf(content)
            st.download_button("Download PDF", open(path, "rb"), "custom.pdf")

        st.subheader("Generate Certificate")
        name = st.text_input("Recipient Name")
        if st.button("Create Certificate"):
            cert_path = creator.create_certificate(name)
            st.download_button("Download Certificate", open(cert_path, "rb"), "certificate.pdf")

# If no file
else:
    st.warning("Upload a PDF to start using the tool.")
