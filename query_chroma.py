import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection("college_data")

question = input("Ask a question: ")

question_embedding = model.encode(question).tolist()

results = collection.query(
    query_embeddings=[question_embedding],
    n_results=2
)

print("\nSOURCES:\n")
print(results["metadatas"][0])

print("\nTOP RESULTS:\n")

for doc in results["documents"][0]:
    print("=" * 50)
    print(doc[:1000])
    print()