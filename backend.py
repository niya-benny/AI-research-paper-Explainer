from pypdf import PdfReader


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