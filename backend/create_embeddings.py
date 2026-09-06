import json
import faiss
from sentence_transformers import SentenceTransformer

# Load our saved chunks
with open("backend/chunks.json", "r", encoding="utf-8") as file:
    chunks = json.load(file)

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Get the text from each chunk
texts = [chunk["text"] for chunk in chunks]

# Convert text into embeddings
embeddings = model.encode(
    texts,
    show_progress_bar=True
)

print("Embeddings created!")
print("Number of embeddings:", len(embeddings))
print("Embedding dimensions:", embeddings.shape[1])

# Create FAISS index
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save FAISS index
faiss.write_index(index, "backend/faiss.index")

print("FAISS index saved!")