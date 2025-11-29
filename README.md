Mini Vector Database + RAG Pipeline (Built From Scratch)

This project is part of my AI Engineering learning journey.
In the last few days, I learned about embeddings, cosine similarity, vector search, and RAG — and I built a mini semantic search + RAG pipeline completely from scratch in Python.

This project does not use any external libraries for vector search.
Everything is implemented manually to understand how RAG works internally.

🚀 Features Implemented

Custom text chunking

Fake embedding generation (random vectors)

Cosine similarity implementation

A simple vector database

Top-K semantic search

Context-based answer generation

Full RAG pipeline (without LLM)

This is a tiny version of how real vector databases like FAISS or ChromaDB work.

📂 Project Structure
mini-rag/
│
├── vectordb.py      # All functions (chunking, embeddings, cosine similarity, search, answer)
├── README.md        # Project documentation
└── output.png       # Screenshot of sample output


I kept everything inside a single file to stay focused on learning.
Later, this can be modularized into multiple files.

🧠 How It Works
1️⃣ Chunking

Breaks text into overlapping chunks.

2️⃣ Fake Embeddings

Generates random vectors to simulate embedding behavior.

3️⃣ Vector Store

Stores:

{
  "id": 0,
  "chunk": "text...",
  "embedding": [0.23, -0.44, ...]
}

4️⃣ Cosine Similarity

Manually implemented to compare vectors.

5️⃣ Search

Finds the Top K most similar chunks to the query.

6️⃣ Answer Generation

Returns the top chunk as a “context-based answer”.

🖥️ Example Output

[
  {'score': 0.3616, 'chunk_text': 'I like momos'},
  {'score': -0.0016, 'chunk_text': 'Python is fun'}
]

Answer (based on context): I like momos

📸 Screenshots

<img width="764" height="833" alt="Screenshot 2025-11-30 000504" src="https://github.com/user-attachments/assets/fd6231c9-0868-4ae7-bad9-12017f0b56cf" />

<img width="851" height="854" alt="Screenshot 2025-11-30 000536" src="https://github.com/user-attachments/assets/bf4ff269-c463-4b6d-8175-2f92cdef7c64" />

<img width="1320" height="332" alt="Screenshot 2025-11-30 000610" src="https://github.com/user-attachments/assets/09ec3670-7c1e-4480-8d8e-8fc1010c2f7c" />

🔮 Next Steps (Upcoming Work)

Replace fake embeddings with OpenAI embeddings

Use a real LLM to generate natural answers

Integrate ChromaDB or FAISS

Build a complete Agentic RAG pipeline

Add a simple Flask API over the RAG system

🧑‍💻 Author

Amey Raut
4th Year IT Engineering Student
Learning AI + Python daily and building small projects.

⭐ If you like this project

Please ⭐ the repo — it helps a lot and motivates me to keep building!



