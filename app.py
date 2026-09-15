import streamlit as st
import shutil
import os
from pdf_processor import extract_text
from rag import create_database, ask_question, summarize_document

st.set_page_config(
    page_title="Advanced RAG Assistant",
    page_icon="📚",
    layout="wide"
)

# Initialize Session State Variables for memory management
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
if "chunk_count" not in st.session_state:
    st.session_state["chunk_count"] = 0

# Sidebar Control Panel Dashboard
with st.sidebar:
    st.title("⚙️ Control Dashboard")
    st.subheader("Document Metrics")
    st.metric(label="Total Processed Chunks", value=st.session_state["chunk_count"])
    
    st.divider()
    if st.button("Wipe Vector Database & Clear History", type="primary"):
        if os.path.exists("chroma_db"):
            shutil.rmtree("chroma_db")
        if os.path.exists("uploads"):
            shutil.rmtree("uploads")
            os.makedirs("uploads")
        st.session_state.clear()
        st.success("Application reset successfully!")
        st.rerun()

# Primary Web Application Layout
st.title("📚 AI PDF Knowledge Assistant (Pro Version)")
st.write("Upload an educational document to leverage batch embeddings, text summarization, and interactive chat history memory.")

uploaded_file = st.file_uploader("Upload your PDF document", type=["pdf"])

if uploaded_file:
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
    file_path = "uploads/" + uploaded_file.name
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Render processing validation controls
    if "db" not in st.session_state:
        if st.button("Process PDF"):
            with st.spinner("Executing optimized chunking and embedding steps..."):
                text = extract_text(file_path)
                if not text.strip():
                    st.error("Failed to parse valid text contents from document.")
                else:
                    db, count = create_database(text)
                    st.session_state["db"] = db
                    st.session_state["raw_text"] = text
                    st.session_state["chunk_count"] = count
                    st.success("Document analyzed and persistent vector index built!")
                    st.rerun()

if "db" in st.session_state:
    st.divider()
    
    # High-level overview block
    st.subheader("📋 Document Summary")
    if st.button("Generate Architectural Overview Summary"):
        with st.spinner("Running contextual synthesis..."):
            summary = summarize_document(st.session_state["raw_text"])
        st.info("High-Level Summary Overview:")
        st.markdown(summary)
        
    st.divider()
    st.subheader("💬 Interactive Query Engine")
    
    # Display running chat memory logs dynamically
    for role, message in st.session_state["chat_history"]:
        if role == "User":
            st.markdown(f"**👤 You:** {message}")
        else:
            st.markdown(f"**🤖 Assistant:** {message}")
            
    # Input panel controls
    question = st.text_input("Ask a question about the document:", key="query_box")
    
    if st.button("Submit Question"):
        if question.strip():
            with st.spinner("Scanning persistent vector arrays..."):
                answer, source_docs = ask_question(st.session_state["db"], question)
            
            # Store transaction in session chat log memory
            st.session_state["chat_history"].append(("User", question))
            st.session_state["chat_history"].append(("Assistant", answer))
            
            st.rerun()
        else:
            st.warning("Please enter a text question.")
            
    # Display reference grounding verification blocks directly in the app
    if st.session_state["chat_history"]:
        st.divider()
        st.subheader("🔍 Retained Reference Sources")
        st.caption("These are the high-confidence document chunks extracted by the database for your last query:")
        
        # Pull the last question search if sources exist from vector lookup
        if 'source_docs' in locals():
            for idx, doc in enumerate(source_docs):
                with st.expander(f"Reference Source Chunk #{idx + 1}"):
                    st.write(doc.page_content)
