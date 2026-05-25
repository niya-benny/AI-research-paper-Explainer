import streamlit as st
from backend import extract_text_from_pdf
from backend import split_text_into_chunks
from backend import build_llm
from backend import generate_summary
# Page config
st.set_page_config(
    page_title="AI Research Paper Explainer",
    page_icon="📄"
)

st.title("📄 AI Research Paper Explainer")

st.write(
    "Upload a research paper PDF and let AI explain it simply."
)

# File uploader
uploaded_file = st.file_uploader(
    "Upload Research Paper PDF",
    type="pdf"
)

# Analyze button
# analyze_button = st.button("Analyze Paper")
# Analyze button
if st.button("Analyze Paper"):

    if uploaded_file is None:
        st.warning("Please upload a PDF first.")

    else:
        # Save uploaded PDF temporarily
        pdf_path = f"uploaded_papers/{uploaded_file.name}"

        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success("PDF uploaded successfully!")

        # Extract text
        extracted_text = extract_text_from_pdf(pdf_path)
        # Split text into chunks
        chunks = split_text_into_chunks(extracted_text)

        # Show extraction stats
        st.subheader("📚 Extracted Text Preview")

        st.write(extracted_text[:3000])

        # st.info(f"Total characters extracted: {len(extracted_text)}")
        st.info(f"Total characters extracted: {len(extracted_text)}")

        st.subheader("✂️ Chunk Information")

        st.write(f"Total chunks created: {len(chunks)}")

        # Show first chunk
        st.write("First chunk preview:")

        st.write(chunks[0])

        # Combine first few chunks
        paper_content = " ".join(chunks[:3])

        # Build AI model
        llm = build_llm()

        with st.spinner("Generating AI Summary..."):

            summary = generate_summary(llm, paper_content)

        st.subheader("🧠 AI Research Summary")

        st.write(summary)