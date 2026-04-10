# EXECUTION GUIDE - Multi-Document RAG Research Assistant

## 🚀 QUICK START (5 minutes)

### Windows Users
```bash
cd PROJECT_28_RAG_ASSISTANT
run.bat
```

### Mac/Linux Users
```bash
cd PROJECT_28_RAG_ASSISTANT
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

---

## 📋 DETAILED SETUP INSTRUCTIONS

### Step 1: Prerequisites
- Python 3.10 or higher
- pip package manager
- API keys for:
  - OpenAI (GPT-4o)
  - Pinecone (vector database)
  - Cohere (reranking)

### Step 2: Clone/Download Project
```bash
cd c:\Users\Dell\Documents\KUNFU
# Project already created at: PROJECT_28_RAG_ASSISTANT
```

### Step 3: Create Virtual Environment
```bash
cd PROJECT_28_RAG_ASSISTANT
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Configure API Keys
1. Copy `.env.example` to `.env`
2. Edit `.env` with your API keys:
```
OPENAI_API_KEY=sk-...
PINECONE_API_KEY=...
PINECONE_ENVIRONMENT=us-east-1
COHERE_API_KEY=...
```

### Step 6: Launch Application
```bash
streamlit run app.py
```

Application opens at: `http://localhost:8501`

---

## 🎯 FIRST-TIME USAGE WORKFLOW

### Phase 1: Document Upload (5-10 minutes)

1. **Prepare Documents**
   - Gather PDF files (50+ recommended for full demo)
   - Or create a ZIP archive with PDFs
   - Ensure PDFs are text-extractable (not scanned images)

2. **Upload in Streamlit**
   - Click "Upload Documents" in left sidebar
   - Choose upload type: "PDF Files" or "ZIP Archive"
   - Select files/archive
   - Click "Process PDFs" or "Process ZIP"
   - Wait for completion (shows progress)

3. **Verify Processing**
   - Check "Collection Status" tab
   - Should show: Documents count, Chunks count, ✅ Indexed
   - View document list

### Phase 2: Run Sample Query (2-3 minutes)

1. **Enter Research Question**
   - Example: "What are the main themes across these documents?"
   - Or: "Identify contradictions between sources"

2. **Configure Search**
   - Search type: "Hybrid Search" (recommended)
   - Top K: 10 (default)
   - Check "Generate Report" if desired

3. **Execute Search**
   - Click "Search & Synthesize"
   - Wait for results (30-60 seconds)

4. **Review Results**
   - Read synthesis with citations
   - Check agreements section
   - Review contradictions
   - Expand retrieved chunks to see sources

### Phase 3: Generate Report (2-3 minutes)

1. **Enable Report Generation**
   - Check "Generate Report" checkbox before search

2. **Download Report**
   - After synthesis completes
   - Click "Download Report" button
   - Save Word document

3. **Review Report**
   - Open in Microsoft Word
   - Check formatting and citations
   - Add additional notes if needed

---

## 💡 EXAMPLE QUERIES BY USE CASE

### Academic Research
```
"Synthesize the main research findings across all papers. 
What methodologies are most common? Where do researchers disagree?"
```

### Legal Analysis
```
"Compare the legal precedents cited in these case documents. 
Which cases are cited most frequently? Are there conflicting interpretations?"
```

### Business Intelligence
```
"Analyze the competitive strategies described in these company reports. 
What are the key differences? Where do they have similar approaches?"
```

### Policy Analysis
```
"What are the policy recommendations across these government documents? 
Where is there consensus? What are the main areas of disagreement?"
```

### Literature Review
```
"Create a systematic review of this research topic. 
Identify the main themes, key findings, and research gaps."
```

---

## 🔧 CONFIGURATION TUNING

### For Better Quality Results
Edit `config.py`:
```python
TOP_K_RETRIEVAL = 30      # Retrieve more candidates
TOP_K_RERANKED = 5        # Keep top 5 after reranking
HYBRID_SEARCH_WEIGHT = 0.5 # Balance semantic + keyword
```

### For Faster Processing
```python
TOP_K_RETRIEVAL = 10      # Fewer candidates
TOP_K_RERANKED = 3        # Fewer final results
CHUNK_SIZE = 1500         # Larger chunks
```

### For More Detailed Analysis
```python
CHUNK_SIZE = 500          # Smaller chunks
CHUNK_OVERLAP = 200       # More overlap
HIERARCHICAL_CHUNK_SIZE = 2000
```

---

## 📊 SYSTEM ARCHITECTURE OVERVIEW

```
┌─────────────────────────────────────────────────────────┐
│         Multi-Document RAG Research Assistant           │
└─────────────────────────────────────────────────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
    ┌───▼────┐      ┌────▼────┐      ┌────▼────┐
    │Document│      │Embedding│      │ Vector  │
    │Processor│      │ Manager │      │  Store  │
    └────┬────┘      └────┬────┘      └────┬────┘
         │                │                │
         └────────────────┼────────────────┘
                          │
                    ┌─────▼─────┐
                    │ Retriever  │
                    │(Hybrid+    │
                    │Reranking)  │
                    └─────┬─────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
    ┌───▼────┐      ┌────▼────┐      ┌────▼────┐
    │Synthesis│      │Agreement │      │Report   │
    │Engine   │      │Detector  │      │Generator│
    └────┬────┘      └────┬────┘      └────┬────┘
         │                │                │
         └────────────────┼────────────────┘
                          │
                    ┌─────▼──────┐
                    │  Streamlit  │
                    │     UI      │
                    └─────────────┘
```

---

## 🐛 TROUBLESHOOTING

### Problem: "ModuleNotFoundError"
**Solution**:
```bash
# Ensure virtual environment is activated
venv\Scripts\activate
# Reinstall dependencies
pip install -r requirements.txt
```

### Problem: "API Key Error"
**Solution**:
1. Verify `.env` file exists in project root
2. Check API keys have no extra spaces
3. Verify keys are valid in respective dashboards
4. Restart Streamlit: `Ctrl+C` then `streamlit run app.py`

### Problem: "Slow Processing"
**Solution**:
1. Reduce CHUNK_SIZE in config.py
2. Use fewer documents initially
3. Check internet connection
4. Verify API rate limits not exceeded

### Problem: "Low Quality Results"
**Solution**:
1. Increase TOP_K_RETRIEVAL
2. Adjust HYBRID_SEARCH_WEIGHT
3. Check document quality
4. Try more specific queries

### Problem: "Memory Error"
**Solution**:
1. Process documents in smaller batches
2. Reduce CHUNK_SIZE
3. Close other applications
4. Use machine with more RAM

---

## 📈 PERFORMANCE METRICS

### Expected Performance
- Document processing: ~10-20 PDFs per minute
- Query response: 30-60 seconds (including reranking)
- Report generation: 20-30 seconds
- Retrieval precision: 70-85% (with reranking)

### Optimization Tips
- Pre-index all documents upfront
- Use hybrid search for speed
- Reduce top_k for faster processing
- Batch queries for efficiency

---

## 🎓 LEARNING RESOURCES

### Understanding RAG
- Retrieval: Finding relevant documents
- Augmented: Using retrieved docs to improve answers
- Generation: Creating synthesis with citations

### Key Components
1. **Document Processor**: Extracts text, creates chunks
2. **Embeddings**: Converts text to vectors
3. **Vector Store**: Stores and searches embeddings
4. **Retriever**: Finds relevant chunks
5. **Synthesis**: Combines information with citations
6. **Report Generator**: Creates formatted output

### Best Practices
- Use high-quality PDFs
- Ask specific questions
- Verify citations
- Review generated reports
- Validate contradictions

---

## 🚀 ADVANCED USAGE

### Batch Processing
```python
from src.document_processor import DocumentProcessor
from src.synthesis import CrossDocumentSynthesis

processor = DocumentProcessor()
synthesis = CrossDocumentSynthesis()

# Process multiple queries
queries = ["Question 1?", "Question 2?", "Question 3?"]
for query in queries:
    result = synthesis.synthesize_answer(query, chunks)
    print(result)
```

### Custom Filtering
```python
# Filter by document
results = retriever.retrieve_from_documents(
    query="Your question",
    document_names=["Document1.pdf", "Document2.pdf"]
)
```

### Export to Database
```python
import json
with open("results.json", "w") as f:
    json.dump(synthesis_result, f, indent=2)
```

---

## 📞 SUPPORT

### Common Issues
- See Troubleshooting section above
- Check README.md for detailed documentation
- Review PROMPT_GUIDE.md for usage examples

### API Documentation
- OpenAI: https://platform.openai.com/docs
- Pinecone: https://docs.pinecone.io
- Cohere: https://docs.cohere.com

### Project Structure
```
PROJECT_28_RAG_ASSISTANT/
├── app.py                    # Main application
├── config.py                 # Configuration
├── requirements.txt          # Dependencies
├── .env                      # API keys (create this)
├── .env.example              # Template
├── run.bat                   # Quick start (Windows)
├── README.md                 # Documentation
├── PROMPT_GUIDE.md           # Usage guide
├── EXECUTION_GUIDE.md        # This file
└── src/
    ├── __init__.py
    ├── document_processor.py
    ├── embeddings.py
    ├── vector_store.py
    ├── retrieval.py
    ├── synthesis.py
    └── report_generator.py
```

---

## ✅ VERIFICATION CHECKLIST

Before running queries:
- [ ] Python 3.10+ installed
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] `.env` file created with API keys
- [ ] API keys are valid and have sufficient quota
- [ ] Streamlit running without errors
- [ ] Documents uploaded and indexed
- [ ] Collection status shows ✅ Indexed

---

## 🎉 YOU'RE READY!

Your Multi-Document RAG Research Assistant is now ready to use!

**Next Steps**:
1. Upload your document collection
2. Ask your first research question
3. Review the synthesis results
4. Generate a research report
5. Customize configuration as needed

Happy researching! 🚀

---

**Version**: 1.0.0
**Last Updated**: 2024
**Status**: Production Ready
