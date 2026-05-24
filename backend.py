from pypdf import PdfReader
import langchain.text_splitter
from langchain.text_splitter import RecursiveCharacterTextSplitter

def extract_text_from_pdf(pdf_path):
    """
    Extracts all text from a PDF file.

    Args:
        pdf_path (str): Path to uploaded PDF

    Returns:
        str: Complete extracted text
    """

    reader = PdfReader(pdf_path)

    full_text = ""

    # Loop through all pages
    for page in reader.pages:
        text = page.extract_text()

        # Avoid NoneType errors
        if text:
            full_text += text + "\n"

    return full_text
def split_text_into_chunks(text):
    """
    Splits large text into smaller overlapping chunks.

    Args:
        text (str): Extracted PDF text

    Returns:
        list: List of text chunks
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,      # Max characters per chunk
        chunk_overlap=200     # Overlap between chunks
    )

    chunks = text_splitter.split_text(text)

    return chunks