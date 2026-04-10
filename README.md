# 📚 Multi-Document RAG Research Assistant

A comprehensive AI-powered research assistant that processes multiple PDF documents and provides intelligent synthesis across document collections using Google Gemini API.

## ✨ Features

- **📄 Multi-Document Processing**: Upload and process multiple PDFs simultaneously
- **🔍 Intelligent Chunking**: Hierarchical text splitting for optimal context preservation
- **🔗 Hybrid Search**: Combines semantic and keyword-based retrieval
- **🤖 Cross-Document Synthesis**: AI-powered answer generation using Gemini
- **✅ Agreement Detection**: Identifies consensus points across documents
- **⚠️ Contradiction Detection**: Highlights conflicting information
- **📊 Research Reports**: Generate professional DOCX reports
- **🎯 Smart Reranking**: Cohere-powered result reranking for improved relevance
- **🔐 Secure API Management**: Environment-based configuration with no hardcoded keys

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- API Keys (free tiers available):
  - [Google Gemini](https://makersuite.google.com/app/apikey)
  - [Pinecone](https://app.pinecone.io) (optional)
  - [Cohere](https://dashboard.cohere.com) (optional)

### Installation (5 minutes)

```bash
# 1. Clone and navigate
git clone <repo-url>
cd PROJECT_28_RAG_ASSISTANT

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure API keys
cp .env.example .env
# Edit .env with your API keys

# 5. Run application
streamlit run app.py
```

**Access at**: http://localhost:8501

## 📖 Documentation

| Guide | Purpose |
|-------|---------|
| [Setup Guide](SETUP_GUIDE.md) | Detailed installation & configuration |
| [Quick Reference](QUICK_REFERENCE.md) | Common commands & workflows |
| [Troubleshooting](TROUBLESHOOTING.md) | Solutions to common issues |
| [Security Guide](SECURITY_GUIDE.md) | API key management & best practices |
| [Deployment Guide](DEPLOYMENT_GUIDE.md) | Production deployment options |

## 🏗️ Architecture

### Core Modules

```
src/
├── document_processor.py    # PDF → Text → Chunks
├── embeddings.py            # Text → Vectors (Gemini)
├── vector_store.py          # Vector storage (Pinecone)
├── retrieval.py             # Hybrid search & reranking
├── synthesis.py             # Cross-document synthesis (Gemini)
└── report_generator.py      # Report generation (Gemini)
```

### Data Flow

```
📄 PDF Upload
    ↓
📝 Text Extraction
    ↓
✂️ Chunking (1000 chars)
    ↓
🔢 Embedding (Gemini)
    ↓
📦 Vector Storage (Pinecone)
    ↓
🔍 Query Processing
    ├─→ Semantic Search (Dense)
    ├─→ Keyword Search (BM25)
    └─→ Hybrid Combination
    ↓
🎯 Reranking (Cohere)
    ↓
🤖 Synthesis (Gemini)
    ↓
📊 Report Generation
```

## ⚙️ Configuration

Edit `config.py` to customize behavior:

```python
# Chunking
CHUNK_SIZE = 1000              # Size of text chunks
CHUNK_OVERLAP = 200            # Overlap between chunks

# Retrieval
TOP_K_RETRIEVAL = 20           # Initial retrieval count
TOP_K_RERANKED = 5             # Final results after reranking
HYBRID_SEARCH_WEIGHT = 0.5     # Balance: 0.5 = equal, 0.7 = favor semantic

# Processing
BATCH_SIZE = 32                # Embedding batch size
```

## 🔑 API Providers

### Google Gemini (Primary)
- **Embeddings**: `models/embedding-001` (768-dimensional)
- **LLM**: `gemini-pro`
- **Get Key**: https://makersuite.google.com/app/apikey
- **Pricing**: Free tier available

### Pinecone (Vector Database)
- **Type**: Serverless vector database
- **Get Key**: https://app.pinecone.io
- **Status**: Optional (system works without it)
- **Pricing**: Free tier available

### Cohere (Reranking)
- **Model**: `rerank-english-v2.0`
- **Get Key**: https://dashboard.cohere.com
- **Status**: Optional (system works without it)
- **Pricing**: Free tier available

## 💡 Usage Examples

### Upload Documents
```
1. Open sidebar → "Upload" tab
2. Select PDF files or ZIP archive
3. Click "Process PDFs" or "Process ZIP"
4. Wait for processing to complete
```

### Query Documents
```
1. Enter research question in main area
2. Choose search type:
   - Hybrid Search: Best overall (semantic + keyword)
   - Semantic Search: Meaning-based
   - Per-Document: Results from each document
3. Adjust "Results to retrieve" slider (5-20)
4. Click "🚀 Search & Synthesize"
```

### Generate Report
```
1. Check "Generate Report" checkbox
2. Click "🚀 Search & Synthesize"
3. Wait for report generation
4. Click "📥 Download Report" to save DOCX file
```

## 📁 Project Structure

```
PROJECT_28_RAG_ASSISTANT/
├── app.py                      # Main Streamlit application
├── config.py                   # Configuration settings
├── requirements.txt            # Python dependencies
├── .env                        # API keys (DO NOT COMMIT)
├── .env.example               # Template for .env
├── .gitignore                 # Git ignore rules
├── README.md                  # This file
├── SETUP_GUIDE.md             # Setup instructions
├── QUICK_REFERENCE.md         # Common commands
├── TROUBLESHOOTING.md         # Common issues
├── SECURITY_GUIDE.md          # API key management
├── DEPLOYMENT_GUIDE.md        # Production deployment
├── src/
│   ├── __init__.py
│   ├── document_processor.py   # PDF processing
│   ├── embeddings.py           # Embedding generation
│   ├── vector_store.py         # Vector database
│   ├── retrieval.py            # Search & reranking
│   ├── synthesis.py            # Answer synthesis
│   └── report_generator.py     # Report generation
└── data/
    ├── uploads/                # Uploaded PDF files
    └── indexes/                # Generated indexes & reports
```

## 🔒 Security

⚠️ **Critical**: Never commit `.env` file to version control

### Best Practices
- ✅ Use `.env.example` as template
- ✅ Store API keys in `.env` (local only)
- ✅ Use platform secrets for deployment
- ✅ Rotate keys regularly
- ✅ Monitor API usage
- ❌ Never hardcode API keys
- ❌ Never share API keys in messages
- ❌ Never log API keys

See [Security Guide](SECURITY_GUIDE.md) for detailed instructions.

## 🚢 Deployment

Supported platforms:

| Platform | Ease | Cost | Best For |
|----------|------|------|----------|
| **Streamlit Cloud** | ⭐⭐⭐⭐⭐ | Free/Paid | Quick deployment |
| **Docker** | ⭐⭐⭐⭐ | Free | Flexibility |
| **AWS App Runner** | ⭐⭐⭐⭐ | Paid | Production |
| **Google Cloud Run** | ⭐⭐⭐⭐ | Paid | Production |
| **Heroku** | ⭐⭐⭐⭐ | Paid | Quick deployment |
| **EC2** | ⭐⭐⭐ | Paid | Full control |

See [Deployment Guide](DEPLOYMENT_GUIDE.md) for step-by-step instructions.

## 🐛 Troubleshooting

### Common Issues

**API Key Not Configured**
```bash
cp .env.example .env
# Edit .env with your API keys
streamlit run app.py
```

**Module Import Error**
```bash
pip install -r requirements.txt --upgrade
```

**Port Already in Use**
```bash
streamlit run app.py --server.port 8502
```

See [Troubleshooting Guide](TROUBLESHOOTING.md) for more solutions.

## ⚡ Performance Tips

- **Faster Processing**: Reduce `CHUNK_SIZE` to 500
- **Better Quality**: Increase `TOP_K_RETRIEVAL` to 30
- **Better Semantic Search**: Set `HYBRID_SEARCH_WEIGHT = 0.7`
- **Memory Constrained**: Reduce `BATCH_SIZE` to 16

## 📊 System Requirements

- **Python**: 3.8+
- **RAM**: 4GB minimum (8GB recommended)
- **Disk**: 2GB for dependencies + data
- **Internet**: Required for API calls

## 🛠️ Built With

- [Streamlit](https://streamlit.io) - Web UI framework
- [LangChain](https://python.langchain.com) - LLM orchestration
- [Pinecone](https://www.pinecone.io) - Vector database
- [Cohere](https://cohere.com) - Reranking API
- [Google Gemini](https://ai.google.dev) - LLM & Embeddings
- [PyPDF2](https://github.com/py-pdf/PyPDF2) - PDF processing
- [python-docx](https://python-docx.readthedocs.io) - Report generation
- [rank-bm25](https://github.com/dorianbrown/rank_bm25) - Keyword search

## 📝 License

MIT License - See LICENSE file for details

## 🤝 Support

For help:
1. Check [Troubleshooting Guide](TROUBLESHOOTING.md)
2. Review [Security Guide](SECURITY_GUIDE.md) for API key issues
3. Check API provider status pages
4. Review application logs

## 🎯 Next Steps

1. **First Time?** → Read [Setup Guide](SETUP_GUIDE.md)
2. **Need Commands?** → Check [Quick Reference](QUICK_REFERENCE.md)
3. **Having Issues?** → See [Troubleshooting](TROUBLESHOOTING.md)
4. **Ready to Deploy?** → Follow [Deployment Guide](DEPLOYMENT_GUIDE.md)
5. **Securing Keys?** → Read [Security Guide](SECURITY_GUIDE.md)

---

**Made with ❤️ using Google Gemini, Pinecone, and Streamlit**
