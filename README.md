# 🧠 RAG-Based AI Assistant (LangChain + Llama 3 + Groq)

An intelligent Retrieval-Augmented Generation (RAG) application that answers user queries based on custom documents using LLMs and vector search.

---

## 🚀 Features

* 🔍 Semantic search using vector embeddings
* 🤖 LLM-powered responses using Llama 3 (Groq API)
* 🧠 Conversational memory support
* 📄 Supports PDF/Text document ingestion
* ⚡ Fast inference using Groq
* 🌐 Interactive UI with Streamlit

---

## 🏗️ Tech Stack

* Python
* LangChain
* Llama 3 (Groq API)
* FAISS / ChromaDB
* Streamlit
* HuggingFace Embeddings

---

## 📂 Project Architecture

1. Documents are loaded and split into chunks
2. Text is converted into embeddings
3. Stored in a vector database
4. User query → converted to embedding
5. Relevant chunks retrieved
6. LLM generates answer using retrieved context

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/rag-application.git
cd rag-application
pip install -r requirements.txt
```

---

## 🔑 Setup Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run app/main.py
```

---

## 🧪 Example Use Cases

* Ask questions from PDF documents
* Build domain-specific chatbots
* Knowledge base assistant
* Resume / research paper Q&A

---

## 📸 Demo

(Add screenshots here)

---

## 💡 Key Learning Outcomes

* Implemented end-to-end RAG pipeline
* Understood vector similarity search (FAISS)
* Integrated LLM APIs (Groq + Llama 3)
* Built interactive AI apps using Streamlit

---

## 📈 Future Improvements

* Add multi-document support
* Improve retrieval with hybrid search
* Deploy on cloud (AWS / GCP)
* Add authentication

---

## 🤝 Contributing

Pull requests are welcome!

---

## 📄 License

MIT License

---

## 👨‍💻 Author

Aseem C P
BSc Computer Science (AI/ML) Student
Calicut University
