from pypdf import PdfReader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from dotenv import load_dotenv
import os

load_dotenv()

from langchain_openai import ChatOpenAI

from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

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

def build_llm():
    print("Loading phi3:mini")
    
    llm = Ollama(
        model="phi3:mini",
        temperature=0.3
    )

    return llm

SUMMARY_PROMPT = PromptTemplate(
    input_variables=["paper_text"],
    template="""
    You are an AI research assistant.

    Read the following research paper content and generate:

    1. A simple summary
    2. Main objective of the paper
    3. Important findings

    Research Paper:
    {paper_text}
    """
)

def generate_summary(llm, text):
    """
    Generates AI summary from paper text.
    """

    parser = StrOutputParser()

    # Modern LangChain Expression Language (LCEL)
    chain = SUMMARY_PROMPT | llm | parser

    result = chain.invoke({
        "paper_text": text
    })

    return result