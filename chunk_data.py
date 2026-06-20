from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

all_text = ""

for file in os.listdir("data"):
    if file.endswith(".txt"):
        with open(f"data/{file}", "r", encoding="utf-8") as f:
            all_text += f.read() + "\n"

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_text(all_text)

print(f"Total Chunks: {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0])