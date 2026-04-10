# Quick Reference Guide

## Essential Commands

### Setup & Installation
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate              # Windows
source venv/bin/activate           # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Update dependencies
pip install -r requirements.txt --upgrade
```

### Running the Application
```bash
# Standard run
streamlit run app.py

# Run on specific port
streamlit run app.py --server.port 8502

# Run with debug logging
streamlit run app.py --logger.level=debug

# Run with no browser auto-open
streamlit run app.py --server.headless true
```

### Configuration
```bash
# Copy template to create .env
cp .env.example .env

# Edit .env with your API keys
# Then restart Streamlit
```

### Dependency Management
```bash
# List installed packages
pip list

# Check specific package
pip show google-generativeai

# Upgrade specific package
pip install --upgrade google-generativeai

# Install from requirements
pip install -r requirements.txt

# Generate requirements from current environment
pip freeze > requirements.txt
```

## Workflow Examples

### Example 1: First Time Setup
```bash
# 1. Navigate to project
cd PROJECT_28_RAG_ASSISTANT

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure API keys
cp .env.example .env
# Edit .env with your keys

# 5. Run application
streamlit run app.py
```

### Example 2: Upload and Query Documents
```
1. Open http://localhost:8501
2. In sidebar, click "Upload" tab
3. Select PDF files or ZIP archive
4. Click "Process PDFs" or "Process ZIP"
5. Wait for processing to complete
6. Enter research question in main area
7. Click "🚀 Search & Synthesize"
8. View results and optionally generate report
```

### Example 3: Generate Research Report
```
1. Upload documents (see Example 2)
2. Enter research question
3. Check "Generate Report" checkbox
4. Click "🚀 Search & Synthesize"
5. Click "📥 Download Report" when ready
```

## File Structure Quick Reference

```
PROJECT_28_RAG_ASSISTANT/
├── app.py                          # Main application
├── config.py                       # Configuration
├── requirements.txt                # Dependencies
├── .env                           # API keys (DO NOT COMMIT)
├── .env.example                   # Template
├── SETUP_GUIDE.md                 # Setup instructions
├── TROUBLESHOOTING.md             # Common issues
├── QUICK_REFERENCE.md             # This file
├── src/
│   ├── __init__.py
│   ├── document_processor.py       # PDF → Chunks
│   ├── embeddings.py              # Text → Vectors
│   ├── vector_store.py            # Pinecone integration
│   ├── retrieval.py               # Search & reranking
│   ├── synthesis.py               # Answer generation
│   └── report_generator.py        # Report creation
└── data/
    ├── uploads/                   # Uploaded PDFs
    └── indexes/                   # Generated data
```

## Configuration Quick Reference

### Key Settings in `config.py`

```python
# Chunking
CHUNK_SIZE = 1000              # Size of text chunks
CHUNK_OVERLAP = 200            # Overlap between chunks
HIERARCHICAL_CHUNK_SIZE = 3000 # Larger chunks for summaries

# Retrieval
TOP_K_RETRIEVAL = 20           # Initial retrieval count
TOP_K_RERANKED = 5             # Final results after reranking
TOP_DOCUMENTS = 5              # Results per document
HYBRID_SEARCH_WEIGHT = 0.5     # Dense vs sparse balance

# Processing
BATCH_SIZE = 32                # Embedding batch size
MAX_DOCUMENTS = 100            # Max documents to process
```

## API Provider Quick Reference

### Gemini (Google)
- **Embeddings**: `models/embedding-001` (768-dim)
- **LLM**: `gemini-pro`
- **Get Key**: https://makersuite.google.com/app/apikey
- **Pricing**: Free tier available

### Pinecone
- **Index**: Serverless, cosine similarity
- **Get Key**: https://app.pinecone.io
- **Optional**: System works without it
- **Pricing**: Free tier available

### Cohere
- **Model**: `rerank-english-v2.0`
- **Get Key**: https://dashboard.cohere.com
- **Optional**: System works without it
- **Pricing**: Free tier available

## Keyboard Shortcuts (Streamlit)

- `C` - Clear cache
- `R` - Rerun script
- `Ctrl+C` - Stop server (in terminal)

## Environment Variables

```bash
# Required
GEMINI_API_KEY=<your-key>

# Optional but recommended
EMBEDDING_PROVIDER=gemini
LLM_PROVIDER=gemini
PINECONE_API_KEY=<your-key>
PINECONE_ENVIRONMENT=us-east-1
COHERE_API_KEY=<your-key>
```

## Debugging Tips

### Check if virtual environment is active
```bash
# Should show (venv) in prompt
which python  # macOS/Linux - should show venv path
where python  # Windows - should show venv path
```

### Verify API keys are loaded
```python
# In Python shell
import os
from dotenv import load_dotenv
load_dotenv()
print(os.getenv("GEMINI_API_KEY"))  # Should print your key
```

### Check installed packages
```bash
pip list | grep -E "streamlit|langchain|google"
```

### View Streamlit logs
```bash
# Logs are in ~/.streamlit/logs/
# Windows: %USERPROFILE%\.streamlit\logs\
# macOS/Linux: ~/.streamlit/logs/
```

## Common Errors & Quick Fixes

| Error | Quick Fix |
|-------|-----------|
| `ModuleNotFoundError` | `pip install -r requirements.txt` |
| `API Key Not Configured` | Create `.env` from `.env.example` |
| `Port already in use` | `streamlit run app.py --server.port 8502` |
| `Pinecone failed` | Non-critical; system continues |
| `Rate limit exceeded` | Wait a few minutes, reduce batch size |
| `PDF upload fails` | Check file is valid PDF, not corrupted |

## Performance Tuning

### For Large Document Collections
```python
# In config.py
CHUNK_SIZE = 500              # Smaller chunks
BATCH_SIZE = 16               # Smaller batches
TOP_K_RETRIEVAL = 10          # Fewer initial results
```

### For Fast Responses
```python
# In config.py
CHUNK_SIZE = 2000             # Larger chunks
TOP_K_RETRIEVAL = 5           # Fewer results
HYBRID_SEARCH_WEIGHT = 0.7    # Favor dense search
```

### For Better Quality
```python
# In config.py
CHUNK_SIZE = 1000             # Balanced
TOP_K_RETRIEVAL = 30          # More results
TOP_K_RERANKED = 10           # More reranked results
```

## Useful Links

- **Gemini API**: https://ai.google.dev
- **Pinecone Docs**: https://docs.pinecone.io
- **Cohere Docs**: https://docs.cohere.com
- **Streamlit Docs**: https://docs.streamlit.io
- **LangChain Docs**: https://python.langchain.com
