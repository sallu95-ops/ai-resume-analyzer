import streamlit as st
import PyPDF2

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and analyze your skills.")

st.divider()

# Resume Upload
st.subheader("📤 Upload Your Resume")

uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    resume_text = ""

    for page in pdf_reader.pages:
        text = page.extract_text()
        if text:
            resume_text += text

    st.success("✅ Resume uploaded successfully!")

    st.subheader("📄 Resume Preview")

    st.text_area(
        "Extracted Resume Text",
        resume_text,
        height=300
    )

else:
    st.info("Please upload your PDF resume to start analysis.")
