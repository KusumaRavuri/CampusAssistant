import os
import json
import faiss

from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from google import genai


# ============================================================
# 1. LOAD GEMINI API KEY
# ============================================================

# Load .env for local development
load_dotenv("backend/.env")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "Gemini API key not found. "
        "Make sure GEMINI_API_KEY is set in Streamlit Secrets."
    )

# Create Gemini client
client = genai.Client(api_key=api_key)


# ============================================================
# 2. LOAD RAG DATA
# ============================================================

with open("backend/chunks.json", "r", encoding="utf-8") as file:
    chunks = json.load(file)


# ============================================================
# 3. LOAD EMBEDDING MODEL
# ============================================================

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# ============================================================
# 4. LOAD FAISS VECTOR DATABASE
# ============================================================

index = faiss.read_index(
    "backend/faiss.index"
)


# ============================================================
# 5. RETRIEVAL
# ============================================================

def retrieve(question, top_k=5):

    # Convert question into an embedding
    question_embedding = embedding_model.encode(
        [question]
    )

    # Search FAISS
    distances, indices = index.search(
        question_embedding,
        top_k
    )

    results = []

    for i, index_number in enumerate(indices[0]):

        # Make sure the index is valid
        if index_number < 0 or index_number >= len(chunks):
            continue

        result = chunks[index_number]

        results.append({
            "text": result["text"],
            "page": result["page"],
            "source": result["source"],
            "distance": float(distances[0][i])
        })

    return results


# ============================================================
# 6. GENERATION
# ============================================================

def generate_answer(question):

    # --------------------------------------------------------
    # Retrieve relevant chunks
    # --------------------------------------------------------

    results = retrieve(question)


    # --------------------------------------------------------
    # Build context
    # --------------------------------------------------------

    context = ""

    for result in results:

        context += f"""
SOURCE: {result['source']}
PAGE: {result['page']}

{result['text']}

--------------------------------
"""


    # --------------------------------------------------------
    # Prompt for Gemini
    # --------------------------------------------------------

    prompt = f"""
You are a GITAM Campus Assistant.

Answer the student's question using ONLY the information
provided in the CONTEXT below.

Do NOT invent, assume, or add university rules that are not
present in the context.

If the answer is not available in the context, say:

"I couldn't find this information in the provided academic regulations."

Student Question:
{question}

CONTEXT:
{context}

Give a clear and concise answer.

At the end, mention the relevant page number.
"""


    # --------------------------------------------------------
    # Gemini LLM
    # --------------------------------------------------------

    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        return response.text, results


    # --------------------------------------------------------
    # SHOW ACTUAL GEMINI ERROR
    # --------------------------------------------------------

    except Exception as e:

        print("========================================")
        print("GEMINI ERROR")
        print("TYPE:", type(e).__name__)
        print("ERROR:", str(e))
        print("========================================")

        raise RuntimeError(
            f"Gemini API Error: {type(e).__name__} | {str(e)}"
        )
