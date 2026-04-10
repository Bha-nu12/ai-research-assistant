import streamlit as st
import os
import json
from pathlib import Path
from datetime import datetime
import zipfile
import tempfile
from dotenv import load_dotenv
import base64

load_dotenv()

st.set_page_config(
    page_title="AI Research Assistant Pro",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add background image
def add_bg_image():
    bg_image = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800;900&family=Inter:wght@300;400;600;700&family=Playfair+Display:wght@700;800;900&display=swap');
        
        * {
            font-family: 'Poppins', 'Inter', sans-serif;
        }
        
        .stApp {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 25%, #7e22ce 50%, #ec4899 75%, #f97316 100%);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
            background-attachment: fixed;
        }
        
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        /* Main container */
        .main {
            background: rgba(255, 255, 255, 0.99);
            border-radius: 25px;
            padding: 40px;
            box-shadow: 0 25px 80px rgba(0, 0, 0, 0.4);
            animation: slideIn 0.8s ease-out;
            backdrop-filter: blur(10px);
        }
        
        .main p, .main span, .main div {
            color: #0f172a !important;
        }
        
        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        /* Sidebar styling */
        .sidebar .sidebar-content {
            background: linear-gradient(135deg, rgba(30, 60, 114, 0.95) 0%, rgba(42, 82, 152, 0.95) 100%);
            border-radius: 20px;
            padding: 25px;
            backdrop-filter: blur(10px);
        }
        
        /* Sidebar - FORCE ALL TEXT WHITE */
        section[data-testid="stSidebar"] * {
            color: #ffffff !important;
        }
        
        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3,
        section[data-testid="stSidebar"] h4,
        section[data-testid="stSidebar"] h5,
        section[data-testid="stSidebar"] h6,
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] span,
        section[data-testid="stSidebar"] div,
        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] small {
            color: #ffffff !important;
            text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
        }
        
        /* Headers */
        h1 {
            font-family: 'Playfair Display', serif;
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-size: 3.8em;
            font-weight: 900;
            text-align: center;
            margin-bottom: 10px;
            animation: fadeInDown 1s ease-out;
            letter-spacing: -1px;
        }
        
        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-40px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        h2 {
            font-family: 'Playfair Display', serif;
            color: #0f172a;
            font-size: 2.2em;
            margin-top: 30px;
            margin-bottom: 20px;
            border-left: 6px solid #ec4899;
            padding-left: 20px;
            animation: slideInLeft 0.6s ease-out;
            font-weight: 800;
            letter-spacing: -0.5px;
        }
        
        h3 {
            font-family: 'Poppins', sans-serif;
            color: #0f172a;
            font-size: 1.6em;
            font-weight: 700;
            letter-spacing: -0.3px;
        }
        
        @keyframes slideInLeft {
            from {
                opacity: 0;
                transform: translateX(-40px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
        
        /* Buttons */
        .stButton > button {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #7e22ce 100%);
            color: white;
            border: none;
            border-radius: 15px;
            padding: 15px 35px;
            font-weight: bold;
            font-size: 1.1em;
            cursor: pointer;
            transition: all 0.4s ease;
            box-shadow: 0 8px 25px rgba(30, 60, 114, 0.4);
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .stButton > button:hover {
            transform: translateY(-5px) scale(1.02);
            box-shadow: 0 15px 40px rgba(30, 60, 114, 0.6);
            background: linear-gradient(135deg, #2a5298 0%, #7e22ce 50%, #ec4899 100%);
        }
        
        .stButton > button:active {
            transform: translateY(-2px);
        }
        
        /* Input fields */
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea,
        .stSelectbox > div > div > select,
        .stNumberInput > div > div > input {
            border: 3px solid #2a5298;
            border-radius: 12px;
            padding: 15px;
            font-size: 1.05em;
            transition: all 0.3s ease;
            background: rgba(255, 255, 255, 1) !important;
            color: #000000 !important;
        }
        
        .stTextInput > div > div > input:focus,
        .stTextArea > div > div > textarea:focus,
        .stSelectbox > div > div > select:focus,
        .stNumberInput > div > div > input:focus {
            border-color: #ec4899;
            box-shadow: 0 0 20px rgba(236, 72, 153, 0.4);
            background: white;
        }
        
        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 15px;
            background: rgba(255, 255, 255, 0.1);
            padding: 10px;
            border-radius: 15px;
        }
        
        .stTabs [data-baseweb="tab"] {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: white;
            border-radius: 12px;
            padding: 12px 25px;
            font-weight: bold;
            font-size: 1.05em;
            transition: all 0.3s ease;
        }
        
        .stTabs [data-baseweb="tab"]:hover {
            transform: scale(1.08);
            box-shadow: 0 6px 20px rgba(30, 60, 114, 0.4);
        }
        
        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #ec4899 0%, #f97316 100%);
            box-shadow: 0 8px 25px rgba(236, 72, 153, 0.5);
        }
        
        /* Metrics */
        .stMetric {
            background: linear-gradient(135deg, rgba(30, 60, 114, 0.15) 0%, rgba(236, 72, 153, 0.15) 100%);
            border-radius: 18px;
            padding: 25px;
            border: 2px solid #2a5298;
            animation: fadeIn 0.8s ease-out;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }
        
        .stMetric:hover {
            transform: translateY(-8px);
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15);
            border-color: #ec4899;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        /* Expanders */
        .stExpander {
            border: 3px solid #2a5298;
            border-radius: 15px;
            background: linear-gradient(135deg, rgba(30, 60, 114, 0.08) 0%, rgba(236, 72, 153, 0.08) 100%);
            transition: all 0.3s ease;
        }
        
        .stExpander:hover {
            border-color: #ec4899;
            box-shadow: 0 8px 20px rgba(236, 72, 153, 0.2);
        }
        
        .stExpander > div > div > button {
            color: #0f172a !important;
            font-weight: bold;
            font-size: 1.05em;
            font-family: 'Poppins', sans-serif;
        }
        
        /* Alert boxes */
        .stInfo {
            background: linear-gradient(135deg, rgba(59, 130, 246, 0.2) 0%, rgba(96, 165, 250, 0.2) 100%);
            border-left: 6px solid #3b82f6;
            border-radius: 12px;
            padding: 18px;
            animation: slideUp 0.5s ease-out;
        }
        
        .stSuccess {
            background: linear-gradient(135deg, rgba(34, 197, 94, 0.2) 0%, rgba(74, 222, 128, 0.2) 100%);
            border-left: 6px solid #22c55e;
            border-radius: 12px;
            padding: 18px;
            animation: slideUp 0.5s ease-out;
        }
        
        .stWarning {
            background: linear-gradient(135deg, rgba(251, 146, 60, 0.2) 0%, rgba(253, 224, 71, 0.2) 100%);
            border-left: 6px solid #fb923c;
            border-radius: 12px;
            padding: 18px;
            animation: slideUp 0.5s ease-out;
        }
        
        .stError {
            background: linear-gradient(135deg, rgba(239, 68, 68, 0.2) 0%, rgba(248, 113, 113, 0.2) 100%);
            border-left: 6px solid #ef4444;
            border-radius: 12px;
            padding: 18px;
            animation: slideUp 0.5s ease-out;
        }
        
        @keyframes slideUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        /* File upload */
        .stFileUploadDropzone {
            border: 4px dashed #2a5298;
            border-radius: 18px;
            background: linear-gradient(135deg, rgba(30, 60, 114, 0.08) 0%, rgba(236, 72, 153, 0.08) 100%);
            transition: all 0.3s ease;
            padding: 30px;
        }
        
        .stFileUploadDropzone:hover {
            border-color: #ec4899;
            background: linear-gradient(135deg, rgba(30, 60, 114, 0.15) 0%, rgba(236, 72, 153, 0.15) 100%);
            transform: scale(1.02);
        }
        
        /* Subtitle */
        .subtitle {
            text-align: center;
            color: #0f172a;
            font-size: 1.5em;
            margin-bottom: 40px;
            animation: fadeIn 1.2s ease-out;
            font-weight: 600;
            letter-spacing: 0.3px;
            font-family: 'Inter', sans-serif;
        }
        
        /* Cards */
        .card {
            background: linear-gradient(135deg, rgba(30, 60, 114, 0.12) 0%, rgba(236, 72, 153, 0.12) 100%);
            border-radius: 18px;
            padding: 25px;
            margin: 20px 0;
            border: 2px solid #2a5298;
            transition: all 0.4s ease;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
        }
        
        .card:hover {
            transform: translateY(-8px);
            box-shadow: 0 15px 40px rgba(30, 60, 114, 0.25);
            border-color: #ec4899;
            background: linear-gradient(135deg, rgba(30, 60, 114, 0.18) 0%, rgba(236, 72, 153, 0.18) 100%);
        }
        
        /* Checkbox */
        .stCheckbox > label {
            color: #0f172a !important;
            font-weight: 600;
            font-size: 1.05em;
            font-family: 'Poppins', sans-serif;
        }
        
        /* Slider */
        .stSlider > div > div > div {
            background: linear-gradient(90deg, #1e3c72 0%, #ec4899 100%);
        }
        
        /* Spinner */
        .stSpinner > div {
            border-color: #2a5298;
            border-right-color: #ec4899;
        }
        
        /* Footer */
        .footer {
            text-align: center;
            color: #ffffff !important;
            font-weight: bold;
            font-size: 1.1em;
            margin-top: 50px;
            padding: 20px;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 15px;
            animation: fadeIn 1.5s ease-out;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
        }
        
        /* Divider */
        hr {
            border: 2px solid rgba(30, 60, 114, 0.3);
            border-radius: 10px;
            margin: 30px 0;
        }
        
        /* Sidebar text */
        .sidebar .sidebar-content h2,
        .sidebar .sidebar-content h3 {
            color: #ffffff !important;
            font-family: 'Poppins', sans-serif;
            font-weight: 700;
            text-shadow: 0 2px 6px rgba(0, 0, 0, 0.4);
        }
        
        .sidebar .sidebar-content p,
        .sidebar .sidebar-content span,
        .sidebar .sidebar-content div,
        .sidebar .sidebar-content label,
        .sidebar .sidebar-content button {
            color: #ffffff !important;
            font-family: 'Inter', sans-serif;
            font-weight: 500;
            text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
        }
        
        .sidebar .sidebar-content .stRadio > label,
        .sidebar .sidebar-content .stCheckbox > label,
        .sidebar .sidebar-content .stSelectbox label,
        .sidebar .sidebar-content .stNumberInput label,
        .sidebar .sidebar-content .stSlider label {
            color: #ffffff !important;
            font-weight: 600 !important;
            text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
        }
        
        .sidebar .sidebar-content .stMetric {
            color: #ffffff !important;
        }
        
        .sidebar .sidebar-content .stMetric label,
        .sidebar .sidebar-content .stMetric span {
            color: #ffffff !important;
        }
        
        /* Radio buttons */
        .stRadio > label {
            color: #0f172a !important;
            font-weight: 600;
            font-family: 'Poppins', sans-serif;
        }
        
        /* Selectbox */
        .stSelectbox label {
            color: #0f172a !important;
            font-weight: 600;
            font-family: 'Poppins', sans-serif;
        }
        
        /* Text and labels */
        label {
            color: #0f172a !important;
            font-family: 'Poppins', sans-serif;
            font-weight: 600;
        }
        
        .stTextInput label,
        .stTextArea label,
        .stSelectbox label,
        .stNumberInput label,
        .stSlider label {
            color: #0f172a !important;
            font-weight: 600;
        }
        
        /* General text */
        body, p, span, div, li {
            color: #0f172a !important;
            font-family: 'Inter', 'Poppins', sans-serif;
        }
    </style>
    """
    st.markdown(bg_image, unsafe_allow_html=True)

add_bg_image()

# Header
st.markdown("<h1>🚀 AI Research Assistant Pro</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Advanced Multi-Document Analysis with AI-Powered Synthesis</p>", unsafe_allow_html=True)

llm_provider = os.getenv("LLM_PROVIDER", "openai").lower()

if llm_provider == "gemini":
    api_key_configured = os.getenv("GEMINI_API_KEY")
else:
    api_key_configured = os.getenv("OPENAI_API_KEY")

if not api_key_configured:
    st.error("""
    ❌ **API Keys Not Configured**
    
    Please create a `.env` file with your API keys:
    
    For Gemini:
    ```
    GEMINI_API_KEY=your-gemini-key
    EMBEDDING_PROVIDER=gemini
    LLM_PROVIDER=gemini
    PINECONE_API_KEY=your-key
    PINECONE_ENVIRONMENT=us-east-1
    COHERE_API_KEY=your-key
    ```
    
    Then restart the app with: `streamlit run app.py`
    """)
    st.stop()

try:
    from src.document_processor import DocumentProcessor
    from src.embeddings import EmbeddingsManager
    from src.vector_store import VectorStore
    from src.retrieval import RetrieverWithReranking
    from src.synthesis import CrossDocumentSynthesis
    from src.report_generator import ResearchReportGenerator
except Exception as e:
    st.error(f"Error loading modules: {e}")
    st.info("Make sure all dependencies are installed: `pip install -r requirements.txt`")
    st.stop()

UPLOAD_FOLDER = "data/uploads"
INDEX_FOLDER = "data/indexes"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(INDEX_FOLDER, exist_ok=True)

if "processor" not in st.session_state:
    st.session_state.processor = DocumentProcessor()
    st.session_state.embeddings_manager = EmbeddingsManager()
    st.session_state.vector_store = VectorStore()
    st.session_state.retriever = None
    st.session_state.synthesis = CrossDocumentSynthesis()
    st.session_state.report_gen = ResearchReportGenerator()
    st.session_state.collection_data = None
    st.session_state.documents = []
    st.session_state.search_history = []

# Sidebar
with st.sidebar:
    st.markdown("<h2 style='color: white; text-align: center; font-size: 1.8em;'>📋 Collection Manager</h2>", unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["📤 Upload", "📊 Manage", "📈 Analytics", "⚙️ Settings"])
    
    with tab1:
        st.subheader("📤 Upload Documents")
        
        upload_type = st.radio("Upload type:", ["PDF Files", "ZIP Archive"], label_visibility="collapsed")
        
        if upload_type == "PDF Files":
            uploaded_files = st.file_uploader(
                "Select PDF files",
                type="pdf",
                accept_multiple_files=True
            )
            
            if uploaded_files and st.button("🚀 Process PDFs", use_container_width=True):
                with st.spinner("⏳ Processing documents..."):
                    try:
                        pdf_paths = []
                        for uploaded_file in uploaded_files:
                            file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
                            with open(file_path, "wb") as f:
                                f.write(uploaded_file.getbuffer())
                            pdf_paths.append(file_path)
                        
                        collection_data = st.session_state.processor.process_pdf_collection(pdf_paths)
                        st.session_state.collection_data = collection_data
                        
                        chunks = collection_data["chunks"]
                        chunks_with_embeddings = st.session_state.embeddings_manager.embed_chunks(chunks)
                        
                        st.session_state.vector_store.upsert_chunks(chunks_with_embeddings)
                        
                        st.session_state.retriever = RetrieverWithReranking(
                            st.session_state.vector_store,
                            st.session_state.embeddings_manager
                        )
                        st.session_state.retriever.build_bm25_index(chunks)
                        
                        st.session_state.documents = [doc["name"] for doc in collection_data["documents"]]
                        
                        metadata_path = os.path.join(INDEX_FOLDER, "collection_metadata.json")
                        st.session_state.processor.save_collection_metadata(collection_data, metadata_path)
                        
                        st.success(f"✅ Processed {len(pdf_paths)} documents with {len(chunks)} chunks")
                    except Exception as e:
                        st.error(f"Error processing documents: {e}")
        
        else:
            zip_file = st.file_uploader("Select ZIP archive", type="zip")
            
            if zip_file and st.button("🚀 Process ZIP", use_container_width=True):
                with st.spinner("⏳ Processing ZIP archive..."):
                    try:
                        with tempfile.TemporaryDirectory() as temp_dir:
                            with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                                zip_ref.extractall(temp_dir)
                            
                            pdf_paths = list(Path(temp_dir).rglob("*.pdf"))
                            
                            if pdf_paths:
                                collection_data = st.session_state.processor.process_pdf_collection(
                                    [str(p) for p in pdf_paths]
                                )
                                st.session_state.collection_data = collection_data
                                
                                chunks = collection_data["chunks"]
                                chunks_with_embeddings = st.session_state.embeddings_manager.embed_chunks(chunks)
                                
                                st.session_state.vector_store.upsert_chunks(chunks_with_embeddings)
                                
                                st.session_state.retriever = RetrieverWithReranking(
                                    st.session_state.vector_store,
                                    st.session_state.embeddings_manager
                                )
                                st.session_state.retriever.build_bm25_index(chunks)
                                
                                st.session_state.documents = [doc["name"] for doc in collection_data["documents"]]
                                
                                metadata_path = os.path.join(INDEX_FOLDER, "collection_metadata.json")
                                st.session_state.processor.save_collection_metadata(collection_data, metadata_path)
                                
                                st.success(f"✅ Processed {len(pdf_paths)} documents")
                            else:
                                st.error("No PDF files found in ZIP")
                    except Exception as e:
                        st.error(f"Error processing ZIP: {e}")
    
    with tab2:
        st.subheader("📊 Collection Status")
        
        if st.session_state.collection_data:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("📄 Documents", st.session_state.collection_data["total_documents"])
            with col2:
                st.metric("📦 Chunks", st.session_state.collection_data["total_chunks"])
            with col3:
                st.metric("✅ Indexed", "Yes" if st.session_state.retriever else "No")
            
            st.subheader("📚 Documents in Collection")
            for doc in st.session_state.collection_data["documents"]:
                st.write(f"📄 {doc['name']} ({doc['chunk_count']} chunks)")
        else:
            st.info("No documents uploaded yet")
    
    with tab3:
        st.subheader("📈 Collection Analytics")
        
        if st.session_state.collection_data:
            try:
                stats = st.session_state.vector_store.get_index_stats()
                st.json(stats)
            except Exception as e:
                st.info(f"Analytics not available: {e}")
        else:
            st.info("Upload documents to see analytics")
    
    with tab4:
        st.subheader("⚙️ Settings")
        
        st.write("**API Configuration**")
        st.write(f"Provider: {llm_provider.upper()}")
        st.write(f"Status: {'✅ Connected' if api_key_configured else '❌ Not Connected'}")
        
        st.write("**Search Settings**")
        default_top_k = st.slider("Default results to retrieve:", 5, 50, 10)
        
        st.write("**Export Settings**")
        if st.button("📥 Export Collection Metadata"):
            if st.session_state.collection_data:
                metadata_json = json.dumps(st.session_state.collection_data, indent=2)
                st.download_button(
                    label="Download Metadata",
                    data=metadata_json,
                    file_name="collection_metadata.json",
                    mime="application/json"
                )
            else:
                st.warning("No collection data to export")

# Main content
st.markdown("<h2>🔍 Research Query</h2>", unsafe_allow_html=True)

if st.session_state.retriever:
    col1, col2 = st.columns([3, 1])
    
    with col1:
        query = st.text_area(
            "Enter your research question:",
            placeholder="e.g., What are the key differences between these companies' strategies?",
            height=120,
            label_visibility="collapsed"
        )
    
    with col2:
        st.write("**Quick Templates**")
        if st.button("📝 Summarize"):
            query = "Provide a comprehensive summary of the main topics covered in these documents."
        if st.button("🔄 Compare"):
            query = "Compare and contrast the different perspectives presented in these documents."
        if st.button("❓ Key Points"):
            query = "What are the most important key points and takeaways from these documents?"
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        search_type = st.selectbox(
            "Search type:",
            ["Hybrid Search", "Semantic Search", "Per-Document"],
            label_visibility="collapsed"
        )
    
    with col2:
        top_k = st.slider("Results:", 5, 50, 10, label_visibility="collapsed")
    
    with col3:
        generate_report = st.checkbox("📄 Report", value=False)
    
    with col4:
        show_chunks = st.checkbox("📚 Show Chunks", value=True)
    
    if st.button("🚀 Search & Synthesize", use_container_width=True):
        if query:
            st.session_state.search_history.append({
                "query": query,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "type": search_type
            })
            
            with st.spinner("🔄 Searching and synthesizing..."):
                try:
                    if search_type == "Hybrid Search":
                        results = st.session_state.retriever.retrieve_with_reranking(query, top_k)
                    elif search_type == "Semantic Search":
                        query_embedding = st.session_state.embeddings_manager.embed_query(query)
                        results = st.session_state.vector_store.search(query_embedding, top_k)
                    else:
                        results_by_doc = st.session_state.retriever.retrieve_from_documents(
                            query, st.session_state.documents
                        )
                        results = []
                        for doc_results in results_by_doc.values():
                            results.extend(doc_results)
                    
                    synthesis_result = st.session_state.synthesis.synthesize_answer(query, results)
                    agreements = st.session_state.synthesis.identify_agreements(query, results)
                    contradictions = st.session_state.synthesis.detect_contradictions(query, results)
                    
                    st.markdown("<h2>📊 Synthesis Results</h2>", unsafe_allow_html=True)
                    
                    st.markdown(f"<div class='card'>{synthesis_result['synthesis']}</div>", unsafe_allow_html=True)
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown("<h3 style='color: #22c55e;'>✅ Agreements</h3>", unsafe_allow_html=True)
                        if agreements:
                            for agreement in agreements:
                                st.write(f"• {agreement}")
                        else:
                            st.info("No agreements found")
                    
                    with col2:
                        st.markdown("<h3 style='color: #fb923c;'>⚠️ Contradictions</h3>", unsafe_allow_html=True)
                        if contradictions:
                            for contradiction in contradictions:
                                st.write(f"• {contradiction}")
                        else:
                            st.info("No contradictions found")
                    
                    if show_chunks:
                        st.markdown("<h2>📚 Retrieved Chunks</h2>", unsafe_allow_html=True)
                        for i, chunk in enumerate(results[:5], 1):
                            with st.expander(f"📄 Chunk {i} - {chunk.get('document', 'Unknown')} (Page {chunk.get('page', '?')})"):
                                st.write(chunk.get("content", ""))
                    
                    if generate_report:
                        st.markdown("<h2>📄 Generating Report...</h2>", unsafe_allow_html=True)
                        report_content = st.session_state.report_gen.generate_report(
                            query,
                            synthesis_result,
                            agreements,
                            contradictions,
                            st.session_state.documents
                        )
                        
                        report_path = os.path.join(INDEX_FOLDER, f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.docx")
                        st.session_state.report_gen.export_to_docx(
                            report_content,
                            query,
                            st.session_state.documents,
                            report_path
                        )
                        
                        with open(report_path, "rb") as f:
                            st.download_button(
                                label="📥 Download Report",
                                data=f.read(),
                                file_name=os.path.basename(report_path),
                                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                            )
                except Exception as e:
                    st.error(f"Error during synthesis: {e}")
        else:
            st.warning("Please enter a research question")
else:
    st.info("👈 Upload documents in the sidebar to start researching")

# Search History
if st.session_state.search_history:
    with st.expander("📜 Search History"):
        for i, search in enumerate(reversed(st.session_state.search_history[-10:]), 1):
            st.write(f"{i}. **{search['query'][:50]}...** ({search['type']}) - {search['timestamp']}")

st.markdown("---")
st.markdown("<div class='footer'>🚀 AI Research Assistant Pro | Built with LangChain, Pinecone, Cohere & Google Gemini ✨</div>", unsafe_allow_html=True)
