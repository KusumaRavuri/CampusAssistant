# 🎓 GITAM Campus Assistant

An AI-powered campus assistant that answers questions about **GITAM academic regulations** using Retrieval-Augmented Generation (RAG).

## 🚀 Live Demo

👉 **[Open GITAM Campus Assistant](https://campus-assistant-gitam.streamlit.app/)**

## 📌 About the Project

GITAM Campus Assistant helps students quickly find information from academic regulations instead of manually searching through lengthy PDF documents.

The application retrieves relevant sections from the regulations and uses an LLM to generate a clear, context-based answer.

## ✨ Features

- 🔎 Semantic search over GITAM academic regulations
- 🤖 AI-generated answers using RAG
- 📚 Shows relevant source pages for answers
- ⚡ Fast question-and-answer interface
- 🌐 Deployed using Streamlit
- 📱 Responsive user interface

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **RAG (Retrieval-Augmented Generation)**
- **FAISS** – vector similarity search
- **Sentence Transformers** – text embeddings
- **Gemini API** – answer generation
- **SQL** – database concepts / data handling

## 🧠 How It Works

```text
User Question
      ↓
Sentence Transformer
      ↓
FAISS Similarity Search
      ↓
Relevant Regulation Chunks
      ↓
Gemini API
      ↓
Context-Based Answer
      ↓
Sources / Page References
```

## 📂 Project Structure

```text
CampusAssistant/
│
├── backend/
│   ├── rag.py
│   ├── search.py
│   ├── regulations.txt
│   ├── chunks.json
│   └── faiss.index
│
├── frontend/
│   └── app.py
│
├── requirements.txt
└── README.md
```

## ▶️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/KusumaRavuri/CampusAssistant.git
cd CampusAssistant
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Gemini API key

Create a `.env` file and add:

```text
GEMINI_API_KEY=your_api_key_here
```

Do not commit your API key to GitHub.

### 5. Start the application

```bash
streamlit run frontend/app.py
```

The application will open in your browser.

## 📄 Data Source

The assistant is designed around GITAM academic regulations and retrieves relevant content from the indexed regulation documents before generating answers.

## 🎯 Purpose

This project demonstrates the practical use of **RAG, vector search, embeddings, and generative AI** to build a useful domain-specific academic assistant.

## 👩‍💻 Author

**Kusuma Ravuri**  
B.Tech – Computer Science and Engineering, GITAM

- GitHub: https://github.com/KusumaRavuri
