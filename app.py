import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# ── Page config (MUST be first Streamlit call) ──────────────────────────────
st.set_page_config(
    page_title="DocuMind AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Syne:wght@400;700;800&display=swap');

/* ── Root palette ── */
:root {
    --bg:        #0d0f1a;
    --surface:   #151828;
    --card:      #1c2035;
    --border:    #2a2f4a;
    --accent1:   #7c6af7;   /* violet */
    --accent2:   #f7746a;   /* coral */
    --accent3:   #4fd1c5;   /* teal */
    --accent4:   #f6c344;   /* amber */
    --text:      #e8eaf6;
    --muted:     #7b82a8;
    --radius:    14px;
}

/* ── Global reset ── */
html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--bg) !important;
    font-family: 'Space Grotesk', sans-serif;
    color: var(--text);
}

[data-testid="stSidebar"] {
    background: var(--surface) !important;
    border-right: 1px solid var(--border);
}

/* ── Hide default header ── */
header[data-testid="stHeader"] { display: none; }

/* ── Hero banner ── */
.hero {
    background: linear-gradient(135deg, #1a1040 0%, #0d1a2e 50%, #1a1040 100%);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 2.5rem 2rem 2rem;
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 200px; height: 200px;
    background: radial-gradient(circle, rgba(124,106,247,.35) 0%, transparent 70%);
    border-radius: 50%;
}
.hero::after {
    content: '';
    position: absolute;
    bottom: -40px; left: 20%;
    width: 160px; height: 160px;
    background: radial-gradient(circle, rgba(247,116,106,.25) 0%, transparent 70%);
    border-radius: 50%;
}
.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: 2.6rem;
    font-weight: 800;
    background: linear-gradient(90deg, var(--accent1), var(--accent2), var(--accent3));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.1;
    margin: 0 0 .4rem;
}
.hero-sub {
    color: var(--muted);
    font-size: 1rem;
    margin: 0;
}

/* ── Stat pills ── */
.stats-row { display: flex; gap: .75rem; margin-bottom: 1.5rem; flex-wrap: wrap; }
.stat-pill {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 50px;
    padding: .45rem 1rem;
    font-size: .82rem;
    color: var(--muted);
    display: flex; align-items: center; gap: .4rem;
}
.stat-pill span { color: var(--text); font-weight: 600; }

/* ── Cards ── */
.card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.25rem 1.4rem;
    margin-bottom: 1rem;
}
.card-title {
    font-size: .78rem;
    text-transform: uppercase;
    letter-spacing: .12em;
    color: var(--muted);
    margin-bottom: .6rem;
}

/* ── Chat bubbles ── */
.chat-wrap { display: flex; flex-direction: column; gap: 1rem; margin-bottom: 1.5rem; }
.bubble {
    padding: 1rem 1.2rem;
    border-radius: var(--radius);
    font-size: .95rem;
    line-height: 1.6;
    max-width: 88%;
}
.bubble-user {
    background: linear-gradient(135deg, #2a1f6b, #3d2070);
    border: 1px solid var(--accent1);
    align-self: flex-end;
}
.bubble-bot {
    background: var(--card);
    border: 1px solid var(--border);
    align-self: flex-start;
}
.bubble-label {
    font-size: .72rem;
    text-transform: uppercase;
    letter-spacing: .1em;
    margin-bottom: .35rem;
    font-weight: 600;
}
.label-user { color: var(--accent1); }
.label-bot  { color: var(--accent3); }

/* ── Source chunk cards ── */
.source-card {
    background: #111625;
    border-left: 3px solid var(--accent4);
    border-radius: 0 10px 10px 0;
    padding: .75rem 1rem;
    margin-bottom: .5rem;
    font-size: .82rem;
    color: var(--muted);
    line-height: 1.5;
}
.source-num {
    font-weight: 700;
    color: var(--accent4);
    margin-right: .4rem;
}

/* ── Streamlit overrides ── */
.stTextInput > div > div > input,
.stTextArea textarea {
    background: var(--card) !important;
    color: var(--text) !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    font-family: 'Space Grotesk', sans-serif !important;
}
.stTextInput > div > div > input:focus,
.stTextArea textarea:focus {
    border-color: var(--accent1) !important;
    box-shadow: 0 0 0 2px rgba(124,106,247,.25) !important;
}

/* Primary button */
.stButton > button {
    background: linear-gradient(135deg, var(--accent1), #9b59f5) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
    padding: .55rem 1.4rem !important;
    transition: opacity .2s, transform .15s !important;
}
.stButton > button:hover { opacity: .88 !important; transform: translateY(-1px) !important; }
.stButton > button:active { transform: translateY(0) !important; }

/* File uploader */
[data-testid="stFileUploadDropzone"] {
    background: var(--card) !important;
    border: 2px dashed var(--border) !important;
    border-radius: var(--radius) !important;
}
[data-testid="stFileUploadDropzone"]:hover { border-color: var(--accent1) !important; }

/* Selectbox */
[data-baseweb="select"] > div {
    background: var(--card) !important;
    border-color: var(--border) !important;
    color: var(--text) !important;
    border-radius: 10px !important;
}

/* Slider */
[data-testid="stSlider"] .st-b3 { background: var(--accent1) !important; }

/* Expander */
[data-testid="stExpander"] {
    background: var(--card) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
}
[data-testid="stExpander"] summary { color: var(--muted) !important; font-size: .85rem !important; }

/* Divider */
hr { border-color: var(--border) !important; margin: 1.2rem 0 !important; }

/* Success / info / warning banners */
[data-testid="stAlert"] { border-radius: var(--radius) !important; }

/* Spinner */
[data-testid="stSpinner"] { color: var(--accent3) !important; }

/* Scrollbar */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 6px; }

/* ── Badge ── */
.badge {
    display: inline-block;
    padding: .18rem .65rem;
    border-radius: 50px;
    font-size: .72rem;
    font-weight: 700;
    letter-spacing: .06em;
    text-transform: uppercase;
}
.badge-violet { background: rgba(124,106,247,.18); color: var(--accent1); border: 1px solid var(--accent1); }
.badge-teal   { background: rgba(79,209,197,.18);  color: var(--accent3); border: 1px solid var(--accent3); }
.badge-coral  { background: rgba(247,116,106,.18); color: var(--accent2); border: 1px solid var(--accent2); }
</style>
""", unsafe_allow_html=True)


# ── Session state defaults ───────────────────────────────────────────────────
for key, val in {
    "messages": [],
    "rag_ready": False,
    "vectorstore": None,
    "retriever": None,
    "chain": None,
    "chunk_count": 0,
    "doc_name": "",
}.items():
    if key not in st.session_state:
        st.session_state[key] = val


# ── Helper: build RAG pipeline ───────────────────────────────────────────────
@st.cache_resource(show_spinner=False)
def build_pipeline(file_bytes: bytes, file_name: str, chunk_size: int,
                   chunk_overlap: int, top_k: int, groq_key: str):
    import tempfile
    from langchain_community.document_loaders import PyPDFLoader, TextLoader
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from langchain_community.embeddings import HuggingFaceEmbeddings
    from langchain_community.vectorstores import FAISS
    from langchain_groq import ChatGroq
    from langchain_core.prompts import ChatPromptTemplate

    # Save uploaded file to tmp
    suffix = ".pdf" if file_name.endswith(".pdf") else ".txt"
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(file_bytes)
        tmp_path = tmp.name

    loader = PyPDFLoader(tmp_path) if suffix == ".pdf" else TextLoader(tmp_path, encoding="utf-8")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": top_k})

    prompt = ChatPromptTemplate.from_messages([
        ("system",
         "You are DocuMind, an intelligent document assistant. "
         "Answer the user's question using ONLY the provided context. "
         "Be concise, accurate, and helpful. "
         "If the answer isn't in the context, say so honestly."),
        ("human", "Context:\n{context}\n\nQuestion: {question}"),
    ])

    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0, api_key=groq_key)
    chain = prompt | llm

    return retriever, chain, len(chunks)


# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="text-align:center;padding:1.2rem 0 1rem;">
        <div style="font-size:2.8rem;">🧠</div>
        <div style="font-family:'Syne',sans-serif;font-size:1.3rem;font-weight:800;
                    background:linear-gradient(90deg,#7c6af7,#4fd1c5);
                    -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                    background-clip:text;">DocuMind AI</div>
        <div style="color:#7b82a8;font-size:.75rem;margin-top:.2rem;">RAG-powered document chat</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ── API Key ──
    st.markdown('<div class="card-title">🔑 Groq API Key</div>', unsafe_allow_html=True)
    groq_key = st.text_input("", type="password", placeholder="gsk_...",
                             value=os.getenv("GROQ_API_KEY", ""), label_visibility="collapsed")

    st.markdown("---")

    # ── Upload ──
    st.markdown('<div class="card-title">📄 Upload Document</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("", type=["pdf", "txt"], label_visibility="collapsed")

    st.markdown("---")

    # ── Settings ──
    with st.expander("⚙️  Advanced Settings"):
        chunk_size    = st.slider("Chunk Size",    200, 2000, 500, 50)
        chunk_overlap = st.slider("Chunk Overlap",  0,  400,  50, 10)
        top_k         = st.slider("Top-K Results",  1,   10,   3,  1)

    st.markdown("---")

    # ── Build button ──
    build_clicked = st.button("🚀  Build RAG Pipeline", use_container_width=True)

    if build_clicked:
        if not groq_key:
            st.error("🔑 Please enter your Groq API key.")
        elif not uploaded_file:
            st.warning("📂 Please upload a PDF or TXT file.")
        else:
            with st.spinner("⚡ Building pipeline…"):
                try:
                    retriever, chain, n_chunks = build_pipeline(
                        uploaded_file.read(), uploaded_file.name,
                        chunk_size, chunk_overlap, top_k, groq_key,
                    )
                    st.session_state.retriever   = retriever
                    st.session_state.chain       = chain
                    st.session_state.chunk_count = n_chunks
                    st.session_state.doc_name    = uploaded_file.name
                    st.session_state.rag_ready   = True
                    st.session_state.messages    = []
                    st.success(f"✅ Ready! {n_chunks} chunks indexed.")
                except Exception as e:
                    st.error(f"❌ Error: {e}")

    # ── Status ──
    st.markdown("---")
    if st.session_state.rag_ready:
        st.markdown(f"""
        <div class="card" style="padding:.9rem 1rem;">
            <div style="font-size:.75rem;color:#7b82a8;margin-bottom:.5rem;text-transform:uppercase;letter-spacing:.1em;">Status</div>
            <div style="display:flex;align-items:center;gap:.5rem;margin-bottom:.35rem;">
                <span style="font-size:.95rem;">📄</span>
                <span style="font-size:.82rem;color:#e8eaf6;word-break:break-all;">{st.session_state.doc_name}</span>
            </div>
            <div style="display:flex;gap:.5rem;flex-wrap:wrap;">
                <span class="badge badge-teal">✔ Ready</span>
                <span class="badge badge-violet">{st.session_state.chunk_count} chunks</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="card" style="padding:.9rem 1rem;text-align:center;">
            <div style="font-size:1.5rem;margin-bottom:.3rem;">💤</div>
            <div style="font-size:.8rem;color:#7b82a8;">No document loaded</div>
        </div>
        """, unsafe_allow_html=True)

    # ── Clear chat ──
    if st.session_state.messages:
        if st.button("🗑️  Clear Chat", use_container_width=True):
            st.session_state.messages = []
            st.rerun()


# ── Main area ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-title">🧠 DocuMind AI</div>
    <p class="hero-sub">Upload a document · Build the pipeline · Ask anything</p>
</div>
""", unsafe_allow_html=True)

# ── Stats row ──
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f"""
    <div class="stat-pill">💬 <span>{len(st.session_state.messages)}</span> messages</div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f"""
    <div class="stat-pill">📦 <span>{st.session_state.chunk_count}</span> chunks</div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown(f"""
    <div class="stat-pill">🤖 <span>Llama 3.3 70B</span></div>
    """, unsafe_allow_html=True)
with col4:
    status_badge = '<span class="badge badge-teal">● Live</span>' if st.session_state.rag_ready \
                   else '<span class="badge badge-coral">● Idle</span>'
    st.markdown(f'<div class="stat-pill">{status_badge}</div>', unsafe_allow_html=True)

st.markdown("---")

# ── Chat window ──────────────────────────────────────────────────────────────
if not st.session_state.rag_ready:
    st.markdown("""
    <div style="text-align:center;padding:3rem 1rem;">
        <div style="font-size:3.5rem;margin-bottom:1rem;">📂</div>
        <div style="font-family:'Syne',sans-serif;font-size:1.4rem;font-weight:700;color:#e8eaf6;margin-bottom:.6rem;">
            No Document Loaded
        </div>
        <div style="color:#7b82a8;font-size:.92rem;max-width:380px;margin:auto;line-height:1.6;">
            Upload a <strong style="color:#7c6af7;">PDF</strong> or
            <strong style="color:#4fd1c5;">TXT</strong> file in the sidebar,
            then click <strong style="color:#f7746a;">Build RAG Pipeline</strong> to start chatting.
        </div>
    </div>
    """, unsafe_allow_html=True)
else:
    # Render existing messages
    if st.session_state.messages:
        st.markdown('<div class="chat-wrap">', unsafe_allow_html=True)
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                st.markdown(f"""
                <div class="bubble bubble-user">
                    <div class="bubble-label label-user">👤 You</div>
                    {msg["content"]}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="bubble bubble-bot">
                    <div class="bubble-label label-bot">🧠 DocuMind</div>
                    {msg["content"]}
                </div>
                """, unsafe_allow_html=True)

                # Show sources if available
                if "sources" in msg and msg["sources"]:
                    with st.expander(f"📚 View {len(msg['sources'])} source chunk(s)"):
                        for i, src in enumerate(msg["sources"], 1):
                            st.markdown(f"""
                            <div class="source-card">
                                <span class="source-num">#{i}</span>{src[:380]}{'…' if len(src) > 380 else ''}
                            </div>
                            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="text-align:center;padding:2.5rem 1rem;">
            <div style="font-size:2.8rem;margin-bottom:.8rem;">💡</div>
            <div style="font-family:'Syne',sans-serif;font-size:1.2rem;font-weight:700;color:#e8eaf6;margin-bottom:.5rem;">
                Pipeline Ready!
            </div>
            <div style="color:#7b82a8;font-size:.9rem;">Ask your first question below.</div>
        </div>
        """, unsafe_allow_html=True)

    # ── Input row ──
    st.markdown("---")
    col_inp, col_btn = st.columns([5, 1])
    with col_inp:
        question = st.text_input(
            "",
            placeholder="💬  Ask anything about your document…",
            label_visibility="collapsed",
            key="question_input",
        )
    with col_btn:
        ask_clicked = st.button("Send ➤", use_container_width=True)

    # ── Handle query ──
    if ask_clicked and question.strip():
        st.session_state.messages.append({"role": "user", "content": question})

        with st.spinner("🔍 Searching document & generating answer…"):
            try:
                chunks_retrieved = st.session_state.retriever.invoke(question)
                context = "\n".join([c.page_content for c in chunks_retrieved])
                response = st.session_state.chain.invoke({"context": context, "question": question})
                answer = response.content
                sources = [c.page_content for c in chunks_retrieved]
            except Exception as e:
                answer = f"❌ Error: {e}"
                sources = []

        st.session_state.messages.append({"role": "assistant", "content": answer, "sources": sources})
        st.rerun()

    # ── Suggested questions ──
    if not st.session_state.messages:
        st.markdown("""
        <div style="margin-top:1rem;">
            <div style="font-size:.75rem;text-transform:uppercase;letter-spacing:.12em;color:#7b82a8;margin-bottom:.75rem;">
                💡 Try asking…
            </div>
        </div>
        """, unsafe_allow_html=True)
        suggestions = [
            "📝 Summarise the main points",
            "🔍 What is the key conclusion?",
            "📊 List any statistics mentioned",
            "❓ What topics does this cover?",
        ]
        cols = st.columns(2)
        for i, sug in enumerate(suggestions):
            with cols[i % 2]:
                if st.button(sug, key=f"sug_{i}", use_container_width=True):
                    q = sug.split(" ", 1)[1]
                    st.session_state.messages.append({"role": "user", "content": q})
                    with st.spinner("🔍 Thinking…"):
                        try:
                            chunks_retrieved = st.session_state.retriever.invoke(q)
                            context = "\n".join([c.page_content for c in chunks_retrieved])
                            response = st.session_state.chain.invoke({"context": context, "question": q})
                            answer = response.content
                            sources = [c.page_content for c in chunks_retrieved]
                        except Exception as e:
                            answer = f"❌ Error: {e}"
                            sources = []
                    st.session_state.messages.append({"role": "assistant", "content": answer, "sources": sources})
                    st.rerun()