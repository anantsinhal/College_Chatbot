

import os
import chromadb
import google.generativeai as genai

from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

# Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")


embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection("college_data")

print("College Chatbot Ready!")
print("Type 'exit' to quit.\n")

while True:

    question = input("You: ")

    if question.lower() == "exit":
        break

   
    question_embedding = embedding_model.encode(question).tolist()


    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=7
    )

    # Show metadata sources
    print("\nSOURCES:\n")
    print(results["metadatas"][0])
    print(results["distances"][0])

    # Combine retrieved chunks
    retrieved_chunks = "\n\n".join(results["documents"][0])

    print("\nRETRIEVED CHUNKS:\n")
    print(retrieved_chunks[:3000])


    prompt = f"""

You are a SMIT College Assistant.

Rules:
- Give short answers.
- Answer in 1-3 sentences maximum.
- If the question is about a person, give only their designation and important role.
- Do not provide unnecessary details.
- Use only the provided context.

Context:
{retrieved_chunks}

Question:
{question}
"""

   
    response = model.generate_content(prompt)

    print("\nBot:")
    print(response.text)

    print("\n" + "=" * 60 + "\n")