from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import os

all_text = ""

for file in os.listdir("data"):
    if file.endswith(".txt"):
        with open(f"data/{file}", "r", encoding="utf-8") as f:
            all_text += f.read() + "\n"

splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=30
)

chunks = splitter.split_text(all_text)

print(f"Total Chunks: {len(chunks)}")

model = SentenceTransformer("all-MiniLM-L6-v2")

embedding = model.encode(chunks[0])

print(f"Embedding Dimension: {len(embedding)}")
print(embedding[:10])