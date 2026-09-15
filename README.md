# Advanced AI PDF Knowledge Assistant (Pro Version)

A production-grade **Retrieval-Augmented Generation (RAG)** application built with **Streamlit**, **LangChain**, and the **Gemini 3.6 API** engine. This application allows users to upload dense educational or technical PDF documents, generate high-level structured topic summaries, and engage in an interactive contextual chat dialog backed by persistent vector search tracking.

## 🚀 Key Features

- **Document Parsing & Text Extraction:** Extracts and structures data using `pypdf`, integrating a dedicated surrogate text cleaner to remove special characters or invalid string encodings.
- **Throttled Batch Embeddings Processing:** Bypasses Gemini API free-tier rate limits (`RESOURCE_EXHAUSTED`) using custom chunking windows (`chunk_size=1000`, `chunk_overlap=150`) combined with a safe 3.0-second batch interval logic.
- **Persistent Local Database (ChromaDB):** Generates numerical vector records using `gemini-embedding-001` and manages references dynamically using isolated database target folder directories.
- **Contextual Synthesis Layout:** Powered by the newly updated **`gemini-3.6-flash`** model to execute semantic lookups without AI hallucinations.
- **Control Dashboard Sidebar:** A sidebar panel featuring real-time data statistics (Total Processed Chunks) alongside administrative system wipe triggers.
- **Interactive Chat Log Memory:** Remembers past user queries and responses within the running layout session.
- **Grounding Transparency:** Includes drop-down verification cards exposing raw source fragments fetched directly from the database matching the user's last question.

---

## 🏗️ Project Directory Structure

```text
mini_rag/
├── app.py              # Streamlit Web Application Interface Layout
├── rag.py              # Vector Database, Splitting, and Gemini API Engine Logic
├── pdf_processor.py    # Text Extraction and UTF-8 Surrogate Data Filtering
├── requirements.txt    # Application Dependency Packages List
├── .gitignore          # Access Rule Filter (Excludes venv/ and secure profiles)
└── .env                # Private API Key Profile Configuration (Hidden)
```

---

## 💻 Local Installation & Setup Instructions

### 1. Clone or Open the Project
Open your Zsh terminal window on macOS and navigate directly to your working directory:
```bash
cd "~/drive/SEMESTER 5/VAC/mini_rag"
```

### 2. Configure Your Virtual Environment
```bash
# Create the environment path
python3 -m venv venv

# Activate the local environment
source venv/bin/activate
```

### 3. Install Package Dependencies
Install all required project core layers at once:
```bash
pip install -r requirements.txt
```

### 4. Create and Configure Your Environment File
Create a `.env` file in the root folder directory:
```bash
touch .env
```
Open the file and enter your Google AI Studio credential signature:
```text
GEMINI_API_KEY=YOUR_ACTUAL_API_KEY_HERE
```

---

## 🛠️ Running the Application

Launch the local web development platform directly from your active environment terminal:
```bash
python3 -m streamlit run app.py
```
Your default browser will launch automatically to your running application at **`http://localhost:8501`**.

---

## 📐 Conceptual Parameters Summary

- **Text Splitter Model:** `RecursiveCharacterTextSplitter`
- **Chunk Parameters:** `chunk_size=1000`, `chunk_overlap=150`
- **Embeddings Space Vector Array:** `models/gemini-embedding-001`
- **Generative Synthesis Target Model:** `models/gemini-3.6-flash`
