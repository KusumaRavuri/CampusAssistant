import json
import faiss
from sentence_transformers import SentenceTransformer

# Load saved chunks
with open("backend/chunks.json", "r", encoding="utf-8") as file:
    chunks = json.load(file)

# Load the same embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index("backend/faiss.index")


def search(query, top_k=3):
    # Convert the student's question into an embedding
    query_embedding = model.encode([query])

    # Search FAISS
    distances, indices = index.search(query_embedding, top_k)

    print("\nQuestion:", query)
    print("\nRelevant information:\n")

    for rank, index_number in enumerate(indices[0]):
        result = chunks[index_number]

        print(f"--- Result {rank + 1} ---")
        print("Page:", result["page"])
        print("Source:", result["source"])
        print("Distance:", distances[0][rank])
        print("Text:")
        print(result["text"])
        print()


# Test question
question = input("Ask a question about the regulations: ")

search(question)