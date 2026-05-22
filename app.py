import streamlit as st

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
analyze_button = st.button("Analyze Paper")