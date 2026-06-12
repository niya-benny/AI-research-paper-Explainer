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


METHODOLOGY_PROMPT = PromptTemplate(
    input_variables=["paper_text"],
    template="""
You are a research assistant.

Read the research paper content below and explain the methodology in simple language.

Focus on:
1. Dataset used
2. Models used
3. Research process
4. Tools or technologies used
5. How experiments were conducted

Paper Content:
{paper_text}

Explain in easy-to-understand bullet points.
"""
)

def explain_methodology(llm, text):
    """
    Explains the methodology of the research paper.
    """

    parser = StrOutputParser()

    chain = METHODOLOGY_PROMPT | llm | parser

    result = chain.invoke({
        "paper_text": text
    })

    return result

KEY_POINTS_PROMPT = PromptTemplate(
    input_variables=["paper_text"],
    template="""
You are an expert research analyst.

Read the research paper content below.

Generate:

1. Top 5 Key Contributions
2. Important Findings
3. Limitations of the Study

Paper Content:
{paper_text}

Format the answer using bullet points.
"""
)

def generate_key_points(llm, text):
    """
    Extracts key contributions and findings.
    """

    parser = StrOutputParser()

    chain = KEY_POINTS_PROMPT | llm | parser

    result = chain.invoke({
        "paper_text": text
    })

    return result

VIVA_PROMPT = PromptTemplate(
    input_variables=["paper_text"],
    template="""
You are a university professor.

Read the research paper content below.

Generate:

1. 10 Viva Questions
2. Short Answers for each question

Paper Content:
{paper_text}

Format:

Q1:
A1:

Q2:
A2:

...
"""
)

def generate_viva_questions(llm, text):
    """
    Generates viva questions from research paper.
    """

    parser = StrOutputParser()

    chain = VIVA_PROMPT | llm | parser

    result = chain.invoke({
        "paper_text": text
    })

    return result