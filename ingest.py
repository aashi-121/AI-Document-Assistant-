from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Step 1: Load PDF
loader = PyPDFLoader("data/Aashi_AI.pdf")
documents = loader.load()

print("Document loaded successfully")

# Step 2: Split into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks")

# Step 3: Create embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

print("Embeddings model loaded")

# Step 4: Store in FAISS vector database
vectorstore = FAISS.from_documents(
    documents=chunks,
    embedding=embeddings
)

# Step 5: Save vector database
vectorstore.save_local("vectorstore")

print("Vector database created and saved successfully")