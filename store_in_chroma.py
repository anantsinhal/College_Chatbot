import os
import chromadb

from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Embedding Model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Text Splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

# ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

# Delete old collection
try:
    client.delete_collection("college_data")
    print("Old collection deleted.")
except:
    print("No existing collection found.")

# Create new collection
collection = client.get_or_create_collection(
    name="college_data"
)

chunk_id = 0
total_chunks = 0

# Process each file separately
for file in os.listdir("data"):

    if not file.endswith(".txt"):
        continue

    print(f"Processing: {file}")

    with open(f"data/{file}", "r", encoding="utf-8") as f:
        text = f.read()

    chunks = splitter.split_text(text)

    total_chunks += len(chunks)

    for chunk in chunks:

        embedding = model.encode(chunk).tolist()

        collection.add(
            ids=[str(chunk_id)],
            documents=[chunk],
            embeddings=[embedding],
            metadatas=[{
                "source": file
            }]
        )

        chunk_id += 1

print("\n===================================")
print(f"Total Chunks Stored: {total_chunks}")
print("Stored successfully with metadata!")
print("===================================")