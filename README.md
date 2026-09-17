# 🌟 Advanced AI PDF Knowledge Assistant 

<div align="center">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Streamlit"/>
  <img src="https://img.shields.io/badge/LangChain-121212?style=for-the-badge&logo=langchain&logoColor=white" alt="LangChain"/>
  <img src="https://img.shields.io/badge/Google_Gemini-8E75B2?style=for-the-badge&logo=googlebard&logoColor=white" alt="Gemini API"/>
  <img src="https://img.shields.io/badge/ChromaDB-339933?style=for-the-badge&logo=chroma&logoColor=white" alt="ChromaDB"/>
</div>

<br/>

> A production-grade **Retrieval-Augmented Generation (RAG)** application built with **Streamlit**, **LangChain**, and the **Gemini 3.6 API** engine. Empower yourself to upload dense educational or technical PDF documents, generate high-level structured topic summaries, and engage in interactive, contextual chat dialogs backed by persistent vector search tracking.

---

## ✨ Key Features

| Feature | Description |
| :--- | :--- |
| 📄 **Document Parsing & Text Extraction** | Extracts and structures data using `pypdf`, integrating a dedicated surrogate text cleaner to remove special characters or invalid string encodings. |
| ⏱️ **Throttled Batch Embeddings** | Bypasses Gemini API free-tier rate limits (`RESOURCE_EXHAUSTED`) using custom chunking windows (`chunk_size=1000`, `chunk_overlap=150`) combined with safe 3.0-second batch interval logic. |
| 🗄️ **Persistent Local Database** | Generates numerical vector records via `gemini-embedding-001` and manages references dynamically using isolated **ChromaDB** target folder directories. |
| 🧠 **Contextual Synthesis Layout** | Powered by the cutting-edge **`gemini-3.6-flash`** model to execute accurate semantic lookups without AI hallucinations. |
| 🎛️ **Control Dashboard Sidebar** | A sidebar panel featuring real-time data statistics (Total Processed Chunks) alongside administrative system wipe triggers. |
| 💬 **Interactive Chat Log Memory** | Seamlessly remembers past user queries and responses within the running layout session. |
| 🔍 **Grounding Transparency** | Includes drop-down verification cards exposing raw source fragments fetched directly from the database matching the user's last question. |

---

## 🏗️ Project Directory Structure

```text
📁 mini_rag/
├── 🌐 app.py              # Streamlit Web Application Interface Layout
├── 🧠 rag.py              # Vector Database, Splitting, and Gemini API Engine Logic
├── 📝 pdf_processor.py    # Text Extraction and UTF-8 Surrogate Data Filtering
├── 📦 requirements.txt    # Application Dependency Packages List
├── 🚫 .gitignore          # Access Rule Filter (Excludes venv/ and secure profiles)
└── 🔐 .env                # Private API Key Profile Configuration (Hidden)
```

---

## 💻 Local Installation & Setup

### 1️⃣ Clone or Open the Project
Open your Zsh terminal window on macOS and navigate directly to your working directory:
```bash
cd "~/drive/SEMESTER 5/VAC/mini_rag"
```

### 2️⃣ Configure Your Virtual Environment
Set up a clean sandbox for your Python packages:
```bash
# Create the environment path
python3 -m venv venv

# Activate the local environment
source venv/bin/activate
```

### 3️⃣ Install Package Dependencies
Install all required project core layers at once:
```bash
pip install -r requirements.txt
```

### 4️⃣ Create and Configure Your Environment File
Create a `.env` file in the root folder directory:
```bash
touch .env
```
Open the file and securely enter your Google AI Studio credential signature:
```text
GEMINI_API_KEY=YOUR_ACTUAL_API_KEY_HERE
```

---

## 🚀 Running the Application

Launch the local web development platform directly from your active environment terminal:
```bash
python3 -m streamlit run app.py
```
🎉 **Boom!** Your default browser will launch automatically to your running application at **`http://localhost:8501`**.

---

## 📐 Conceptual Parameters Summary

⚙️ **Under the Hood Details:**
- **Text Splitter Model:** `RecursiveCharacterTextSplitter`
- **Chunk Parameters:** `chunk_size=1000` &nbsp;\|&nbsp; `chunk_overlap=150`
- **Embeddings Space Vector Array:** `models/gemini-embedding-001`
- **Generative Synthesis Target Model:** `models/gemini-3.6-flash`

---
<div align="center">
  <i>Built with ❤️ for advanced AI knowledge retrieval</i>
</div>
