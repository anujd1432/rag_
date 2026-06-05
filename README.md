<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Syne&weight=800&size=42&pause=1000&color=7C6AF7&center=true&vCenter=true&width=600&height=80&lines=🧠+DocuMind+AI" alt="DocuMind AI" />

<img src="https://readme-typing-svg.demolab.com?font=Space+Grotesk&size=20&pause=2000&color=4FD1C5&center=true&vCenter=true&width=600&height=40&lines=RAG-powered+Document+Intelligence+%F0%9F%9A%80;Upload+%E2%80%A2+Index+%E2%80%A2+Ask+Anything+%F0%9F%92%AC;Powered+by+LlaMA+3.3+70B+%2B+FAISS+%2B+LangChain" alt="Subtitle" />

<br/>

[![Live Demo](https://img.shields.io/badge/🌐_Live_Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://s89vwpzlbrjx9qfjyxep59.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-0.3-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)](https://langchain.com)
[![Groq](https://img.shields.io/badge/Groq-LlaMA_3.3_70B-F55036?style=for-the-badge)](https://groq.com)
[![FAISS](https://img.shields.io/badge/FAISS-Vector_Store-0078D4?style=for-the-badge)](https://faiss.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-f6c344?style=for-the-badge)](LICENSE)

<br/>

> **Chat with any document.** Upload a PDF or TXT, watch it get chunked & embedded in seconds, then ask questions in natural language — all powered by LlaMA 3.3 70B via Groq's blazing-fast inference.

<br/>

---

</div>

## ✨ Features

| | Feature | Description |
|---|---|---|
| 📂 | **Multi-format Upload** | Supports `.pdf` and `.txt` documents |
| ⚡ | **Instant Indexing** | Splits, embeds & stores vectors in seconds |
| 🧠 | **LlaMA 3.3 70B** | State-of-the-art LLM via Groq's ultra-fast API |
| 🔍 | **Semantic Search** | FAISS similarity search for relevant context retrieval |
| 💬 | **Conversational UI** | Beautiful dark-mode chat interface with history |
| 📚 | **Source Transparency** | Collapsible source chunk viewer per answer |
| 🎛️ | **Tunable Settings** | Control chunk size, overlap, and top-K results |
| 💡 | **Smart Suggestions** | One-click example questions to get you started |

---

## 🖥️ Live Demo

<div align="center">

### 🔗 [https://s89vwpzlbrjx9qfjyxep59.streamlit.app](https://s89vwpzlbrjx9qfjyxep59.streamlit.app)

</div>

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        DocuMind AI                          │
│                                                             │
│   📄 Document                                               │
│       │                                                     │
│       ▼                                                     │
│   ✂️  Text Splitter  ──► RecursiveCharacterTextSplitter     │
│       │              (chunk_size=500, overlap=50)           │
│       ▼                                                     │
│   🔢 Embeddings  ────► sentence-transformers/all-MiniLM-L6  │
│       │                                                     │
│       ▼                                                     │
│   🗄️  Vector Store  ──► FAISS (in-memory)                   │
│                                                             │
│   💬 User Query                                             │
│       │                                                     │
│       ├──► 🔍 Retriever  (top-k similarity search)         │
│       │         │                                           │
│       │         ▼                                           │
│       └──► 🤖 LlaMA 3.3 70B  (via Groq API)                │
│                 │                                           │
│                 ▼                                           │
│            ✅ Answer  +  📚 Source Chunks                   │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 Quick Start

### 1 · Clone the repo

```bash
git clone https://github.com/your-username/documind-ai.git
cd documind-ai
```

### 2 · Install dependencies

```bash
pip install -r requirements.txt
```

### 3 · Set up environment variables

```bash
cp .env.example .env
# Then add your GROQ_API_KEY to .env
```

```env
GROQ_API_KEY=gsk_your_key_here
```

> 🔑 Get a free API key at [console.groq.com](https://console.groq.com)

### 4 · Run the app

```bash
streamlit run rag_app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser 🎉

---

## 📦 Dependencies

```txt
streamlit
langchain
langchain-community
langchain-groq
langchain-text-splitters
faiss-cpu
sentence-transformers
pypdf
python-dotenv
```

Install all at once:

```bash
pip install streamlit langchain langchain-community langchain-groq \
            langchain-text-splitters faiss-cpu sentence-transformers \
            pypdf python-dotenv
```

---

## 📁 Project Structure

```
documind-ai/
│
├── rag_app.py          # 🎯 Main Streamlit application
├── requirements.txt    # 📦 Python dependencies
├── .env.example        # 🔑 Environment variable template
├── .env                # 🔒 Your secrets (git-ignored)
├── sample_text.txt     # 📄 Example document (optional)
└── README.md           # 📖 This file
```

---

## ⚙️ Configuration

Tune the RAG pipeline from the **Advanced Settings** panel in the sidebar:

| Parameter | Default | Description |
|---|---|---|
| `Chunk Size` | `500` | Max characters per text chunk |
| `Chunk Overlap` | `50` | Overlap between consecutive chunks |
| `Top-K Results` | `3` | Number of chunks retrieved per query |

> Larger chunks = more context per answer. Smaller chunks = more precise retrieval. Experiment! 🧪

---

## 🧩 Tech Stack

<div align="center">

| Layer | Technology |
|---|---|
| 🖼️ **Frontend** | Streamlit + Custom CSS |
| 🔗 **Orchestration** | LangChain |
| 🤖 **LLM** | LlaMA 3.3 70B via Groq |
| 🔢 **Embeddings** | `sentence-transformers/all-MiniLM-L6-v2` |
| 🗄️ **Vector Store** | FAISS |
| 📄 **Document Loading** | PyPDFLoader · TextLoader |
| ✂️ **Text Splitting** | RecursiveCharacterTextSplitter |

</div>

---

## 🤝 Contributing

Contributions are welcome! Here's how:

```bash
# 1. Fork the repo
# 2. Create your feature branch
git checkout -b feature/amazing-feature

# 3. Commit your changes
git commit -m "✨ Add amazing feature"

# 4. Push and open a Pull Request
git push origin feature/amazing-feature
```

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with ❤️ and a lot of ☕

⭐ **Star this repo** if you found it useful!

[![Star History Chart](https://img.shields.io/github/stars/your-username/documind-ai?style=social)](https://github.com/your-username/documind-ai)

</div>
