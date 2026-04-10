# Setup Guide - Multi-Document RAG Research Assistant

## Prerequisites
- Python 3.8+
- Virtual environment (recommended)

## Installation Steps

### 1. Clone/Setup Project
```bash
cd PROJECT_28_RAG_ASSISTANT
```

### 2. Create Virtual Environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Keys
Copy `.env.example` to `.env` and fill in your API keys:
```bash
cp .env.example .env
```

Edit `.env` with your credentials:
- **GEMINI_API_KEY**: Get from [Google AI Studio](https://makersuite.google.com/app/apikey)
- **PINECONE_API_KEY**: Get from [Pinecone Console](https://app.pinecone.io)
- **COHERE_API_KEY**: Get from [Cohere Dashboard](https://dashboard.cohere.com)

### 5. Run Application
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## Features

### Document Upload
- Upload single or multiple PDF files
- Or upload a ZIP archive containing PDFs
- Automatic text extraction and chunking

### Research Query
- Enter research questions
- Choose search type: Hybrid, Semantic, or Per-Document
- Adjust retrieval parameters

### Synthesis & Analysis
- Cross-document synthesis using Gemini
- Identify agreements between documents
- Detect contradictions
- Generate research reports (DOCX format)

## Troubleshooting

### Import Errors
If you see import errors, ensure all dependencies are installed:
```bash
pip install -r requirements.txt --upgrade
```

### API Key Issues
- Verify `.env` file exists in project root
- Check API keys are valid and have appropriate permissions
- Ensure environment variables are loaded (restart Streamlit if changed)

### Pinecone Connection
- If Pinecone is unavailable, the system runs in mock mode
- Vector search will still work with semantic search
- Reranking requires Cohere API

## Project Structure
```
PROJECT_28_RAG_ASSISTANT/
├── app.py                 # Main Streamlit application
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── .env                   # API keys (DO NOT COMMIT)
├── .env.example          # Template for .env
├── src/
│   ├── document_processor.py    # PDF processing
│   ├── embeddings.py            # Embedding generation
│   ├── vector_store.py          # Pinecone integration
│   ├── retrieval.py             # Hybrid search & reranking
│   ├── synthesis.py             # Cross-document synthesis
│   └── report_generator.py      # Report generation
└── data/
    ├── uploads/          # Uploaded PDF files
    └── indexes/          # Generated indexes & reports
```

## API Providers

### Gemini (Primary)
- Embeddings: `models/embedding-001` (768-dimensional)
- LLM: `gemini-pro`
- Free tier available

### Pinecone (Vector Database)
- Serverless index
- Cosine similarity search
- Optional (system works without it)

### Cohere (Reranking)
- Rerank model: `rerank-english-v2.0`
- Improves retrieval quality
- Optional (system works without it)

## Performance Tips

1. **Chunk Size**: Adjust `CHUNK_SIZE` in `config.py` (default: 1000)
2. **Retrieval**: Increase `TOP_K_RETRIEVAL` for more comprehensive results
3. **Reranking**: Use `TOP_K_RERANKED` to limit final results
4. **Batch Processing**: Adjust `BATCH_SIZE` for embedding generation

## Security Notes

- Never commit `.env` file to version control
- Use `.env.example` as template for sharing configuration
- Rotate API keys regularly
- Use environment-specific keys for development/production
