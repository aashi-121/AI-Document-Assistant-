📄 AI Document Assistant using LLM + RAG + LangChain + FAISS  
An AI-powered document assistant that enables context-aware question answering over custom PDF and text documents using a Retrieval-Augmented Generation (RAG) pipeline.  

This system converts documents into embeddings, stores them in a vector database, retrieves relevant content using semantic search, and generates accurate answers using a Large Language Model (LLM).

🚀 Features
📂 Upload and process PDF documents
✂️ Intelligent text chunking
🔢 Embedding generation using Sentence Transformers (all-MiniLM-L6-v2)
🗂 Vector storage using FAISS
🔍 Semantic similarity search
🤖 LLM integration (Llama 3 via Ollama)
🧠 Context-aware answer generation
❌ Reduced hallucination using RAG

🧠 Architecture Overview
PDF Document
      ↓
Document Loader (LangChain)
      ↓
Text Chunking
      ↓
Embeddings (all-MiniLM-L6-v2)
      ↓
FAISS Vector Database
      ↓
User Query
      ↓
Query Embedding
      ↓
Similarity Search (FAISS)
      ↓
Retrieve Relevant Chunks
      ↓
LLM (Llama 3)
      ↓
Final Answer


🛠 Tech Stack
Python
LangChain
FAISS (Vector Database)
Sentence Transformers (all-MiniLM-L6-v2)
Llama 3 (via Ollama)
PyPDF


📦 Installation
1️⃣ Clone Repository
```
git clone https://github.com/yourusername/ai-document-assistant.git
cd ai-document-assistant
```

2️⃣ Install Dependencies
```
pip install langchain
pip install langchain-community
pip install langchain-text-splitters
pip install faiss-cpu
pip install sentence-transformers
pip install langchain-ollama
pip install pypdf
```

3️⃣ Install Ollama (for Llama 3)


⚙️ How It Works
Step 1: Add your document

Place your PDF inside:
```
data/sample.pdf
```

Step 2: Create Vector Database

Run:
```
python ingest.py
```
Step 3: Ask Questions


🧩 Core Concepts Used
🔹 Retrieval-Augmented Generation (RAG)

Combines document retrieval with LLM-based answer generation to reduce hallucination.

🔹 Embeddings

Text is converted into numerical vectors using all-MiniLM-L6-v2 to enable semantic similarity search.

🔹 FAISS

Stores embeddings and performs efficient similarity search.

🔹 LLM (Llama 3)

Generates human-like responses using retrieved document context.

👩‍💻 Author

Aashi Sharma
Computer Science Engineer | AI & Data Enthusiast
