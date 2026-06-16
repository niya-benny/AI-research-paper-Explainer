# 📄 AI Research Paper Explainer

Transform complex research papers into simple, understandable insights using AI.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-red)
![LangChain](https://img.shields.io/badge/LangChain-LLM-green)
![Ollama](https://img.shields.io/badge/Ollama-Phi3-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🚀 Overview

Reading research papers can be time-consuming and challenging, especially when dealing with complex methodologies, technical jargon, and dense academic writing.

**AI Research Paper Explainer** is an intelligent NLP-powered application that automatically analyzes research papers and generates:

✅ Simple AI-generated summaries

✅ Methodology explanations in plain language

✅ Key contributions and findings

✅ Research limitations

✅ Viva questions and answers for presentations and examinations

The system helps students, researchers, and educators quickly understand academic papers without reading every page manually.

---

## ✨ Features

### 📚 PDF Research Paper Analysis

Upload any research paper in PDF format and extract its textual content automatically.

### 🧠 AI-Powered Summary Generation

Generate concise summaries that explain:

* Research objective
* Problem statement
* Important findings
* Overall contribution

### ⚙️ Methodology Simplification

Understand complex research methodologies through:

* Dataset information
* Models used
* Experimental workflow
* Technologies and tools
* Research process

### ⭐ Key Contributions Extraction

Automatically identify:

* Top contributions
* Major findings
* Research limitations

### 🎓 Viva Question Generator

Generate university-style viva questions and answers to help prepare for:

* Project reviews
* Seminars
* Research presentations
* Academic examinations

---

## 🏗️ System Architecture

```text
Research Paper PDF
        │
        ▼
PDF Text Extraction (PyPDF)
        │
        ▼
Text Chunking
(Recursive Character Splitter)
        │
        ▼
Local LLM (Phi-3 Mini via Ollama)
        │
 ┌──────┼─────────┬─────────┐
 ▼      ▼         ▼         ▼
Summary Methodology Key Points Viva Q&A
```

---

## 🛠️ Technologies Used

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python     | Backend Development       |
| Streamlit  | User Interface            |
| LangChain  | LLM Orchestration         |
| Ollama     | Local Model Serving       |
| Phi-3 Mini | Large Language Model      |
| PyPDF      | PDF Text Extraction       |
| dotenv     | Environment Configuration |

---

## 📂 Project Structure

```bash
AI-Research-Paper-Explainer/
│
├── app.py
├── backend.py
├── uploaded_papers/
├── .env
├── requirements.txt
└── README.md
```

---

## ⚡ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AI-Research-Paper-Explainer.git

cd AI-Research-Paper-Explainer
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Install Ollama & Phi-3

Install Ollama:

```bash
https://ollama.com/download
```

Pull Phi-3 Mini:

```bash
ollama pull phi3:mini
```

Verify:

```bash
ollama list
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 📸 Application Workflow

### Step 1

Upload a research paper PDF.

### Step 2

Click **Analyze Paper**.

### Step 3

The system extracts and processes the document.

### Step 4

AI generates:

* Summary
* Methodology Explanation
* Key Contributions
* Findings
* Viva Questions & Answers

---

## 🔮 Future Enhancements

* Retrieval-Augmented Generation (RAG)
* Multi-paper comparison
* Citation extraction
* Research trend analysis
* Knowledge graph generation
* Interactive paper chatbot
* Multilingual explanations
* PDF summary export
  
---

## 🤝 Contributions

Contributions, feature requests, and suggestions are welcome.

Feel free to fork the repository and improve the project.

---

## 👨‍💻 Author

**Niya Benny**

Data Science Student

Passionate about Artificial Intelligence, Machine Learning, NLP, and Research Automation.

---

## ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the project

📢 Share it with others

---

### "Making Research Papers Easier to Understand with AI."
