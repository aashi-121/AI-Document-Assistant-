from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM

# Step 1: Load embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Step 2: Load vector database
vectorstore = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)

print("Vector database loaded successfully")

# Step 3: Load LLM
llm = OllamaLLM(model="llama3")

print("LLM loaded successfully")

# Step 4: Create retriever
retriever = vectorstore.as_retriever()

# Step 5: Ask questions loop
while True:

    query = input("\nAsk your question (type 'exit' to quit): ")

    if query.lower() == "exit":
        break

    docs = retriever.invoke(query)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
Answer the question using only the context below.

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)

    print("\nAnswer:", response)