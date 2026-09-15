import os
import time
import shutil
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_chroma import Chroma

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=API_KEY
)

def create_database(text):
    # Dynamically pick a unique directory path name to avoid locked database file system conflicts
    timestamp = int(time.time())
    persist_dir = f"chroma_db_{timestamp}"
        
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150
    )
    raw_chunks = splitter.create_documents([text])
    chunks = [doc for doc in raw_chunks if doc.page_content.strip()]
    
    batch_size = 15
    db = Chroma.from_documents(
        documents=chunks[:batch_size],
        embedding=embeddings,
        persist_directory=persist_dir
    )
    
    for i in range(batch_size, len(chunks), batch_size):
        batch = chunks[i:i + batch_size]
        db.add_documents(documents=batch)
        time.sleep(3.0)
        
    return db, len(chunks)

def ask_question(db, question):
    docs = db.similarity_search(question, k=3)
    context = "\n\n".join(doc.page_content for doc in docs)
    
    prompt = f"""
You are an advanced academic tutor. Answer the question using ONLY the context provided below.
Context:
{context}

Question:
{question}

If the answer is not available in the context, say:
"I could not find the answer in the uploaded document."
"""
    llm = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",
        google_api_key=API_KEY
    )
    response = llm.invoke(prompt)
    
    answer_text = ""
    if hasattr(response, 'text'):
        answer_text = response.text
    elif isinstance(response.content, dict) and 'text' in response.content:
        answer_text = response.content['text']
    else:
        answer_text = str(response.content)
        
    return answer_text, docs

def summarize_document(text):
    truncated_text = text[:40000]
    prompt = f"""
Provide a highly detailed, professional summary of the document provided below.
Your summary must include:
1. Core Topic Overview.
2. Key Concepts & Mathematical Elements.
3. Step-by-Step Workflow breakdown.
4. Final Takeaway/Conclusion.

Document Content:
{truncated_text}
"""
    llm = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",
        google_api_key=API_KEY
    )
    response = llm.invoke(prompt)
    
    if hasattr(response, 'text'):
        return response.text
    elif isinstance(response.content, dict) and 'text' in response.content:
        return response.content['text']
    else:
        return str(response.content)
